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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['year', 'month', 'hour', 'weekday', 'temp', 'feel_temp', 'humidity', 'windspeed', 'season_fall', 'season_spring', 'season_summer', 'season_winter', 'holiday_false', 'holiday_true', 'workingday_false', 'workingday_true', 'weather_clear', 'weather_heavy_rain', 'weather_misty', 'weather_rain', 'workingday_true_hour_inter', 'feel_temp_humidity_TruncatedSVD', 'feel_temp_humidity_combination', 'temp_windspeed_sub', 'windspeed_abs', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are my suggested 10 column-tool combinations for this iteration:

1. `create_interaction(feel_temp, windspeed)`: Since there is a correlation between 'feel_temp' and 'windspeed', creating an interaction feature might help capture the combined effect of both on demand for shared bikes.
2. `reduce_dimentionality(columns=['temp_humidity_PCA', 'feel_temp_humidity_combination'], method='TruncatedSVD')`: As TruncatedSVD is highly correlated with 'feel_temp_humidity_combination' and 'temp_humidity_PCA', reducing their dimensionality might help improve the model performance.
3. `apply_math_function(feel_temp, function='square')`: Squaring the 'feel_temp' values could capture the potential non-linear relationship with the target variable 'target'.
4. `k_bins_discretizer(humidity, n_bins=5, strategy='quantile')`: Discretizing 'humidity' into 5 bins based on quantiles might help create meaningful categorical features for the model.
5. `subtract_columns(temp, humidity)`: Subtracting 'humidity' from 'temp' might create a new feature that could represent the difference between the two and may have a correlation with the target variable.
6. `linear_combination(casual, registered, weight_1=0.5, weight_2=0.5)`: Creating a new column by linearly combining 'casual' and 'registered' might help capture their joint effect on bike demand.
7. `binarizer(workingday_true_hour_inter, threshold=14)`: Binarizing the 'workingday_true_hour_inter' feature when its value is greater than 14 could create a new binary feature that might be useful for model improvement.
8. `power_transformer(windspeed, method='box-cox', power=0.5)`: Box-Cox transformation of 'windspeed' with power 0.5 might help normalize and stabilize the distribution of the data before feeding it to the ML model.
9. `ordinal_encoder(season)`: Encoding categorical 'season' variable as ordinal values might help the model understand the sequence or order between different seasons better.
10. `min_max_scaler(cnt)`: Scaling 'cnt' data using MinMaxScaler might help keep the values within a certain range for better model performance.

**JSON:**
