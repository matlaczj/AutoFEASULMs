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


def standard_scaler(df, column_name, drop_old=False):
    scaler = StandardScaler()
    new_column_name = f"{column_name}_standard_scaled"
    df[new_column_name] = scaler.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def min_max_scaler(df, column_name, drop_old=False):
    scaler = MinMaxScaler()
    new_column_name = f"{column_name}_min_max_scaled"
    df[new_column_name] = scaler.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def max_abs_scaler(df, column_name, drop_old=False):
    scaler = MaxAbsScaler()
    new_column_name = f"{column_name}_max_abs_scaled"
    df[new_column_name] = scaler.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def quantile_transformer(
    df, column_name, n_quantiles=100, output_distribution="uniform", drop_old=False
):
    if output_distribution not in ["uniform", "normal"]:
        raise ValueError("output_distribution must be either 'uniform' or 'normal'")
    if n_quantiles not in range(2, 101):
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
    if method not in ["yeo-johnson", "box-cox"]:
        raise ValueError("method must be either 'yeo-johnson' or 'box-cox'")
    transformer = PowerTransformer(method=method)
    new_column_name = f"{column_name}_power_transformed_{method}"
    df[new_column_name] = transformer.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def normalizer(df, column_name, norm="l2", drop_old=False):
    if norm not in ["l1", "l2", "max"]:
        raise ValueError("norm must be either 'l1', 'l2', or 'max'")
    transformer = Normalizer(norm=norm)
    new_column_name = f"{column_name}_normalized_{norm}"
    df[new_column_name] = transformer.transform(df[[column_name]].values)
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def binarizer(df, column_name, threshold=0.0, drop_old=False):
    transformer = Binarizer(threshold=threshold)
    new_column_name = f"{column_name}_binarized_{threshold}"
    df[new_column_name] = transformer.transform(df[[column_name]].values)
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def polynomial_features(df, column_name, degree=2, drop_old=False):
    if degree not in range(2, 11):
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
    df, column_name, n_bins=5, encode="onehot", strategy="quantile", drop_old=False
):
    if encode not in ["onehot", "onehot-dense", "ordinal"]:
        raise ValueError("encode must be either 'onehot', 'onehot-dense', or 'ordinal'")
    if strategy not in ["uniform", "quantile", "kmeans"]:
        raise ValueError("strategy must be either 'uniform', 'quantile', or 'kmeans'")
    if n_bins not in range(2, 101):
        raise ValueError("n_bins must be between 2 and 20")
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode=encode, strategy=strategy)
    transformed = discretizer.fit_transform(df[[column_name]])
    new_column_name = f"{column_name}_bin_{n_bins}_{encode}_{strategy}"
    df = pd.concat([df, pd.DataFrame(transformed, columns=[new_column_name])], axis=1)
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def ordinal_encoder(df, column_name, drop_old=False):
    encoder = OrdinalEncoder()
    new_column_name = f"{column_name}_ordinal_encoded"
    df[new_column_name] = encoder.fit_transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def one_hot_encoder(df, column_name, drop_old=False):
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


def linear_combination(
    df, column_name_1, column_name_2, weight_1=1, weight_2=1, drop_old=False
):
    df[f"{column_name_1}_{column_name_2}_linear_combination"] = (
        df[column_name_1] * weight_1 + df[column_name_2] * weight_2
    )
    if drop_old:
        df.drop([column_name_1, column_name_2], axis=1, inplace=True)
    return df


def apply_math_function(df, column_name, function, drop_old=False):
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
    if function not in function_dict:
        raise ValueError(f"Unknown function: {function}")
    transformer = FunctionTransformer(func=function_dict[function])
    df[f"{column_name}_{function}"] = transformer.transform(df[[column_name]])
    if drop_old:
        df.drop(column_name, axis=1, inplace=True)
    return df


def create_interaction(df, column_name_1, column_name_2, drop_old=False):
    df[f"{column_name_1}_{column_name_2}_interaction"] = (
        df[column_name_1] * df[column_name_2]
    )
    if drop_old:
        df.drop([column_name_1, column_name_2], axis=1, inplace=True)
    return df


# %%
