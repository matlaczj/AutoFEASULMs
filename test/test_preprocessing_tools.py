# %%
from sklearn import datasets
import pandas as pd
import pytest
from src.preprocessing_tools import (
    standard_scaler,
    min_max_scaler,
    max_abs_scaler,
    quantile_transformer,
    power_transformer,
    normalizer,
    binarizer,
    polynomial_features,
    k_bins_discretizer,
    ordinal_encoder,
    one_hot_encoder,
    linear_combination,
    apply_math_function,
    create_interaction,
)


iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)


@pytest.mark.parametrize(
    "column",
    ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
)
def test_standard_scaler(column):
    result = standard_scaler(df, column)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "column",
    ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
)
def test_min_max_scaler(column):
    result = min_max_scaler(df, column)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "column",
    ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
)
def test_max_abs_scaler(column):
    result = max_abs_scaler(df, column)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "n_quantiles,output_distribution,column",
    [
        (10, "uniform", "sepal length (cm)"),
        (50, "normal", "sepal width (cm)"),
        (100, "uniform", "petal length (cm)"),
    ],
)
def test_quantile_transformer(n_quantiles, output_distribution, column):
    result = quantile_transformer(
        df,
        column,
        n_quantiles=n_quantiles,
        output_distribution=output_distribution,
    )
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "method,column",
    [("yeo-johnson", "sepal length (cm)"), ("box-cox", "sepal width (cm)")],
)
def test_power_transformer(method, column):
    result = power_transformer(df, column, method=method)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "norm,column",
    [
        ("l1", "sepal length (cm)"),
        ("l2", "sepal width (cm)"),
        ("max", "petal length (cm)"),
    ],
)
def test_normalizer(norm, column):
    result = normalizer(df, column, norm=norm)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "threshold,column",
    [(0.0, "sepal length (cm)"), (0.5, "sepal width (cm)"), (1.0, "petal length (cm)")],
)
def test_binarizer(threshold, column):
    result = binarizer(df, column, threshold=threshold)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "degree,column",
    [(2, "sepal length (cm)"), (3, "sepal width (cm)"), (4, "petal length (cm)")],
)
def test_polynomial_features(degree, column):
    result = polynomial_features(df, column, degree=degree)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "n_bins,encode,strategy,column",
    [
        (5, "onehot", "quantile", "sepal length (cm)"),
        (3, "ordinal", "uniform", "sepal width (cm)"),
        (4, "onehot", "quantile", "petal length (cm)"),
        (2, "ordinal", "uniform", "petal width (cm)"),
    ],
)
def test_k_bins_discretizer(n_bins, encode, strategy, column):
    result = k_bins_discretizer(
        df, column, n_bins=n_bins, encode=encode, strategy=strategy
    )
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "column",
    ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
)
def test_ordinal_encoder(column):
    result = ordinal_encoder(df, column)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "column",
    ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
)
def test_one_hot_encoder(column):
    result = one_hot_encoder(df, column)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "column1,column2",
    [
        ("sepal length (cm)", "sepal width (cm)"),
        ("petal length (cm)", "petal width (cm)"),
        ("sepal length (cm)", "petal length (cm)"),
        ("sepal width (cm)", "petal width (cm)"),
    ],
)
def test_linear_combination(column1, column2):
    result = linear_combination(df, column1, column2)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "function,column",
    [
        ("log", "sepal length (cm)"),
        ("sqrt", "sepal width (cm)"),
        ("exp", "petal length (cm)"),
        ("square", "petal width (cm)"),
        ("cube", "sepal length (cm)"),
        ("inverse", "sepal width (cm)"),
        ("log2", "petal length (cm)"),
        ("log10", "petal width (cm)"),
        ("abs", "sepal length (cm)"),
        ("ceil", "sepal width (cm)"),
        ("floor", "petal length (cm)"),
        ("round", "petal width (cm)"),
    ],
)
def test_apply_math_function(function, column):
    result = apply_math_function(df, column, function=function)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize(
    "column1,column2",
    [
        ("sepal length (cm)", "sepal width (cm)"),
        ("petal length (cm)", "petal width (cm)"),
        ("sepal length (cm)", "petal length (cm)"),
        ("sepal width (cm)", "petal width (cm)"),
    ],
)
def test_create_interaction(column1, column2):
    result = create_interaction(df, column1, column2)
    assert isinstance(result, pd.DataFrame)


# %%
