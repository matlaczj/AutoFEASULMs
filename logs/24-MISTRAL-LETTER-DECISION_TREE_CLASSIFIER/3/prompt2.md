**TASK:**
Turn the content into valid json like on the schema.
Remember to put values of arguments in correct lists.
Tool called `apply_math_function` expects `categorical_arguments` to be filled with one of accepted string values and `numerical_arguments` to be empty! Same goes for `normalizer` etc. Look at TOOLS section for accepted values.

**TOOLS:**
- `standard_scaler(column_name:)`
- `min_max_scaler(column_name:)`
- `max_abs_scaler(column_name:)`
- `quantile_transformer(column_name:, n_quantiles:, output_distribution:['uniform', 'normal'])`
- `power_transformer(column_name:, method:['yeo-johnson', 'box-cox'])`
- `apply_math_function(column_name:, function:['log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round'])`
- `normalizer(column_name:, norm:['l1', 'l2', 'max'])`
- `binarizer(column_name:, threshold:)`
- `polynomial_features(column_name:, degree:)`
- `k_bins_discretizer(column_name:, n_bins:, encode:['ordinal'], strategy:['uniform', 'quantile', 'kmeans'])`
- `ordinal_encoder(column_name:)`
- `one_hot_encoder(column_name:)`
- `linear_combination(column_name_1:, column_name_2:, weight_1:, weight_2:)`
- `create_interaction(column_name_1:, column_name_2:)`
- `subtract_columns(column_name_1:, column_name_2:)`
- `reduce_dimentionality(columns:, method:['PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis'])`

**SCHEMA:**
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x-box', 'y-box', 'width', 'high', 'onpix', 'x-bar', 'y-bar', 'x2bar', 'y2bar', 'xybar', 'x2ybr', 'xy2br', 'x-ege', 'xegvy', 'y-ege', 'yegvx', 'x-bar_y-bar_sub', 'x-box_y-box_combination', 'onpix_log', 'x-ege_width_inter', 'high_min_max_scaled', 'onpix_power_transformed_yeo-johnson', 'width_high_PCA', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given information, here are my suggestions for creating new columns in this iteration:

1. `x-ege_high_inter`: Create an interaction between 'x-ege' and 'high' to understand how these two features relate to the target class.
2. `onpix_width_scaled`: Apply min-max scaler on 'onpix' and 'width' columns to ensure both are on a similar scale before creating new features from them.
3. `x-box_high_inter`: Create an interaction between 'x-box' and 'high' to understand how these two features relate to the target class.
4. `y-ege_onpix_scaled`: Apply standard scaler on both 'y-ege' and 'onpix' columns before creating new features from them, as they have a moderate correlation.
5. `x-box_power_transformed_yegvx`: Power transform 'x-box' using Yeo-Johnson method and create an interaction with 'y-ege' and 'x'.
6. `width_onpix_product`: Multiply 'width' and 'onpix' columns to create a new feature representing the area of the bounding box.
7. `y-box_power_transformed_xy2br`: Power transform 'y-box' using Yeo-Johnson method and create an interaction with 'x-bar', 'y2bar' and 'xy2br'.
8. `high_width_sum`: Sum 'high' and 'width' columns to create a new feature representing the total height and width of the bounding box.
9. `onpix_quantiled_n=50_distr=normal`: Apply quantile transformation using normal distribution on the 'onpix' column.
10. `x-ege_abs_high`: Take absolute value of both 'x-ege' and 'high' columns to create a new feature that could be useful for identifying extreme values in the data.

**JSON:**
