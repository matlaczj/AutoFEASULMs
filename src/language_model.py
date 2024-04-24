# %%
from llama_cpp import Llama
from typing import List, Dict, Union, Optional
from utils import (
    describe_unique_values,
    describe_strong_correlations,
    describe_transformations,
)
import pandas as pd
import json


def initialize_llm(
    model_path: str,
    chat_format: str,
    n_gpu_layers: int = -1,
    n_ctx: int = 512 * 16,
    n_batch=512 * 8,
) -> Llama:
    """
    Initializes a Llama language model. Default values tweaked for RTX 2070 Super.

    Args:
        model_path (str): The path to the model file.
        chat_format (str): The format of the chat.
        n_gpu_layers (int, optional): The number of GPU layers. Defaults to -1.
        n_ctx (int, optional): The context size. Defaults to 8192.
        n_batch (int, optional): The batch size. Defaults to 4096.

    Returns:
        Llama: The initialized Llama language model.
    """
    return Llama(
        model_path=model_path,
        chat_format=chat_format,
        n_gpu_layers=n_gpu_layers,
        n_ctx=n_ctx,
        n_batch=n_batch,
    )


def create_chat_completion(
    llm: Llama,
    messages: List[Dict[str, str]],
    response_format: Dict[str, Union[str, Dict]] = None,
    stop: Optional[Union[str, List[str]]] = [],
    temperature: float = 0.7,
    top_p: float = 0.95,
    top_k: int = 40,
    min_p: float = 0.05,
    max_tokens: int = None,
    repeat_penalty: float = 1.1,
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """
    Creates a chat completion using the Llama language model.

    Args:
        llm (Llama): The language model to use.
        messages (List[Dict[str, str]]): The list of message dictionaries.
        response_format (Dict[str, Union[str, Dict]], optional): The format of the response. Defaults to None.
        stop (Optional[Union[str, List[str]]], optional): The stop sequence(s). Defaults to [].
        temperature (float, optional): The randomness of the output. Lower values make the output more deterministic. Defaults to 0.7.
        top_p (float, optional): The cumulative probability cutoff for token selection. Defaults to 0.95.
        top_k (int, optional): The number of top tokens to consider for selection. Defaults to 40.
        min_p (float, optional): The minimum probability cutoff for token selection. Defaults to 0.05.
        max_tokens (int, optional): The maximum number of tokens in the output. Defaults to None.
        repeat_penalty (float, optional): The penalty for repeating tokens. Higher values discourage repetition. Defaults to 1.1.

    Returns:
        Dict[str, Union[str, List[Dict[str, str]]]]: The chat completion.
    """
    return llm.create_chat_completion(
        messages=messages,
        response_format=response_format,
        stop=stop,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        min_p=min_p,
        max_tokens=max_tokens,
        repeat_penalty=repeat_penalty,
    )


def get_message_content(completion: Dict[str, Union[str, List[Dict[str, str]]]]) -> str:
    content = completion["choices"][0]["message"]["content"]
    print(content)
    return content


def run_inference_iteration(
    llm: Llama,
    df: pd.DataFrame,
    short_description: str,
    problem_type: str,
    target_variable: str,
    machine_learning_model: str,
    n_new_features: int,
    schema: dict,
    n_unique_values: int = 10,
    perc_digits_after_decimal: int = 25,
    correlations_threshold: float = 0.3,
) -> Dict[str, Union[str, List[Union[str, float]]]]:
    """Runs an inference iteration. Writes the prompt and completion to log files.
    Does not write code. Instead suggests tools and their arguments.

    Args:
        llm (Llama): Model to use.
        df (pd.DataFrame): Dataframe to analyze.
        short_description (str): Short description of the dataset.
        problem_type (str): Type of problem like regression or classification.
        target_variable (str): Target variable to predict.
        machine_learning_model (str): Name of the machine learning model to optimize features for.
        n_new_features (int): Number of new features to suggest in each iteration.
        schema (dict): Schema to use for final json output.
        n_unique_values (int, optional): Number of unique values to describe each column in `df`. Defaults to 10.
        perc_digits_after_decimal (int, optional): Percentage of digits after decimal to describe each column in `df`. Defaults to 25.
        correlations_threshold (float, optional): Threshold for interesting correlations. Defaults to 0.3.

    Returns:
        Dict[str, Union[str, List[Union[str, float]]]]: Description of the new features to create by using the tools and their arguments.
    """
    from src.config import config

    with open(config["project_base_dir"] + r"\src\logs\schema.json", "w") as f:
        f.write(json.dumps(schema))

    unqiue_values = describe_unique_values(
        df=df, n=n_unique_values, perc_digits_after_decimal=perc_digits_after_decimal
    )
    correlations = describe_strong_correlations(df=df, threshold=correlations_threshold)

    function_headers = describe_transformations(
        filename="preprocessing_tools.py",
        skip_args=["df", "drop_old"],
        if_def=False,
        if_backtick=True,
    )

    prompt1 = f"{short_description}**COLUMNS:**\n- *UNIQUE VALUES:*\n{unqiue_values}- *CORRELATIONS:*\n{correlations}\n\n**TOOLS:**\n{function_headers}\n\n**RULES:**\n- You are a feature engineering and selection program that works in iterations.\n- You create new features from existing columns to make ML {machine_learning_model} model better at predicting target variable '{target_variable}' in {problem_type} problem.\n- Target column should remain unchanged as it would be considered cheating.\n- Every iteration you suggest {n_new_features} new column-tool combinations.\n- You don't write code. Instead you suggest tools and their arguments.\n\n**CURRENT ITERATION:**"

    with open(config["project_base_dir"] + r"\src\logs\prompt1.md", "w") as f:
        f.write(prompt1)

    completion1 = create_chat_completion(
        llm=llm,
        messages=[
            {"role": "user", "content": prompt1},
        ],
    )
    message_content = get_message_content(completion1)

    with open(config["project_base_dir"] + r"\src\logs\output1.md", "w") as f:
        f.write(message_content)

    prompt2 = f"**TASK:**\nTurn the content into valid json like on the schema.\nRemember to put values of arguments in correct lists.\n**TOOLS:**\n{function_headers}\n**SCHEMA:**\n{schema}\n**CONTENT**:\n{message_content}\n**JSON:**\n"

    schema["properties"]["transformations"]["items"]["properties"]["columns"]["items"][
        "enum"
    ] = [col for col in df.columns]

    with open(config["project_base_dir"] + r"\src\logs\prompt2.md", "w") as f:
        f.write(prompt2)

    completion2 = create_chat_completion(
        llm=llm,
        messages=[
            {
                "role": "user",
                "content": prompt2,
            },
        ],
        response_format={
            "type": "json_object",
            "schema": schema,
        },
    )

    json_content = json.loads(get_message_content(completion2))
    with open(config["project_base_dir"] + r"\src\logs\output2.json", "w") as f:
        json.dump(json_content, f)

    llm.reset()

    return json_content
