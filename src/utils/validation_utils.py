import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, mean_absolute_percentage_error, make_scorer
from typing import Dict
from colorama import Fore
from pandas import Series


def check_if_dtype(df, column_name, dtype):
    if check_dtype(df, column_name) == dtype:
        return True
    else:
        return False


def check_dtype(df, column_name):
    numeric_types = [
        "int8",
        "int16",
        "int32",
        "int64",
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "float16",
        "float32",
        "float64",
        "complex64",
        "complex128",
    ]
    non_numeric_types = [
        "object",
        "datetime64[ns]",
        "timedelta[ns]",
        "category",
        "period",
        "sparse",
        "interval",
        "bool",
    ]

    if df[column_name].dtypes in numeric_types:
        return "Numeric"
    elif df[column_name].dtypes in non_numeric_types:
        return "Non-numeric"
    else:
        return "Unknown"


from sklearn.model_selection import GridSearchCV


def cross_validate_model(
    df,
    target: Series,
    target_variable: str,
    model,
    problem_type,
    param_grid,
    cross_val=5,
    scorers: Dict = {
        "classification": accuracy_score,
        "regression": mean_absolute_percentage_error,
    },
):
    # Split the dataset into features (X) and target variable (y)
    try:
        X = df.drop(target_variable, axis=1)
    except KeyError:
        X = df
    y = target

    # Select only numeric columns from X
    X = X.select_dtypes(include=["number", "bool"])

    scorer = scorers[problem_type]

    # Perform hyperparameter tuning using GridSearchCV
    grid_search = GridSearchCV(
        model,
        param_grid,
        cv=cross_val,
        scoring=make_scorer(scorer),
        return_train_score=True,
    )
    print(f"{Fore.GREEN}Performing GridSearchCV.")
    grid_search.fit(X, y)
    print(f"{Fore.GREEN}GridSearchCV completed.\n")

    # Get the best model
    best_model = grid_search.best_estimator_

    # Perform cross-validation on the best model
    scores = cross_validate(
        best_model,
        X,
        y,
        cv=cross_val,
        scoring=make_scorer(scorer),
        return_train_score=True,
    )

    # Calculate the mean and standard deviation of the cross-validation scores
    mean_test_score = np.mean(scores["test_score"])
    std_test_score = np.std(scores["test_score"])

    mean_train_score = np.mean(scores["train_score"])
    std_train_score = np.std(scores["train_score"])

    print(f"{Fore.GREEN}Mean of test {scorer.__name__} scores: {mean_test_score:.2f}")
    print(f"{Fore.GREEN}Std of test {scorer.__name__} scores: {std_test_score:.2f}\n")

    print(f"{Fore.GREEN}Mean of train {scorer.__name__} scores: {mean_train_score:.2f}")
    print(f"{Fore.GREEN}Std of train {scorer.__name__} scores: {std_train_score:.2f}\n")

    return mean_test_score, std_test_score, mean_train_score, std_train_score
