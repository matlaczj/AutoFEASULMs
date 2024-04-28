import pandas as pd
from src.utils.validation_utils import check_if_dtype, check_dtype


# Test for check_if_dtype
def test_check_if_dtype():
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"], "C": [True, False, True]})
    assert check_if_dtype(df, "A", "Numeric") == True
    assert check_if_dtype(df, "B", "Non-numeric") == True
    assert check_if_dtype(df, "C", "Numeric") == True
    assert check_if_dtype(df, "A", "Non-numeric") == False


# Test for check_dtype
def test_check_dtype():
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"], "C": [True, False, True]})
    assert check_dtype(df, "A") == "Numeric"
    assert check_dtype(df, "B") == "Non-numeric"
    assert check_dtype(df, "C") == "Numeric"
