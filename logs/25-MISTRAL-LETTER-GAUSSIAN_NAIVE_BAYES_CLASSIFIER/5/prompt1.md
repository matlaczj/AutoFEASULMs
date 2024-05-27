**INTRODUCTION:**
Predict the letter category based on features (these columns might not exist, use columns from COLUMNS section):
class (target): This column is the target variable or label that you want to predict. It's a nominal variable with 26 distinct values, representing different classes or categories.
x-box: This column represents the horizontal position of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
y-box: This column represents the vertical position of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
width: This column represents the width of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
high: This column represents the height of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
onpix: This column represents the total number of "on" pixels (i.e., pixels that are part of the letter) in the bounding box. It's a numeric variable with 16 distinct values.
x-bar: This column represents the mean x-coordinate of "on" pixels in the bounding box. It's a numeric variable with 16 distinct values.

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'x-box': 3.53, 5.06, 3.78, 3.72, 12.26, 1.42, 2.03, 3.65, 2.76, 5.08 ...
example unique values in 'y-box': 8.54, 11.24, 6.13, 1.53, 9.57, 9.03, 10.67, 6.02, 11.6, 10.73 ...
example unique values in 'width': 7.17, 8.87, 3.48, 1.15, 2.35, 8.64, 8.19, 3.12, 10.43, 4.96 ...
example unique values in 'high': 7.53, 5.37, 5.21, 5.91, 7.13, 9.69, 7.73, 6.22, 8.04, 3.94 ...
example unique values in 'onpix': -0.75, 6.42, 4.89, 2.45, 0.67, 4.09, 4.62, 3.71, 4.75, 2.07 ...
example unique values in 'x-bar': 5.57, 7.66, 6.5, 5.09, 7.44, 7.55, 8.05, 6.72, 9.66, 7.26 ...
example unique values in 'y-bar': 8.85, 8.16, 5.95, 5.09, 2.41, 6.41, 5.37, 6.7, 8.99, 4.3 ...
example unique values in 'x2bar': 0.98, 3.42, 5.87, 15.02, 4.09, 3.46, 3.75, 6.22, 5.73, 2.96 ...
example unique values in 'y2bar': 5.61, 3.24, 7.79, 2.27, 6.29, 3.31, 8.55, 7.19, 7.37, 7.78 ...
example unique values in 'xybar': 6.85, 11.14, 7.23, 10.64, 13.83, 9.53, 11.18, 6.49, 7.13, 4.93 ...
example unique values in 'x2ybr': 4.42, 4.74, 4.96, 5.01, 8.4, 6.95, 8.6, 4.85, 7.27, 7.8 ...
example unique values in 'xy2br': 5.57, 8.95, 7.26, 8.15, 5.74, 8.95, 4.39, 7.75, 7.28, 9.42 ...
example unique values in 'x-ege': 1.84, 1.8, -1.02, 0.48, 3.28, 9.4, 0.17, -0.86, 0.13, 1.31 ...
example unique values in 'xegvy': 7.42, 10.69, 8.2, 3.27, 7.92, 8.12, 9.0, 6.25, 8.63, 8.73 ...
example unique values in 'y-ege': 6.25, 3.98, 0.7, 1.58, 7.07, 1.63, 4.37, 1.17, -0.72, 3.36 ...
example unique values in 'yegvx': 5.67, 10.84, 8.95, 8.26, 6.8, 11.07, 5.4, 7.17, 9.17, 7.51 ...
example unique values in 'x-box_y-box_inter': 25.06, 15.82, 2.27, 12.59, -0.01, 5.47, 0.42, 31.19, 63.77, 10.55 ...
example unique values in 'width_high_sub': 0.6, 3.3, -0.44, -1.13, -1.77, -1.38, 1.16, 0.58, 0.9, 0.84 ...
example unique values in 'onpix_log': 2.37, 0.65, 1.55, -4.46, 1.41, -0.94, 0.98, 1.24, 0.78, -1.7 ...
example unique values in 'width_min_max_scaled': 0.4, 0.41, 0.49, 0.36, 0.2, 0.64, 0.38, 0.67, 0.74, 0.57 ...
example unique values in 'x-box_min_max_scaled': 0.34, 0.36, 0.3, 0.4, 0.15, 0.37, 0.38, 0.18, 0.24, 0.52 ...
example unique values in 'onpix_width_combination': 8.15, 4.71, 7.67, 8.62, 7.31, 1.93, 13.06, 7.45, 6.52, 6.88 ...
example unique values in 'x-ege_standard_scaled': -0.43, -0.28, 1.42, 0.36, -0.42, 0.37, -0.73, -0.93, 0.25, -0.47 ...
example unique values in 'x-ege_quantiled_n=100_distr=uniform': 0.79, 0.63, 0.96, 0.04, 0.83, 0.24, 0.3, 0.86, 0.78, 0.47 ...
example unique values in 'x-box_y-box_sub': -4.52, -7.99, -4.32, -5.05, -2.8, -2.12, -1.38, -6.3, -1.25, -5.95 ...
example unique values in 'x2ybr_abs': 5.82, 5.99, 1.14, 8.68, 13.02, 10.37, 11.46, 5.59, 4.45, 7.1 ...
example unique values in 'x-bar_y-bar_inter': 56.45, 52.39, 26.86, 45.12, 51.16, 1.17, 32.59, 56.75, 44.85, 48.19 ...
example unique values in 'width_log': 1.36, 1.46, 0.49, 1.35, 2.07, 1.74, 1.71, 1.72, 1.32, 1.34 ...
example unique values in 'width_power_transformed_yeo-johnson': -1.65, -1.06, 0.74, -0.51, 0.72, 0.56, 0.62, 1.35, -0.33, 0.8 ...
example unique values in 'onpix_quantiled_n=100_distr=uniform': 0.27, 0.57, 0.82, 0.2, 0.72, 0.23, 0.94, 0.26, 0.84, 0.06 ...
example unique values in 'width_high_combination': 2.87, 7.17, 8.92, 3.79, 3.3, 5.49, 6.45, 3.4, 4.05, 5.93 ...
example unique values in 'width_log_high_sub': -5.25, -3.64, -1.81, -3.24, -4.3, -4.39, -9.25, -1.38, -2.07, -2.18 ...
example unique values in 'x-box_y-box_PCA': -0.93, -0.45, 0.28, 4.52, -2.1, 1.61, 1.49, 2.17, 2.93, -1.81 ...
all unique values in 'onpix_binarized_th=0.0': 1.0, 0.0
example unique values in 'target': 22, 8, 9, 17, 19, 18, 23, 24, 25, 21 ...
- *CORRELATIONS:*
correlation between 'x-ege_standard_scaled' and 'x-ege': 1.0
correlation between 'width_min_max_scaled' and 'width': 1.0
correlation between 'x-box_y-box_inter' and 'x-box': 0.92
correlation between 'x-box_y-box_PCA' and 'x-box_y-box_inter': 0.9
correlation between 'width_high_combination' and 'width_power_transformed_yeo-johnson': 0.88
correlation between 'width_high_combination' and 'width': 0.87
correlation between 'x-box_y-box_sub' and 'y-box': -0.83
correlation between 'x-box_y-box_PCA' and 'x-box': 0.8
correlation between 'x-box_y-box_PCA' and 'x-box_min_max_scaled': 0.8
correlation between 'width_high_combination' and 'y-box': 0.79
correlation between 'width_high_combination' and 'x-box_min_max_scaled': 0.76
correlation between 'onpix_width_combination' and 'x-box': 0.73
correlation between 'width_log_high_sub' and 'y-box': -0.73
correlation between 'width_power_transformed_yeo-johnson' and 'x-box_y-box_inter': 0.72
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'width_power_transformed_yeo-johnson': 0.72
correlation between 'width_log_high_sub' and 'width_high_sub': 0.72
correlation between 'onpix' and 'width': 0.7
correlation between 'y-box' and 'x-box': 0.69
correlation between 'width_power_transformed_yeo-johnson' and 'onpix_log': 0.66
correlation between 'onpix_log' and 'width': 0.65
correlation between 'width_log' and 'onpix': 0.64
correlation between 'x-box_y-box_PCA' and 'width_log': 0.64
correlation between 'x-box_y-box_PCA' and 'onpix_quantiled_n=100_distr=uniform': 0.61
correlation between 'onpix_width_combination' and 'x-ege': 0.6
correlation between 'x-ege_standard_scaled' and 'onpix_width_combination': 0.6
correlation between 'x-box_y-box_sub' and 'high': -0.59
correlation between 'width_high_sub' and 'high': -0.59
correlation between 'onpix_log' and 'high': 0.57
correlation between 'onpix_log' and 'x-box': 0.57
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'x-ege_standard_scaled': 0.54
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'x-ege': 0.54
correlation between 'x-bar_y-bar_inter' and 'y-bar': 0.52
correlation between 'width_log_high_sub' and 'x-box_min_max_scaled': -0.5
correlation between 'width_high_combination' and 'x-box_y-box_sub': -0.49
correlation between 'width_log_high_sub' and 'onpix': -0.47
correlation between 'onpix_log' and 'x-ege': 0.47
correlation between 'x-ege_standard_scaled' and 'onpix_log': 0.47
correlation between 'width_log' and 'x-ege_standard_scaled': 0.45
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'y-ege': 0.44
correlation between 'width_high_combination' and 'x-ege_standard_scaled': 0.41
correlation between 'onpix_binarized_th=0.0' and 'onpix_log': 0.4
correlation between 'width_high_combination' and 'x-ege_quantiled_n=100_distr=uniform': 0.39
correlation between 'x-ege_standard_scaled' and 'x-box_y-box_inter': 0.38
correlation between 'x-box_y-box_inter' and 'x-ege': 0.38
correlation between 'target' and 'x2ybr': 0.37
correlation between 'x-ege_quantiled_n=100_distr=uniform' and 'x-box_y-box_inter': 0.37
correlation between 'y-bar' and 'x-bar': -0.33
correlation between 'target' and 'xegvy': 0.31
correlation between 'onpix_binarized_th=0.0' and 'width_log': 0.31
correlation between 'x-box_y-box_sub' and 'onpix_log': -0.3

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: -8.79%
Score: 0.5190
Added columns: {'x-box_y-box_inter', 'width_high_sub', 'onpix_log', 'width_high_PCA', 'width_min_max_scaled'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: -7.32%
Score: 0.4810
Added columns: {'x-ege_standard_scaled', 'onpix_width_combination', 'x-box_min_max_scaled'}
Removed columns: set()
Iteration 3:
Score change relative to previous iteration: 2.49%
Score: 0.4930
Added columns: {'x-box_y-box_sub', 'width_log', 'x-bar_y-bar_inter', 'onpix_sqrt', 'x2ybr_abs', 'x-ege_quantiled_n=100_distr=uniform'}
Removed columns: set()
Iteration 4:
Score change relative to previous iteration: -2.64%
Score: 0.4800
Added columns: {'x-box_y-box_PCA', 'width_log_high_sub', 'onpix_quantiled_n=100_distr=uniform', 'width_power_transformed_yeo-johnson', 'width_high_combination', 'onpix_binarized_th=0.0'}
Removed columns: {'width_high_PCA', 'onpix_sqrt'}

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
- You create new features from existing columns to make ML Gaussian Naive Bayes Classifier model better at predicting target variable 'target' in classification problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**