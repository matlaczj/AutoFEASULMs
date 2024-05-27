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
all unique values in 'target': 0, 1, 2
- *CORRELATIONS:*
correlation between 'target' and 'petalwidth': 0.95
correlation between 'target' and 'petallength': 0.94
correlation between 'petalwidth' and 'petallength': 0.93
correlation between 'petallength' and 'sepallength': 0.83
correlation between 'petalwidth' and 'sepallength': 0.8
correlation between 'target' and 'sepallength': 0.77
correlation between 'petallength' and 'sepalwidth': -0.4
correlation between 'target' and 'sepalwidth': -0.4
correlation between 'petalwidth' and 'sepalwidth': -0.32

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