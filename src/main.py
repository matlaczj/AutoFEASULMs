# %%
import os
import json
import time
from func_timeout import FunctionTimedOut
from src.config import config
from language_model import initialize_llm, run_inference_iteration
from experiments import prepare_experiments, datasets, classical_models, experiment_base
from utils.data_operations_utils import (
    handle_invalid_data,
    transform_date_columns,
    drop_correlated_columns,
    select_most_correlated,
    one_hot_encode,
    load_openml_dataset,
    execute_transformations,
    default_func,
    remove_duplicate_columns,
    add_noise,
    check_all_columns_are_series,
)
from utils.validation_utils import cross_validate_model
from utils.ast_utils import get_model_dict
from utils.main_utils import check_early_stopping, plot_experiment_results
import warnings
from colorama import Fore

warnings.filterwarnings("ignore")

# SECTION OF THINGS THAT NEED TO BE DONE:
# TODO More column analysis in prompt.
# TODO: Check for memory leakage of context.
# TODO: Add more functions and remove some of them.
# TODO: Speed up inference by using a single prompt for all columns.
# TODO: Explain bad regression results with diabetes dataset.
# TODO: Reduce context size by reducing number of correlations mentioned.
# TODO: Change what lines are printed on the visualization.
# TODO: Handle only tabular numeric datasets.
# TODO: Improve column names.
# TODO: Do hyperparameter tuning to show real value of FE. Or just set HP.
# TODO: Seed and temperature to increase reproducibility and determinism.
# TODO: Use reduce_dimentionality function to reduce the number of columns.
# TODO: Colorful print statements.
# TODO: Improve dataset descriptions.
# TODO: Experiment with smaller mistral versions.
# TODO: Reverse FE if score decreases. Like a tree search (add a parameter to the config).
# TODO: Compare with SOTA Classical Methods: Featurewiz
# TODO: Improve vis and create table with results.
# TODO: Add more tools.
# TODO: Lock original columns.

# DEFINE GLOBAL VARIABLES AND LOAD THE EXPERIMENTS
global df, llm, scores
experiments = prepare_experiments(datasets, classical_models, experiment_base)

# PRINT THE NUMBER OF EXPERIMENTS AND THEIR IDS FOR CONVENIENCE
print(f"{Fore.GREEN}Number of experiments: {len(experiments)}{Fore.RESET}\n")
for experiment in experiments:
    print(f"{Fore.YELLOW}{experiment['ID']}{Fore.RESET}")

# TEST IF ALL DATASETS CAN BE LOADED
df_dict = {}
for dataset in datasets:
    name = dataset["name"]
    df, target = load_openml_dataset(
        name,
        max_records=experiment["dataset"]["max_records"],
    )
    df_dict[name] = df
