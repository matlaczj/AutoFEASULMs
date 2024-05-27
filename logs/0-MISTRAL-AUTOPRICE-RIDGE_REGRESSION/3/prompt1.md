**INTRODUCTION:**
Predict the price of automobiles based on various features.
**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'symboling': -0.93, 0.36, 2.13, 2.87, -0.27, 1.05, 3.13, 0.14, 2.11, 2.38 ...
example unique values in 'normalized-losses': 74.86, 103.8, 64.88, 93.23, 130.24, 135.76, 112.04, 159.85, 259.06, 154.17 ...
example unique values in 'wheel-base': 99.71, 102.77, 94.42, 98.11, 96.69, 106.92, 98.89, 114.03, 97.1, 103.71 ...
example unique values in 'length': 145.65, 178.41, 187.96, 167.05, 169.87, 178.56, 140.57, 189.77, 175.84, 177.23 ...
example unique values in 'width': 64.27, 65.41, 63.99, 66.8, 70.9, 63.19, 63.18, 65.96, 66.97, 62.87 ...
example unique values in 'height': 52.07, 56.41, 58.35, 51.93, 49.69, 51.41, 51.97, 55.81, 56.4, 56.84 ...
example unique values in 'curb-weight': 3737.76, 2118.57, 3501.02, 2030.98, 2308.85, 3228.68, 1429.28, 2791.54, 2213.82, 2632.23 ...
example unique values in 'engine-size': 89.67, 90.89, 131.47, 116.51, 96.74, 146.46, 121.74, 122.82, 101.75, 117.55 ...
example unique values in 'bore': 3.58, 2.99, 2.97, 3.81, 2.96, 3.48, 3.25, 3.77, 3.58, 3.19 ...
example unique values in 'stroke': 2.91, 3.49, 3.05, 3.25, 3.21, 3.43, 2.92, 3.38, 3.16, 2.66 ...
example unique values in 'compression-ratio': 7.53, 9.35, 7.56, 9.0, 8.7, 10.51, 10.74, 9.03, 7.2, 10.01 ...
example unique values in 'horsepower': 163.66, 74.14, 102.48, 59.66, 70.35, 65.87, 116.98, 75.34, 57.52, 79.36 ...
example unique values in 'peak-rpm': 5817.16, 4502.96, 4889.83, 5421.47, 5996.91, 4426.94, 5453.31, 5481.16, 4869.92, 4822.73 ...
example unique values in 'city-mpg': 27.44, 22.58, 16.26, 35.69, 26.32, 31.99, 18.75, 17.33, 39.1, 20.21 ...
example unique values in 'highway-mpg': 39.88, 31.78, 37.26, 33.72, 38.59, 31.46, 29.5, 35.17, 37.94, 30.93 ...
all unique values in 'length_binarized_n=5_enc=ordinal_strat=quantile': 3.0, 4.0, 2.0, 0.0, 1.0
example unique values in 'symboling_city-mpg_combination': -8.69, -8.03, -9.28, -10.96, -9.01, -4.8, -9.13, -5.66, -3.84, -7.82 ...
example unique values in 'bore_power_transformed_box-cox': -0.33, -1.33, 1.62, 1.48, -0.75, -0.57, 0.9, -1.58, 0.39, 0.98 ...
example unique values in 'symboling_length_inter': 130.45, 364.4, -13.2, 145.65, -27.36, 219.19, -309.45, 299.86, 189.6, 185.9 ...
example unique values in 'normalized-losses_log': 4.59, 4.42, 4.84, 4.57, 4.55, 5.2, 4.51, 4.75, 4.63, 5.23 ...
example unique values in 'city-mpg_highway-mpg_sub': -5.41, -7.47, -2.79, -2.81, -5.24, -3.84, -7.81, -4.33, -5.81, -3.79 ...
all unique values in 'width_normalized_l2': 1.0
example unique values in 'target': 10.21, 9.87, 10.78, 10.51, 10.21, 11.02, 9.88, 10.68, 10.04, 10.68 ...
- *CORRELATIONS:*
correlation between 'symboling_length_inter' and 'symboling': 1.0
correlation between 'symboling_city-mpg_combination' and 'city-mpg': -0.97
correlation between 'length_binarized_n=5_enc=ordinal_strat=quantile' and 'length': 0.95
correlation between 'highway-mpg' and 'city-mpg': 0.89
correlation between 'symboling_city-mpg_combination' and 'highway-mpg': -0.84
correlation between 'city-mpg' and 'horsepower': -0.82
correlation between 'target' and 'length_binarized_n=5_enc=ordinal_strat=quantile': 0.81
correlation between 'engine-size' and 'curb-weight': 0.81
correlation between 'highway-mpg' and 'horsepower': -0.8
correlation between 'target' and 'horsepower': 0.8
correlation between 'curb-weight' and 'wheel-base': 0.78
correlation between 'horsepower' and 'curb-weight': 0.77
correlation between 'width' and 'length': 0.76
correlation between 'target' and 'wheel-base': 0.76
correlation between 'width' and 'wheel-base': 0.76
correlation between 'target' and 'city-mpg': -0.75
correlation between 'engine-size' and 'width': 0.73
correlation between 'target' and 'symboling_city-mpg_combination': 0.7
correlation between 'engine-size' and 'length': 0.68
correlation between 'city-mpg' and 'length': -0.67
correlation between 'length_binarized_n=5_enc=ordinal_strat=quantile' and 'highway-mpg': -0.66
correlation between 'engine-size' and 'wheel-base': 0.65
correlation between 'bore_power_transformed_box-cox' and 'length_binarized_n=5_enc=ordinal_strat=quantile': 0.64
correlation between 'highway-mpg' and 'width': -0.63
correlation between 'length_binarized_n=5_enc=ordinal_strat=quantile' and 'horsepower': 0.63
correlation between 'city-mpg' and 'engine-size': -0.62
correlation between 'bore_power_transformed_box-cox' and 'length': 0.62
correlation between 'bore_power_transformed_box-cox' and 'curb-weight': 0.62
correlation between 'target' and 'bore': 0.62
correlation between 'bore_power_transformed_box-cox' and 'city-mpg': -0.6
correlation between 'city-mpg' and 'bore': -0.59
correlation between 'bore_power_transformed_box-cox' and 'horsepower': 0.58
correlation between 'horsepower' and 'bore': 0.58
correlation between 'highway-mpg' and 'bore': -0.57
correlation between 'bore' and 'wheel-base': 0.54
correlation between 'bore_power_transformed_box-cox' and 'symboling_city-mpg_combination': 0.54
correlation between 'symboling_city-mpg_combination' and 'bore': 0.54
correlation between 'normalized-losses_log' and 'symboling_length_inter': 0.53
correlation between 'symboling_length_inter' and 'normalized-losses': 0.51
correlation between 'normalized-losses' and 'symboling': 0.51
correlation between 'height' and 'symboling': -0.49
correlation between 'height' and 'length': 0.48
correlation between 'symboling_length_inter' and 'height': -0.47
correlation between 'length_binarized_n=5_enc=ordinal_strat=quantile' and 'height': 0.46
correlation between 'symboling_length_inter' and 'wheel-base': -0.45
correlation between 'symboling_city-mpg_combination' and 'wheel-base': 0.44
correlation between 'normalized-losses_log' and 'height': -0.43
correlation between 'peak-rpm' and 'compression-ratio': -0.4
correlation between 'normalized-losses_log' and 'symboling_city-mpg_combination': 0.32
correlation between 'curb-weight' and 'height': 0.32

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: -3.72%
Error: 0.0147
Added columns: {'height_binarized_n=5_enc=ordinal_strat=quantile', 'symboling_length_inter', 'city-mpg_highway-mpg_sub', 'width_normalized_l2'}
Removed columns: set()
Iteration 2:
Error change relative to previous iteration: 3.06%
Error: 0.0151
Added columns: {'normalized-losses_log', 'symboling_city-mpg_combination', 'bore_power_transformed_box-cox', 'length_binarized_n=5_enc=ordinal_strat=quantile'}
Removed columns: {'height_binarized_n=5_enc=ordinal_strat=quantile'}

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