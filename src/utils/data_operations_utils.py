import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import fetch_openml
from typing import Dict, List
from pandas import DataFrame
from src.tools import tool_handlers
from src.utils.ast_utils import run_function_by_name
from src.utils.validation_utils import check_if_dtype
from colorama import Fore


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


def one_hot_encode(df, max_columns=10):
    for col in df.columns:
        if df[col].dtype in ["object", "category"]:
            dummies = pd.get_dummies(df[col], prefix=col)
            if len(dummies.columns) <= max_columns:
                df = pd.concat([df, dummies], axis=1)
            df.drop(col, axis=1, inplace=True)
    df = bool_to_int(df)
    return df


def bool_to_int(df):
    for col in df.columns:
        if df[col].dtype == "bool":
            df[col] = df[col].astype("int8")
    return df


def load_openml_dataset(
    name: str,
    target_column: str = "target",
    problem_type: str = None,
    max_records: int = 1000,
):
    """Load a dataset from OpenML by name.
    https://www.openml.org/search?type=data&status=active

    Args:
        name (str): The name of the dataset to load.

    Returns:
        X (pd.DataFrame): The features DataFrame, including the target column.
        y (pd.Series): The target Series.
    """
    print(
        Fore.YELLOW
        + f"Loading dataset: {name}, target_column: {target_column}, problem_type: {problem_type}"
        + Fore.RESET
    )

    data = fetch_openml(name, as_frame=True)
    X = data["data"]
    X[target_column] = data["target"]

    # If number of rows is greater than `max_records`, sample `max_records` rows.
    if X.shape[0] > max_records:
        X = X.sample(max_records, random_state=777)

    # Convert the target to numeric if it is non-numeric
    if check_if_dtype(
        pd.DataFrame(X[target_column], columns=[target_column]),
        target_column,
        "Non-numeric",
    ):
        X[target_column] = LabelEncoder().fit_transform(X[target_column])

    # Because we use MAPE for regression, we need to log-transform the target and add 1
    if problem_type == "regression":
        X[target_column] = np.log(X[target_column] + 1) + 1
    y = X[target_column]

    return X, y


def execute_transformations(
    df: DataFrame,
    transformations: Dict[str, List],
    drop_old: bool = False,
):
    for tr in transformations["transformations"]:
        try:
            columns_before = df.columns
            print(
                Fore.GREEN + f"Executing transformation: {tr['function']}" + Fore.RESET
            )
            returned = run_function_by_name(
                tool_handlers,
                tr["function"] + "_handler",
                df,
                tr,
                drop_old,
            )
            if returned is not None:
                column_after = returned.columns
                print(
                    Fore.GREEN
                    + f"Added columns: {set(column_after) - set(columns_before)}"
                    + Fore.RESET
                )
                if returned.shape[0] == df.shape[0]:
                    df = returned
                else:
                    print(
                        Fore.RED
                        + f"Shape mismatch: {returned.shape[0]} vs {df.shape[0]}. Skipping transformation: {tr['function']}"
                        + Fore.RESET
                    )
        except (ValueError, AttributeError) as e:
            print(
                Fore.RED
                + f"Error in executing transformation: {tr['function']}"
                + Fore.RESET
            )
            print(Fore.RED + str(e) + "\n" + Fore.RESET)
    return df


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
            # Handle the case where the column is an object
            try:
                if df[correlated_column].dtype == "object":
                    print(
                        Fore.RED
                        + f"Column '{correlated_column}' is object"
                        + Fore.RESET
                    )
                    continue
            except Exception as e:
                print(Fore.RED + f"Error: {e}" + Fore.RESET)
                continue
            to_drop.append(correlated_column)
            print(
                Fore.RED
                + f"Dropping column '{correlated_column}' because of high correlation with '{column}'"
                + Fore.RESET
            )

    # Drop the first column that has high correlation with any other variable
    df = df.drop(to_drop, axis=1)
    columns_after = df.columns
    print(
        Fore.RED
        + f"Removed columns: {set(columns_before) - set(columns_after)}\n"
        + Fore.RESET
    )
    return df


def select_most_correlated(df, target, n):
    # Calculate the absolute correlation of each column with the target
    corr_with_target = df.corr()[target].abs()

    # Sort the correlations in descending order
    sorted_corr_with_target = corr_with_target.sort_values(ascending=False)

    # Select the top N columns
    top_n_columns = sorted_corr_with_target.index[
        0:n
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


def transform_date_columns(df):
    for col in df.columns:
        try:
            # If the column is of datetime type
            if np.issubdtype(df[col].dtype, np.datetime64):
                # Try to convert the column to datetime
                df[col] = pd.to_datetime(
                    df[col], errors="raise", infer_datetime_format=True
                )
                df[col + "_year"] = df[col].dt.year
                df[col + "_month"] = df[col].dt.month
                df[col + "_day"] = df[col].dt.day
                df[col + "_dayofweek"] = df[col].dt.dayofweek
                df[col + "_dayofyear"] = df[col].dt.dayofyear

                # Drop the original date column
                df.drop(col, axis=1, inplace=True)
        except Exception as e:
            print(Fore.RED + f"Not Convertible To Datetime {col}: {e}" + Fore.RESET)
            continue
        print("\n")
    return df


def add_noise(df, target_column, noise_perc_of_range):
    """Add Gaussian noise to numeric columns of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to add noise to.
        target_column (str): The name of the target column. Noise will not be added to this column.
        noise_perc_of_range (float): The standard deviation of the Gaussian noise as a fraction of the range of each column.

    Returns:
        df (pd.DataFrame): The DataFrame with noise added.
    """
    np.random.seed(777)

    for col in df.columns:
        if (
            col != target_column
            and np.issubdtype(df[col].dtype, np.number)
            and df[col].nunique() > 2
        ):
            # Compute the range of this column
            col_range = df[col].max() - df[col].min()

            # Generate noise scaled by the range of this column
            noise = np.random.normal(0, noise_perc_of_range * col_range, df[col].shape)

            # Add the noise to this column
            df[col] += noise

    return df


def check_all_columns_are_series(df):
    for column in df.columns:
        if isinstance(df[column], pd.DataFrame):
            print(
                Fore.RED + f"Column '{column}' is a DataFrame. Dropping." + Fore.RESET
            )
            df = df.drop(column, axis=1)
        if df[column].dtype == "object":
            print(
                Fore.RED
                + f"Column '{column}' dtype is an object. Dropping."
                + Fore.RESET
            )
            df = df.drop(column, axis=1)
        if isinstance(df[column].iloc[0], pd.DataFrame):
            print(
                Fore.RED
                + f"Column '{column}' contains a DataFrame. Dropping."
                + Fore.RESET
            )
            df = df.drop(column, axis=1)
        if not isinstance(df[column], pd.Series):
            print(
                Fore.RED + f"Column '{column}' is not a Series. Dropping." + Fore.RESET
            )
            df = df.drop(column, axis=1)
    return df
