import pytest
import pandas as pd
import numpy as np
import os
from src.utils import *


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


def test_check_dtype():
    # Test with a simple DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
    assert check_dtype(df, "A") == "Numeric"
    assert check_dtype(df, "B") == "Non-numeric"


def test_check_if_dtype():
    # Test with a simple DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
    assert check_if_dtype(df, "A", "Numeric") == True
    assert check_if_dtype(df, "B", "Non-numeric") == True
    assert check_if_dtype(df, "A", "Non-numeric") == False
