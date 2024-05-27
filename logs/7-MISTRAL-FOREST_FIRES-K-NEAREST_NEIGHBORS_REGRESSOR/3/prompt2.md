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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x', 'y', 'ffmc', 'dmc', 'dc', 'isi', 'temp', 'rh', 'wind', 'rain', 'day_fri', 'day_mon', 'day_sat', 'day_sun', 'day_thu', 'day_tue', 'day_wed', 'wind_temp_inter', 'rh_power_transformed_box-cox', 'ffmc_min_max_scaled', 'rain_isi_sub', 'rh_temp_inter', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given dataset and considering the previous iteration history, here are 10 new column-tool combinations that could potentially improve the ML K-Nearest Neighbors Regressor model:

1. `polyomial_features(column_name='temp', degree=3)`: This feature engineering technique will create polynomial features up to a given degree for the 'temp' column, allowing the model to capture complex relationships between the temperature and burned area.
2. `subtract_columns(column_name_1='ffmc', column_name_2='dc')`: By subtracting the 'dc' column from the 'ffmc' column, this new feature could potentially help capture the difference in values, which might be important for predicting burned area.
3. `max_abs_scaler(column_name='rh')`: Scaling the 'rh' (relative humidity) column using max absolute scaling can help bring all data points to a similar range and reduce the impact of outliers that may affect model performance.
4. `create_interaction(column_name_1='x', column_name_2='y')`: Creating an interaction feature between the 'x' and 'y' spatial coordinates can help capture any potential non-linear relationships between these two variables and the burned area.
5. `min_max_scaler(column_name='temp_binarized_n=5_enc=ordinal_strat=quantile')`: Scaling the 'temp_binarized_n=5_enc=ordinal_strat=quantile' feature using min-max scaling can help ensure that all quantiles have equal importance and contribute equally to the model.
6. `power_transformer(column_name='rh', method='box-cox')`: Power transforming the 'rh' (relative humidity) column using the Box-Cox transformation may help normalize the data and reduce skewness, making it easier for the model to learn from the data.
7. `one_hot_encoder(column_name='day_mon')`: One-hot encoding the 'day_mon' (day of the week Monday) column can convert categorical variables into binary features, allowing the model to treat each unique value as a separate feature.
8. `k_bins_discretizer(column_name='isi', n_bins=5, encode='ordinal', strategy='quantile')`: Discretizing the 'isi' column using 5 bins based on quantiles and encoding the categorical labels as ordinal values can help reduce the impact of outliers and improve model interpretability.
9. `normalizer(column_name='rh_power_transformed_box-cox', norm='l2')`: Normalizing the 'rh_power_transformed_box-cox' feature using the L2 norm can help reduce the impact of large values and improve model stability.
10. `linear_combination(column_name_1='ffmc_min_max_scaled', column_name_2='dc_min_max_scaled', weight_1=0.7, weight_2=0.3)`: Creating a linear combination of the 'ffmc_min_max_scaled' and 'dc_min_max_scaled' features, with a 70% weight for 'ffmc_min_max_scaled' and a 30% weight for 'dc_min_max_scaled', can help capture the combined effect of both features on the target variable.

**JSON:**
