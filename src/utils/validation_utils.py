import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, mean_absolute_percentage_error, make_scorer
from typing import Dict


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
        "bool",
        "datetime64[ns]",
        "timedelta[ns]",
        "category",
        "period",
        "sparse",
        "interval",
    ]

    if df[column_name].dtypes in numeric_types:
        return "Numeric"
    elif df[column_name].dtypes in non_numeric_types:
        return "Non-numeric"
    else:
        return "Unknown"


def cross_validate_model(
    df,
    target,
    target_variable,
    model,
    problem_type,
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

    # Perform cross-validation on the model
    scores = cross_val_score(
        model,
        X,
        y,
        cv=cross_val,
        scoring=make_scorer(scorer),
    )

    # # Calculate the mean and standard deviation of the cross-validation scores
    mean_score = np.mean(scores)
    std_score = np.std(scores)

    print(f"Mean of {scorer.__name__} scores: {mean_score:.2f}")
    print(f"Std of {scorer.__name__} scores: {std_score:.2f}")

    return mean_score, std_score
