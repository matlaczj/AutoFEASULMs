**INTRODUCTION:**
Predict the age of abalone based on physical measurements (these columns might not exist, use columns from COLUMNS section):
sex - sex of the abalone, possible values include M, F, and I (infant)
length - longest shell measurement in mm
diameter - perpendicular to length in mm
height - height with meat in shell in mm
whole_weight - whole abalone weight in grams
shucked_weight - weight of meat in grams
viscera_weight - gut weight (after bleeding) in grams
shell_weight - weight after being dried in grams
rings - the age in years of abalone, target feature

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'length': 0.44, 0.7, 0.64, 0.5, 0.44, 0.46, 0.7, 0.38, 0.46, 0.6 ...
example unique values in 'diameter': 0.3, 0.57, 0.41, 0.35, 0.34, 0.3, 0.19, 0.31, 0.43, 0.29 ...
example unique values in 'height': 0.1, 0.17, 0.14, 0.17, 0.14, 0.14, 0.17, 0.18, 0.27, 0.11 ...
example unique values in 'whole_weight': 1.66, 0.94, 0.5, 1.1, 1.06, 1.34, 0.17, 2.07, 0.48, 0.5 ...
example unique values in 'shucked_weight': 0.03, 0.53, 0.37, 0.62, 0.34, 0.21, 0.6, 0.36, 0.41, 0.38 ...
example unique values in 'viscera_weight': 0.08, 0.1, 0.15, 0.01, 0.12, 0.08, 0.29, 0.12, 0.2, 0.34 ...
example unique values in 'shell_weight': 0.21, 0.37, 0.15, 0.27, 0.01, 0.25, 0.22, 0.19, 0.14, 0.11 ...
all unique values in 'sex_f': 0, 1
all unique values in 'sex_i': 0, 1
all unique values in 'sex_m': 1, 0
example unique values in 'height_diameter_inter': 0.05, 0.04, 0.05, 0.12, 0.01, 0.06, 0.06, 0.07, 0.05, 0.03 ...
example unique values in 'height_diameter_inter_standard_scaled': 0.87, 1.01, -0.08, -0.49, -1.24, 0.24, 0.57, -0.24, 0.81, 2.25 ...
example unique values in 'viscera_weight_quantiled_n=4_distr=normal': 0.87, -0.72, -0.42, 0.25, -0.88, -0.13, 0.49, 0.36, -0.11, 1.0 ...
example unique values in 'height_log': -1.92, -2.27, -2.3, -1.83, -1.97, -1.81, -2.18, -2.2, -2.1, -1.9 ...
example unique values in 'height_diameter_sub': -0.29, -0.36, -0.25, -0.26, -0.06, -0.15, -0.26, -0.3, -0.2, -0.31 ...
example unique values in 'length_diameter_sub': 0.13, 0.18, 0.16, 0.15, 0.16, 0.13, 0.09, 0.19, 0.21, 0.08 ...
example unique values in 'target': 3.4, 3.56, 3.64, 3.48, 3.2, 3.77, 3.83, 4.09, 2.95, 4.0 ...
- *CORRELATIONS:*
correlation between 'height_diameter_inter_standard_scaled' and 'height_diameter_inter': 1.0
correlation between 'height_diameter_inter_standard_scaled' and 'height': 0.94
correlation between 'height_diameter_inter' and 'height': 0.94
correlation between 'height_log' and 'height': 0.94
correlation between 'diameter' and 'length': 0.92
correlation between 'height_diameter_sub' and 'diameter': -0.91
correlation between 'viscera_weight' and 'whole_weight': 0.9
correlation between 'shucked_weight' and 'whole_weight': 0.89
correlation between 'shell_weight' and 'whole_weight': 0.88
correlation between 'height_diameter_inter' and 'diameter': 0.87
correlation between 'height_diameter_inter_standard_scaled' and 'diameter': 0.87
correlation between 'whole_weight' and 'diameter': 0.87
correlation between 'height_log' and 'height_diameter_inter_standard_scaled': 0.86
correlation between 'viscera_weight' and 'shucked_weight': 0.85
correlation between 'shell_weight' and 'diameter': 0.85
correlation between 'viscera_weight_quantiled_n=4_distr=normal' and 'whole_weight': 0.85
correlation between 'height_diameter_inter' and 'whole_weight': 0.84
correlation between 'shell_weight' and 'length': 0.84
correlation between 'height_diameter_inter_standard_scaled' and 'whole_weight': 0.84
correlation between 'viscera_weight' and 'length': 0.83
correlation between 'height_diameter_inter_standard_scaled' and 'shell_weight': 0.82
correlation between 'height_diameter_inter' and 'shell_weight': 0.82
correlation between 'height_diameter_sub' and 'whole_weight': -0.73
correlation between 'height_diameter_sub' and 'shell_weight': -0.72
correlation between 'whole_weight' and 'height': 0.71
correlation between 'height_diameter_sub' and 'viscera_weight_quantiled_n=4_distr=normal': -0.71
correlation between 'height_log' and 'length': 0.71
correlation between 'height_diameter_sub' and 'shucked_weight': -0.7
correlation between 'viscera_weight' and 'height': 0.68
correlation between 'height_log' and 'whole_weight': 0.67
correlation between 'height_log' and 'viscera_weight_quantiled_n=4_distr=normal': 0.66
correlation between 'height_log' and 'shucked_weight': 0.61
correlation between 'length_diameter_sub' and 'length': 0.59
correlation between 'height_diameter_sub' and 'height_diameter_inter_standard_scaled': -0.59
correlation between 'sex_i' and 'whole_weight': -0.53
correlation between 'sex_i' and 'viscera_weight': -0.53
correlation between 'sex_i' and 'diameter': -0.53
correlation between 'sex_i' and 'shell_weight': -0.52
correlation between 'height_log' and 'sex_i': -0.48
correlation between 'target' and 'height_diameter_inter': -0.44
correlation between 'target' and 'viscera_weight_quantiled_n=4_distr=normal': -0.43
correlation between 'height_diameter_sub' and 'sex_i': 0.43
correlation between 'target' and 'shell_weight': -0.42
correlation between 'height_diameter_sub' and 'height_log': -0.4
correlation between 'target' and 'height_log': -0.38
correlation between 'target' and 'sex_i': 0.37
correlation between 'length_diameter_sub' and 'whole_weight': 0.35
correlation between 'length_diameter_sub' and 'viscera_weight': 0.35
correlation between 'height_diameter_sub' and 'height': -0.35
correlation between 'viscera_weight_quantiled_n=4_distr=normal' and 'sex_f': 0.31

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: 1.92%
Error: 0.5550
Added columns: {'height_diameter_inter', 'whole_weight_min_max_scaled', 'length_diameter_sub'}
Removed columns: set()
Iteration 2:
Error change relative to previous iteration: -1.21%
Error: 0.5483
Added columns: {'height_diameter_inter_standard_scaled', 'height_log', 'height_diameter_sub', 'viscera_weight_quantiled_n=4_distr=normal'}
Removed columns: {'whole_weight_min_max_scaled'}

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