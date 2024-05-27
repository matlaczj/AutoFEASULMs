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
example unique values in 'length_diameter_combination': 0.44, 0.49, 0.52, 0.65, 0.23, 0.43, 0.51, 0.53, 0.51, 0.38 ...
example unique values in 'viscera_weight_min_max_scaled': 0.45, 0.65, 0.29, 0.28, 0.22, 0.27, 0.4, 0.22, 0.74, 0.44 ...
example unique values in 'height_diameter_PCA': -0.12, 0.2, 0.05, -0.07, 0.26, 0.01, -0.2, -0.03, 0.02, -0.14 ...
example unique values in 'length_min_max_scaled': 0.67, 0.43, 0.49, 0.81, 0.69, 0.47, 0.39, 0.82, 0.74, 0.51 ...
example unique values in 'diameter_min_max_scaled': 0.62, 0.69, 0.49, 0.56, 0.08, 0.12, 0.56, 0.56, 0.36, 0.69 ...
example unique values in 'whole_weight_log': -2.85, -0.5, -0.07, -0.97, -2.67, -1.85, 0.17, 0.2, -0.27, -0.07 ...
example unique values in 'viscera_weight_log': -1.63, -3.12, -1.14, -2.1, -1.23, -1.39, -2.53, -0.83, -2.8, -1.16 ...
example unique values in 'shucked_weight_quantiled_n=100_distr=normal': -1.58, -1.59, 1.79, -0.63, 1.36, -1.18, -0.29, 0.59, 2.4, 0.05 ...
example unique values in 'height_diameter_sub': -0.36, -0.29, -0.31, -0.32, -0.26, -0.29, -0.15, -0.42, -0.23, -0.24 ...
example unique values in 'shucked_weight_length_sub': -0.2, -0.09, -0.17, -0.24, 0.14, -0.15, -0.17, -0.04, -0.04, -0.21 ...
all unique values in 'whole_weight_binarized_th=0.0': 1.0, 0.0
all unique values in 'height_diameter_sub_normalized_l2': -1.0, 1.0
example unique values in 'target': 3.08, 3.2, 3.83, 3.71, 1.69, 1.0, 3.3, 3.94, 3.89, 3.48 ...
- *CORRELATIONS:*
correlation between 'diameter_min_max_scaled' and 'height_diameter_PCA': -1.0
correlation between 'height_diameter_PCA' and 'diameter': -1.0
correlation between 'diameter_min_max_scaled' and 'length_min_max_scaled': 0.92
correlation between 'length_min_max_scaled' and 'height_diameter_PCA': -0.92
correlation between 'diameter' and 'length': 0.92
correlation between 'shucked_weight_length_sub' and 'shucked_weight': 0.88
correlation between 'height_diameter_PCA' and 'whole_weight': -0.88
correlation between 'height_diameter_PCA' and 'shell_weight': -0.86
correlation between 'height_diameter_sub' and 'length_diameter_combination': -0.86
correlation between 'whole_weight_log' and 'diameter_min_max_scaled': 0.86
correlation between 'height_diameter_sub' and 'height_diameter_PCA': 0.86
correlation between 'whole_weight_log' and 'length_min_max_scaled': 0.86
correlation between 'shucked_weight_quantiled_n=100_distr=normal' and 'length': 0.84
correlation between 'length_min_max_scaled' and 'shell_weight': 0.84
correlation between 'shucked_weight_length_sub' and 'shucked_weight_quantiled_n=100_distr=normal': 0.84
correlation between 'viscera_weight' and 'length': 0.83
correlation between 'length_min_max_scaled' and 'viscera_weight': 0.83
correlation between 'diameter_min_max_scaled' and 'viscera_weight': 0.83
correlation between 'length_diameter_combination' and 'shucked_weight': 0.83
correlation between 'shucked_weight_quantiled_n=100_distr=normal' and 'diameter': 0.83
correlation between 'viscera_weight_min_max_scaled' and 'diameter': 0.83
correlation between 'height_diameter_sub' and 'length_min_max_scaled': -0.81
correlation between 'shell_weight' and 'shucked_weight': 0.8
correlation between 'viscera_weight_log' and 'diameter_min_max_scaled': 0.8
correlation between 'shucked_weight_quantiled_n=100_distr=normal' and 'whole_weight_log': 0.79
correlation between 'shucked_weight_quantiled_n=100_distr=normal' and 'viscera_weight_log': 0.74
correlation between 'viscera_weight_log' and 'shell_weight': 0.73
correlation between 'height' and 'diameter': 0.72
correlation between 'height_diameter_sub' and 'viscera_weight': -0.7
correlation between 'length_min_max_scaled' and 'height': 0.7
correlation between 'whole_weight_log' and 'height': 0.68
correlation between 'shucked_weight_length_sub' and 'viscera_weight_min_max_scaled': 0.65
correlation between 'shucked_weight' and 'height': 0.65
correlation between 'length_min_max_scaled' and 'sex_i': -0.54
correlation between 'whole_weight_log' and 'sex_i': -0.53
correlation between 'sex_i' and 'whole_weight': -0.53
correlation between 'sex_m' and 'sex_i': -0.53
correlation between 'sex_i' and 'diameter': -0.53
correlation between 'sex_i' and 'shell_weight': -0.52
correlation between 'sex_i' and 'sex_f': -0.47
correlation between 'sex_i' and 'shucked_weight': -0.47
correlation between 'shucked_weight_length_sub' and 'height': 0.44
correlation between 'target' and 'height_diameter_PCA': 0.43
correlation between 'target' and 'viscera_weight': -0.43
correlation between 'target' and 'diameter_min_max_scaled': -0.42
correlation between 'shucked_weight_length_sub' and 'height_diameter_sub': -0.42
correlation between 'target' and 'height': -0.4
correlation between 'target' and 'shucked_weight_quantiled_n=100_distr=normal': -0.39
correlation between 'target' and 'viscera_weight_log': -0.39
correlation between 'sex_f' and 'viscera_weight': 0.31

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: -6.74%
Error: 0.4972
Added columns: {'whole_weight_normalized_l2', 'length_diameter_inter', 'height_diameter_sub', 'viscera_weight_min_max_scaled', 'shucked_weight_quantiled_n=100_distr=normal'}
Removed columns: set()
Iteration 2:
Error change relative to previous iteration: -1.65%
Error: 0.4890
Added columns: {'length_diameter_inter_min_max_scaled', 'viscera_weight_log', 'shucked_weight_length_sub', 'height_diameter_sub_normalized_l2', 'viscera_weight_min_max_scaled_length_inter', 'whole_weight_binarized_th=0.0'}
Removed columns: {'whole_weight_normalized_l2', 'length_diameter_inter'}
Iteration 3:
Error change relative to previous iteration: 0.01%
Error: 0.4891
Added columns: {'length_diameter_combination', 'diameter_min_max_scaled', 'length_min_max_scaled'}
Removed columns: {'length_diameter_inter_min_max_scaled', 'viscera_weight_min_max_scaled_length_inter'}
Iteration 4:
Error change relative to previous iteration: -0.11%
Error: 0.4885
Added columns: {'height_diameter_PCA', 'whole_weight_log'}
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