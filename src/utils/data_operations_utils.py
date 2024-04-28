# %%
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import fetch_openml
from typing import Dict, List, Tuple
from pandas import DataFrame, Series
from src.tools import tool_handlers
from src.utils.ast_utils import run_function_by_name
from src.utils.validation_utils import check_if_dtype


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
    return df


def load_openml_dataset(name: str):
    """Load a dataset from OpenML by name.
    https://www.openml.org/search?type=data&status=active

    Args:
        name (str): The name of the dataset to load.

    Returns:
        X (pd.DataFrame): The features DataFrame, including the target column.
        y (pd.Series): The target Series.
    """
    data = fetch_openml(name, as_frame=True)
    X = data["data"]
    X["target"] = data["target"]
    # Convert the target to numeric if it is non-numeric
    if check_if_dtype(
        pd.DataFrame(X["target"], columns=["target"]), "target", "Non-numeric"
    ):
        X["target"] = LabelEncoder().fit_transform(X["target"])
    y = X["target"]
    return X, y


def preprocess_loaded_dataset(
    df: DataFrame, target_variable: str
) -> Tuple[DataFrame, Series]:
    # Handle invalid data
    df = handle_invalid_data(df)

    # Encode target variable if it is non-numeric
    if check_if_dtype(df, target_variable, "Non-numeric"):
        df[target_variable] = LabelEncoder().fit_transform(df[target_variable])

    # Transform date columns
    df = transform_date_columns(df)

    # One-hot encode non-numeric columns
    df = one_hot_encode(df)

    # Select only numeric columns
    df = df.select_dtypes(include=["number", "bool"])

    # Rename target variable to 'target'
    df = df.rename(columns={target_variable: "target"})

    # Create a separate Series for the target variable
    target = df["target"].copy()

    return df, target


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
    df = df.drop(to_drop, axis=1)
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
            print(f"Not Convertible To Datetime {col}: {e}")
            continue
    return df


# %%
