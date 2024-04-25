# %%
from language_model import initialize_llm, run_inference_iteration
from utils import (
    get_model_dict,
    load_dataset_by_name,
    execute_transformations,
    cross_validate_model,
    calculate_percentage_change,
    drop_correlated_columns,
    remove_duplicate_columns,
    handle_invalid_data,
    select_most_correlated,
    default_func,
)
from response_schemas import schema
from src.tool_handlers import *
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, mean_absolute_percentage_error
from visualizing.visualizations import plot_scores
from src.config import config
import os
import json

# TODO Dropping columns.
# TODO More column analysis in prompt.
# TODO Play with other models from `sklearn.datasets`.
# TODO: Select N most correlated features with target.
# TODO: Check for memory leakage of context.
# TODO: Do hyperparameter tuning to show real value of feature engineering.
# TODO: Reverse FE if score decreases.
# TODO: Save ALL details to logs.

# Define the experiment
experiment = {
    "ID": "MIST-WINE-CLAS-SVC-1",
    "model": {
        "name": "MISTRAL-7B-INSTRUCT-V0.2.Q6_K",  # "MISTRAL-7B-INSTRUCT-V0.2.Q6_K"
        "chat_format": "mistral-instruct",  # "mistral-instruct"
        "n_gpu_layers": -1,
        "n_ctx": 512 * 16,
        "n_batch": 512 * 8,
    },
    "dataset": {
        "target_variable": "target",
        "name": "wine",
        "short_description": """
**Attribute Information**:
- Alcohol: Percentage of alcohol content in the wine.
- Malic acid: Concentration of malic acid in the wine.
- Ash: Amount of ash in the wine after combustion.
- Alcalinity of ash: Measure of the basicity of ash in the wine.
- Magnesium: Concentration of magnesium in the wine.
- Total phenols: Total amount of phenolic compounds in the wine.
- Flavanoids: Concentration of flavonoid compounds in the wine.
- Nonflavanoid phenols: Concentration of non-flavonoid phenolic compounds in the wine.
- Proanthocyanins: Concentration of proanthocyanins in the wine.
- Color intensity: Intensity of color in the wine.
- Hue: Hue or shade of the wine.
- OD280/OD315 of diluted wines: Ratio of optical density at 280nm to 315nm of diluted wines.
- Proline: Concentration of proline in the wine.
- class_0, class_1, class_2: Labels indicating the class or category of the wine samples.

""",
    },
    "problem": {
        "type": "classification",
        "machine_learning_model": "Support Vector Machine Classifier",
        "model": SVC(),
    },
    "feature_engineering": {
        "iterations": 20,
        "n_new_features": 5,
        "n_unique_values": 10,
        "perc_digits_after_decimal": 20,
        "correlations_threshold": 0.3,
        "temperature": 1.5,
        "n_most_correlated": 20,
        "threshold_features": 0.8,
        "threshold_target": 0.1,
    },
    "validation": {
        "kfold": 10,
        "scorers": {
            "classification": accuracy_score,
            "regression": mean_absolute_percentage_error,
        },
    },
    "schema": schema,
}


# Create the directory if it doesn't exist
exp_base = config["project_base_dir"] + f"\\src\\logs\\{experiment['ID']}\\"
os.makedirs(exp_base, exist_ok=True)

with open(exp_base + "experiment.json", "w") as f:
    f.write(json.dumps(experiment, default=default_func))

# Load the dataset
global df
df, target = load_dataset_by_name(experiment["dataset"]["name"])
handle_invalid_data(df)

# %%
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

mean_score2, mean_std2 = None, None
model_path = get_model_dict(use_cache=False)[experiment["model"]["name"]]

llm = initialize_llm(
    model_path=model_path,
    chat_format=experiment["model"]["chat_format"],
    n_gpu_layers=experiment["model"]["n_gpu_layers"],
    n_ctx=experiment["model"]["n_ctx"],
    n_batch=experiment["model"]["n_batch"],
)
# %%

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
        )
    except ValueError as e:
        print(f"ValueError: {e}")
        break

    df = execute_transformations(
        df=df,
        transformations=json_content,
        drop_old=False,
    )
    handle_invalid_data(df)
    df = remove_duplicate_columns(df)

    if experiment["problem"]["type"] == "regression":
        df = select_most_correlated(
            df=df,
            target=experiment["dataset"]["target_variable"],
            n=experiment["feature_engineering"]["n_most_correlated"],
        )
    else:
        df = drop_correlated_columns(
            df=df,
            target=experiment["dataset"]["target_variable"],
            threshold_features=experiment["feature_engineering"]["threshold_features"],
            threshold_target=experiment["feature_engineering"]["threshold_target"],
        )

    # Prevent leakage of target variable
    df = df.drop(
        columns=[
            col for col in df.columns if experiment["dataset"]["target_variable"] in col
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
        score_axis_title=(
            "10-Fold Cross-Val Accuracy Score [%] With Std Dev"
            if experiment["problem"]["type"] == "classification"
            else "10-Fold Cross-Val Mean Abs Perc Error [%] With Std Dev"
        ),
        path=iter_base + "scores.pdf",
    )
