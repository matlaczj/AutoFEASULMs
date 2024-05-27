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
example unique values in 'temp_power_transformed_yeo-johnson': 0.32, -2.02, -1.24, 0.59, -0.91, -1.56, -1.23, 0.36, -0.46, 0.58 ...
example unique values in 'temp_quantiled_n=100_distr=uniform': 0.89, 0.1, 0.73, 0.63, 0.07, 0.19, 0.57, 0.42, 0.84, 0.95 ...
example unique values in 'windspeed_temp_combination': 11.83, 32.73, 27.75, 42.95, 33.76, 63.73, 18.88, 34.4, 31.26, 37.07 ...
example unique values in 'temp_log': 2.51, 2.11, 3.23, 3.15, 2.87, 2.92, 3.47, 3.25, 2.63, 3.09 ...
example unique values in 'humidity_log': -1.5, -0.79, -0.92, -0.52, -0.85, -0.9, -0.02, -0.36, -1.31, -0.35 ...
example unique values in 'season_fall_windspeed_inter': 24.01, 10.25, 17.34, 7.35, -1.07, 17.14, 12.96, -3.56, -0.77, 27.73 ...
example unique values in 'windspeed_min_max_scaled': 0.27, 0.29, 0.56, 0.32, 0.48, 0.22, 0.54, 0.23, 0.35, 0.18 ...
all unique values in 'humidity_log_normalized_l2': -1.0, 1.0
all unique values in 'season_fall_workingday_false_inter': 0, 1
example unique values in 'temp_feel_temp_sub': -1.82, -2.46, -4.18, -4.39, -6.36, -1.65, -7.8, -7.64, 1.45, -0.96 ...
example unique values in 'temp_humidity_inter': 18.93, 17.82, 15.19, 24.86, 7.98, 23.54, 12.8, 3.98, 11.2, 6.48 ...
all unique values in 'humidity_normalized_l2': 1.0
example unique values in 'target': 5.26, 6.49, 6.33, 6.54, 6.34, 7.39, 5.11, 7.2, 3.89, 7.68 ...
- *CORRELATIONS:*
correlation between 'holiday_true' and 'holiday_false': -1.0
correlation between 'windspeed_min_max_scaled' and 'windspeed': 1.0
correlation between 'temp_quantiled_n=100_distr=uniform' and 'temp_power_transformed_yeo-johnson': 0.99
correlation between 'feel_temp' and 'temp': 0.94
correlation between 'temp_quantiled_n=100_distr=uniform' and 'feel_temp': 0.94
correlation between 'temp_power_transformed_yeo-johnson' and 'feel_temp': 0.94
correlation between 'temp_log' and 'temp': 0.91
correlation between 'temp_log' and 'temp_quantiled_n=100_distr=uniform': 0.89
correlation between 'season_fall_windspeed_inter' and 'season_fall': 0.77
correlation between 'windspeed_temp_combination' and 'windspeed': 0.72
correlation between 'temp_humidity_inter' and 'temp': 0.72
correlation between 'windspeed_temp_combination' and 'temp_power_transformed_yeo-johnson': 0.66
correlation between 'windspeed_temp_combination' and 'temp_quantiled_n=100_distr=uniform': 0.65
correlation between 'temp_humidity_inter' and 'humidity': 0.62
correlation between 'season_fall' and 'temp': 0.62
correlation between 'temp_log' and 'windspeed_temp_combination': 0.61
correlation between 'temp_humidity_inter' and 'humidity_log': 0.61
correlation between 'season_spring' and 'feel_temp': -0.61
correlation between 'windspeed_temp_combination' and 'feel_temp': 0.6
correlation between 'season_spring' and 'temp': -0.59
correlation between 'temp_log' and 'season_spring': -0.59
correlation between 'temp_quantiled_n=100_distr=uniform' and 'season_spring': -0.59
correlation between 'temp_humidity_inter' and 'season_spring': -0.54
correlation between 'season_fall_windspeed_inter' and 'temp': 0.51
correlation between 'season_fall_windspeed_inter' and 'temp_quantiled_n=100_distr=uniform': 0.51
correlation between 'temp_log' and 'season_fall': 0.5
correlation between 'season_spring' and 'month': -0.5
correlation between 'temp_humidity_inter' and 'season_fall': 0.49
correlation between 'season_fall_windspeed_inter' and 'windspeed_temp_combination': 0.48
correlation between 'season_fall_workingday_false_inter' and 'workingday_false': 0.43
correlation between 'season_fall_workingday_false_inter' and 'season_fall_windspeed_inter': 0.39
correlation between 'weather_clear' and 'humidity': -0.39
correlation between 'target' and 'feel_temp': 0.38
correlation between 'target' and 'temp_power_transformed_yeo-johnson': 0.38
correlation between 'target' and 'temp': 0.38
correlation between 'target' and 'windspeed_temp_combination': 0.37
correlation between 'target' and 'temp_log': 0.35
correlation between 'season_summer' and 'season_fall': -0.35
correlation between 'season_summer' and 'season_spring': -0.35
correlation between 'target' and 'humidity': -0.34
correlation between 'weather_rain' and 'humidity': 0.34
correlation between 'windspeed_min_max_scaled' and 'humidity_log': -0.32
correlation between 'temp_humidity_inter' and 'windspeed_temp_combination': 0.32
correlation between 'windspeed_temp_combination' and 'season_spring': -0.32
correlation between 'temp_feel_temp_sub' and 'feel_temp': -0.32
correlation between 'windspeed_temp_combination' and 'season_fall': 0.32
correlation between 'season_winter' and 'season_summer': -0.31
correlation between 'season_winter' and 'season_spring': -0.31
correlation between 'season_fall_workingday_false_inter' and 'temp_quantiled_n=100_distr=uniform': 0.31
correlation between 'season_summer' and 'month': -0.31

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: 1.80%
Error: 0.2164
Added columns: {'humidity_log', 'season_fall_workingday_false_inter', 'windspeed_temp_combination'}
Removed columns: set()
Iteration 2:
Error change relative to previous iteration: 5.00%
Error: 0.2272
Added columns: {'temp_humidity_inter', 'humidity_log_normalized_l2', 'temp_feel_temp_sub', 'windspeed_min_max_scaled'}
Removed columns: set()
Iteration 3:
Error change relative to previous iteration: -1.25%
Error: 0.2243
Added columns: {'season_fall_windspeed_inter'}
Removed columns: set()
Iteration 4:
Error change relative to previous iteration: -0.05%
Error: 0.2242
Added columns: {'temp_quantiled_n=100_distr=uniform', 'humidity_normalized_l2', 'temp_power_transformed_yeo-johnson', 'temp_log'}
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
- You create new features from existing columns to make ML K-Nearest Neighbors Regressor model better at predicting target variable 'target' in regression problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**