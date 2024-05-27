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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['year', 'month', 'hour', 'weekday', 'temp', 'feel_temp', 'humidity', 'windspeed', 'season_fall', 'season_spring', 'season_summer', 'season_winter', 'holiday_false', 'holiday_true', 'workingday_false', 'workingday_true', 'weather_clear', 'weather_heavy_rain', 'weather_misty', 'weather_rain', 'windspeed_temp_combination', 'humidity_log', 'windspeed_min_max_scaled', 'humidity_log_normalized_l2', 'season_fall_workingday_false_inter', 'temp_feel_temp_sub', 'temp_humidity_inter', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are my suggested 10 column-tool combinations for this iteration:

1. `normalizer(column_name='humidity', norm='l2')`
Apply L2 normalization to 'humidity' to bring all feature values closer to zero mean and unit length.

2. `apply_math_function(column_name='temp', function='log')`
Take the logarithm of 'temp' to help stabilize the variance and improve model training, as temperature data often have a large range and skewed distribution.

3. `create_interaction(column_name_1='season_fall', column_name_2='workingday_false')`
Create an interaction feature between 'season_fall' and 'workingday_false' to capture any synergistic or additive effects of these two features on the target variable.

4. `k_bins_discretizer(column_name='windspeed', n_bins=5, encode='ordinal')`
Discretize 'windspeed' into 5 equal bins and convert them into ordinal labels to capture any non-linear relationships or hidden patterns.

5. `quantile_transformer(column_name='temp', n_quantiles=3, output_distribution='normal')`
Apply quantile normalization on 'temp' with 3 quantiles and normal distribution output to transform each feature value to have a mean of zero and standard deviation of one.

6. `ordinal_encoder(column_name='season')`
Encode the categorical variable 'season' into ordinal labels to help the model understand any underlying patterns or trends associated with different seasons.

7. `reduce_dimentionality(columns=['temp', 'feel_temp'], method='PCA')`
Use Principal Component Analysis (PCA) to reduce the dimensionality of ['temp' and 'feel_temp'] into a lower-dimensional representation while retaining most of the original information.

8. `linear_combination(column_name_1='humidity', column_name_2='windspeed', weight_1=0.5, weight_2=-0.5)`
Create a new feature as a linear combination of 'humidity' and 'windspeed,' where the weights have been chosen based on the correlation between these features and target variable.

9. `power_transformer(column_name='temp', method='yeo-johnson')`
Apply the Yeo-Johnson power transformation to 'temp' to normalize its distribution and improve model performance.

10. `binarizer(column_name='holiday_true', threshold=0)`
Binarize 'holiday_true' by replacing all non-zero values with 1 and zero values with 0 to simplify the feature representation and make it more suitable for machine learning algorithms.

**JSON:**
