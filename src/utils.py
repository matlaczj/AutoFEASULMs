import ast
import os
from typing import Dict
from functools import lru_cache
from typing import Dict, List


def extract_functions_with_args(filename: str) -> Dict[str, List[str]]:
    """
    Extracts function names and their arguments from a given Python file.

    Args:
        filename (str): The name of the Python file.

    Returns:
        Dict[str, List[str]]: A dictionary where keys are function names and values are lists of argument names.

    Examples:
        >>> get_func_names_with_args("def foo(a, b, c=1): pass")
        {'foo': ['a', 'b', 'c']}
    """

    def get_func_args(function_node: ast.FunctionDef) -> List[str]:
        """
        Extracts argument names from a given function node.

        Args:
            function_node (ast.FunctionDef): The function node to extract arguments from.

        Returns:
            List[str]: A list of argument names.

        Examples:
            >>> get_func_args(ast.parse("def foo(a, b, c=1): pass").body[0])
            ['a', 'b', 'c']
        """
        return [arg.arg for arg in function_node.args.args]

    with open(filename, "r") as source:
        tree = ast.parse(source.read())
    functions = {
        node.name: get_func_args(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }
    return functions


def get_model_dict(use_cache: bool = True) -> Dict[str, str]:
    """
    Returns a dictionary mapping model names to their file paths.

    Args:
        use_cache (bool, optional): Whether to use caching. Defaults to True.

    Returns:
        Dict[str, str]: A dictionary where keys are model names and values are file paths.

    Examples:
        >>> get_model_dict()
        {'MODEL1': '/path/to/model1.gguf', 'MODEL2': '/path/to/model2.gguf'}
    """

    def get_model_dict_no_cache(base_dir: str) -> Dict[str, str]:
        """
        Returns a dictionary mapping model names to their file paths, without using cache.

        Args:
            base_dir (str): The base directory to start searching for models.

        Returns:
            Dict[str, str]: A dictionary where keys are model names and values are file paths.
        """
        model_dict = {}

        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".gguf"):
                    value = os.path.join(root, file)
                    key = value.split(os.sep)[-1].replace(".gguf", "").upper()
                    model_dict[key] = value

        return model_dict

    @lru_cache(maxsize=None)
    def get_model_dict_with_cache(base_dir: str) -> Dict[str, str]:
        """
        Returns a dictionary mapping model names to their file paths, using cache.

        Args:
            base_dir (str): The base directory to start searching for models.

        Returns:
            Dict[str, str]: A dictionary where keys are model names and values are file paths.
        """
        return get_model_dict_no_cache(base_dir)

    from config import config

    base_dir = config["model_base_dir"]
    if use_cache:
        model_dict = get_model_dict_with_cache(base_dir)
    else:
        model_dict = get_model_dict_no_cache(base_dir)
    print("Model dictionary loaded. Available models:")
    for key in model_dict.keys():
        print(key)
    return model_dict
