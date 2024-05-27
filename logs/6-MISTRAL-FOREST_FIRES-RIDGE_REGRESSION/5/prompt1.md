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
example unique values in 'ffmc_dc_sub_rh_combination': -566.48, -93.27, -114.27, -209.02, -654.46, -493.47, -524.5, 75.31, -593.33, -354.22 ...
example unique values in 'ffmc_isi_combination': 44.65, 43.56, 40.2, 45.33, 39.55, 40.73, 49.21, 41.42, 42.94, 43.49 ...
example unique values in 'rh_standard_scaled': -0.41, 0.71, 0.01, -1.32, 0.04, -0.4, 1.02, 0.03, 1.41, -0.9 ...
example unique values in 'ffmc_dc_sub': 20.64, -437.2, -642.35, 34.18, -632.12, -562.07, 53.33, -727.03, 15.58, -629.11 ...
example unique values in 'temp_standard_scaled': -1.45, -2.89, -1.97, 0.09, 1.2, 0.29, 0.09, 0.47, -0.43, 0.79 ...
example unique values in 'dc_power_transformed_yeo-johnson': -1.39, 0.23, 0.8, -2.12, 0.59, 0.52, 0.74, 0.6, -1.7, 1.02 ...
example unique values in 'dc_dmc_sub': 574.54, 673.39, 560.75, 323.51, 622.23, 601.14, 496.26, 439.68, 517.7, 5.58 ...
example unique values in 'temp_wind_inter': 58.89, 92.11, 44.06, 6.62, 91.01, 39.44, 62.73, 21.11, 28.64, 49.77 ...
example unique values in 'ffmc_dc_dmc_sub_sub': -488.62, -433.84, -588.26, -388.61, -12.1, -454.23, -393.42, -359.18, -207.04, -323.96 ...
all unique values in 'rh_binarized_n=5_enc=ordinal_strat=uniform': 1.0, 0.0, 4.0, 3.0, 2.0
all unique values in 'rh_binarized_n=5_enc=ordinal_strat=quantile': 3.0, 1.0, 0.0, 4.0, 2.0
example unique values in 'temp_rh_combination': 32.16, 30.49, 30.84, 32.32, 34.97, 34.66, 48.08, 27.32, 23.46, 27.2 ...
all unique values in 'rain_binarized_th=0.0': 0.0, 1.0
example unique values in 'isi_poly_2': 3.19, 53.5, 73.55, 136.88, 84.11, 244.82, 131.02, 79.94, 37.8, 158.88 ...
example unique values in 'rain_abs': 0.64, 0.32, 0.07, 0.52, 0.0, 0.0, 0.06, 0.87, 0.06, 0.02 ...
example unique values in 'dmc_log': 2.37, 5.61, 5.62, 5.17, 4.1, 4.58, 4.94, 4.86, 3.66, 4.9 ...
example unique values in 'temp_log': 3.11, 3.49, 2.93, 2.6, 2.81, 2.29, 3.17, 2.96, 3.31, 1.36 ...
example unique values in 'temp_rh_inter': 654.74, 1048.37, 1164.48, 896.43, 965.77, 937.85, 407.12, 778.78, 813.58, 721.14 ...
example unique values in 'target': 1.58, 4.37, 2.08, 4.9, 1.29, 2.4, 3.61, 1.44, 4.31, 2.56 ...
- *CORRELATIONS:*
correlation between 'dc_power_transformed_yeo-johnson' and 'ffmc_dc_sub': -1.0
correlation between 'dc_power_transformed_yeo-johnson' and 'ffmc_dc_sub_rh_combination': -1.0
correlation between 'dc_power_transformed_yeo-johnson' and 'dc': 1.0
correlation between 'ffmc_dc_sub_rh_combination' and 'dc': -1.0
correlation between 'dc_dmc_sub' and 'ffmc_dc_sub_rh_combination': -0.97
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'rh': 0.95
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'rh_standard_scaled': 0.95
correlation between 'temp_rh_combination' and 'rh_standard_scaled': 0.93
correlation between 'temp_binarized_n=5_enc=ordinal_strat=quantile' and 'temp': 0.93
correlation between 'temp_standard_scaled' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': 0.93
correlation between 'temp_rh_combination' and 'rh': 0.93
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'rh': 0.92
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'rh_standard_scaled': 0.92
correlation between 'temp_rh_combination' and 'rh_binarized_n=5_enc=ordinal_strat=uniform': 0.89
correlation between 'dmc_log' and 'dc_power_transformed_yeo-johnson': 0.71
correlation between 'ffmc_dc_sub_rh_combination' and 'dmc': -0.64
correlation between 'rain_binarized_th=0.0' and 'rain': 0.61
correlation between 'temp_log' and 'dmc_log': 0.59
correlation between 'dmc_log' and 'ffmc_dc_dmc_sub_sub': -0.58
correlation between 'temp_rh_inter' and 'dmc_log': 0.52
correlation between 'temp_rh_inter' and 'rh_binarized_n=5_enc=ordinal_strat=quantile': 0.52
correlation between 'temp_standard_scaled' and 'rh_standard_scaled': -0.51
correlation between 'temp_binarized_n=5_enc=ordinal_strat=quantile' and 'rh': -0.5
correlation between 'temp_rh_inter' and 'rh': 0.49
correlation between 'temp_wind_inter' and 'temp_standard_scaled': 0.49
correlation between 'y' and 'x': 0.49
correlation between 'temp_rh_inter' and 'rh_standard_scaled': 0.49
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'temp': -0.49
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': -0.48
correlation between 'temp_log' and 'ffmc_dc_sub': -0.47
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'temp_standard_scaled': -0.47
correlation between 'ffmc_dc_sub_rh_combination' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': -0.47
correlation between 'temp_log' and 'dc_power_transformed_yeo-johnson': 0.47
correlation between 'temp' and 'dmc': 0.46
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': -0.46
correlation between 'dc_power_transformed_yeo-johnson' and 'temp_standard_scaled': 0.46
correlation between 'ffmc_dc_dmc_sub_sub' and 'dmc': -0.45
correlation between 'ffmc_dc_sub' and 'temp_binarized_n=5_enc=ordinal_strat=quantile': -0.44
correlation between 'temp_rh_inter' and 'dc': 0.43
correlation between 'temp_log' and 'rh': -0.43
correlation between 'temp_log' and 'rh_binarized_n=5_enc=ordinal_strat=uniform': -0.42
correlation between 'ffmc_dc_dmc_sub_sub' and 'temp_standard_scaled': -0.41
correlation between 'dmc_log' and 'ffmc': 0.38
correlation between 'temp_log' and 'rh_binarized_n=5_enc=ordinal_strat=quantile': -0.38
correlation between 'dmc_log' and 'isi': 0.37
correlation between 'temp_rh_inter' and 'dc_dmc_sub': 0.35
correlation between 'temp_rh_inter' and 'ffmc_dc_dmc_sub_sub': -0.35
correlation between 'temp' and 'ffmc': 0.35
correlation between 'temp_wind_inter' and 'isi': 0.33
correlation between 'temp_binarized_n=5_enc=ordinal_strat=quantile' and 'ffmc': 0.32

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: 0.14%
Error: 0.7763
Added columns: {'dc_dmc_sub', 'temp_standard_scaled', 'rh_binarized_n=5_enc=ordinal_strat=quantile'}
Removed columns: set()
Iteration 2:
Error change relative to previous iteration: -0.37%
Error: 0.7734
Added columns: {'temp_wind_inter', 'rain_binarized_th=0.0', 'ffmc_dc_sub', 'rh_binarized_n=5_enc=ordinal_strat=uniform', 'rh_standard_scaled', 'ffmc_isi_combination', 'dmc_log'}
Removed columns: set()
Iteration 3:
Error change relative to previous iteration: -0.49%
Error: 0.7696
Added columns: {'temp_rh_combination', 'temp_rh_inter', 'dc_log', 'temp_binarized_n=5_enc=ordinal_strat=quantile', 'dc_power_transformed_yeo-johnson'}
Removed columns: set()
Iteration 4:
Error change relative to previous iteration: -0.25%
Error: 0.7677
Added columns: {'ffmc_dc_dmc_sub_sub', 'isi_poly_2', 'temp_log', 'rain_abs', 'ffmc_dc_sub_rh_combination'}
Removed columns: {'dc_log'}

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