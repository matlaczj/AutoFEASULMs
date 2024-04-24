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

# TODO Dropping columns.
# TODO More column analysis in prompt.
# TODO Play with other models from `sklearn.datasets`.
# TODO: Select N most correlated features with target.

# Define the experiment
experiment = {
    "model": {
        "name": "MISTRAL-7B-INSTRUCT-V0.2.Q6_K",
        "chat_format": "mistral-instruct",
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
        "n_new_features": 10,
        "n_unique_values": 10,
        "perc_digits_after_decimal": 25,
        "correlations_threshold": 0.3,
        "threshold_features": 0.9,
        "threshold_target": 0.05,
        "iterations": 10,
    },
    "validation": {
        "kfold": 10,
    },
    "schema": schema,
}

# Load the dataset
global df
df, target = load_dataset_by_name(experiment["dataset"]["name"])
handle_invalid_data(df)

# %%
scores = []
mean_score1, std_score1 = cross_validate_model(
    df=df,
    target=target,
    target_variable=experiment["dataset"]["target_variable"],
    model=experiment["problem"]["model"],
    problem_type=experiment["problem"]["type"],
    cross_val=experiment["validation"]["kfold"],
)
scores.append({"mean_score": mean_score1, "std_score": std_score1})
# %%
mean_score2, std_score2 = None, None

# Initialize the model
model_path = get_model_dict(use_cache=False)[experiment["model"]["name"]]
llm = initialize_llm(
    model_path=model_path,
    chat_format=experiment["model"]["chat_format"],
    n_gpu_layers=experiment["model"]["n_gpu_layers"],
    n_ctx=experiment["model"]["n_ctx"],
    n_batch=experiment["model"]["n_batch"],
)

for iteration in range(1, experiment["feature_engineering"]["iterations"] + 1):
    print(f"ITERATION: {iteration}")
    # Run the inference iteration
    # Adding target to allow correlation analysis
    df["target"] = target
    json_content = run_inference_iteration(
        llm=llm,
        df=df,
        short_description=experiment["dataset"]["short_description"],
        problem_type=experiment["problem"]["type"],
        target_variable=experiment["dataset"]["target_variable"],
        machine_learning_model=experiment["problem"]["machine_learning_model"],
        n_new_features=experiment["feature_engineering"]["n_new_features"],
        schema=experiment["schema"],
        n_unique_values=experiment["feature_engineering"]["n_unique_values"],
        perc_digits_after_decimal=experiment["feature_engineering"][
            "perc_digits_after_decimal"
        ],
        correlations_threshold=experiment["feature_engineering"][
            "correlations_threshold"
        ],
    )

    df = execute_transformations(
        df=df,
        transformations=json_content,
        drop_old=False,
    )
    handle_invalid_data(df)
    df = remove_duplicate_columns(df)

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

    mean_score2, std_score2 = cross_validate_model(
        df=df,
        target=target,
        target_variable=experiment["dataset"]["target_variable"],
        model=experiment["problem"]["model"],
        problem_type=experiment["problem"]["type"],
        cross_val=experiment["validation"]["kfold"],
    )
    scores.append({"mean_score": mean_score2, "std_score": std_score2})
    calculate_percentage_change(mean_score1, mean_score2, std_score1, std_score2)

print(scores)
