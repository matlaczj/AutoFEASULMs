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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['year', 'month', 'hour', 'weekday', 'temp', 'feel_temp', 'humidity', 'windspeed', 'season_fall', 'season_spring', 'season_summer', 'season_winter', 'holiday_false', 'holiday_true', 'workingday_false', 'workingday_true', 'weather_clear', 'weather_heavy_rain', 'weather_misty', 'weather_rain', 'windspeed_temp_combination', 'humidity_log', 'season_fall_workingday_false_inter', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are my suggested 10 new column-tool combinations for this iteration:

1. `polynomial_features(weather_misty, degree=3)`: To capture higher order interactions of weather patterns with mist, which might influence bike demand.
2. `k_bins_discretizer(humidity, n_bins=5, encode='ordinal', strategy='quantile')`: Discretize the humidity column into 5 bins using quantiles and create ordinal encoded bins.
3. `linear_combination(temp, feel_temp, weights=[0.6, 0.4])`: Create a new feature by linearly combining normalized temperature and feeling temperature with given weights to represent the combined effect on bike demand.
4. `create_interaction(season_fall, windspeed)`: Generate an interaction feature between season and wind speed as they might have complex relationships affecting bike usage.
5. `subtract_columns(temp, min_humidity)`: Subtract minimum humidity from the temperature to capture how temperature changes relative to humidity.
6. `power_transformer(casual, method='box-cox')`: Apply Box-Cox power transformation to the casual users count for better distribution and correlation with target variable.
7. `reduce_dimentionality(columns=['workingday', 'weekday'], method='PCA')`: Reduce dimensionality of working day and weekday columns using PCA.
8. `binarizer(holiday, threshold=0)`: Binarize the holiday column so that it becomes a binary feature representing whether or not it is a holiday.
9. `apply_math_function(weather_rain, function='abs')`: Apply absolute value to the weather rain column as some negative values might be causing issues in modeling.
10. `one_hot_encoder(season)`: One-hot encode the season column since it is a categorical feature and needs to be encoded before being used for regression models.

**JSON:**
