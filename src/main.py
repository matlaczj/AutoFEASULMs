# %%
from language_model import (
    initialize_llm,
    create_chat_completion,
    get_message_content,
)
from utils import get_model_dict
from response_schemas import schemas
from sklearn.datasets import load_iris
import pandas as pd
import json
import pprint

# %%
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
# %%
model_dict = get_model_dict(use_cache=False)
# %%
llm = initialize_llm(
    model_path=model_dict["MISTRAL-7B-INSTRUCT-V0.2.Q6_K"],
    chat_format="mistral-instruct",
)
# %%
column_names = df.columns.tolist()
transformations = [
    "standard_scaler",
    "min_max_scaler",
    "max_abs_scaler",
    "quantile_transformer",
    "power_transformer",
    "normalizer",
    "binarizer",
    "polynomial_features",
    "k_bins_discretizer",
    "ordinal_encoder",
    "one_hot_encoder",
    "apply_math_function",
]
# %%
response_format = {
    "type": "json_object",
    "schema": schemas["dual_argument_schema"],
}
response_format["schema"]["properties"]["column_name_1"]["enum"] = column_names
response_format["schema"]["properties"]["column_name_2"]["enum"] = column_names

pp = pprint.PrettyPrinter()
pp.pprint(response_format)
# %%
messages = [
    {
        "role": "user",
        "content": f"""
You are an expert in data preprocessing. I have a dataset and I would like to create new features that will make my machine learning models more accurate. Can you help me with that? I will show you list of available transformations and column names. You can choose one of the transformations and 2 of the columns. I will then apply the transformation to the selected column. Respond with valid json. Here is the information you need:

Column names: {column_names}

Available transformations: {transformations}
""",
    },
]

print(messages[0]["content"])
# %%
response = create_chat_completion(
    llm=llm,
    messages=messages,
    response_format=response_format,
)

content = get_message_content(response)
json.loads(content)
# %%
