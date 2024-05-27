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
example unique values in 'onpix_quantiled_n=100_distr=uniform': 0.29, 0.86, 0.81, 0.15, 0.39, 0.76, 0.78, 0.62, 0.88, 0.8 ...
example unique values in 'x-bar_y-box_inter': 130.32, 27.16, 44.39, 13.34, 18.68, 52.87, 7.73, 34.96, 38.94, 58.35 ...
example unique values in 'x-ege_abs': 0.36, 0.15, 0.41, 7.24, 0.85, 3.95, 0.32, 0.3, 3.71, 2.79 ...
example unique values in 'onpix_min_max_scaled': 0.48, 0.71, 0.23, 0.21, 0.09, 0.11, 0.26, 0.29, 0.2, 0.24 ...
example unique values in 'x-box_high_inter': 20.32, 1.52, 42.38, 0.1, 62.93, 0.17, 22.68, 13.32, 40.81, 125.06 ...
example unique values in 'y-ege_standard_scaled': -1.45, 0.98, -1.69, -0.65, 0.54, -0.69, -0.99, 0.98, -0.1, -0.94 ...
example unique values in 'x-box_y-ege_inter': 2.24, 11.86, 23.37, 3.96, 39.71, 0.55, 12.22, 13.97, -1.65, 46.21 ...
example unique values in 'width_onpix_PCA': -2.54, -0.08, 1.89, -3.24, 3.07, -2.0, 4.44, -1.62, 2.41, -3.93 ...
example unique values in 'high_log': 0.39, 2.01, 2.13, 1.22, 1.42, 1.96, 2.02, 1.52, 1.49, 1.98 ...
example unique values in 'onpix_quantiled_n=50_distr=normal': 1.12, -1.08, -1.09, 0.64, 0.38, 0.89, -1.24, 1.18, 0.04, -0.2 ...
example unique values in 'onpix_power_transformed_yeo-johnson': -0.43, -0.58, -0.34, 1.5, -0.77, 0.52, -0.91, -0.89, 1.72, -0.89 ...
example unique values in 'width_high_PCA': -0.95, 0.52, -2.26, 4.05, 2.26, -0.76, -0.06, -1.24, -0.45, -1.97 ...
example unique values in 'x-box_y-box_sub': -1.28, -9.26, -3.81, -4.28, -4.39, -4.35, -6.15, -1.19, 2.4, 2.63 ...
all unique values in 'onpix_normalized_l2': 1.0, -1.0
example unique values in 'x-ege_log': 0.96, -0.23, 0.88, 1.65, -1.92, 1.77, -2.61, 0.81, -0.18, 0.72 ...
example unique values in 'target': 20, 0, 23, 8, 9, 13, 18, 25, 10, 2 ...
- *CORRELATIONS:*
correlation between 'high_min_max_scaled' and 'high': 1.0
correlation between 'x-box_power_transformed_yeo-johnson' and 'x-box': 0.99
correlation between 'onpix_quantiled_n=50_distr=normal' and 'onpix': 0.97
correlation between 'onpix_quantiled_n=50_distr=normal' and 'onpix_min_max_scaled': 0.97
correlation between 'onpix_quantiled_n=50_distr=normal' and 'onpix_quantiled_n=100_distr=uniform': 0.97
correlation between 'width_high_PCA' and 'high': -0.94
correlation between 'onpix_power_transformed_yeo-johnson' and 'width_onpix_PCA': 0.93
correlation between 'onpix_quantiled_n=50_distr=normal' and 'onpix_log': 0.91
correlation between 'width_high_PCA' and 'high_log': -0.85
correlation between 'x-bar_y-bar_sub' and 'y-bar': -0.84
correlation between 'x-box_y-ege_inter' and 'y-ege': 0.82
correlation between 'width_high_PCA' and 'y-box': -0.8
correlation between 'high_log' and 'x-box_y-box_combination': 0.72
correlation between 'x-box_power_transformed_yeo-johnson' and 'y-box': 0.7
correlation between 'width_onpix_PCA' and 'x-box_y-box_combination': 0.7
correlation between 'x-ege_width_inter' and 'width': 0.69
correlation between 'y-box' and 'x-box': 0.69
correlation between 'onpix_min_max_scaled' and 'x-ege_width_inter': 0.69
correlation between 'x-box_y-ege_inter' and 'x-box_high_inter': 0.65
correlation between 'width_onpix_PCA' and 'high_min_max_scaled': 0.62
correlation between 'onpix_power_transformed_yeo-johnson' and 'x-box_y-box_combination': 0.61
correlation between 'x-box_high_inter' and 'onpix': 0.6
correlation between 'high_min_max_scaled' and 'x-box': 0.6
correlation between 'width_onpix_PCA' and 'x-ege_abs': 0.6
correlation between 'high' and 'width': 0.59
correlation between 'high_log' and 'width': 0.57
correlation between 'onpix_quantiled_n=100_distr=uniform' and 'y-box': 0.57
correlation between 'onpix_log' and 'high': 0.57
correlation between 'high_log' and 'onpix_quantiled_n=100_distr=uniform': 0.56
correlation between 'x-box_power_transformed_yeo-johnson' and 'x-ege_width_inter': 0.55
correlation between 'x-bar_y-box_inter' and 'x-box_power_transformed_yeo-johnson': 0.54
correlation between 'x-bar_y-box_inter' and 'x-box': 0.53
correlation between 'high_log' and 'onpix': 0.52
correlation between 'x-box_y-box_sub' and 'width_high_PCA': 0.51
correlation between 'x-box_y-ege_inter' and 'onpix_log': 0.51
correlation between 'onpix_min_max_scaled' and 'x-bar_y-box_inter': 0.49
correlation between 'x-ege_log' and 'onpix_min_max_scaled': 0.47
correlation between 'x-box_y-ege_inter' and 'high': 0.46
correlation between 'xegvy' and 'x2ybr': 0.46
correlation between 'y-ege_standard_scaled' and 'onpix_quantiled_n=100_distr=uniform': 0.44
correlation between 'x-box_power_transformed_yeo-johnson' and 'x-ege': 0.43
correlation between 'onpix_quantiled_n=50_distr=normal' and 'y-ege_standard_scaled': 0.43
correlation between 'x-ege_abs' and 'x-box': 0.43
correlation between 'x-ege_abs' and 'x-box_power_transformed_yeo-johnson': 0.42
correlation between 'x-ege_log' and 'onpix_log': 0.41
correlation between 'x-ege_abs' and 'y2bar': -0.4
correlation between 'target' and 'x2ybr': 0.37
correlation between 'x-box_y-box_sub' and 'x-box_high_inter': -0.32
correlation between 'x-ege_log' and 'x-box_high_inter': 0.31
correlation between 'x-ege_log' and 'width_high_PCA': -0.31

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
Iteration 3:
Score change relative to previous iteration: 1.56%
Score: 0.4560
Added columns: {'width_onpix_PCA', 'y-ege_standard_scaled', 'onpix_min_max_scaled', 'onpix_quantiled_n=50_distr=normal', 'x-box_high_inter', 'x-box_y-ege_inter', 'high_log'}
Removed columns: {'width_high_PCA', 'width_high_inter'}
Iteration 4:
Score change relative to previous iteration: -3.51%
Score: 0.4400
Added columns: {'x-box_y-box_sub', 'onpix_power_transformed_yeo-johnson', 'width_high_PCA', 'x-ege_log', 'onpix_normalized_l2'}
Removed columns: {'onpix_width_high_TruncatedSVD'}

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