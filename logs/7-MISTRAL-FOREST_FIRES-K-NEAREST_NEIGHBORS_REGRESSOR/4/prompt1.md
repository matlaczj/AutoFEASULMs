**INTRODUCTION:**
Predict the burned area of forest fires based on various features (these columns might not exist, use columns from COLUMNS section):
X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
month - month of the year: 'jan' to 'dec'
day - day of the week: 'mon' to 'sun'
FFMC - FFMC index from the FWI system: 18.7 to 96.20
DMC - DMC index from the FWI system: 1.1 to 291.3
DC - DC index from the FWI system: 7.9 to 860.6
ISI - ISI index from the FWI system: 0.0 to 56.10
temp - temperature in Celsius degrees: 2.2 to 33.30
RH - relative humidity in %: 15.0 to 100
wind - wind speed in km/h: 0.40 to 9.40
rain - outside rain in mm/m2 : 0.0 to 6.4
area - the burned area of the forest (in ha): 0.00 to 1090.84 (this output variable is very skewed towards 0.0, thus it may make sense to model with the logarithm transform).

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'x': 3.68, 2.04, 1.19, 4.17, 6.69, 4.72, 0.59, 7.22, 3.41, 2.74 ...
example unique values in 'y': 2.5, 6.49, 4.85, 3.6, 4.29, 5.39, 5.96, 4.92, 4.11, 4.35 ...
example unique values in 'ffmc': 79.12, 91.53, 97.9, 89.79, 89.1, 81.25, 90.26, 76.26, 86.84, 82.3 ...
example unique values in 'dmc': 251.85, 114.25, 68.75, 175.37, 124.31, 144.56, 291.53, 116.81, 159.17, 10.74 ...
example unique values in 'dc': 631.34, 701.23, 557.89, 747.07, 778.07, 617.35, 13.53, 92.69, 78.12, 749.53 ...
example unique values in 'isi': 10.62, 14.0, 14.04, 2.77, 8.58, 10.43, 9.14, 8.99, 4.48, 7.63 ...
example unique values in 'temp': 21.63, 28.83, 21.75, 23.76, 17.15, 16.15, 20.17, 22.04, 17.53, 26.67 ...
example unique values in 'rh': 35.24, 49.56, 25.02, 62.2, 66.89, 22.69, 43.95, 48.52, 61.56, 30.1 ...
example unique values in 'wind': 0.97, 8.82, 4.32, 1.61, 3.97, 1.32, 8.49, 2.42, 1.07, 2.0 ...
example unique values in 'rain': -0.24, -0.1, 0.35, 0.4, -0.23, 0.31, -0.01, -0.12, -0.0, 0.05 ...
all unique values in 'day_fri': 1, 0
all unique values in 'day_mon': 0, 1
all unique values in 'day_sat': 0, 1
all unique values in 'day_sun': 0, 1
all unique values in 'day_thu': 0, 1
all unique values in 'day_tue': 0, 1
all unique values in 'day_wed': 0, 1
all unique values in 'temp_binarized_n=5_enc=ordinal_strat=quantile': 0.0, 1.0, 3.0, 4.0, 2.0
example unique values in 'ffmc_dc_isi_temp_PCA': -147.29, 327.0, 289.17, 159.51, -241.17, -95.45, -119.92, 461.76, -169.99, 54.28 ...
example unique values in 'rh_max_abs_scaled': 0.43, 0.43, 0.4, 0.79, 0.26, 0.34, 0.47, 0.26, 0.38, 0.38 ...
example unique values in 'ffmc_dc_sub': -626.51, 22.86, 75.26, -605.82, 8.88, -618.11, -576.53, -656.22, -551.06, -669.36 ...
example unique values in 'x_y_inter': 26.28, 25.87, 18.12, 3.78, 11.97, 30.73, 31.75, 8.94, 20.24, 11.84 ...
example unique values in 'wind_temp_inter': 44.41, 10.43, 47.97, 42.23, 181.17, 120.47, 103.52, 85.19, 43.53, 143.53 ...
example unique values in 'rh_power_transformed_box-cox': 0.0, 1.62, -0.01, 1.31, -0.61, 0.62, 1.33, 0.11, -1.65, 1.09 ...
example unique values in 'x_y_sub': -0.85, 3.14, 1.22, -0.76, -1.44, 1.35, -2.14, 1.09, -2.3, 0.94 ...
all unique values in 'rh_power_transformed_box-cox_normalized_l2': 1.0, -1.0
example unique values in 'isi_log': 2.13, 2.37, 0.9, 2.47, 2.3, 2.47, 2.38, 1.95, 0.58, 2.2 ...
example unique values in 'ffmc_min_max_scaled': 0.83, 0.95, 0.75, 0.78, 0.81, 0.86, 0.83, 0.82, 0.0, 0.93 ...
example unique values in 'rain_isi_sub': -8.43, -22.97, -13.03, -9.05, -6.81, -6.07, -4.79, -11.31, -16.0, -14.6 ...
all unique values in 'isi_binarized_n=5_enc=ordinal_strat=quantile': 0.0, 1.0, 2.0, 4.0, 3.0
example unique values in 'rh_temp_inter': 385.75, 1121.48, 1007.08, 762.6, 1381.38, 913.71, 1326.38, 397.66, 587.89, 1510.38 ...
example unique values in 'target': 2.56, 1.74, 4.49, 2.73, 2.55, 2.47, 2.37, 1.74, 1.97, 4.01 ...
- *CORRELATIONS:*
correlation between 'ffmc_dc_sub' and 'ffmc_dc_isi_temp_PCA': 1.0
correlation between 'rain_isi_sub' and 'isi': -1.0
correlation between 'rh_power_transformed_box-cox' and 'rh': 0.98
correlation between 'rh_power_transformed_box-cox' and 'rh_max_abs_scaled': 0.98
correlation between 'temp_binarized_n=5_enc=ordinal_strat=quantile' and 'temp': 0.93
correlation between 'isi_binarized_n=5_enc=ordinal_strat=quantile' and 'isi': 0.89
correlation between 'x_y_sub' and 'x': 0.84
correlation between 'isi_log' and 'isi': 0.82
correlation between 'rain_isi_sub' and 'isi_log': -0.82
correlation between 'rh_power_transformed_box-cox_normalized_l2' and 'rh_power_transformed_box-cox': 0.8
correlation between 'isi_binarized_n=5_enc=ordinal_strat=quantile' and 'isi_log': 0.8
correlation between 'rh_power_transformed_box-cox_normalized_l2' and 'rh_max_abs_scaled': 0.77
correlation between 'rh_power_transformed_box-cox_normalized_l2' and 'rh': 0.77
correlation between 'x_y_inter' and 'y': 0.77
correlation between 'wind_temp_inter' and 'wind': 0.67
correlation between 'ffmc_dc_isi_temp_PCA' and 'dmc': -0.65
correlation between 'dc' and 'dmc': 0.65
correlation between 'ffmc_dc_sub' and 'dmc': -0.65
correlation between 'rh_temp_inter' and 'rh_power_transformed_box-cox': 0.53
correlation between 'rh_max_abs_scaled' and 'temp': -0.51
correlation between 'rh' and 'temp': -0.51
correlation between 'temp_binarized_n=5_enc=ordinal_strat=quantile' and 'rh': -0.5
correlation between 'y' and 'x': 0.49
correlation between 'rh_temp_inter' and 'rh': 0.49
correlation between 'rh_power_transformed_box-cox' and 'temp': -0.49
correlation between 'rh_power_transformed_box-cox' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': -0.48
correlation between 'isi_binarized_n=5_enc=ordinal_strat=quantile' and 'ffmc_min_max_scaled': 0.47
correlation between 'temp' and 'dc': 0.47
correlation between 'ffmc_dc_isi_temp_PCA' and 'temp': -0.47
correlation between 'temp' and 'dmc': 0.46
correlation between 'ffmc_min_max_scaled' and 'isi': 0.45
correlation between 'wind_temp_inter' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': 0.45
correlation between 'rh_temp_inter' and 'ffmc_dc_sub': -0.43
correlation between 'rh_power_transformed_box-cox_normalized_l2' and 'temp': -0.43
correlation between 'rh_temp_inter' and 'temp': 0.42
correlation between 'temp_binarized_n=5_enc=ordinal_strat=quantile' and 'dmc': 0.42
correlation between 'isi_binarized_n=5_enc=ordinal_strat=quantile' and 'temp': 0.4
correlation between 'isi_binarized_n=5_enc=ordinal_strat=quantile' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': 0.37
correlation between 'isi_log' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': 0.36
correlation between 'rh_temp_inter' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': 0.36
correlation between 'temp' and 'ffmc': 0.35
correlation between 'rain_isi_sub' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': -0.35
correlation between 'wind_temp_inter' and 'isi': 0.33
correlation between 'ffmc_min_max_scaled' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': 0.32
correlation between 'temp_binarized_n=5_enc=ordinal_strat=quantile' and 'ffmc': 0.32
correlation between 'isi_log' and 'ffmc_dc_sub': -0.32
correlation between 'ffmc_min_max_scaled' and 'dmc': 0.32
correlation between 'rain_isi_sub' and 'wind_temp_inter': -0.32
correlation between 'isi_log' and 'wind_temp_inter': 0.31
correlation between 'isi_binarized_n=5_enc=ordinal_strat=quantile' and 'dmc': 0.3

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: -4.37%
Error: 0.9057
Added columns: {'wind_temp_inter', 'rh_temp_inter', 'ffmc_min_max_scaled', 'rain_isi_sub', 'rh_power_transformed_box-cox'}
Removed columns: set()
Iteration 2:
Error change relative to previous iteration: 1.28%
Error: 0.9173
Added columns: {'isi_log', 'x_y_sub', 'temp_binarized_n=5_enc=ordinal_strat=quantile', 'ffmc_dc_isi_temp_PCA'}
Removed columns: set()
Iteration 3:
Error change relative to previous iteration: -1.87%
Error: 0.9001
Added columns: {'isi_binarized_n=5_enc=ordinal_strat=quantile', 'x_y_inter', 'ffmc_dc_sub', 'rh_power_transformed_box-cox_normalized_l2', 'rh_max_abs_scaled'}
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