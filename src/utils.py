import ast, os, random
from functools import lru_cache
from pandas import DataFrame, Series
import numpy as np
from typing import Dict, List, Any, Tuple
from sklearn import datasets
from src import tool_handlers
from sklearn.model_selection import cross_val_score
from sklearn.metrics import (
    make_scorer,
    r2_score,
    f1_score,
    explained_variance_score,
    mean_absolute_percentage_error,
    accuracy_score,
)
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import json


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


def describe_strong_correlations(
    df: DataFrame, threshold: float, n_samples: int = 100
) -> str:
    """
    Get a list of pairs of columns in a DataFrame that have a correlation above a certain threshold.

    Parameters:
    df (DataFrame): The DataFrame to calculate correlations on.
    threshold (float): The correlation threshold. Pairs of columns with a correlation above this threshold will be returned.
    n_samples (int): The number of samples to return. Defaults to 100.

    Returns:
    str: A string containing the pairs of columns and their correlations.
    """

    # Get the correlation matrix
    correlations = df.corr()

    # Create a mask to ignore self-
    mask = np.triu(np.ones_like(correlations, dtype=bool))

    # Apply the mask to the correlation matrix
    filtered_corr = correlations.mask(mask)

    # Find where absolute correlation is above the threshold
    strong_correlations = filtered_corr[filtered_corr.abs() > threshold]

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

    # Sort the list of correlations in descending order by absolute value
    sorted_correlations = sorted(
        correlation_list, key=lambda x: abs(x[2]), reverse=True
    )

    # Sample N correlations
    sampled_correlations = random.sample(
        sorted_correlations, min(n_samples, len(sorted_correlations))
    )

    return "\n".join(
        [
            "correlation between '{}' and '{}': {}".format(*corr)
            for corr in sampled_correlations
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


def load_dataset_by_name(name: str) -> Tuple[DataFrame, Series]:
    """Load a dataset by name from the `sklearn.datasets` module.

    Args:
        name (str): The name of the dataset to load. Possible values are: "breast_cancer", "diabetes", "digits", "files", "iris", "linnerud", "sample_image", "sample_images", "wine".

    Returns:
        Tuple[DataFrame, Series]: A tuple containing the features DataFrame and the target Series.

    Example:
        >>> df = load_dataset_by_name("diabetes")
    """

    try:
        load_func = getattr(datasets, f"load_{name}")
        X, y = load_func(return_X_y=True, as_frame=True)
        # Convert the target to numeric if it is non-numeric
        if check_if_dtype(pd.DataFrame(y, columns=["y"]), "y", "Non-numeric"):
            y = LabelEncoder().fit_transform(y)
        X["target"] = y
        return X, y
    except AttributeError:
        print(f"No dataset found with name: {name}")
        return None, None


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
        print(f"No function '{function_name}' found in module: {module.__name__}")
        return None
    except ImportError:
        print(f"No module found with name: {module.__name__}")
        return None


def execute_transformations(
    df: DataFrame,
    transformations: Dict[str, List],
    drop_old: bool = False,
):
    for tr in transformations["transformations"]:
        try:
            columns_before = df.columns
            print(f"Executing transformation: {tr['function']}")
            returned = run_function_by_name(
                tool_handlers,
                tr["function"] + "_handler",
                df,
                tr,
                drop_old,
            )
            if returned is not None:
                column_after = returned.columns
                print(f"Added columns: {set(column_after) - set(columns_before)}")
                df = returned
        except (ValueError, AttributeError) as e:
            print(f"Error in executing transformation: {tr['function']}")
            print(e)
    return df


def cross_validate_model(
    df,
    target,
    target_variable,
    model,
    problem_type,
    cross_val=5,
    scorers: Dict = {
        "classification": accuracy_score,
        "regression": mean_absolute_percentage_error,
    },
):
    # Split the dataset into features (X) and target variable (y)
    try:
        X = df.drop(target_variable, axis=1)
    except KeyError:
        X = df
    y = target

    scorer = scorers[problem_type]

    # Perform cross-validation on the model
    scores = cross_val_score(
        model,
        X,
        y,
        cv=cross_val,
        scoring=make_scorer(scorer),
    )

    # # Calculate the mean and standard deviation of the cross-validation scores
    mean_score = np.mean(scores)
    std_score = np.std(scores)

    print(f"Mean of {scorer.__name__} scores: {mean_score:.2f}")
    print(f"Std of {scorer.__name__} scores: {std_score:.2f}")

    return mean_score, std_score


def calculate_percentage_change(mean_score1, mean_score2, std_score1, std_score2):
    score_change_percentage = ((mean_score2 - mean_score1) / abs(mean_score1)) * 100
    std_change_percentage = ((std_score2 - std_score1) / abs(std_score1)) * 100
    print(f"Mean score change: {score_change_percentage:.2f}%")
    print(f"Std score change: {std_change_percentage:.2f}%")
    return score_change_percentage, std_change_percentage


def remove_duplicate_columns(df):
    df = df.loc[:, ~df.T.duplicated(keep="first")]
    return df


def drop_correlated_columns(df, threshold_features=0.95):
    columns_before = df.columns

    # Recalculate the correlation matrix
    corr_matrix = df.corr().abs()

    # Create a mask for correlations that are above the threshold with any other variable
    high_corr_with_others = np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    high_corr_matrix = corr_matrix.where(high_corr_with_others)

    # Find the first column that has high correlation with any other variable
    to_drop = []
    for column in high_corr_matrix.columns:
        high_corr = high_corr_matrix[column] > threshold_features
        if any(high_corr):
            # Get the name of the first highly correlated column
            correlated_column = high_corr.idxmax()
            to_drop.append(correlated_column)
            print(
                f"Dropping column '{correlated_column}' because of high correlation with '{column}'"
            )

    # Drop the first column that has high correlation with any other variable
    df = df.drop(df[to_drop], axis=1)
    columns_after = df.columns
    print(f"Removed columns: {set(columns_before) - set(columns_after)}")
    return df


def select_most_correlated(df, target, n):
    # Calculate the absolute correlation of each column with the target
    corr_with_target = df.corr()[target].abs()

    # Sort the correlations in descending order
    sorted_corr_with_target = corr_with_target.sort_values(ascending=False)

    # Select the top N columns
    top_n_columns = sorted_corr_with_target.index[
        1 : n + 1
    ]  # We start from 1 to exclude the target itself

    # Return a dataframe with only the selected columns
    return df[top_n_columns]


def handle_invalid_data(df):
    # Replace infinities with np.nan
    df = df.replace(
        [np.inf, -np.inf],
        np.nan,
    )

    # Fill np.nan with most common value in each column
    df = df.fillna(df.mode().iloc[0])

    return df


def default_func(obj):
    """Usage: json_str = json.dumps(data, default=default_func)"""
    # If the object has a __str__ method, use it
    if hasattr(obj, "__str__"):
        return str(obj)
    # Otherwise, use the default behavior
    return json.JSONEncoder.default(obj)
