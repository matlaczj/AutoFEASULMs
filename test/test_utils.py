import pandas as pd
from src.utils import (
    extract_functions_with_args_and_values,
    describe_transformations,
    get_model_dict,
    round_to_percent_digits,
    describe_unique_values,
    describe_strong_correlations,
)
import pandas as pd
from src.utils import drop_correlated_columns
from sklearn.datasets import (
    load_boston,
    load_diabetes,
    fetch_california_housing,
    load_iris,
    load_breast_cancer,
    load_wine,
)
from utils import load_benchmark_dataset


def test_extract_functions_with_args_and_values():
    # Test with a simple python file
    result = extract_functions_with_args_and_values(r"test\file.py")
    assert isinstance(result, dict)


def test_describe_transformations():
    # Test with a simple python file
    result = describe_transformations(r"test\file.py")
    assert isinstance(result, str)


def test_get_model_dict():
    # Test with use_cache = True
    result = get_model_dict(True)
    assert isinstance(result, dict)

    # Test with use_cache = False
    result = get_model_dict(False)
    assert isinstance(result, dict)


def test_round_to_percent_digits():
    # Test with a float number and a percentage
    result = round_to_percent_digits(123.456789, 50)
    assert isinstance(result, float)


def test_describe_unique_values():
    # Test with a simple DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = describe_unique_values(df, 2)
    assert isinstance(result, str)


def test_describe_strong_correlations():
    # Test with a simple DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = describe_strong_correlations(df, 0.5)
    assert isinstance(result, str)


def test_drop_correlated_columns():
    # Create a DataFrame for testing
    df = pd.DataFrame(
        {
            "target": [1, 2, 3, 4, 5],
            "low_corr": [
                1,
                1,
                1,
                1,
                1,
            ],  # This column has low correlation with the target
            "high_corr1": [
                1,
                2,
                3,
                4,
                5,
            ],  # These two columns have high correlation with each other
            "high_corr2": [1, 2, 3, 4, 5],
            "unrelated": [
                5,
                4,
                3,
                2,
                1,
            ],  # This column is not correlated with the target or any other column
        }
    )

    # Apply the function
    result = drop_correlated_columns(df, "target")

    # Check that the low_corr column was dropped
    assert "low_corr" not in result.columns

    # Check that only one of the high_corr columns was dropped
    assert ("high_corr1" in result.columns) != ("high_corr2" in result.columns)

    # Check that the unrelated column was not dropped
    assert "unrelated" in result.columns

    # Check that the target column was not dropped
    assert "target" in result.columns


def test_load_benchmark_dataset():
    # Test loading the boston dataset
    X, y = load_benchmark_dataset("boston")
    assert X is not None
    assert y is not None
    assert X.shape == load_boston(return_X_y=False, as_frame=True)["data"].shape
    assert y.shape == load_boston(return_X_y=False, as_frame=True)["target"].shape

    # Test loading the diabetes dataset
    X, y = load_benchmark_dataset("diabetes")
    assert X is not None
    assert y is not None
    assert X.shape == load_diabetes(return_X_y=False, as_frame=True)["data"].shape
    assert y.shape == load_diabetes(return_X_y=False, as_frame=True)["target"].shape

    # Test loading the california dataset
    X, y = load_benchmark_dataset("california")
    assert X is not None
    assert y is not None
    assert (
        X.shape
        == fetch_california_housing(return_X_y=False, as_frame=True)["data"].shape
    )
    assert (
        y.shape
        == fetch_california_housing(return_X_y=False, as_frame=True)["target"].shape
    )

    # Test loading the iris dataset
    X, y = load_benchmark_dataset("iris")
    assert X is not None
    assert y is not None
    assert X.shape == load_iris(return_X_y=False, as_frame=True)["data"].shape
    assert y.shape == load_iris(return_X_y=False, as_frame=True)["target"].shape

    # Test loading the breast_cancer dataset
    X, y = load_benchmark_dataset("breast_cancer")
    assert X is not None
    assert y is not None
    assert X.shape == load_breast_cancer(return_X_y=False, as_frame=True)["data"].shape
    assert (
        y.shape == load_breast_cancer(return_X_y=False, as_frame=True)["target"].shape
    )

    # Test loading the wine dataset
    X, y = load_benchmark_dataset("wine")
    assert X is not None
    assert y is not None
    assert X.shape == load_wine(return_X_y=False, as_frame=True)["data"].shape
    assert y.shape == load_wine(return_X_y=False, as_frame=True)["target"].shape

    # Test loading a non-existent dataset
    X, y = load_benchmark_dataset("non_existent")
    assert X is None
    assert y is None
