**INTRODUCTION:**
Predict the demand for shared bikes based on various features (these columns might not exist, use columns from COLUMNS section):
season : season (1:springer, 2:summer, 3:fall, 4:winter)
yr : year (0: 2011, 1:2012)
mnth : month ( 1 to 12)
hr : hour (0 to 23)
holiday : weather day is holiday or not
weekday : day of the week
workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
weathersit :
1: Clear, Few clouds, Partly cloudy, Partly cloudy
2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
temp : Normalized temperature in Celsius. The values are divided to 41 (max)
atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
hum: Normalized humidity. The values are divided to 100 (max)
windspeed: Normalized wind speed. The values are divided to 67 (max)
casual: count of casual users
registered: count of registered users
cnt: count of total rental bikes including both casual and registered

**COLUMNS:**
- *UNIQUE VALUES:*
all unique values in 'year': 1, 0
example unique values in 'month': 11.57, 1.06, 0.88, 8.74, 7.24, 2.46, 10.94, 5.68, 7.7, 6.99 ...
example unique values in 'hour': 14.3, 6.36, 20.2, 19.74, 4.34, 9.05, 9.5, 17.03, 8.91, 9.58 ...
example unique values in 'weekday': 2.09, 2.43, 5.74, 5.08, 1.68, 1.82, 2.59, 4.06, 5.72, 5.98 ...
example unique values in 'temp': 38.36, 9.27, 30.88, 14.53, 11.82, 33.05, 35.49, 22.49, 20.59, 21.99 ...
example unique values in 'feel_temp': 14.69, 35.95, 36.44, 22.8, 16.96, 19.52, 5.06, 12.12, 10.7, 33.87 ...
example unique values in 'humidity': 0.46, 0.63, 0.46, 0.41, 0.85, 0.29, 0.34, 0.49, 0.87, 0.85 ...
example unique values in 'windspeed': -0.56, 7.61, 5.03, 0.32, 0.97, 12.77, 25.59, -1.14, 29.16, 2.53 ...
all unique values in 'season_fall': 1, 0
all unique values in 'season_spring': 0, 1
all unique values in 'season_summer': 0, 1
all unique values in 'season_winter': 0, 1
all unique values in 'holiday_false': 1, 0
all unique values in 'holiday_true': 0, 1
all unique values in 'workingday_false': 0, 1
all unique values in 'workingday_true': 1, 0
all unique values in 'weather_clear': 1, 0
all unique values in 'weather_heavy_rain': 0
all unique values in 'weather_misty': 0, 1
all unique values in 'weather_rain': 0, 1
example unique values in 'workingday_true_hour_inter': 12.11, 17.61, 12.34, 7.25, 19.45, 0.59, 2.21, 11.69, 4.88, 13.56 ...
example unique values in 'feel_temp_humidity_TruncatedSVD': 39.02, 12.79, 33.88, 18.29, 11.43, 15.88, 24.38, 27.05, 32.66, 33.77 ...
example unique values in 'feel_temp_square': 246.53, 280.72, 246.52, 170.49, 1288.82, 1496.4, 122.75, 846.59, 683.56, 663.63 ...
example unique values in 'temp_humidity_PCA_feel_temp_humidity_combination_TruncatedSVD': 13.71, 9.63, 32.04, 31.97, 22.22, 20.01, 38.84, 27.83, 19.1, 26.5 ...
example unique values in 'feel_temp_humidity_combination': 35.26, 19.78, 8.77, 13.49, 42.19, 37.41, 13.58, 33.9, 10.07, 27.03 ...
example unique values in 'humidity_square': 0.24, 0.24, 0.28, 0.07, 0.98, 0.5, 0.4, 0.29, 1.01, 0.51 ...
example unique values in 'feel_temp_windspeed_inter': 283.08, 146.7, 312.93, 218.08, 465.87, -81.36, 215.52, 50.28, 211.98, 391.86 ...
example unique values in 'season_fall_windspeed_inter': 27.73, 4.95, 18.44, 19.61, 12.43, 8.36, 16.77, 1.83, 18.55, 16.98 ...
example unique values in 'temp_windspeed_sub': 26.68, 1.94, 2.98, -6.78, 15.92, 8.55, 20.16, 10.62, -4.77, 2.86 ...
example unique values in 'windspeed_min_max_scaled': 0.35, 0.18, 0.19, 0.3, 0.36, 0.44, 0.24, 0.1, 0.23, 0.38 ...
example unique values in 'windspeed_abs': 14.19, 6.94, 1.06, 10.97, 11.56, 36.38, 18.01, 5.07, 6.83, 18.23 ...
example unique values in 'workingday_true_hour_inter_hour_sub': -9.5, -0.23, -16.36, -10.02, -22.5, -0.33, -19.71, -12.31, -21.45, -7.42 ...
example unique values in 'temp_humidity_inter': 14.3, 15.09, 12.31, 18.81, 16.45, 24.21, 5.28, 10.85, 7.77, 8.23 ...
all unique values in 'feel_temp_humidity_combination_normalized_l1': 1.0, -1.0
example unique values in 'target': 5.03, 2.61, 6.92, 6.14, 6.71, 6.65, 6.47, 5.19, 7.67, 5.28 ...
- *CORRELATIONS:*
correlation between 'temp_humidity_PCA_feel_temp_humidity_combination_TruncatedSVD' and 'feel_temp': 1.0
correlation between 'feel_temp_humidity_combination' and 'feel_temp_humidity_TruncatedSVD': 1.0
correlation between 'holiday_true' and 'holiday_false': -1.0
correlation between 'workingday_true' and 'workingday_false': -1.0
correlation between 'windspeed_min_max_scaled' and 'windspeed': 1.0
correlation between 'windspeed_abs' and 'windspeed': 0.99
correlation between 'windspeed_abs' and 'windspeed_min_max_scaled': 0.99
correlation between 'feel_temp_square' and 'feel_temp': 0.98
correlation between 'feel_temp_humidity_combination' and 'feel_temp_square': 0.98
correlation between 'feel_temp' and 'temp': 0.94
correlation between 'feel_temp_humidity_combination' and 'temp': 0.94
correlation between 'feel_temp_square' and 'temp': 0.93
correlation between 'workingday_true_hour_inter_hour_sub' and 'workingday_true': 0.8
correlation between 'windspeed_min_max_scaled' and 'feel_temp_windspeed_inter': 0.8
correlation between 'weather_misty' and 'weather_clear': -0.79
correlation between 'temp_humidity_inter' and 'temp': 0.72
correlation between 'temp_humidity_inter' and 'feel_temp': 0.69
correlation between 'temp_windspeed_sub' and 'temp': 0.69
correlation between 'temp_windspeed_sub' and 'feel_temp_square': 0.64
correlation between 'temp_humidity_inter' and 'feel_temp_square': 0.64
correlation between 'temp_humidity_inter' and 'humidity': 0.62
correlation between 'workingday_true_hour_inter' and 'hour': 0.62
correlation between 'temp_humidity_PCA_feel_temp_humidity_combination_TruncatedSVD' and 'season_spring': -0.61
correlation between 'feel_temp_humidity_combination' and 'season_spring': -0.61
correlation between 'temp_humidity_PCA_feel_temp_humidity_combination_TruncatedSVD' and 'season_fall': 0.61
correlation between 'temp_humidity_inter' and 'humidity_square': 0.6
correlation between 'feel_temp_humidity_TruncatedSVD' and 'season_fall': 0.6
correlation between 'season_spring' and 'temp': -0.59
correlation between 'target' and 'hour': 0.55
correlation between 'temp_windspeed_sub' and 'season_fall': 0.51
correlation between 'season_spring' and 'month': -0.5
correlation between 'season_fall_windspeed_inter' and 'feel_temp': 0.49
correlation between 'temp_windspeed_sub' and 'season_spring': -0.47
correlation between 'season_fall_windspeed_inter' and 'feel_temp_windspeed_inter': 0.46
correlation between 'feel_temp_windspeed_inter' and 'feel_temp_square': 0.45
correlation between 'feel_temp_windspeed_inter' and 'temp': 0.42
correlation between 'humidity_square' and 'weather_clear': -0.4
correlation between 'target' and 'workingday_true_hour_inter': 0.4
correlation between 'target' and 'feel_temp_square': 0.38
correlation between 'target' and 'feel_temp_humidity_TruncatedSVD': 0.38
correlation between 'target' and 'feel_temp_humidity_combination': 0.37
correlation between 'season_summer' and 'season_fall': -0.35
correlation between 'target' and 'humidity_square': -0.34
correlation between 'temp_humidity_inter' and 'season_fall_windspeed_inter': 0.33
correlation between 'season_winter' and 'season_summer': -0.31
correlation between 'season_winter' and 'season_spring': -0.31
correlation between 'season_winter' and 'season_fall': -0.31
correlation between 'temp_windspeed_sub' and 'feel_temp_windspeed_inter': -0.3
correlation between 'windspeed_min_max_scaled' and 'humidity': -0.3
correlation between 'windspeed' and 'humidity': -0.3

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: 0.59%
Error: 0.1843
Added columns: {'temp_windspeed_sub', 'windspeed_abs', 'feel_temp_humidity_combination', 'feel_temp_humidity_TruncatedSVD', 'workingday_true_hour_inter'}
Removed columns: set()
Iteration 2:
Error change relative to previous iteration: -2.33%
Error: 0.1800
Added columns: {'temp_humidity_PCA', 'temp_humidity_inter', 'feel_temp_humidity_combination_normalized_l1', 'windspeed_min_max_scaled'}
Removed columns: set()
Iteration 3:
Error change relative to previous iteration: -0.19%
Error: 0.1797
Added columns: {'feel_temp_square', 'feel_temp_windspeed_inter', 'temp_humidity_PCA_feel_temp_humidity_combination_TruncatedSVD'}
Removed columns: set()
Iteration 4:
Error change relative to previous iteration: 0.04%
Error: 0.1798
Added columns: {'workingday_true_hour_inter_hour_sub', 'humidity_square', 'season_fall_windspeed_inter'}
Removed columns: set()

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

**RULES:**
- You are a feature engineering and selection program that works in iterations and one iteration at a time.
- You create new features from existing columns to make ML Ridge Regression model better at predicting target variable 'target' in regression problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**