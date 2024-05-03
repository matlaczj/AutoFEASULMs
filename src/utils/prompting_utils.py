from pandas import DataFrame
import numpy as np
import random
from src.utils.ast_utils import extract_functions_with_args_and_values
from src.utils.data_operations_utils import round_to_percent_digits
from typing import List, Dict, Union


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
    random.seed(777)

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
    random.seed(777)

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

    # Sample N correlations
    sampled_correlations = random.sample(
        correlation_list,
        min(n_samples, len(correlation_list)),
    )

    # Sort the list of correlations in descending order by absolute value
    sorted_correlations = sorted(
        sampled_correlations, key=lambda x: abs(x[2]), reverse=True
    )

    return "\n".join(
        [
            "correlation between '{}' and '{}': {}".format(*corr)
            for corr in sorted_correlations
        ]
    )


def describe_optimization_history(
    data: List[Dict[str, Union[float, List[str]]]], problem_type: str
) -> None:
    """
    This function describes the optimization process based on the data from the optimization iterations.

    Parameters:
    data (List[Dict[str, Union[float, List[str]]]]): A list of dictionaries containing iteration data.
    problem_type (str): The type of problem, either "classification" or "regression".

    Returns:
    None
    """
    # Initialize an empty string to store all prompts
    all_prompts = ""

    # Loop over the data list from the second element
    for i in range(1, len(data)):
        # Get the data for the current and previous iterations
        current_iter = data[i]
        previous_iter = data[i - 1]
        # Extract the relevant information
        current_score = current_iter["mean_score"]
        current_columns = current_iter["columns"]
        previous_score = previous_iter["mean_score"]
        previous_columns = previous_iter["columns"]
        # Calculate the changes in score and columns
        added_columns = set(current_columns) - set(previous_columns)
        removed_columns = set(previous_columns) - set(current_columns)
        score_change_perc = (current_score - previous_score) / previous_score * 100
        # Assemble the prompt for this iteration
        prompt = f"""Iteration {i}:\n{"Score" if problem_type == "classification" else "Error"} change relative to previous iteration: {score_change_perc:.2f}%\nAdded columns: {added_columns}\nRemoved columns: {removed_columns}\n"""
        # Add the prompt for this iteration to all_prompts
        all_prompts += prompt

    return all_prompts
