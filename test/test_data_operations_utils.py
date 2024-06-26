import pandas as pd
import numpy as np
from src.utils.data_operations_utils import (
    round_to_percent_digits,
    one_hot_encode,
    load_openml_dataset,
    execute_transformations,
    drop_correlated_columns,
    select_most_correlated,
    handle_invalid_data,
    default_func,
    transform_date_columns,
    bool_to_int,
    check_all_columns_are_series,
)


# Test for round_to_percent_digits
def test_round_to_percent_digits():
    assert round_to_percent_digits(123.456789, 50) == 123.457
    assert round_to_percent_digits(123.456789, 100) == 123.456789
    assert round_to_percent_digits(123.456789, 0) == 123.46
    assert round_to_percent_digits(123, 50) == 123
    assert round_to_percent_digits(123, 0) == 123
    assert round_to_percent_digits(123, 100) == 123


# Test for one_hot_encode
def test_one_hot_encode():
    df = pd.DataFrame({"A": ["a", "b", "a"], "B": ["b", "a", "c"], "C": [1, 2, 3]})
    df_encoded = one_hot_encode(df)
    assert "A_a" in df_encoded.columns
    assert "A_b" in df_encoded.columns
    assert "B_a" in df_encoded.columns
    assert "B_b" in df_encoded.columns
    assert "B_c" in df_encoded.columns
    assert "C" in df_encoded.columns
    assert "C_1" not in df_encoded.columns
    assert "C_2" not in df_encoded.columns
    assert "C_3" not in df_encoded.columns


# Test for load_openml_dataset
def test_load_openml_dataset():
    X, y = load_openml_dataset("iris")
    assert X.shape[0] == y.shape[0]
    assert "target" in X.columns


# Test for execute_transformations
def test_execute_transformations():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    transformations = {
        "transformations": [
            {
                "function": "create_interaction",
                "columns": ["A", "B"],
                "numerical_arguments": [],
                "categorical_arguments": [],
            },
        ]
    }
    df = execute_transformations(df, transformations)
    assert "A_B_inter" in df.columns
    assert df["A_B_inter"].equals(df["A"] * df["B"])


# Test for drop_correlated_columns
def test_drop_correlated_columns():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [1, 2, 3], "C": [4, 5, 6]})
    df = drop_correlated_columns(df, 0.9)
    assert "A" not in df.columns
    assert "B" in df.columns
    assert "C" in df.columns


# Test for select_most_correlated
def test_select_most_correlated():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "target": [1, 2, 3]})
    df = select_most_correlated(df, "target", 1)
    assert "A" in df.columns
    assert "B" not in df.columns


# Test for handle_invalid_data
def test_handle_invalid_data():
    df = pd.DataFrame({"A": [1, 2, np.inf], "B": [4, 5, 6]})
    df = handle_invalid_data(df)
    assert list(df["A"]) == [1, 2, 1]


# Test for default_func
def test_default_func():
    class TestClass:
        def __str__(self):
            return "test"

    assert default_func(TestClass()) == "test"
    assert default_func(123) == "123"


# Test for transform_date_columns
def test_transform_date_columns():
    df = pd.DataFrame({"A": pd.date_range(start="1/1/2018", periods=3)})
    df = transform_date_columns(df)
    assert "A_year" in df.columns
    assert "A_month" in df.columns
    assert "A_day" in df.columns
    assert "A_dayofweek" in df.columns
    assert "A_dayofyear" in df.columns
    assert "A" not in df.columns


def test_bool_to_int():
    # Create a DataFrame with boolean values
    df = pd.DataFrame(
        {
            "A": [True, False, True],
            "B": [False, False, True],
            "C": [1, 2, 3],  # non-boolean column
        }
    )

    # Convert boolean columns to integers
    df = bool_to_int(df)

    # Check that the data types of the columns are correct
    assert df["A"].dtype == "int8"


def test_check_all_columns_are_series():
    # Test 1: All columns are Series
    df1 = pd.DataFrame({"A": pd.Series([1, 2, 3]), "B": pd.Series([4, 5, 6])})
    assert check_all_columns_are_series(df1).equals(df1)

    # Test 2: One column is not a Series
    df2 = pd.DataFrame(
        {"A": pd.Series([1, 2, 3]), "B": [4, 5, 6]}  # This column is not a Series
    )
    assert check_all_columns_are_series(df2).equals(df1)
