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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'target', 'sex_f', 'sex_i', 'sex_m']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given information, I suggest the following 10 column-tool combinations for this iteration:

1. `height_diameter_ratio = height / diameter` and apply `standard_scaler(column_name:'height_diameter_ratio')`
2. `whole_weight_normalized = normalizer(column_name:'whole_weight', norm='l2')`
3. Create a new column 'age_predicted' using the following equation: age_predicted = (height * diameter / whole\_weight) * 10
and apply `linear_combination(column_names=['height', 'diameter', 'whole_weight'], weights=[0.5, 0.3, -0.2])` and name the new column as 'age_prediction_linear'
4. Create a new binary column 'is_male' using `sex_m` values with `binarizer(column_name:'sex_m', threshold=1)`
5. Use `k_bins_discretizer(column_name:'whole_weight', n_bins=5, encode='quantile', strategy='quantile')` and name the new columns as 'whole_weight_bin1' through 'whole_weight_bin5'
6. Create a new column 'height_diameter_diff' using `subtract_columns(column_names=['height', 'diameter'])`
7. Use `polynomial_features(column_name:'length', degree=2)` and extract the squared term named as 'length_squared'
8. Create a new column 'sex_male_female_ratio' using the following equation: sex_male_female_ratio = (number_of_M / (number_of_M + number_of_F)) and apply `linear_combination(column_names=['sex_f', 'sex_m'], weights=[1, -1])`
9. Use `quantile_transformer(column_name:'viscera_weight', n_quantiles=4, output_distribution='normal')` and name the new columns as 'viscera_percentile_1' through 'viscera_percentile_4'
10. Create a new column 'height_log' using `apply_math_function(column_name:'height', function='log')`.

**JSON:**
