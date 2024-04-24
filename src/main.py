# %%
from language_model import initialize_llm, run_inference_iteration
from utils import get_model_dict, load_dataset_by_name
from response_schemas import schema

# TODO Dropping columns.
# TODO More column analysis in prompt.
# TODO Play with other models from `sklearn.datasets`.
# %%
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
    "schema": schema,
}

# %%
# Load the dataset
df = load_dataset_by_name(experiment["dataset"]["name"])

# Initialize the model
model_path = get_model_dict(use_cache=False)[experiment["model"]["name"]]
llm = initialize_llm(
    model_path=model_path,
    chat_format=experiment["model"]["chat_format"],
    n_gpu_layers=experiment["model"]["n_gpu_layers"],
    n_ctx=experiment["model"]["n_ctx"],
    n_batch=experiment["model"]["n_batch"],
)
# %%
# Run the inference iteration
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
    correlations_threshold=experiment["feature_engineering"]["correlations_threshold"],
)

# TODO: Use tools mentioned in the completion to create new features.

# %%
