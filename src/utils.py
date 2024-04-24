import ast, os, random
from functools import lru_cache
from pandas import DataFrame
import numpy as np
from typing import Dict, List, Any
from sklearn import datasets


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


def describe_transformations(
    filename: str, skip_args=[], if_def=False, if_backtick=False
) -> str:
    """Extracts function names and their arguments from a given Python file. Then, it returns a string with the function names and their arguments.

    Args:
        filename (str): The name of the Python file.
        skip_args (list, optional): Arguments to skip. Defaults to [].
        if_def (bool, optional): Whether to include 'def' before the function name. Defaults to False.
        if_backtick (bool, optional): Whether to include backticks around the function name. Defaults to False.

    Returns:
        str: A string with the function names and their arguments.
    """
    functions = extract_functions_with_args_and_values(filename)

    function_headers = "\n".join(
        f"""{"def " if if_def else "- "}{'`' if if_backtick else ''}{func}({', '.join(f'{arg}:{functions[func][arg] if functions[func][arg] is not None else ""}' for arg in args if arg not in skip_args)}){'`' if if_backtick else ''}"""
        for func, args in functions.items()
    )
    return function_headers


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
    print("Model dictionary loaded. Available models:")
    for key in model_dict.keys():
        print(key)
    return model_dict


def round_to_percent_digits(number: float, perc: int) -> float:
    """
    Rounds a float number to a percentage of its decimal digits.

    Args:
        number (float): The number to round.
        perc (int): The percentage of decimal digits to keep.

    Returns:
        float: The rounded number.
    """
    # Convert the number to a string
    number_str = str(number)
    # Split the string into the integer and fractional parts
    parts = number_str.split(".")
    if len(parts) == 2:
        # Calculate the number of digits to keep
        digits_to_keep = int(len(parts[1]) * (perc / 100))
        # Convert the number back to a float and round it
        number = round(number, max(2, digits_to_keep))
    return number


def describe_unique_values(
    df: DataFrame, n: int, perc_digits_after_decimal: int = 25
) -> str:
    """This function describes the unique values in each column of a DataFrame.

    Args:
        df (DataFrame): The DataFrame to describe.
        n (int): The number of unique values to display.
        perc_digits_after_decimal (int, optional): The percentage of decimal digits to keep. Defaults to 25%.

    Returns:
        str: A string containing descriptions of the unique values in each column.
    """
    result = ""

    for column in df.columns:
        unique_values = [
            round_to_percent_digits(number=value, perc=perc_digits_after_decimal)
            for value in df[column].unique()
        ]
        if len(unique_values) > n:
            result += f"example unique values in '{column}': {str(random.sample(unique_values, n))[1:-1]} ...\n"
        else:
            result += f"all unique values in '{column}': {str(unique_values)[1:-1]}\n"

    return result


def describe_strong_correlations(df: DataFrame, threshold: float) -> str:
    """
    Get a list of pairs of columns in a DataFrame that have a correlation above a certain threshold.

    Parameters:
    df (DataFrame): The DataFrame to calculate correlations on.
    threshold (float): The correlation threshold. Pairs of columns with a correlation above this threshold will be returned.

    Returns:
    str: A string containing the pairs of columns and their correlations.
    """

    # Get the correlation matrix
    correlations = df.corr()

    # Create a mask to ignore self-
    mask = np.triu(np.ones_like(correlations, dtype=bool))

    # Apply the mask to the correlation matrix
    filtered_corr = correlations.mask(mask)

    # Find where correlation is above the threshold
    strong_correlations = filtered_corr[filtered_corr > threshold]

    # Drop rows and columns with all NaN values (these are the ones below the threshold)
    strong_correlations.dropna(axis=0, how="all", inplace=True)
    strong_correlations.dropna(axis=1, how="all", inplace=True)

    # Convert the DataFrame to a Series with a MultiIndex
    stacked_correlations = strong_correlations.stack()

    # Convert the Series to a list of tuples, including the correlation values
    correlation_list = [
        (index[0], index[1], round(corr, 2))
        for index, corr in stacked_correlations.items()
    ]

    # Sort the list of correlations in descending order
    sorted_correlations = sorted(correlation_list, key=lambda x: x[2], reverse=True)

    return "\n".join(
        [
            "correlation between '{}' and '{}': {}".format(*corr)
            for corr in sorted_correlations
        ]
    )


def check_dtype(df, column_name):
    numeric_types = [
        "int8",
        "int16",
        "int32",
        "int64",
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "float16",
        "float32",
        "float64",
        "complex64",
        "complex128",
    ]
    non_numeric_types = [
        "object",
        "bool",
        "datetime64[ns]",
        "timedelta[ns]",
        "category",
        "period",
        "sparse",
        "interval",
    ]

    if df[column_name].dtypes in numeric_types:
        return "Numeric"
    elif df[column_name].dtypes in non_numeric_types:
        return "Non-numeric"
    else:
        return "Unknown"


def check_if_dtype(df, column_name, dtype):
    if check_dtype(df, column_name) == dtype:
        return True
    else:
        print(f"Column '{column_name}' should be of type '{dtype}'")
        return False


def load_dataset_by_name(name: str) -> DataFrame:
    """Load a dataset by name from the `sklearn.datasets` module.

    Args:
        name (str): The name of the dataset to load. Possible values are: "breast_cancer", "diabetes", "digits", "files", "iris", "linnerud", "sample_image", "sample_images", "wine".

    Returns:
        DataFrame: The loaded dataset with target variable.

    Example:
        >>> df = load_dataset_by_name("diabetes")
    """

    try:
        load_func = getattr(datasets, f"load_{name}")
        X, y = load_func(return_X_y=True, as_frame=True)
        X["target"] = y
        return X
    except AttributeError:
        print(f"No dataset found with name: {name}")
        return None
