# %%
from typing import Dict
from llama_cpp import Llama
from typing import List, Dict, Union, Optional


def initialize_llm(
    model_path: str,
    chat_format: str,
    n_gpu_layers: int = -1,
    n_ctx: int = 512 * 2,
    n_batch=512 * 1,
) -> Llama:
    """
    Initializes a Llama language model.

    Args:
        model_path (str): The path to the model file.
        chat_format (str): The format of the chat.
        n_gpu_layers (int, optional): The number of GPU layers. Defaults to -1.
        n_ctx (int, optional): The context size. Defaults to 1024.
        n_batch (int, optional): The batch size. Defaults to 512.

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
