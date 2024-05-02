import pandas as pd
from src.utils.prompting_utils import (
    describe_transformations,
    describe_unique_values,
    describe_strong_correlations,
    describe_optimization_history,
)
from src.config import config
from pytest import raises


# Test for describe_transformations
def test_describe_transformations():
    filename = config["project_base_dir"] + r"\src\utils\prompting_utils.py"
    result = describe_transformations(filename)
    assert (
        "describe_transformations(filename:, skip_args:, if_def:, if_backtick:)"
        in result
    )
    assert "describe_unique_values(df:, n:, perc_digits_after_decimal:)" in result
    assert "describe_strong_correlations(df:, threshold:, n_samples:)" in result


# Test for describe_unique_values
def test_describe_unique_values():
    df = pd.DataFrame({"A": [1, 2, 3, 1, 2, 3], "B": ["a", "b", "c", "a", "b", "c"]})
    result = describe_unique_values(df, 2)
    assert "example unique values in 'A': 1, 2 ...\n" in result
    assert "example unique values in 'B': 'b', 'c' ...\n" in result
    result = describe_unique_values(df, 4)
    assert "all unique values in 'A': 1, 2, 3\n" in result
    assert "all unique values in 'B': 'a', 'b', 'c'\n" in result


# Test for describe_strong_correlations
def test_describe_strong_correlations():
    df = pd.DataFrame(
        {"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10], "C": [5, 4, 3, 2, 1]}
    )
    result = describe_strong_correlations(df, 0.9, 100)
    assert "correlation between 'B' and 'A': 1.0\n" in result
    assert "correlation between 'C' and 'A': -1.0\n" in result
    assert "correlation between 'C' and 'B': -1.0" in result


def test_describe_optimization_history_classification():
    data = [
        {"mean_score": 0.8, "columns": ["col1", "col2", "col3"]},
        {"mean_score": 0.85, "columns": ["col1", "col2", "col4"]},
    ]
    result = describe_optimization_history(data, "classification")
    expected = "Score change relative to previous iteration: 6.25%\nAdded columns: {'col4'}\nRemoved columns: {'col3'}\n"
    assert result == expected


def test_describe_optimization_history_regression():
    data = [
        {"mean_score": 0.2, "columns": ["col1", "col2", "col3"]},
        {"mean_score": 0.15, "columns": ["col1", "col2", "col4"]},
    ]
    result = describe_optimization_history(data, "regression")
    expected = "Error change relative to previous iteration: -25.00%\nAdded columns: {'col4'}\nRemoved columns: {'col3'}\n"
    assert result == expected


def test_describe_optimization_history_no_change():
    data = [
        {"mean_score": 0.8, "columns": ["col1", "col2", "col3"]},
        {"mean_score": 0.8, "columns": ["col1", "col2", "col3"]},
    ]
    result = describe_optimization_history(data, "classification")
    expected = "Score change relative to previous iteration: 0.00%\nAdded columns: set()\nRemoved columns: set()\n"
    assert result == expected


def test_describe_optimization_history_empty_data():
    with raises(IndexError):
        describe_optimization_history([], "classification")
