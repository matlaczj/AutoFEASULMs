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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x', 'y', 'ffmc', 'dmc', 'dc', 'isi', 'temp', 'rh', 'wind', 'rain', 'day_fri', 'day_mon', 'day_sat', 'day_sun', 'day_thu', 'day_tue', 'day_wed', 'temp_binarized_n=5_enc=ordinal_strat=quantile', 'dc_log', 'ffmc_isi_combination', 'rh_standard_scaled', 'ffmc_dc_sub', 'temp_standard_scaled', 'dc_power_transformed_yeo-johnson', 'dc_dmc_sub', 'temp_wind_inter', 'rh_binarized_n=5_enc=ordinal_strat=uniform', 'rh_binarized_n=5_enc=ordinal_strat=quantile', 'temp_rh_combination', 'rain_binarized_th=0.0', 'dmc_log', 'temp_rh_inter', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are my suggested feature engineering operations for this iteration:

1. `power_transformer(column_name='ffmc', method='yeo-johnson')`
2. `power_transformer(column_name='dc', method='box-cox')`
3. `linear_combination(column_name_1='ffmc_power_transformed', column_name_2='dc_power_transformed', weight_1=0.7, weight_2=0.3)`
4. `subtract_columns(column_name_1='ffmc_power_transformed', column_name_2='dc_power_transformed')`
5. `create_interaction(column_name_1='x', column_name_2='y')`
6. `k_bins_discretizer(column_name='month', n_bins=3, encode='ordinal', strategy='quantile')`
7. `binarizer(column_name='day_fri', threshold=1)`
8. `binarizer(column_name='rh_binarized_n=5_enc=ordinal_strat=uniform', threshold=2.0)`
9. `apply_math_function(column_name='temp', function='sqrt')`
10. `polynomial_features(column_name='rain', degree=3)`

**JSON:**
