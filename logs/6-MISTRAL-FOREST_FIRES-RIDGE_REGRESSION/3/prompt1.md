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
example unique values in 'ffmc_isi_combination': 43.68, 41.55, 42.13, 40.48, 45.37, 43.48, 41.01, 40.17, 39.18, 48.4 ...
example unique values in 'rh_standard_scaled': 0.02, 0.03, -0.14, 2.27, -1.03, -0.52, 0.3, -1.02, -0.3, -0.31 ...
example unique values in 'ffmc_dc_sub': -626.51, 22.86, 75.26, -605.82, 8.88, -618.11, -576.53, -656.22, -551.06, -669.36 ...
example unique values in 'temp_standard_scaled': -2.31, 0.91, 0.48, -1.34, -1.73, 0.37, -1.34, 0.7, -1.6, -0.12 ...
example unique values in 'dc_dmc_sub': 675.56, 304.78, 166.57, 485.27, 439.86, 604.92, 198.54, 557.22, 552.05, 385.02 ...
example unique values in 'temp_wind_inter': 84.56, 127.88, 10.67, 24.91, 155.98, 92.07, 130.84, 50.24, 74.32, 47.73 ...
all unique values in 'rh_binarized_n=5_enc=ordinal_strat=uniform': 1.0, 0.0, 4.0, 3.0, 2.0
all unique values in 'rh_binarized_n=5_enc=ordinal_strat=quantile': 3.0, 1.0, 0.0, 4.0, 2.0
all unique values in 'rain_binarized_th=0.0': 0.0, 1.0
example unique values in 'dmc_log': 4.93, 4.59, 4.92, 3.61, 4.91, 5.59, 5.04, 5.44, 5.27, 2.87 ...
example unique values in 'target': 2.95, 1.73, 1.74, 2.92, 2.77, 2.11, 2.1, 3.9, 4.3, 4.97 ...
- *CORRELATIONS:*
correlation between 'ffmc_dc_sub' and 'dc': -1.0
correlation between 'temp_standard_scaled' and 'temp': 1.0
correlation between 'rh_standard_scaled' and 'rh': 1.0
correlation between 'dc_dmc_sub' and 'dc': 0.97
correlation between 'dc_dmc_sub' and 'ffmc_dc_sub': -0.97
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'rh_standard_scaled': 0.95
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'rh': 0.95
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'rh_standard_scaled': 0.92
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'rh': 0.92
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'rh_binarized_n=5_enc=ordinal_strat=uniform': 0.88
correlation between 'dmc_log' and 'dmc': 0.85
correlation between 'ffmc_isi_combination' and 'ffmc': 0.8
correlation between 'dmc_log' and 'dc': 0.73
correlation between 'dmc_log' and 'ffmc_dc_sub': -0.72
correlation between 'temp_wind_inter' and 'wind': 0.67
correlation between 'dc' and 'dmc': 0.65
correlation between 'ffmc_dc_sub' and 'dmc': -0.65
correlation between 'rain_binarized_th=0.0' and 'rain': 0.61
correlation between 'dmc_log' and 'dc_dmc_sub': 0.59
correlation between 'dmc_log' and 'temp_standard_scaled': 0.55
correlation between 'dmc_log' and 'temp': 0.55
correlation between 'temp_standard_scaled' and 'rh_standard_scaled': -0.51
correlation between 'temp_standard_scaled' and 'rh': -0.51
correlation between 'rh_standard_scaled' and 'temp': -0.51
correlation between 'rh' and 'temp': -0.51
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'temp_standard_scaled': -0.49
correlation between 'y' and 'x': 0.49
correlation between 'temp_wind_inter' and 'temp_standard_scaled': 0.49
correlation between 'temp_wind_inter' and 'temp': 0.49
correlation between 'rh_binarized_n=5_enc=ordinal_strat=uniform' and 'temp': -0.49
correlation between 'ffmc_dc_sub' and 'temp': -0.47
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'temp': -0.47
correlation between 'temp_standard_scaled' and 'dc': 0.47
correlation between 'rh_binarized_n=5_enc=ordinal_strat=quantile' and 'temp_standard_scaled': -0.47
correlation between 'temp' and 'dc': 0.47
correlation between 'temp_standard_scaled' and 'ffmc_dc_sub': -0.47
correlation between 'dc_dmc_sub' and 'dmc': 0.46
correlation between 'temp_standard_scaled' and 'dmc': 0.46
correlation between 'temp' and 'dmc': 0.46
correlation between 'isi' and 'ffmc': 0.45
correlation between 'dc_dmc_sub' and 'temp_standard_scaled': 0.41
correlation between 'dc_dmc_sub' and 'temp': 0.41
correlation between 'temp_standard_scaled' and 'isi': 0.39
correlation between 'temp' and 'isi': 0.39
correlation between 'dmc_log' and 'ffmc': 0.38
correlation between 'dmc_log' and 'isi': 0.37
correlation between 'temp' and 'ffmc': 0.35
correlation between 'temp_standard_scaled' and 'ffmc': 0.35
correlation between 'temp_wind_inter' and 'isi': 0.33
correlation between 'dmc' and 'ffmc': 0.32

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