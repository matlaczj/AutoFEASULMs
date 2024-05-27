**INTRODUCTION:**
Predict whether a passenger survived the Titanic disaster based on features (these columns might not exist, use columns from COLUMNS section):
Survived (target): This column indicates whether a passenger survived the Titanic disaster or not. It has two distinct values: 0 for not survived and 1 for survived.
Pclass: This column represents the passenger class or ticket class of the passenger. It has three distinct values, typically indicating first, second, or third class.
Sex: This column represents the gender of the passenger. It has two distinct values: male and female.
Age: This column represents the age of the passenger. It has seven distinct values, likely grouped into age ranges or categories.
Fare: This column represents the fare or price paid by the passenger for their ticket. It has six distinct values, possibly indicating different fare categories.
Embarked: This column represents the port of embarkation for the passenger. It has three distinct values, typically indicating different ports such as Southampton, Cherbourg, and Queenstown.
relatives: This column represents the number of relatives (e.g., siblings, spouse, parents, children) aboard the Titanic for the passenger. It has nine distinct values, likely representing different counts of relatives.
Title: This column represents the title or honorific of the passenger (e.g., Mr., Mrs., Miss). It has five distinct values, possibly indicating different titles or social statuses.

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'class': 0.85, -1.86, 0.68, 0.9, 0.08, -2.01, 1.21, 0.88, 0.2, 1.22 ...
all unique values in 'age': -0.23, 4.38
all unique values in 'sex': 0.52, -1.92
example unique values in 'sex_class_inter': -0.43, 3.56, 0.13, 0.11, 0.41, 0.62, 0.43, 0.46, 3.44, 0.66 ...
all unique values in 'age_age_sub': 0.0
all unique values in 'age_log': -1.48, 1.48
all unique values in 'age_min_max_scaled': 0.0, 1.0
example unique values in 'class_exp': 1.18, 2.72, 0.14, 3.19, 2.78, 1.03, 2.68, 1.2, 0.74, 2.92 ...
all unique values in 'age_max_abs_scaled': -0.05, 1.0
example unique values in 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA': -0.99, -0.56, -0.94, 1.76, 2.35, 0.66, -1.03, 0.08, -1.24, 3.6 ...
example unique values in 'class_age_sub_age_min_max_scaled_PCA': -1.23, -1.25, -1.35, -0.3, -0.08, -1.29, 1.73, -0.37, -0.34, 1.85 ...
example unique values in 'class_exp_age_combination': 0.05, 1.21, 0.3, 0.13, 1.36, 0.36, 0.51, 0.29, -0.02, 0.92 ...
all unique values in 'sex_power_transformed_yeo-johnson': 0.5, -2.02
all unique values in 'target': 0, 1
- *CORRELATIONS:*
correlation between 'age_log' and 'age': 1.0
correlation between 'age_max_abs_scaled' and 'age_min_max_scaled': 1.0
correlation between 'age_min_max_scaled' and 'age': 1.0
correlation between 'sex_power_transformed_yeo-johnson' and 'sex': 1.0
correlation between 'age_max_abs_scaled' and 'age_log': 1.0
correlation between 'age_min_max_scaled' and 'age_log': 1.0
correlation between 'age_max_abs_scaled' and 'age': 1.0
correlation between 'class_exp' and 'class': 0.92
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA': 0.87
correlation between 'sex_power_transformed_yeo-johnson' and 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA': -0.77
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'sex': -0.77
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'age_log': 0.74
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'age_max_abs_scaled': 0.74
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'age': 0.74
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'age_min_max_scaled': 0.74
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'class': -0.74
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'class_exp': -0.74
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'class_exp': -0.72
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'class': -0.71
correlation between 'class_exp_age_combination' and 'class': 0.67
correlation between 'class_exp_age_combination' and 'class_exp': 0.66
correlation between 'class_exp_age_combination' and 'age_log': 0.65
correlation between 'class_exp_age_combination' and 'age': 0.65
correlation between 'class_exp_age_combination' and 'age_min_max_scaled': 0.65
correlation between 'class_exp_age_combination' and 'age_max_abs_scaled': 0.65
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'age_log': 0.53
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'age_max_abs_scaled': 0.53
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'age_min_max_scaled': 0.53
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'age': 0.53
correlation between 'sex_power_transformed_yeo-johnson' and 'sex_class_inter': -0.52
correlation between 'sex_class_inter' and 'sex': -0.52
correlation between 'target' and 'sex': -0.47
correlation between 'target' and 'sex_power_transformed_yeo-johnson': -0.47
correlation between 'target' and 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA': 0.42
correlation between 'sex_power_transformed_yeo-johnson' and 'class': 0.4
correlation between 'sex' and 'class': 0.4
correlation between 'class_exp' and 'sex': 0.4
correlation between 'sex_power_transformed_yeo-johnson' and 'class_exp': 0.4
correlation between 'class_age_sub_age_min_max_scaled_PCA' and 'sex': -0.37
correlation between 'sex_power_transformed_yeo-johnson' and 'class_age_sub_age_min_max_scaled_PCA': -0.37
correlation between 'target' and 'sex_class_inter': 0.35
correlation between 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA' and 'sex_class_inter': 0.32

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: -2.25%
Score: 0.7810
Added columns: {'age_log', 'age_min_max_scaled', 'class_age_combination', 'sex_class_inter', 'age_age_sub', 'class_sex_age_PCA'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: 0.90%
Score: 0.7880
Added columns: {'class_exp', 'age_max_abs_scaled', 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA', 'class_age_sub'}
Removed columns: {'class_age_combination', 'class_sex_age_PCA'}
Iteration 3:
Score change relative to previous iteration: -0.25%
Score: 0.7860
Added columns: {'class_exp_age_combination', 'sex_power_transformed_yeo-johnson', 'class_age_sub_age_min_max_scaled_PCA'}
Removed columns: {'class_age_sub'}

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