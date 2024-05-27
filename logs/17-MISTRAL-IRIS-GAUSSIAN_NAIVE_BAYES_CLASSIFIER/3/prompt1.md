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
example unique values in 'sepallength_sepalwidth_sub': 1.25, 3.6, 2.98, 3.77, 2.99, 3.28, 1.64, 1.34, 1.23, 2.29 ...
all unique values in 'petallength_binarized_n=5_enc=ordinal_strat=quantile': 1.0, 0.0, 3.0, 2.0, 4.0
example unique values in 'sepallength_min_max_scaled': 0.86, 0.44, 0.01, 0.18, 0.69, 0.44, 0.51, 0.17, 0.24, 0.24 ...
example unique values in 'petallength_power_transformed_box-cox': 0.63, -0.59, -1.17, 0.89, 1.33, 1.04, 0.66, 0.54, 1.12, 0.41 ...
example unique values in 'sepallength_sepalwidth_inter': 17.78, 22.55, 11.3, 15.91, 17.47, 22.1, 21.44, 17.31, 13.28, 25.07 ...
all unique values in 'petalwidth_normalized_l2': 1.0, -1.0
example unique values in 'petalwidth_quantiled_n=100_distr=uniform': 0.78, 0.26, 0.49, 0.84, 0.54, 0.9, 0.87, 0.12, 0.27, 0.66 ...
example unique values in 'sepallength_sepalwidth_combination': 2.96, 4.01, 4.11, 4.39, 4.58, 3.04, 3.77, 3.66, 4.5, 2.6 ...
example unique values in 'petallength_petalwidth_inter': 0.39, 14.62, 0.45, 6.07, 0.32, 3.11, 7.13, 0.42, 0.31, 5.2 ...
all unique values in 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform': 0.0, 1.0, 3.0, 2.0, 4.0
all unique values in 'sepallength_normalized_l2': 1.0
example unique values in 'petalwidth_sqrt': 1.45, 1.59, 1.48, 1.33, 1.1, 0.4, 0.54, 1.3, 1.18, 0.29 ...
all unique values in 'target': 0, 1, 2
- *CORRELATIONS:*
correlation between 'petalwidth_quantiled_n=100_distr=uniform' and 'petalwidth': 0.99
correlation between 'petalwidth_sqrt' and 'petalwidth': 0.98
correlation between 'sepallength_sepalwidth_combination' and 'sepallength_min_max_scaled': 0.97
correlation between 'petallength_petalwidth_inter' and 'petalwidth_quantiled_n=100_distr=uniform': 0.97
correlation between 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform' and 'petalwidth_quantiled_n=100_distr=uniform': 0.97
correlation between 'petalwidth_sqrt' and 'petalwidth_quantiled_n=100_distr=uniform': 0.97
correlation between 'petallength_petalwidth_inter' and 'petalwidth_poly_2': 0.97
correlation between 'petalwidth_quantiled_n=100_distr=uniform' and 'petalwidth_poly_2': 0.97
correlation between 'petallength_petalwidth_inter' and 'petalwidth': 0.97
correlation between 'petallength_petalwidth_inter' and 'petallength_power_transformed_box-cox': 0.95
correlation between 'target' and 'petallength_petalwidth_inter': 0.95
correlation between 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform' and 'petalwidth_poly_2': 0.95
correlation between 'petallength_binarized_n=5_enc=ordinal_strat=quantile' and 'petallength': 0.95
correlation between 'target' and 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform': 0.94
correlation between 'target' and 'petallength_power_transformed_box-cox': 0.94
correlation between 'target' and 'petallength': 0.94
correlation between 'target' and 'petalwidth_quantiled_n=100_distr=uniform': 0.93
correlation between 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform' and 'petallength': 0.93
correlation between 'petalwidth' and 'petallength': 0.93
correlation between 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform' and 'petallength_power_transformed_box-cox': 0.92
correlation between 'petalwidth_quantiled_n=100_distr=uniform' and 'petallength': 0.91
correlation between 'target' and 'petallength_binarized_n=5_enc=ordinal_strat=quantile': 0.91
correlation between 'petalwidth_sqrt' and 'petalwidth_poly_2': 0.91
correlation between 'petallength_binarized_n=5_enc=ordinal_strat=quantile' and 'petalwidth': 0.88
correlation between 'petallength_power_transformed_box-cox' and 'petalwidth_poly_2': 0.86
correlation between 'petalwidth_sqrt' and 'petallength_binarized_n=5_enc=ordinal_strat=quantile': 0.86
correlation between 'petalwidth_sqrt' and 'sepallength_sepalwidth_combination': 0.83
correlation between 'petallength' and 'sepallength': 0.83
correlation between 'sepallength_sepalwidth_combination' and 'petalwidth': 0.83
correlation between 'petallength_petalwidth_inter' and 'sepallength_min_max_scaled': 0.83
correlation between 'petallength_binarized_n=5_enc=ordinal_strat=quantile' and 'sepallength_sepalwidth_sub': 0.81
correlation between 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform' and 'sepallength_min_max_scaled': 0.8
correlation between 'petallength_binarized_n=5_enc=ordinal_strat=quantile' and 'sepallength': 0.8
correlation between 'sepallength_min_max_scaled' and 'petalwidth': 0.8
correlation between 'petalwidth_quantiled_n=100_distr=uniform' and 'sepallength_min_max_scaled': 0.79
correlation between 'petalwidth_sqrt' and 'sepallength': 0.78
correlation between 'target' and 'sepallength_min_max_scaled': 0.77
correlation between 'petalwidth_poly_2' and 'sepallength': 0.76
correlation between 'sepallength_sepalwidth_sub' and 'petalwidth_poly_2': 0.73
correlation between 'sepallength_sepalwidth_inter' and 'sepallength_min_max_scaled': 0.68
correlation between 'sepallength_sepalwidth_inter' and 'sepalwidth': 0.67
correlation between 'sepallength_sepalwidth_sub' and 'sepalwidth': -0.54
correlation between 'petallength_petalwidth_inter' and 'sepallength_sepalwidth_inter': 0.44
correlation between 'petalwidth_quantiled_n=100_distr=uniform' and 'sepallength_sepalwidth_inter': 0.42
correlation between 'petallength_power_transformed_box-cox' and 'sepalwidth': -0.4
correlation between 'petallength' and 'sepalwidth': -0.4
correlation between 'sepallength_sepalwidth_inter' and 'petalwidth': 0.37
correlation between 'sepallength_sepalwidth_inter' and 'petallength': 0.33
correlation between 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform' and 'sepalwidth': -0.32
correlation between 'petallength_binarized_n=5_enc=ordinal_strat=quantile' and 'sepalwidth': -0.3

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: 0.70%
Score: 0.9600
Added columns: {'petalwidth_normalized_l2', 'petallength_power_transformed_box-cox', 'petallength_petalwidth_combination', 'sepallength_sepalwidth_inter', 'sepallength_sepalwidth_sub', 'petalwidth_poly_2', 'sepallength_min_max_scaled', 'petallength_binarized_n=5_enc=ordinal_strat=quantile'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: 0.00%
Score: 0.9600
Added columns: {'sepallength_normalized_l2', 'sepallength_sepalwidth_combination', 'petalwidth_quantiled_n=100_distr=uniform', 'petalwidth_binarized_n=5_enc=ordinal_strat=uniform', 'petalwidth_sqrt', 'petallength_petalwidth_inter'}
Removed columns: {'petallength_petalwidth_combination'}

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