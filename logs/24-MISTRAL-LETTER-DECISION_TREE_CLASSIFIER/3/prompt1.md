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
example unique values in 'x-bar_y-bar_sub': 10.27, -3.79, 1.52, 4.75, 2.13, 2.04, -2.22, -2.15, -4.17, 1.76 ...
example unique values in 'x-box_y-box_combination': 7.33, 9.34, 6.9, 4.56, 5.62, 7.39, 6.67, 2.66, 1.56, 6.84 ...
example unique values in 'onpix_log': 2.37, 0.65, 1.55, -4.46, 1.41, -0.94, 0.98, 1.24, 0.78, -1.7 ...
example unique values in 'x-ege_width_inter': 13.32, 5.2, 11.95, 9.06, 0.44, 27.95, 10.1, 85.92, 49.41, 12.35 ...
example unique values in 'high_min_max_scaled': 0.3, 0.64, 0.63, 0.42, 0.13, 0.54, 0.47, 0.23, 0.47, 0.57 ...
example unique values in 'x-box_power_transformed_yeo-johnson': -0.25, -0.56, 0.07, -0.56, -0.76, -1.73, 0.85, 0.46, -0.21, 0.03 ...
example unique values in 'width_high_inter': 9.26, 48.43, 35.95, 19.27, 14.2, 35.79, 45.36, 51.28, 32.51, 57.67 ...
example unique values in 'onpix_quantiled_n=100_distr=uniform': 0.71, 0.1, 0.72, 0.1, 0.62, 0.33, 0.21, 0.73, 0.77, 0.33 ...
example unique values in 'x-bar_y-box_inter': 60.46, 75.36, 64.96, 73.99, 3.24, 20.69, 35.68, 99.99, 48.37, 66.83 ...
example unique values in 'onpix_width_high_TruncatedSVD': 10.83, 15.03, 9.74, 5.57, 10.19, 3.49, 9.76, 8.71, 7.86, 8.71 ...
example unique values in 'x-ege_abs': 2.0, 1.62, 0.61, 0.31, 2.87, 0.3, 2.3, 0.48, 8.84, 2.41 ...
example unique values in 'target': 22, 7, 6, 12, 9, 16, 4, 21, 13, 17 ...
- *CORRELATIONS:*
correlation between 'x-box_power_transformed_yeo-johnson' and 'x-box': 0.99
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'onpix': 0.94
correlation between 'x-ege_width_inter' and 'x-ege': 0.92
correlation between 'x-ege_abs' and 'x-ege_width_inter': 0.92
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'onpix_log': 0.9
correlation between 'onpix_width_high_TruncatedSVD' and 'high': 0.87
correlation between 'onpix_width_high_TruncatedSVD' and 'onpix_quantiled_n=100_distr=uniform': 0.84
correlation between 'x-bar_y-box_inter' and 'y-box': 0.81
correlation between 'high' and 'y-box': 0.78
correlation between 'x-bar_y-box_inter' and 'x-box_y-box_combination': 0.77
correlation between 'x-box_y-box_combination' and 'high': 0.77
correlation between 'width_high_inter' and 'x-box_power_transformed_yeo-johnson': 0.76
correlation between 'width_high_inter' and 'y-box': 0.73
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'width': 0.71
correlation between 'width_high_inter' and 'onpix': 0.71
correlation between 'y-box' and 'x-box': 0.69
correlation between 'x-ege_width_inter' and 'width': 0.69
correlation between 'onpix_width_high_TruncatedSVD' and 'x-bar_y-box_inter': 0.65
correlation between 'width_high_inter' and 'onpix_log': 0.64
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'x-box_power_transformed_yeo-johnson': 0.63
correlation between 'onpix_width_high_TruncatedSVD' and 'x-ege_width_inter': 0.63
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'x-box': 0.61
correlation between 'onpix_log' and 'x-box_y-box_combination': 0.6
correlation between 'high_min_max_scaled' and 'width': 0.59
correlation between 'high' and 'width': 0.59
correlation between 'x-box_power_transformed_yeo-johnson' and 'onpix': 0.59
correlation between 'x-ege' and 'onpix': 0.59
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'y-box': 0.57
correlation between 'high_min_max_scaled' and 'onpix': 0.56
correlation between 'onpix' and 'high': 0.56
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'x-ege': 0.54
correlation between 'x-ege_abs' and 'onpix_quantiled_n=100_distr=uniform': 0.53
correlation between 'x-ege_width_inter' and 'onpix_log': 0.52
correlation between 'x-bar_y-box_inter' and 'onpix_quantiled_n=100_distr=uniform': 0.52
correlation between 'x-ege' and 'width': 0.51
correlation between 'onpix_width_high_TruncatedSVD' and 'x-ege': 0.49
correlation between 'x-ege_width_inter' and 'x-box_y-box_combination': 0.48
correlation between 'xegvy' and 'y-bar': 0.48
correlation between 'onpix_log' and 'x-ege': 0.47
correlation between 'x-ege_abs' and 'onpix_log': 0.46
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'y-ege': 0.44
correlation between 'x-box_power_transformed_yeo-johnson' and 'x-ege': 0.43
correlation between 'width_high_inter' and 'x-ege': 0.43
correlation between 'x-ege_abs' and 'x-box': 0.43
correlation between 'y-ege' and 'onpix': 0.43
correlation between 'x-ege_abs' and 'x-box_power_transformed_yeo-johnson': 0.42
correlation between 'x-ege' and 'y2bar': -0.4
correlation between 'target' and 'x2ybr': 0.37
correlation between 'x-bar_y-box_inter' and 'x-ege_width_inter': 0.37
correlation between 'x-ege_abs' and 'x-box_y-box_combination': 0.34

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: -2.40%
Score: 0.4470
Added columns: {'x-bar_y-bar_sub', 'onpix_log', 'x-box_y-box_combination', 'high_min_max_scaled', 'x-ege_width_inter', 'onpix_power_transformed_yeo-johnson', 'width_high_PCA'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: 0.45%
Score: 0.4490
Added columns: {'onpix_quantiled_n=100_distr=uniform', 'x-box_power_transformed_yeo-johnson', 'x-bar_y-box_inter', 'x-ege_abs', 'onpix_width_high_TruncatedSVD', 'width_high_inter'}
Removed columns: {'onpix_power_transformed_yeo-johnson'}

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
- You create new features from existing columns to make ML Decision Tree Classifier model better at predicting target variable 'target' in classification problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**