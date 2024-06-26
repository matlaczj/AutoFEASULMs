# NOTE: Keep this up to date with `preprocessing_tools.py` file.
# NOTE: Fill columns' enum with the column names from analysed dataset.
# NOTE: These are only schemas. Example of full response format:
# response_format = {
#     "type": "json_object",
#     "schema": schema,
# }
# TODO: Auto-generate this from `preprocessing_tools.py` file.

schema = {
    "type": "object",
    "properties": {
        "transformations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "function": {
                        "type": "string",
                        "enum": [
                            "standard_scaler",
                            "min_max_scaler",
                            "max_abs_scaler",
                            "quantile_transformer",
                            "power_transformer",
                            "apply_math_function",
                            "normalizer",
                            "binarizer",
                            "polynomial_features",
                            "k_bins_discretizer",
                            "ordinal_encoder",
                            "one_hot_encoder",
                            "linear_combination",
                            "create_interaction",
                            "subtract_columns",
                            "reduce_dimentionality",
                        ],
                    },
                    "columns": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "petal_length",
                                "petal_width",
                                "sepal_length",
                                "sepal_width",
                                "species",
                            ],
                        },
                    },
                    "numerical_arguments": {
                        "type": "array",
                        "items": {
                            "type": "number",
                        },
                    },
                    "categorical_arguments": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "uniform",
                                "normal",
                                "yeo-johnson",
                                "box-cox",
                                "max",
                                "ordinal",
                                "quantile",
                                "kmeans",
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
                                "l1",
                                "l2",
                                "PCA",
                                "TruncatedSVD",
                                "FastICA",
                                "FactorAnalysis",
                            ],
                        },
                    },
                },
                "required": [
                    "function",
                    "columns",
                    "numerical_arguments",
                    "categorical_arguments",
                ],
            },
        }
    },
    "required": ["transformations"],
}