# %%
for experiment in experiments:
    # NOTE: TEMPORARY FOR DEBUGGING
    # if int(experiment["ID"].split("-")[0]) < 22:
    #     continue

    # CREATE THE DIRECTORY IF IT DOESN'T EXIST
    exp_base = config["project_base_dir"] + f"\\logs\\{experiment['ID']}\\"
    counter = 1
    while os.path.exists(exp_base):
        exp_base = (
            config["project_base_dir"] + f"\\logs\\{experiment['ID']}-{counter}\\"
        )
        counter += 1
    os.makedirs(exp_base, exist_ok=True)

    # SAVE THE EXPERIMENT JSON
    with open(exp_base + "experiment.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(experiment, default=default_func))

    # LOAD THE DATASET AND PREPROCESS IT
    df, target = load_openml_dataset(
        experiment["dataset"]["name"],
        experiment["dataset"]["target_variable"],
        experiment["problem"]["type"],
        experiment["dataset"]["max_records"],
    )
    df = handle_invalid_data(df)
    df = transform_date_columns(df)
    df = one_hot_encode(df)
    df = add_noise(
        df=df,
        noise_perc_of_range=experiment["dataset"]["noise_perc_of_range"],
        target_column=experiment["dataset"]["target_variable"],
    )
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    df_base = df.copy(deep=True)

    # RUN THE BASELINE MODEL
    scores = []
    mean_val_score, std_val_score, mean_train_score, std_train_score = (
        cross_validate_model(
            df=df,
            target=target,
            target_variable=experiment["dataset"]["target_variable"],
            model=experiment["problem"]["model"],
            problem_type=experiment["problem"]["type"],
            param_grid=experiment["problem"]["param_grid"],
            cross_val=experiment["validation"]["kfold"],
            scorers=experiment["validation"]["scorers"],
        )
    )
    scores.append(
        {
            "mean_score": mean_val_score,
            "mean_std": std_val_score,
            "train_score": mean_train_score,
            "train_std": std_train_score,
            "columns": list(
                set(df.columns) - set([experiment["dataset"]["target_variable"]])
            ),
            "time": 0,
        }
    )

    # INITIALIZE THE LANGUAGE MODEL
    model_path = get_model_dict(use_cache=False)[experiment["model"]["name"]]
    llm = initialize_llm(
        model_path=model_path,
        chat_format=experiment["model"]["chat_format"],
        n_gpu_layers=experiment["model"]["n_gpu_layers"],
        n_ctx=experiment["model"]["n_ctx"],
        n_batch=experiment["model"]["n_batch"],
    )

    # RUN THE FEATURE ENGINEERING ITERATIONS
    for iteration in range(1, experiment["feature_engineering"]["iterations"] + 1):
        print(f"{Fore.GREEN}ITERATION: {iteration}{Fore.RESET}\n")

        # CREATE THE ITERATION DIRECTORY
        iter_base = exp_base + f"{iteration}\\"
        os.makedirs(iter_base, exist_ok=True)

        # START THE TIMER AND BACKUP THE DATAFRAME
        start_time = time.time()

        # TRY TO RUN THE INFERENCE ITERATION
        df[experiment["dataset"]["target_variable"]] = target
        df = check_all_columns_are_series(df)
        try:
            json_content = run_inference_iteration(
                llm=llm,
                df=df,
                short_description=experiment["dataset"]["short_description"],
                problem_type=experiment["problem"]["type"],
                target_variable=experiment["dataset"]["target_variable"],
                machine_learning_model=experiment["problem"]["machine_learning_model"],
                n_new_features=experiment["feature_engineering"]["n_new_features"],
                schema=experiment["schema"],
                exp_base=iter_base,
                iter=iteration,
                scores=scores,
                n_unique_values=experiment["feature_engineering"]["n_unique_values"],
                perc_digits_after_decimal=experiment["feature_engineering"][
                    "perc_digits_after_decimal"
                ],
                correlations_threshold=experiment["feature_engineering"][
                    "correlations_threshold"
                ],
                temperature=experiment["feature_engineering"]["temperature"],
                n_sampled_corr=experiment["feature_engineering"]["n_sampled_corr"],
            )
        except FunctionTimedOut as e:
            print(f"{Fore.RED}FunctionTimedOut: {e}{Fore.RESET}")
            print(f"{Fore.RED}Skipping iteration {iteration}.{Fore.RESET}\n")
            continue

        # EXECUTE THE TRANSFORMATIONS RETURNED BY LANGUAGE MODEL
        df = execute_transformations(
            df=df,
            transformations=json_content,
            drop_old=False,
        )

        # POSTPROCESS AFTERMATH OF EXECUTED TRANSFORMATIONS
        df = handle_invalid_data(df)
        # NOTE: Apparently, the following line is necessary!
        df = remove_duplicate_columns(df)

        # AUTOMATIC FEATURE SELECTION
        if iteration > experiment["feature_engineering"]["delayed_deletion"]:
            if experiment["problem"]["type"] == "regression":
                df = select_most_correlated(
                    df=df,
                    target=experiment["dataset"]["target_variable"],
                    n=experiment["feature_engineering"]["n_most_correlated"],
                )
            df = drop_correlated_columns(
                df=df,
                threshold_features=experiment["feature_engineering"][
                    "threshold_features"
                ],
            )

        # PRESERVING BASE COLUMNS TO PREVENT LOSS OF INFORMATION
        print(Fore.YELLOW + "Preserving base columns." + Fore.RESET)
        if experiment["feature_engineering"]["preserve_base_features"]:
            for column in df_base.columns:
                df[column] = df_base[column].copy(deep=True)
            df = df[
                df_base.columns.tolist()
                + [col for col in df.columns if col not in df_base.columns]
            ]

        # PREVENT THE TARGET VARIABLE LEAKAGE
        print(Fore.YELLOW + "Preventing target variable leakage." + Fore.RESET)
        df = df.drop(
            columns=[
                col
                for col in df.columns
                if experiment["dataset"]["target_variable"] in col
            ]
        )

        # CALCULATE THE SCORES AFTER THE FEATURE ENGINEERING
        mean_val_score, std_val_score, mean_train_score, std_train_score = (
            cross_validate_model(
                df=df,
                target=target,
                target_variable=experiment["dataset"]["target_variable"],
                model=experiment["problem"]["model"],
                problem_type=experiment["problem"]["type"],
                param_grid=experiment["problem"]["param_grid"],
                cross_val=experiment["validation"]["kfold"],
                scorers=experiment["validation"]["scorers"],
            )
        )

        # STOP THE TIMER
        end_time = time.time()
        scores.append(
            {
                "mean_score": mean_val_score,
                "mean_std": std_val_score,
                "train_score": mean_train_score,
                "train_std": std_train_score,
                "columns": list(df.columns),
                "time": end_time - start_time,
            }
        )

        print(f"{Fore.GREEN}Iteration {iteration} completed.{Fore.RESET}\n")

        # SAVE THE SCORES AND VISUALIZATIONS
        with open(iter_base + "scores.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(scores))

        plot_experiment_results(
            dataset_name=experiment["dataset"]["name"],
            model_name=experiment["problem"]["model"],
            problem_type=experiment["problem"]["type"],
            validation_kfold=experiment["validation"]["kfold"],
            scores=scores,
            iter_base=iter_base,
        )

        # EARLY STOPPING MECHANISM CHECK
        if check_early_stopping(
            k=experiment["feature_engineering"]["early_stopping"],
            threshold=experiment["feature_engineering"]["percentage_change_threshold"],
            problem_type=experiment["problem"]["type"],
            scores=scores,
            iteration=iteration,
        ):
            break

    # AFTER THE EXPERIMENT IS DONE DELETE THE VARIABLES TO FREE UP MEMORY FOR THE NEXT EXPERIMENT
    del llm
    del df
    del scores
    print(f"{Fore.GREEN}Experiment {experiment['ID']} completed.{Fore.RESET}\n")

# %%
