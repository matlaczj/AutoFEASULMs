# %%
from llama_cpp import Llama
from typing import List, Dict, Union, Optional
from src.utils.prompting_utils import (
    describe_unique_values,
    describe_strong_correlations,
    describe_transformations,
    describe_optimization_history,
)
import pandas as pd
import json
from func_timeout import func_set_timeout


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
        seed=777,
    )


@func_set_timeout(120)  # Timeout of 2 minutes
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
        seed=777,
    )


def get_message_content(completion: Dict[str, Union[str, List[Dict[str, str]]]]) -> str:
    content = completion["choices"][0]["message"]["content"]
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
    exp_base: str,
    iter: int,
    scores: List[Dict[str, Union[float, List[str]]]],
    n_unique_values: int = 10,
    perc_digits_after_decimal: int = 25,
    correlations_threshold: float = 0.3,
    temperature: float = 0.7,
    n_sampled_corr: int = 100,
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
        exp_base (str): Base directory for the experiment.
        iter (int): Current iteration number.
        scores (List[Dict[str, Union[float, List[str]]]): List of scores from optimization iterations.
        n_unique_values (int, optional): Number of unique values to describe each column in `df`. Defaults to 10.
        perc_digits_after_decimal (int, optional): Percentage of digits after decimal to describe each column in `df`. Defaults to 25.
        correlations_threshold (float, optional): Threshold for interesting correlations. Defaults to 0.3.
        temperature (float, optional): The randomness of the output. Lower values make the output more deterministic. Defaults to 0.7.
        n_sampled_corr (int, optional): Number of samples to use for correlation analysis. Defaults to 100.

    Returns:
        Dict[str, Union[str, List[Union[str, float]]]]: Description of the new features to create by using the tools and their arguments.
    """
    from src.config import config

    unqiue_values = describe_unique_values(
        df=df, n=n_unique_values, perc_digits_after_decimal=perc_digits_after_decimal
    )
    correlations = describe_strong_correlations(
        df=df, threshold=correlations_threshold, n_samples=n_sampled_corr
    )
    optimization_history = (
        (
            "**ITERATION HISTORY:**\n"
            + describe_optimization_history(data=scores, problem_type=problem_type)
            + "\n"
        )
        if iter > 1
        else ""
    )

    function_headers = describe_transformations(
        filename=config["function_header_file_path"],
        skip_args=["df", "drop_old"],
        if_def=False,
        if_backtick=True,
    )

    rules = f"\n**RULES:**\n- You are a feature engineering and selection program that works in iterations and one iteration at a time.\n- You create new features from existing columns to make ML {machine_learning_model} model better at predicting target variable '{target_variable}' in {problem_type} problem.\n- Target column should remain unchanged as it would be considered cheating.\n- Every iteration you suggest {n_new_features} new column-tool combinations.\n- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.\n- You create columns that are highly correlated with target feature.\n- You take into consideration column values, history of iterations, correlations etc. to make better judgements.\n- You don't repeat the same mistake twice expecting different results.\n"

    prompt1 = f"{short_description}**COLUMNS:**\n- *UNIQUE VALUES:*\n{unqiue_values}- *CORRELATIONS:*\n{correlations}\n\n{optimization_history}**TOOLS:**\n{function_headers}\n{rules}\n**CURRENT ITERATION:**"

    with open(exp_base + "prompt1.md", "w", encoding="utf-8") as f:
        f.write(prompt1)

    completion1 = create_chat_completion(
        llm=llm,
        messages=[
            {"role": "user", "content": prompt1},
        ],
        temperature=temperature,
    )
    message_content = get_message_content(completion1)

    with open(exp_base + "output1.md", "w", encoding="utf-8") as f:
        f.write(message_content)

    prompt2 = f"**TASK:**\nTurn the content into valid json like on the schema.\nRemember to put values of arguments in correct lists.\nTool called `apply_math_function` expects `categorical_arguments` to be filled with one of accepted string values and `numerical_arguments` to be empty! Same goes for `normalizer` etc. Look at TOOLS section for accepted values.\n\n**TOOLS:**\n{function_headers}\n\n**SCHEMA:**\n{schema}\n\n**CONTENT**:\n{message_content}\n\n**JSON:**\n"

    schema["properties"]["transformations"]["items"]["properties"]["columns"]["items"][
        "enum"
    ] = [col for col in df.columns]

    with open(exp_base + "schema.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(schema))

    with open(exp_base + "prompt2.md", "w", encoding="utf-8") as f:
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
        temperature=0.8,
    )

    json_content = json.loads(get_message_content(completion2))
    with open(exp_base + "output2.json", "w", encoding="utf-8") as f:
        json.dump(json_content, f)

    return json_content
