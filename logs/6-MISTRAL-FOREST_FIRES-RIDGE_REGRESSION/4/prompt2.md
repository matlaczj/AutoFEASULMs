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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x', 'y', 'ffmc', 'dmc', 'dc', 'isi', 'temp', 'rh', 'wind', 'rain', 'day_fri', 'day_mon', 'day_sat', 'day_sun', 'day_thu', 'day_tue', 'day_wed', 'ffmc_isi_combination', 'rh_standard_scaled', 'ffmc_dc_sub', 'temp_standard_scaled', 'dc_dmc_sub', 'temp_wind_inter', 'rh_binarized_n=5_enc=ordinal_strat=uniform', 'rh_binarized_n=5_enc=ordinal_strat=quantile', 'rain_binarized_th=0.0', 'dmc_log', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are my recommendations for creating 10 new feature columns using existing ones:

1. Create a linear combination of 'ffmc_dc_sub' and 'rh': `linear_combination('ffmc_dc_sub', 'rh', weight_1=0.7, weight_2=-0.3)`
2. Apply log transformation on 'temp' column: `apply_math_function('temp', function='log')`
3. Create a polynomial feature of degree 2 from 'isi': `polynomial_features('isi', degree=2)`
4. Discretize 'rh_binarized_n=5_enc=ordinal_strat=quantile' using equal width bins: `k_bins_discretizer('rh_binarized_n=5_enc=ordinal_strat=quantile', n_bins=5, encode='ordinal', strategy='uniform')`
5. Create an interaction feature between 'ffmc' and 'temp': `create_interaction('ffmc', 'temp')`
6. Subtract 'dc_dmc_sub' from 'ffmc': `subtract_columns('ffmc', 'dc_dmc_sub')`
7. Create a new column as the absolute value of 'rain': `apply_math_function('rain', function='abs')`
8. Standardize 'temp_wind_inter' using z-score normalization: `standard_scaler('temp_wind_inter')`
9. Encode 'day_mon' as one-hot vectors: `one_hot_encoder('day_mon')`
10. Take the square root of 'dc': `apply_math_function('dc', function='sqrt')`

**JSON:**
