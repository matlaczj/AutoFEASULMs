# NOTE: Keep this up to date with `src\preprocessing_tools.py` file.
# NOTE: Fill 3 enums with the column names from analysed dataset after loading.
# NOTE: These are only schemas. Example of full response format:
# response_format = {
#     "type": "json_object",
#     "schema": schemas["single_argument_schema"],
# }

schemas = {
    "single_argument_schema": {
        "type": "object",
        "properties": {
            "function_name": {
                "type": "string",
                "enum": [
                    "standard_scaler",
                    "min_max_scaler",
                    "max_abs_scaler",
                    "quantile_transformer",
                    "power_transformer",
                    "normalizer",
                    "binarizer",
                    "polynomial_features",
                    "k_bins_discretizer",
                    "ordinal_encoder",
                    "one_hot_encoder",
                    "apply_math_function",
                ],
            },
            "column_name": {
                "type": "string",
                "enum": [],  # NOTE: Fill this with the column names.
            },
        },
        "required": ["function_name", "column_name"],
    },
    "dual_argument_schema": {
        "type": "object",
        "properties": {
            "function_name": {
                "type": "string",
                "enum": ["linear_combination", "create_interaction"],
            },
            "column_name_1": {
                "type": "string",
                "enum": [],  # NOTE: Fill this with the column names.
            },
            "column_name_2": {
                "type": "string",
                "enum": [],  # NOTE: Fill this with the column names.
            },
        },
        "required": ["function_name", "column_name_1", "column_name_2"],
    },
    "standard_scaler_schema": {"type": "object", "properties": {}, "required": []},
    "min_max_scaler_schema": {"type": "object", "properties": {}, "required": []},
    "max_abs_scaler_schema": {"type": "object", "properties": {}, "required": []},
    "quantile_transformer_schema": {
        "type": "object",
        "properties": {
            "n_quantiles": {"type": "integer", "minimum": 2, "maximum": 101},
            "output_distribution": {"type": "string", "enum": ["uniform", "normal"]},
        },
        "required": ["n_quantiles", "output_distribution"],
    },
    "power_transformer_schema": {
        "type": "object",
        "properties": {
            "method": {"type": "string", "enum": ["yeo-johnson", "box-cox"]}
        },
        "required": ["method"],
    },
    "normalizer_schema": {
        "type": "object",
        "properties": {"norm": {"type": "string", "enum": ["l1", "l2", "max"]}},
        "required": ["norm"],
    },
    "binarizer_schema": {
        "type": "object",
        "properties": {"threshold": {"type": "number"}},
        "required": ["threshold"],
    },
    "polynomial_features_schema": {
        "type": "object",
        "properties": {"degree": {"type": "integer", "minimum": 2, "maximum": 10}},
        "required": ["degree"],
    },
    "k_bins_discretizer_schema": {
        "type": "object",
        "properties": {
            "n_bins": {"type": "integer", "minimum": 2, "maximum": 101},
            "encode": {"type": "string", "enum": ["onehot", "onehot-dense", "ordinal"]},
            "strategy": {"type": "string", "enum": ["uniform", "quantile", "kmeans"]},
        },
        "required": ["n_bins", "encode", "strategy"],
    },
    "ordinal_encoder_schema": {"type": "object", "properties": {}, "required": []},
    "one_hot_encoder_schema": {"type": "object", "properties": {}, "required": []},
    "linear_combination_schema": {
        "type": "object",
        "properties": {"weight_1": {"type": "number"}, "weight_2": {"type": "number"}},
        "required": ["weight_1", "weight_2"],
    },
    "apply_math_function_schema": {
        "type": "object",
        "properties": {
            "function": {
                "type": "string",
                "enum": [
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
                ],
            }
        },
        "required": ["function"],
    },
    "create_interaction_schema": {"type": "object", "properties": {}, "required": []},
}

{
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "function_name": {
                "type": "string",
                "enum": ["linear_combination", "create_interaction"],
            },
            "column_name_1": {
                "type": "string",
                "enum": [
                    "sepal length (cm)",
                    "sepal width (cm)",
                    "petal length (cm)",
                    "petal width (cm)",
                    "target",
                ],
            },
            "column_name_2": {
                "type": "string",
                "enum": [
                    "sepal length (cm)",
                    "sepal width (cm)",
                    "petal length (cm)",
                    "petal width (cm)",
                    "target",
                ],
            },
        },
        "required": ["function_name", "column_name_1", "column_name_2"],
    },
}
