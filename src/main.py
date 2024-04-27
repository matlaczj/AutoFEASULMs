# %%
from language_model import initialize_llm, run_inference_iteration
from utils import (
    get_model_dict,
    load_dataset_from_sklearn,
    execute_transformations,
    cross_validate_model,
    calculate_percentage_change,
    drop_correlated_columns,
    remove_duplicate_columns,
    handle_invalid_data,
    select_most_correlated,
    default_func,
    load_dataset_from_huggingface,
    one_hot_encode,
    transform_date_columns,
)
from src.tool_handlers import *
from visualizing.visualizations import plot_scores
from src.config import config
import os
import json
from experiments import prepare_experiments, datasets, classical_models, experiment_base
from func_timeout import FunctionTimedOut

# TODO More column analysis in prompt.
# TODO: Check for memory leakage of context.
# TODO: Do hyperparameter tuning to show real value of feature engineering.
# TODO: Reverse FE if score decreases.
# TODO: Add more functions and remove some of them.
# TODO: Speed up inference by using a single prompt for all columns.
# TODO: Explain bad regression results with diabetes dataset.
# TODO: Reduce context size by reducing number of correlations mentioned.
# TODO: Change what lines are printed on the visualization.
# TODO: Handle only tabular numeric datasets.

global df, llm, scores
experiments = prepare_experiments(datasets, classical_models, experiment_base)

print(f"Number of experiments: {len(experiments)}")
for experiment in experiments:
    print(experiment["ID"])

# %%
for experiment in experiments:
    # NOTE: Temporary for debugging
    if int(experiment["ID"].split("-")[0]) != 36:
        continue

    # Create the directory if it doesn't exist
    exp_base = config["project_base_dir"] + f"\\src\\logs\\{experiment['ID']}\\"
    counter = 1
    while os.path.exists(exp_base):
        exp_base = (
            config["project_base_dir"] + f"\\src\\logs\\{experiment['ID']}-{counter}\\"
        )
        counter += 1
    os.makedirs(exp_base, exist_ok=True)

    with open(exp_base + "experiment.json", "w") as f:
        f.write(json.dumps(experiment, default=default_func))

    # Load the dataset
    if experiment["dataset"]["origin"] == "sklearn":
        df, target = load_dataset_from_sklearn(experiment["dataset"]["name"])
    elif experiment["dataset"]["origin"] == "huggingface":
        df, target = load_dataset_from_huggingface(
            experiment["dataset"]["name"], experiment["dataset"]["predicted_variable"]
        )
    else:
        raise ValueError("Dataset origin not recognized.")

    df = handle_invalid_data(df)
    df = transform_date_columns(df)
    df = one_hot_encode(df)

    scores = []
    mean_score1, mean_std1 = cross_validate_model(
        df=df,
        target=target,
        target_variable=experiment["dataset"]["target_variable"],
        model=experiment["problem"]["model"],
        problem_type=experiment["problem"]["type"],
        cross_val=experiment["validation"]["kfold"],
        scorers=experiment["validation"]["scorers"],
    )
    scores.append(
        {"mean_score": mean_score1, "mean_std": mean_std1, "columns": list(df.columns)}
    )

    model_path = get_model_dict(use_cache=False)[experiment["model"]["name"]]

    llm = initialize_llm(
        model_path=model_path,
        chat_format=experiment["model"]["chat_format"],
        n_gpu_layers=experiment["model"]["n_gpu_layers"],
        n_ctx=experiment["model"]["n_ctx"],
        n_batch=experiment["model"]["n_batch"],
    )

    for iteration in range(1, experiment["feature_engineering"]["iterations"] + 1):
        # Run the inference iteration
        print(f"ITERATION: {iteration}")
        iter_base = exp_base + f"{iteration}\\"
        os.makedirs(iter_base, exist_ok=True)

        # Adding target to allow correlation analysis
        df["target"] = target
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
        except ValueError as e:
            print(f"ValueError: {e}")
            continue
        except FunctionTimedOut as e:
            print(f"FunctionTimedOut: {e}")
            continue

        df = execute_transformations(
            df=df,
            transformations=json_content,
            drop_old=False,
        )
        df = handle_invalid_data(df)
        df = remove_duplicate_columns(df)

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

        # Prevent leakage of target variable
        df = df.drop(
            columns=[
                col
                for col in df.columns
                if experiment["dataset"]["target_variable"] in col
            ]
        )

        mean_score2, mean_std2 = cross_validate_model(
            df=df,
            target=target,
            target_variable=experiment["dataset"]["target_variable"],
            model=experiment["problem"]["model"],
            problem_type=experiment["problem"]["type"],
            cross_val=experiment["validation"]["kfold"],
            scorers=experiment["validation"]["scorers"],
        )

        calculate_percentage_change(mean_score1, mean_score2, mean_std1, mean_std2)
        print(f"Iteraion {iteration} completed.")
        scores.append(
            {
                "mean_score": mean_score2,
                "mean_std": mean_std2,
                "columns": list(df.columns),
            }
        )

        with open(iter_base + "scores.json", "w") as f:
            f.write(json.dumps(scores))

        plot_scores(
            scores,
            big_title=f"""Experiment ID: {experiment["ID"]}""",
            score_axis_title=(
                f"""{experiment["validation"]["kfold"]}-Fold Cross-Val Accuracy Score With Std Dev"""
                if experiment["problem"]["type"] == "classification"
                else f"""{experiment["validation"]["kfold"]}-Fold Cross-Val MAPE With Std Dev"""
            ),
            path=iter_base + "scores.pdf",
            if_score=(
                True if experiment["problem"]["type"] == "classification" else False
            ),
        )

        # Early stopping mechanism
        k = experiment["feature_engineering"]["early_stopping"]
        threshold = experiment["feature_engineering"]["percentage_change_threshold"]
        if iteration >= k:
            last_k_scores = [score["mean_score"] for score in scores[-k:]]
            percentage_changes = [
                (last_k_scores[i] - last_k_scores[i + 1]) / last_k_scores[i + 1] * 100
                for i in range(len(last_k_scores) - 1)
            ]
            if all(change < threshold for change in percentage_changes):
                print("Early stopping mechanism triggered.")
                break

    del llm
    del df
    del scores
    print(f"Experiment {experiment['ID']} completed.")

# %%
