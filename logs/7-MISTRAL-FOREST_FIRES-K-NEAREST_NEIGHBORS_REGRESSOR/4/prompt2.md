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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x', 'y', 'ffmc', 'dmc', 'dc', 'isi', 'temp', 'rh', 'wind', 'rain', 'day_fri', 'day_mon', 'day_sat', 'day_sun', 'day_thu', 'day_tue', 'day_wed', 'temp_binarized_n=5_enc=ordinal_strat=quantile', 'ffmc_dc_isi_temp_PCA', 'wind_temp_inter', 'rh_power_transformed_box-cox', 'x_y_sub', 'isi_log', 'ffmc_min_max_scaled', 'rain_isi_sub', 'rh_temp_inter', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given information, I would suggest the following 10 column-tool combinations for this iteration:

1. `min_max_scaler('ffmc')`: Scale 'ffmc' to bring all values within a specific range to improve the model performance.
2. `power_transformer('rh', method='box-cox')`: Apply Box-Cox power transformation to 'rh' column as it has a skewed distribution and may impact model accuracy.
3. `subtract_columns('ffmc', 'dc')`: Subtract 'dc' from 'ffmc' to create a new feature that could potentially capture important information for predicting the target variable.
4. `k_bins_discretizer('rh', n_bins=5, encode='ordinal', strategy='quantile')`: Discretize 'rh' column into 5 bins based on quantiles and encode it as ordinal to simplify model calculations.
5. `polynomial_features(x, degree=2)`: Create polynomial features of degree 2 for 'x' column to capture higher order interactions.
6. `one_hot_encoder('day_fri')`: One-hot encode 'day_fri' column as it is a categorical feature that can impact model performance when treated as continuous.
7. `create_interaction(ffmc, temp)`: Create interaction features between 'ffmc' and 'temp' columns to capture potential non-linear relationships.
8. `binarizer('rh', threshold=50)`: Binarize 'rh' column by setting all values below 50 as 0 and above as 1 to simplify model calculations.
9. `reduce_dimentionality(columns=['ffmc_dc_isi_temp_PCA', 'rh_power_transformed_box-cox'], method='PCA')`: Apply Principal Component Analysis (PCA) to reduce the dimensionality of these columns and retain important information.
10. `linear_combination(isi, rh, weight_1=0.8, weight_2=-0.4)`: Create a new feature by linearly combining 'isi' and 'rh' with specified weights. This can potentially capture significant interactions between the two features that could be useful for modeling the target variable.

**JSON:**
