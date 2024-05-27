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
example unique values in 'target': 2, 14, 21, 11, 24, 13, 20, 19, 15, 23 ...
- *CORRELATIONS:*
correlation between 'high' and 'y-box': 0.78
correlation between 'width' and 'x-box': 0.78
correlation between 'onpix' and 'width': 0.7
correlation between 'y-box' and 'x-box': 0.69
correlation between 'width' and 'y-box': 0.63
correlation between 'high' and 'x-box': 0.6
correlation between 'x-ege' and 'onpix': 0.59
correlation between 'high' and 'width': 0.59
correlation between 'onpix' and 'x-box': 0.57
correlation between 'onpix' and 'high': 0.56
correlation between 'x2ybr' and 'y-bar': 0.55
correlation between 'onpix' and 'y-box': 0.52
correlation between 'x-ege' and 'width': 0.51
correlation between 'xegvy' and 'y-bar': 0.48
correlation between 'xegvy' and 'x2ybr': 0.46
correlation between 'x-ege' and 'x-box': 0.44
correlation between 'y-ege' and 'onpix': 0.43
correlation between 'x-ege' and 'y2bar': -0.4
correlation between 'target' and 'x2ybr': 0.37
correlation between 'y-bar' and 'x-bar': -0.33
correlation between 'target' and 'xegvy': 0.31

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