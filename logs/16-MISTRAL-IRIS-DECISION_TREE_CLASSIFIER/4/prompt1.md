**INTRODUCTION:**
Predict the class of iris plants based on features (these columns might not exist, use columns from COLUMNS section):
**Attribute Information**:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class: 
   -- Iris Setosa
   -- Iris Versicolour
   -- Iris Virginica

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'sepallength': 6.65, 6.06, 5.7, 6.4, 5.41, 6.74, 6.5, 5.5, 6.78, 5.97 ...
example unique values in 'sepalwidth': 2.78, 3.14, 3.18, 3.65, 3.24, 3.34, 3.51, 2.98, 3.16, 3.02 ...
example unique values in 'petallength': 4.68, 1.51, 3.7, 3.41, 5.58, 1.66, 4.82, 1.24, 3.72, 1.45 ...
example unique values in 'petalwidth': 1.82, 1.17, 0.27, 2.04, 1.81, 1.79, 0.18, 2.57, 2.31, 0.8 ...
example unique values in 'petalwidth_poly_2': 0.08, 3.87, 1.86, 2.45, 6.47, 1.33, 0.1, 1.45, 0.04, 4.36 ...
all unique values in 'petallength_binarized_n=5_enc=ordinal_strat=quantile': 1.0, 0.0, 3.0, 2.0, 4.0
example unique values in 'sepalwidth_square': 15.39, 8.38, 10.77, 9.17, 5.69, 7.91, 12.84, 12.07, 15.49, 9.72 ...
example unique values in 'sepallength_min_max_scaled': 0.86, 0.44, 0.01, 0.18, 0.69, 0.44, 0.51, 0.17, 0.24, 0.24 ...
example unique values in 'petallength_quantiled_n=3_distr=normal': 0.29, -0.59, -1.1, 0.52, 1.05, 0.68, 0.31, 0.2, 0.78, 0.09 ...
example unique values in 'sepalwidth_power_transformed_box-cox': -0.03, 0.17, -0.51, -0.02, -0.54, 0.84, -0.32, -0.65, 0.2, 0.7 ...
example unique values in 'petalwidth_power_transformed_yeo-johnson': 0.93, -1.09, 0.19, 1.05, 0.26, 1.23, 1.12, -1.34, -1.06, 0.59 ...
example unique values in 'sepalwidth_quantiled_n=3_distr=normal': 0.25, -0.74, -1.6, -0.09, 0.64, 0.39, -0.69, -0.84, 0.06, 0.15 ...
example unique values in 'sepallength_sepalwidth_sub': 1.08, 5.16, 2.08, 3.58, 1.34, 2.57, 3.01, 1.2, 1.88, 3.56 ...
all unique values in 'petallength_petalwidth_inter_binarized_th=0.0': 1.0, 0.0
example unique values in 'sepallength_sepalwidth_combination': 6.78, 5.99, 5.84, 5.34, 5.05, 5.15, 4.43, 5.77, 5.0, 5.08 ...
example unique values in 'petallength_min_max_scaled': 0.19, 0.83, 0.67, 0.49, 0.48, 0.03, 0.66, 0.76, 0.44, 0.1 ...
all unique values in 'sepalwidth_binarized_n=5_enc=ordinal_strat=quantile': 4.0, 1.0, 3.0, 2.0, 0.0
example unique values in 'sepalwidth_quantiled_n=100_distr=normal': -0.22, 5.2, -0.67, -0.76, 0.71, 2.19, 1.28, 0.46, 0.89, -0.35 ...
example unique values in 'sepalwidth_petallength_combination': 4.56, 4.7, 3.0, 2.44, 3.87, 3.96, 2.61, 4.46, 3.66, 3.85 ...
example unique values in 'sepalwidth_petalwidth_inter': 5.39, 3.86, 8.87, 2.78, 4.3, 0.37, 2.27, 4.06, 3.64, 5.48 ...
example unique values in 'petallength_sepalwidth_sub': 1.2, 1.72, 2.16, 1.82, -2.45, -2.4, -1.29, 1.72, 2.71, -0.9 ...
all unique values in 'petallength_binarized_th=5.0': 0.0, 1.0
example unique values in 'sepalwidth_power_transformed_yeo-johnson': -0.89, -0.9, -0.26, -0.68, 1.34, -1.37, -0.67, -1.4, 0.82, -2.14 ...
all unique values in 'target': 0, 1, 2
- *CORRELATIONS:*
correlation between 'petalwidth_power_transformed_yeo-johnson' and 'petalwidth': 1.0
correlation between 'sepalwidth_power_transformed_yeo-johnson' and 'sepalwidth': 0.99
correlation between 'sepalwidth_power_transformed_box-cox' and 'sepalwidth': 0.99
correlation between 'petallength_sepalwidth_sub' and 'petallength_min_max_scaled': 0.98
correlation between 'sepalwidth_power_transformed_yeo-johnson' and 'sepalwidth_square': 0.98
correlation between 'petallength_sepalwidth_sub' and 'petallength': 0.98
correlation between 'sepalwidth_power_transformed_box-cox' and 'sepalwidth_square': 0.98
correlation between 'sepalwidth_quantiled_n=100_distr=normal' and 'sepalwidth_quantiled_n=3_distr=normal': 0.96
correlation between 'sepalwidth_power_transformed_yeo-johnson' and 'sepalwidth_quantiled_n=100_distr=normal': 0.96
correlation between 'petallength_binarized_n=5_enc=ordinal_strat=quantile' and 'petallength': 0.95
correlation between 'target' and 'petalwidth': 0.95
correlation between 'petallength_min_max_scaled' and 'petalwidth_power_transformed_yeo-johnson': 0.94
correlation between 'target' and 'petallength_sepalwidth_sub': 0.93
correlation between 'sepalwidth_binarized_n=5_enc=ordinal_strat=quantile' and 'sepalwidth_square': 0.91
correlation between 'target' and 'sepalwidth_petallength_combination': 0.91
correlation between 'petallength_quantiled_n=3_distr=normal' and 'petallength': 0.91
correlation between 'petallength_sepalwidth_sub' and 'petallength_quantiled_n=3_distr=normal': 0.89
correlation between 'sepalwidth_petalwidth_inter' and 'petallength': 0.89
correlation between 'sepalwidth_petallength_combination' and 'petalwidth_poly_2': 0.88
correlation between 'petallength_min_max_scaled' and 'petalwidth_poly_2': 0.86
correlation between 'petallength_quantiled_n=3_distr=normal' and 'petallength_binarized_n=5_enc=ordinal_strat=quantile': 0.86
correlation between 'petallength_min_max_scaled' and 'sepallength': 0.83
correlation between 'petallength' and 'sepallength': 0.83
correlation between 'sepallength_sepalwidth_sub' and 'petalwidth_power_transformed_yeo-johnson': 0.82
correlation between 'sepallength_sepalwidth_combination' and 'sepallength_sepalwidth_sub': 0.82
correlation between 'sepallength_sepalwidth_sub' and 'petallength_binarized_n=5_enc=ordinal_strat=quantile': 0.81
correlation between 'sepalwidth_petalwidth_inter' and 'sepallength': 0.8
correlation between 'sepallength_min_max_scaled' and 'petalwidth': 0.8
correlation between 'petallength_binarized_n=5_enc=ordinal_strat=quantile' and 'sepallength': 0.8
correlation between 'petallength_quantiled_n=3_distr=normal' and 'sepallength_min_max_scaled': 0.78
correlation between 'target' and 'sepallength': 0.77
correlation between 'petallength_quantiled_n=3_distr=normal' and 'petalwidth_poly_2': 0.76
correlation between 'petallength_binarized_th=5.0' and 'petallength_binarized_n=5_enc=ordinal_strat=quantile': 0.76
correlation between 'target' and 'petallength_binarized_th=5.0': 0.74
correlation between 'petallength_binarized_th=5.0' and 'sepalwidth_petalwidth_inter': 0.7
correlation between 'petallength_binarized_th=5.0' and 'petalwidth': 0.68
correlation between 'petallength_sepalwidth_sub' and 'sepallength_sepalwidth_combination': 0.68
correlation between 'petallength_binarized_th=5.0' and 'sepallength_min_max_scaled': 0.63
correlation between 'petallength_sepalwidth_sub' and 'sepalwidth': -0.58
correlation between 'petallength_binarized_th=5.0' and 'sepallength_sepalwidth_sub': 0.55
correlation between 'petallength_sepalwidth_sub' and 'sepalwidth_quantiled_n=3_distr=normal': -0.48
correlation between 'target' and 'sepalwidth_square': -0.41
correlation between 'target' and 'sepalwidth_binarized_n=5_enc=ordinal_strat=quantile': -0.4
correlation between 'petallength_min_max_scaled' and 'sepalwidth': -0.4
correlation between 'sepalwidth_quantiled_n=100_distr=normal' and 'petallength': -0.38
correlation between 'target' and 'sepalwidth_power_transformed_box-cox': -0.38
correlation between 'sepalwidth_binarized_n=5_enc=ordinal_strat=quantile' and 'petalwidth_power_transformed_yeo-johnson': -0.32
correlation between 'sepalwidth_binarized_n=5_enc=ordinal_strat=quantile' and 'petalwidth': -0.31
correlation between 'sepalwidth_power_transformed_yeo-johnson' and 'petalwidth_power_transformed_yeo-johnson': -0.31
correlation between 'petalwidth_power_transformed_yeo-johnson' and 'sepalwidth_power_transformed_box-cox': -0.31

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: -0.69%
Score: 0.9533
Added columns: {'petalwidth_normalized_l2', 'petallength_binarized_n=5_enc=ordinal_strat=quantile', 'petalwidth_poly_2', 'sepallength_min_max_scaled', 'sepalwidth_square', 'petallength_quantiled_n=3_distr=normal', 'sepalwidth_sepallength_sub', 'petallength_petalwidth_inter', 'sepalwidth_power_transformed_box-cox'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: 2.10%
Score: 0.9733
Added columns: {'petallength_min_max_scaled', 'sepallength_sepalwidth_combination', 'petalwidth_power_transformed_yeo-johnson', 'sepallength_sepalwidth_sub', 'petallength_petalwidth_inter_binarized_th=0.0', 'sepalwidth_binarized_n=5_enc=ordinal_strat=quantile', 'sepalwidth_quantiled_n=3_distr=normal'}
Removed columns: {'petalwidth_normalized_l2', 'sepalwidth_sepallength_sub', 'petallength_petalwidth_inter'}
Iteration 3:
Score change relative to previous iteration: -0.68%
Score: 0.9667
Added columns: {'sepalwidth_petalwidth_inter', 'petallength_binarized_th=5.0', 'sepalwidth_quantiled_n=100_distr=normal', 'sepalwidth_power_transformed_yeo-johnson', 'petallength_sepalwidth_sub', 'sepalwidth_petallength_combination'}
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
- You create new features from existing columns to make ML Decision Tree Classifier model better at predicting target variable 'target' in classification problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**