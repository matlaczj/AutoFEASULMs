from language_model import initialize_llm, run_inference_iteration
from utils import (
    get_model_dict,
    load_dataset_by_name,
    execute_transformations,
    cross_validate_model,
    calculate_percentage_change,
    drop_correlated_columns,
    remove_duplicate_columns,
)
from response_schemas import schema
from src.tool_handlers import *
from sklearn.tree import DecisionTreeRegressor

# TODO Dropping columns.
# TODO More column analysis in prompt.
# TODO Play with other models from `sklearn.datasets`.

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
        "name": "diabetes",
        "short_description": f"**ATTRIBUTE DESCRIPTIONS:**\n1. 'age': Age in years\n2. 'sex': Gender\n3. 'bmi': Body mass index\n4. 'bp': Average blood pressure\n5. 's1': Total serum cholesterol (tc)\n6. 's2': Low-density lipoproteins (ldl)\n7. 's3': High-density lipoproteins (hdl)\n8. 's4': Total cholesterol / HDL (tch)\n9. 's5': Possibly log of serum triglycerides level (ltg)\n10. 's6': Blood sugar level\n11. 'target': a quantitative measure of disease progression one year after baseline\n\n",
        "target_variable": "target",
    },
    "problem": {"type": "regression", "machine_learning_model": "regression tree"},
    "feature_engineering": {
        "n_new_features": 10,
        "n_unique_values": 10,
        "perc_digits_after_decimal": 25,
        "correlations_threshold": 0.3,
    },
    "validation": {
        "model": DecisionTreeRegressor(),
        "kfold": 10,
    },
    "schema": schema,
}

# Load the dataset
global df
df, target = load_dataset_by_name(experiment["dataset"]["name"])

mean_score1, std_score1 = cross_validate_model(
    df=df,
    target=target,
    target_variable=experiment["dataset"]["target_variable"],
    model=experiment["validation"]["model"],
    problem_type=experiment["problem"]["type"],
    cross_val=experiment["validation"]["kfold"],
)

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

for iteration in range(1, 10):
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
        target_variable=experiment["dataset"]["target_variable"],
    )

    df = remove_duplicate_columns(df)

    df = drop_correlated_columns(
        df=df,
        target=experiment["dataset"]["target_variable"],
        threshold_features=0.9,
        threshold_target=0.1,
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
        model=experiment["validation"]["model"],
        problem_type=experiment["problem"]["type"],
        cross_val=experiment["validation"]["kfold"],
    )

    calculate_percentage_change(mean_score1, mean_score2, std_score1, std_score2)
