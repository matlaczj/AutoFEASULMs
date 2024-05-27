# %%
from src.experiments import (
    prepare_experiments,
    datasets,
    classical_models,
    experiment_base,
)
from src.utils.data_operations_utils import (
    handle_invalid_data,
    transform_date_columns,
    one_hot_encode,
    load_openml_dataset,
    add_noise,
)
from src.utils.validation_utils import cross_validate_model
from featurewiz import FeatureWiz
import warnings, time, json
from colorama import Fore

# %%
warnings.filterwarnings("ignore")

experiments = prepare_experiments(datasets, classical_models, experiment_base)

scores = []

# %%
for experiment in experiments:

    print(Fore.GREEN + f"Running experiment: {experiment['ID']}.")

    print(Fore.YELLOW + f"Loading dataset {experiment['dataset']['name']}.")
    df, target = load_openml_dataset(
        experiment["dataset"]["name"],
        experiment["dataset"]["target_variable"],
        experiment["problem"]["type"],
        experiment["dataset"]["max_records"],
    )

    print(Fore.YELLOW + "Renaming columns.")
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    print(Fore.YELLOW + "Handling invalid data.")
    df = handle_invalid_data(df)
    print(Fore.YELLOW + "Transforming date columns.")
    df = transform_date_columns(df)
    print(Fore.YELLOW + "One hot encoding categorical columns.")
    df = one_hot_encode(df)
    print(Fore.YELLOW + "Adding noise to the dataset.")
    df = add_noise(
        df=df,
        noise_perc_of_range=experiment["dataset"]["noise_perc_of_range"],
        target_column=experiment["dataset"]["target_variable"],
    )

    print(Fore.YELLOW + "Cross validating with no FE.")
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
            "ID": experiment["ID"],
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

    start_time = time.time()

    print(Fore.YELLOW + "Feature engineering.")
    fw = FeatureWiz(
        verbose=2,
        feature_engg=[
            "interactions",
            "groupby",
        ],
    )
    fw.target = experiment["dataset"]["target_variable"]
    fw.mode = "automatic"
    df = df.drop(columns=[experiment["dataset"]["target_variable"]])
    df_new, target = fw.fit_transform(df, target)

    print(Fore.YELLOW + "Cross validating the model.")
    mean_val_score, std_val_score, mean_train_score, std_train_score = (
        cross_validate_model(
            df=df_new,
            target=target,
            target_variable=experiment["dataset"]["target_variable"],
            model=experiment["problem"]["model"],
            problem_type=experiment["problem"]["type"],
            param_grid=experiment["problem"]["param_grid"],
            cross_val=experiment["validation"]["kfold"],
            scorers=experiment["validation"]["scorers"],
        )
    )

    end_time = time.time()

    scores.append(
        {
            "ID": experiment["ID"],
            "mean_score": mean_val_score,
            "mean_std": std_val_score,
            "train_score": mean_train_score,
            "train_std": std_train_score,
            "columns": list(
                set(df_new.columns) - set([experiment["dataset"]["target_variable"]])
            ),
            "time": end_time - start_time,
        }
    )

    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(scores, f)

# %%
import json
import pandas as pd

with open("scores.json", "r") as f:
    scores = json.load(f)
df = pd.DataFrame(scores)
# %%
df_no_fe = df[df["time"] == 0].reset_index(drop=True)
df_fe = df[df["time"] != 0].reset_index(drop=True)
df_fe["gain"] = ((df_no_fe.mean_score - df_fe.mean_score) / df_no_fe.mean_score).round(
    2
)
table = pd.DataFrame(
    {
        "Experiment": df_fe.ID,
        "Initial Score": (df_no_fe.mean_score * 100).round(2),
        "Final Score": (df_fe.mean_score * 100).round(2),
        "Gain": (df_fe.gain * 100).round(2),
        "Time": df_fe.time.round(2),
    }
)
# save to csv
table.to_csv("scores.csv", index=False)
# %%
# load csv
table = pd.read_csv("scores.csv")
# sort table by column 'f' in descending order by absolute value
table = table.reindex(table["f"].abs().sort_values(ascending=False).index).reset_index(
    drop=True
)
# %%
