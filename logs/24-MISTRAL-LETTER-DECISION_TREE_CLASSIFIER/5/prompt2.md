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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x-box', 'y-box', 'width', 'high', 'onpix', 'x-bar', 'y-bar', 'x2bar', 'y2bar', 'xybar', 'x2ybr', 'xy2br', 'x-ege', 'xegvy', 'y-ege', 'yegvx', 'x-bar_y-bar_sub', 'x-box_y-box_combination', 'onpix_log', 'x-ege_width_inter', 'high_min_max_scaled', 'x-box_power_transformed_yeo-johnson', 'onpix_quantiled_n=100_distr=uniform', 'x-bar_y-box_inter', 'onpix_width_high_TruncatedSVD', 'x-ege_abs', 'onpix_min_max_scaled', 'x-box_high_inter', 'y-ege_standard_scaled', 'x-box_y-ege_inter', 'width_onpix_PCA', 'high_log', 'onpix_quantiled_n=50_distr=normal', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given information, I suggest the following 10 column-tool combinations for this iteration:

1. `power_transformer(x-ege, method='yeo-johnson')` - To apply Yeo-Johnson power transformation on the 'x-ege' column.
2. `min_max_scaler(width)` - To perform Min-Max scaling on the 'width' column.
3. `quantile_transformer(onpix, n_quantiles=50, output_distribution='normal')` - To apply Normal quantile transformation with 50 quantiles to the 'onpix' column.
4. `subtract_columns(x-box, y-bar)` - To subtract 'y-bar' from 'x-box'.
5. `apply_math_function(high, function='log')` - To apply logarithmic transformation to the 'high' column.
6. `k_bins_discretizer(width, n_bins=10, encode='ordinal', strategy='quantile')` - To quantize 'width' into 10 equal width bins using quantile discretization.
7. `linear_combination(x-box, y-box, weight_1=0.5, weight_2=0.5)` - To create a new column by linearly combining the values of 'x-box' and 'y-box'.
8. `create_interaction(x-box_power_transformed_yeo-johnson, width)` - To create an interaction feature between the 'x-box_power_transformed_yeo-johnson' and 'width' columns.
9. `one_hot_encoder(y2bar)` - To one-hot encode the unique values in the 'y2bar' column.
10. `ordinal_encoder(x-box_high_inter)` - To ordinal encode the unique values in the 'x-box_high_inter' column.

**JSON:**
