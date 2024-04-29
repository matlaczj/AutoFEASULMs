from typing import Any, Dict, List
import ast, os
from functools import lru_cache
from colorama import Fore


def extract_functions_with_args_and_values(filename: str) -> Dict[str, Dict[str, Any]]:
    def get_func_args(function_node: ast.FunctionDef) -> List[str]:
        return [arg.arg for arg in function_node.args.args]

    def eval_value(node: ast.AST) -> Any:
        if isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.List):
            return [eval_value(elt) for elt in node.elts]
        elif isinstance(node, ast.Dict):
            return {
                eval_value(key): eval_value(value)
                for key, value in zip(node.keys, node.values)
            }
        else:
            return None

    def get_vars_with_suffix(node: ast.AST, suffix: str) -> Dict[str, Any]:
        return {
            target.id: eval_value(stmt.value)
            for stmt in node.body
            if isinstance(stmt, ast.Assign)
            for target in stmt.targets
            if isinstance(target, ast.Name) and target.id.endswith(suffix)
        }

    with open(filename, "r") as source:
        tree = ast.parse(source.read())
    functions = {
        node.name: {
            arg: vars.get(arg + "_accepted", None) for arg in get_func_args(node)
        }
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        for vars in [get_vars_with_suffix(node, "_accepted")]
    }

    return functions


def run_function_by_name(module, function_name: str, *args, **kwargs):
    """Run a function by its name from a specified module.

    Args:
        module: The name of the module where the function is located.
        function_name (str): The name of the function to run.
        *args: Variable length argument list to pass to the function.
        **kwargs: Arbitrary keyword arguments to pass to the function.

    Returns:
        The return value of the function call.

    Example:
        >>> result = run_function_by_name("math", "sqrt", 16)
    """
    try:
        func = getattr(module, function_name)
        return func(*args, **kwargs)
    except AttributeError:
        print(
            f"{Fore.RED}No function '{function_name}' found in module: {module.__name__}{Fore.RESET}\n"
        )
        return None
    except ImportError:
        print(f"{Fore.RED}No module found with name: {module.__name__}{Fore.RESET}\n")
        return None


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

    from src.config import config

    base_dir = config["model_base_dir"]
    if use_cache:
        model_dict = get_model_dict_with_cache(base_dir)
    else:
        model_dict = get_model_dict_no_cache(base_dir)
    print(Fore.GREEN + f"Model dictionary loaded. Available models:\n" + Fore.RESET)
    for key in model_dict.keys():
        print(Fore.GREEN + key + Fore.RESET)
    return model_dict
