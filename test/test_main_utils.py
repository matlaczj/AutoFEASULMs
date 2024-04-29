from src.utils.main_utils import check_early_stopping


def test_check_early_stopping():
    # Test case: early stopping should not be triggered
    scores = [{"mean_score": i} for i in range(1, 6)]
    assert not check_early_stopping(3, 0.1, "regression", scores, 2)

    # Test case: early stopping should be triggered for regression problem
    scores = [{"mean_score": i} for i in range(1, 6)]
    assert check_early_stopping(3, 0.1, "regression", scores, 4)

    # Test case: early stopping should be triggered for non-regression problem
    scores = [{"mean_score": i} for i in reversed(range(1, 6))]
    assert check_early_stopping(3, 0.1, "classification", scores, 4)

    # Test case: early stopping should not be triggered if iteration is less than k
    scores = [{"mean_score": i} for i in range(1, 6)]
    assert not check_early_stopping(5, 0.1, "regression", scores, 4)

    # Test case: early stopping should not be triggered if percentage changes are less than threshold
    scores = [{"mean_score": i} for i in range(1, 6)]
    assert not check_early_stopping(3, 0.5, "regression", scores, 4)

    # Test case: early stopping should be triggered if percentage changes are greater than threshold
    scores = [{"mean_score": i} for i in range(1, 6)]
    assert check_early_stopping(3, 0.1, "regression", scores, 4)

    # Test case: early stopping should not be triggered if percentage changes are greater than threshold for non-regression problem
    scores = [{"mean_score": i} for i in range(1, 6)]
    assert not check_early_stopping(3, 0.1, "classification", scores, 4)

    # Test case: early stopping should be triggered if percentage changes are less than negative threshold for non-regression problem
    scores = [{"mean_score": i} for i in reversed(range(1, 6))]
    assert check_early_stopping(3, 0.1, "classification", scores, 4)
