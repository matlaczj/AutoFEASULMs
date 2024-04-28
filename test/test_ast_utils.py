import pytest
import math
from src.utils.ast_utils import run_function_by_name


# Test for run_function_by_name
def test_run_function_by_name():
    # Test with a valid function
    result = run_function_by_name(math, "sqrt", 16)
    assert result == 4.0

    # Test with a function that doesn't exist in the module
    assert run_function_by_name(math, "non_existent_function", 16) == None

    # Test with a function that requires more arguments
    with pytest.raises(TypeError):
        run_function_by_name(math, "pow", 2) == None

    # Test with a function that requires keyword arguments
    result = run_function_by_name(math, "pow", 2, 3)
    assert result == 8.0
