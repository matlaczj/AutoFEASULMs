# %%
from language_model import initialize_llm, create_chat_completion, get_message_content
from utils import (
    get_model_dict,
    describe_unique_values,
    describe_strong_correlations,
    describe_transformations,
)
from sklearn import datasets
from response_schemas import general
import json

# %%
X, y = datasets.load_iris(return_X_y=True, as_frame=True)
X["species"] = y

target_variable = "species"
problem_type = "classification"
machine_learning_model = "decision tree"
n_new_features = 10
function_headers = describe_transformations(
    filename="preprocessing_tools.py", skip_args=["df", "drop_old"], if_def=False
)
unqiue_values = describe_unique_values(X, 5)
correlations = describe_strong_correlations(X, 0.3)

prompt = f"**COLUMNS:**\n- *UNIQUE VALUES:*\n{unqiue_values}- *CORRELATIONS:*\n{correlations}\n\n**TOOLS:**\n{function_headers}\n\n**RULES:**\n- You are a feature engineering and selection program that works in iterations.\n- You create new features from existing columns to make ML {machine_learning_model} model better at predicting target variable '{target_variable}' in {problem_type} problem.\n- Target column should remain unchanged as it would be considered cheating.\n- Every iteration you suggest {n_new_features} new column-tool combinations.\n\n**CURRENT ITERATION:**"

with open("prompt.md", "w") as f:
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
with open("output.md", "w") as f:
    f.write(message_content)

# %%
completion = create_chat_completion(
    llm=llm,
    messages=[
        {
            "role": "user",
            "content": f"**TASK:**\nTurn the content into valid json like on the schema.\n**SCHEMA:**\n{general}\n**CONTENT**:\n{message_content}\n**JSON:**\n",
        },
    ],
    response_format={
        "type": "json_object",
        "schema": general,
    },
)

# %%
json_content = json.loads(get_message_content(completion))
with open("output.json", "w") as f:
    json.dump(json_content, f, indent=4)
# %%
llm.reset()
# %%
