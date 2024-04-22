# %%
from language_model import initialize_llm, create_chat_completion, get_message_content
from utils import (
    get_model_dict,
    describe_unique_values,
    describe_strong_correlations,
    describe_transformations,
)
from sklearn import datasets
from response_schemas import schema
import json
from config import config

# TODO Dropping columns.
# TODO More column analysis in prompt.
# TODO Play with other models from `sklearn.datasets`.
# %%
with open(config["project_base_dir"] + r"\src\logs\schema.json", "w") as f:
    f.write(json.dumps(schema))

short_description = f"**DATASET DESCRIPTION:**\nTen baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements were obtained for each of n = 442 diabetes patients, as well as the response of interest, a quantitative measure of disease progression one year after baseline.\n\n**ATTRIBUTE INFORMATION:**\nage age in years sex bmi body mass index bp average blood pressure s1 tc, total serum cholesterol s2 ldl, low-density lipoproteins s3 hdl, high-density lipoproteins s4 tch, total cholesterol / HDL s5 ltg, possibly log of serum triglycerides level s6 glu, blood sugar level\n\n"
X, y = datasets.load_diabetes(return_X_y=True, as_frame=True)
target_variable = "diabetes"
X[target_variable] = y
problem_type = "regression"
machine_learning_model = "linear regression"
n_new_features = 10
function_headers = describe_transformations(
    filename="preprocessing_tools.py",
    skip_args=["df", "drop_old"],
    if_def=False,
    if_backtick=True,
)
unqiue_values = describe_unique_values(X, 10, 25)
correlations = describe_strong_correlations(X, 0.3)

prompt = f"{short_description}**COLUMNS:**\n- *UNIQUE VALUES:*\n{unqiue_values}- *CORRELATIONS:*\n{correlations}\n\n**TOOLS:**\n{function_headers}\n\n**RULES:**\n- You are a feature engineering and selection program that works in iterations.\n- You create new features from existing columns to make ML {machine_learning_model} model better at predicting target variable '{target_variable}' in {problem_type} problem.\n- Target column should remain unchanged as it would be considered cheating.\n- Every iteration you suggest {n_new_features} new column-tool combinations.\n\n**CURRENT ITERATION:**"

with open(config["project_base_dir"] + r"\src\logs\prompt.md", "w") as f:
    f.write(prompt)

# %%
llm = initialize_llm(
    model_path=get_model_dict(use_cache=False)["MISTRAL-7B-INSTRUCT-V0.2.Q6_K"],
    chat_format="mistral-instruct",
    n_gpu_layers=-1,
    n_ctx=512 * 16,
    n_batch=512 * 8,
)
# %%
completion = create_chat_completion(
    llm=llm,
    messages=[
        {"role": "user", "content": prompt},
    ],
)

message_content = get_message_content(completion)
with open(config["project_base_dir"] + r"\src\logs\output.md", "w") as f:
    f.write(message_content)

# %%
# with open(config["project_base_dir"] + r"\src\logs\output.md", "r") as f:
#     message_content = f.read()

schema["properties"]["transformations"]["items"]["properties"]["columns"]["items"][
    "enum"
] = [col for col in X.columns]

prompt1 = f"**TASK:**\nTurn the content into valid json like on the schema.\n**TOOLS:**\n{function_headers}\n**SCHEMA:**\n{schema}\n**CONTENT**:\n{message_content}\n**JSON:**\n"

with open(config["project_base_dir"] + r"\src\logs\prompt1.md", "w") as f:
    f.write(prompt1)

# %%
completion1 = create_chat_completion(
    llm=llm,
    messages=[
        {
            "role": "user",
            "content": prompt1,
        },
    ],
    response_format={
        "type": "json_object",
        "schema": schema,
    },
)

# %%
json_content = json.loads(get_message_content(completion1))
with open(config["project_base_dir"] + r"\src\logs\output1.json", "w") as f:
    json.dump(json_content, f)
# %%
llm.reset()
# %%
