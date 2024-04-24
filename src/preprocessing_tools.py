import numpy as np
import pandas as pd
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    MaxAbsScaler,
    QuantileTransformer,
    PowerTransformer,
    Normalizer,
    OrdinalEncoder,
    OneHotEncoder,
    Binarizer,
    PolynomialFeatures,
    KBinsDiscretizer,
    FunctionTransformer,
)
from src.utils import check_if_dtype

# NOTE:
# 1. Every variable ending with '_accepted' is a special variable that is extracted by another script to create prompt. Function headers are also extracted by that script.
# 2. After adding a new function, remember to manually update `response_schemas.py` file and `tool_handlers.py` file.


def standard_scaler(df, column_name, drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    scaler = StandardScaler()
    new_column_name = f"{column_name}_standard_scaled"
    df[new_column_name] = scaler.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def min_max_scaler(df, column_name, drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    scaler = MinMaxScaler()
    new_column_name = f"{column_name}_min_max_scaled"
    df[new_column_name] = scaler.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def max_abs_scaler(df, column_name, drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    scaler = MaxAbsScaler()
    new_column_name = f"{column_name}_max_abs_scaled"
    df[new_column_name] = scaler.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def quantile_transformer(
    df, column_name, n_quantiles=100, output_distribution="uniform", drop_old=False
):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    n_quantiles_accepted = np.arange(2, 101)
    output_distribution_accepted = ["uniform", "normal"]
    if output_distribution not in output_distribution_accepted:
        raise ValueError("output_distribution must be either 'uniform' or 'normal'")
    if n_quantiles not in n_quantiles_accepted:
        raise ValueError("n_quantiles must be between 2 and 101")
    transformer = QuantileTransformer(
        n_quantiles=n_quantiles, output_distribution=output_distribution
    )
    new_column_name = (
        f"{column_name}_quantile_transformed_{n_quantiles}_{output_distribution}"
    )
    df[new_column_name] = transformer.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def power_transformer(df, column_name, method="yeo-johnson", drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    method_accepted = ["yeo-johnson", "box-cox"]
    if method not in method_accepted:
        raise ValueError("method must be either 'yeo-johnson' or 'box-cox'")
    transformer = PowerTransformer(method=method)
    new_column_name = f"{column_name}_power_transformed_{method}"
    df[new_column_name] = transformer.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def apply_math_function(df, column_name, function, drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    function_accepted = [
        "log",
        "sqrt",
        "exp",
        "square",
        "cube",
        "inverse",
        "log2",
        "log10",
        "abs",
        "ceil",
        "floor",
        "round",
    ]
    if function not in function_accepted:
        raise ValueError(f"Unknown function: {function}")
    function_dict = {
        "log": np.log,
        "sqrt": np.sqrt,
        "exp": np.exp,
        "square": np.square,
        "cube": lambda x: np.power(x, 3),
        "inverse": np.reciprocal,
        "log2": np.log2,
        "log10": np.log10,
        "abs": np.abs,
        "ceil": np.ceil,
        "floor": np.floor,
        "round": np.round,
    }
    transformer = FunctionTransformer(func=function_dict[function])
    df[f"{column_name}_{function}"] = transformer.transform(df[[column_name]]).fillna(0)
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def normalizer(df, column_name, norm="l2", drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    norm_accepted = ["l1", "l2", "max"]
    if norm not in norm_accepted:
        raise ValueError("norm must be either 'l1', 'l2', or 'max'")
    transformer = Normalizer(norm=norm)
    new_column_name = f"{column_name}_normalized_{norm}"
    df[new_column_name] = transformer.transform(df[[column_name]].values)
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def binarizer(df, column_name, threshold=0.0, drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    transformer = Binarizer(threshold=threshold)
    new_column_name = f"{column_name}_binarized_{threshold}"
    df[new_column_name] = transformer.transform(df[[column_name]].values)
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def polynomial_features(df, column_name, degree=2, drop_old=False):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    degree_accepted = np.arange(2, 11)
    if degree not in degree_accepted:
        raise ValueError("degree must be between 2 and 10")
    transformer = PolynomialFeatures(degree=degree, include_bias=False)
    transformed = transformer.fit_transform(df[[column_name]])
    new_column_names = [f"{column_name}_poly_{i}" for i in range(2, degree + 1)]
    df = pd.concat(
        [df, pd.DataFrame(transformed[:, 1:], columns=new_column_names)], axis=1
    )
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def k_bins_discretizer(
    df, column_name, n_bins=5, encode="ordinal", strategy="quantile", drop_old=False
):
    if not check_if_dtype(df, column_name, "Numeric"):
        return df
    n_bins_accepted = np.arange(2, 101)
    encode_accepted = ["ordinal"]
    strategy_accepted = ["uniform", "quantile", "kmeans"]
    if encode not in encode_accepted:
        raise ValueError("encode must be 'ordinal'")
    if strategy not in strategy_accepted:
        raise ValueError("strategy must be either 'uniform', 'quantile', or 'kmeans'")
    if n_bins not in n_bins_accepted:
        raise ValueError("n_bins must be between 2 and 20")
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode=encode, strategy=strategy)
    transformed = discretizer.fit_transform(df[[column_name]])
    new_column_name = f"{column_name}_bin_{n_bins}_{encode}_{strategy}"
    df = pd.concat([df, pd.DataFrame(transformed, columns=[new_column_name])], axis=1)
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def ordinal_encoder(df, column_name, drop_old=False):
    if not check_if_dtype(df, column_name, "Non-numeric"):
        return df
    encoder = OrdinalEncoder()
    new_column_name = f"{column_name}_ordinal_encoded"
    df[new_column_name] = encoder.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def one_hot_encoder(df, column_name, drop_old=False):
    if not check_if_dtype(df, column_name, "Non-numeric"):
        return df
    encoder = OneHotEncoder()
    transformed = encoder.fit_transform(df[[column_name]])
    new_df = pd.concat(
        [
            df,
            pd.DataFrame(
                transformed.toarray(),
                columns=[
                    f"{column_name}_one_hot_{category}"
                    for category in encoder.categories_[0]
                ],
            ),
        ],
        axis=1,
    )
    if drop_old:
        new_df.drop(column_name, axis=1, inplace=True)
    return new_df


def remove_column(df, column_name):
    df.drop(column_name, axis=1, inplace=True)
    return df


def linear_combination(
    df, column_name_1, column_name_2, weight_1=1, weight_2=1, drop_old=False
):
    if not (
        check_if_dtype(df, column_name_1, "Numeric")
        and check_if_dtype(df, column_name_2, "Numeric")
    ):
        return df
    df[f"{column_name_1}_{column_name_2}_linear_combination"] = (
        df[column_name_1] * weight_1 + df[column_name_2] * weight_2
    )
    if drop_old:
        df.drop([column_name_1, column_name_2], axis=1, inplace=True)
    return df


def create_interaction(df, column_name_1, column_name_2, drop_old=False):
    if not (
        check_if_dtype(df, column_name_1, "Numeric")
        and check_if_dtype(df, column_name_2, "Numeric")
    ):
        return df
    df[f"{column_name_1}_{column_name_2}_interaction"] = (
        df[column_name_1] * df[column_name_2]
    )
    if drop_old:
        df.drop([column_name_1, column_name_2], axis=1, inplace=True)
    return df


def subtract_columns(df, column_name_1, column_name_2, drop_old=False):
    if not (
        check_if_dtype(df, column_name_1, "Numeric")
        and check_if_dtype(df, column_name_2, "Numeric")
    ):
        return df
    df[f"{column_name_1}_{column_name_2}_subtraction"] = (
        df[column_name_1] - df[column_name_2]
    )
    if drop_old:
        df.drop([column_name_1, column_name_2], axis=1, inplace=True)
    return df


# %%
