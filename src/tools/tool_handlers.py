from src.tools.preprocessing_tools import (
    standard_scaler,
    min_max_scaler,
    max_abs_scaler,
    quantile_transformer,
    power_transformer,
    apply_math_function,
    normalizer,
    binarizer,
    polynomial_features,
    k_bins_discretizer,
    ordinal_encoder,
    one_hot_encoder,
    linear_combination,
    create_interaction,
    subtract_columns,
    reduce_dimentionality,
)
from typing import Dict, Union, List


def standard_scaler_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    return standard_scaler(df, column_name, drop_old)


def min_max_scaler_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    return min_max_scaler(df, column_name, drop_old)


def max_abs_scaler_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    return max_abs_scaler(df, column_name, drop_old)


def quantile_transformer_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    n_quantiles = (
        transformation["numerical_arguments"][0]
        if len(transformation["numerical_arguments"]) > 0
        else 100
    )
    output_distribution = (
        transformation["categorical_arguments"][0]
        if len(transformation["categorical_arguments"]) > 0
        else "uniform"
    )
    return quantile_transformer(
        df, column_name, n_quantiles, output_distribution, drop_old
    )


def power_transformer_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    method = (
        transformation["categorical_arguments"][0]
        if len(transformation["categorical_arguments"]) > 0
        else "yeo-johnson"
    )
    return power_transformer(df, column_name, method, drop_old)


def apply_math_function_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    function = (
        transformation["categorical_arguments"][0]
        if len(transformation["categorical_arguments"]) > 0
        else "log"
    )
    return apply_math_function(df, column_name, function, drop_old)


def normalizer_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    norm = (
        transformation["categorical_arguments"][0]
        if len(transformation["categorical_arguments"]) > 0
        else "l2"
    )
    return normalizer(df, column_name, norm, drop_old)


def binarizer_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    threshold = (
        transformation["numerical_arguments"][0]
        if len(transformation["numerical_arguments"]) > 0
        else 0.0
    )
    return binarizer(df, column_name, threshold, drop_old)


def polynomial_features_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    degree = (
        transformation["numerical_arguments"][0]
        if len(transformation["numerical_arguments"]) > 0
        else 2
    )
    return polynomial_features(df, column_name, degree, drop_old)


def k_bins_discretizer_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    column_name = transformation["columns"][0]
    n_bins = (
        transformation["numerical_arguments"][0]
        if len(transformation["numerical_arguments"]) > 0
        else 5
    )
    categorical_argument = (
        transformation["categorical_arguments"][0]
        if len(transformation["categorical_arguments"]) > 0
        else "ordinal"
    )
    if categorical_argument in ["ordinal"]:
        encode = categorical_argument
        strategy = (
            transformation["categorical_arguments"][1]
            if len(transformation["categorical_arguments"]) > 1
            else "quantile"
        )
    else:
        strategy = categorical_argument
        encode = (
            transformation["categorical_arguments"][1]
            if len(transformation["categorical_arguments"]) > 1
            else "ordinal"
        )
    return k_bins_discretizer(df, column_name, n_bins, encode, strategy, drop_old)


def ordinal_encoder_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) > 0:
        column_name = transformation["columns"][0]
    else:
        return df
    return ordinal_encoder(df, column_name, drop_old)


def one_hot_encoder_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) > 0:
        column_name = transformation["columns"][0]
    else:
        return df
    return one_hot_encoder(df, column_name, drop_old)


def linear_combination_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 2:
        return df
    column_name_1 = transformation["columns"][0]
    column_name_2 = transformation["columns"][1]
    if len(transformation["numerical_arguments"]) < 2:
        return linear_combination(df, column_name_1, column_name_2, drop_old=drop_old)
    weight_1 = transformation["numerical_arguments"][0]
    weight_2 = transformation["numerical_arguments"][1]
    return linear_combination(
        df, column_name_1, column_name_2, weight_1, weight_2, drop_old
    )


def create_interaction_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 2:
        return df
    column_name_1 = transformation["columns"][0]
    column_name_2 = transformation["columns"][1]
    return create_interaction(df, column_name_1, column_name_2, drop_old)


def subtract_columns_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 2:
        return df
    column_name_1 = transformation["columns"][0]
    column_name_2 = transformation["columns"][1]
    return subtract_columns(df, column_name_1, column_name_2, drop_old)


def reduce_dimentionality_handler(
    df,
    transformation: Dict[str, Union[str, List[Union[str, int, float]]]],
    drop_old=False,
):
    if len(transformation["columns"]) < 1:
        return df
    columns = transformation["columns"]
    method = (
        transformation["categorical_arguments"][0]
        if len(transformation["categorical_arguments"]) > 0
        else "PCA"
    )
    return reduce_dimentionality(df, columns, method, drop_old)
