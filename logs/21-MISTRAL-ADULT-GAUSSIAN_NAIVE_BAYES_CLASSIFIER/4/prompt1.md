**INTRODUCTION:**
Predict whether an individual earns more than $50,000 a year based on features (these columns might not exist, use columns from COLUMNS section):
class (target): This column is the target variable or label that you want to predict. It's a nominal variable with two distinct values, likely representing different classes or categories.
age: This column represents the age of individuals. It's a numeric variable with 74 distinct values.
workclass: This column represents the type of employment or work class of individuals. It's a nominal variable with 8 distinct values and 2799 missing attributes.
fnlwgt: This column represents the final weight or sampling weight associated with each observation in the dataset. It's a numeric variable with 28523 distinct values.
education: This column represents the highest level of education achieved by individuals. It's a nominal variable with 16 distinct values.
education-num: This column represents the numerical encoding of education levels. It's a numeric variable with 16 distinct values.
marital-status: This column represents the marital status of individuals. It's a nominal variable with 7 distinct values.

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'fnlwgt': 55270.22, 178738.29, 100097.85, 261157.5, 357036.92, 100060.98, 294824.98, -6907.52, 178607.93, 313612.01 ...
example unique values in 'education-num': 8.54, 10.24, 12.13, 10.53, 8.57, 10.03, 11.67, 6.02, 9.6, 14.73 ...
all unique values in 'age_0': 0, 1
all unique values in 'age_1': 0, 1
all unique values in 'age_2': 1, 0
all unique values in 'age_3': 0, 1
all unique values in 'age_4': 0, 1
all unique values in 'workclass_federal-gov': 0, 1
all unique values in 'workclass_local-gov': 0, 1
all unique values in 'workclass_never-worked': 0
all unique values in 'workclass_private': 1, 0
all unique values in 'workclass_self-emp-inc': 0, 1
all unique values in 'workclass_self-emp-not-inc': 0, 1
all unique values in 'workclass_state-gov': 0, 1
all unique values in 'workclass_without-pay': 0
all unique values in 'marital-status_divorced': 0, 1
all unique values in 'marital-status_married-af-spouse': 0, 1
all unique values in 'marital-status_married-civ-spouse': 1, 0
all unique values in 'marital-status_married-spouse-absent': 0, 1
all unique values in 'marital-status_never-married': 0, 1
all unique values in 'marital-status_separated': 0, 1
all unique values in 'marital-status_widowed': 0, 1
all unique values in 'relationship_husband': 1, 0
all unique values in 'relationship_not-in-family': 0, 1
all unique values in 'relationship_other-relative': 0, 1
all unique values in 'relationship_own-child': 0, 1
all unique values in 'relationship_unmarried': 0, 1
all unique values in 'relationship_wife': 0, 1
all unique values in 'race_amer-indian-eskimo': 0, 1
all unique values in 'race_asian-pac-islander': 0, 1
all unique values in 'race_black': 1, 0
all unique values in 'race_other': 0, 1
all unique values in 'race_white': 0, 1
all unique values in 'sex_female': 0, 1
all unique values in 'sex_male': 1, 0
all unique values in 'capitalgain_0': 1, 0
all unique values in 'capitalgain_1': 0, 1
all unique values in 'capitalgain_2': 0, 1
all unique values in 'capitalgain_3': 0, 1
all unique values in 'capitalgain_4': 0, 1
all unique values in 'capitalloss_0': 1, 0
all unique values in 'capitalloss_1': 0, 1
all unique values in 'capitalloss_2': 0, 1
all unique values in 'capitalloss_3': 0, 1
all unique values in 'capitalloss_4': 0, 1
all unique values in 'hoursperweek_0': 0, 1
all unique values in 'hoursperweek_1': 0, 1
all unique values in 'hoursperweek_2': 1, 0
all unique values in 'hoursperweek_3': 0, 1
all unique values in 'hoursperweek_4': 0, 1
example unique values in 'capitalgain_1_fnlwgt_sub': -399495.38, -209305.99, -296855.29, -381176.79, -257287.78, -191096.06, -140451.08, -382390.76, 20771.22, -252649.9 ...
example unique values in 'age_1_education-num_inter': 15.77, 8.52, 0.0, 12.46, 12.5, 12.3, 8.73, 8.26, 12.78, 12.73 ...
example unique values in 'fnlwgt_quantiled_n=10_distr=uniform': 0.57, 0.86, 0.7, 0.89, 0.9, 0.81, 0.81, 0.58, 0.49, 0.21 ...
all unique values in 'hoursperweek_1_capitalloss_1_combination': 0.0, 0.5, -0.5
all unique values in 'hoursperweek_1_capitalloss_2_sub': 0, 1, 255
all unique values in 'marital-status_married-civ-spouse_workclass_private_inter': 1, 0
example unique values in 'age_0_education-num_combination': 9.57, 6.84, 13.21, 14.42, 8.97, 12.45, 10.16, 9.82, 14.89, 9.02 ...
all unique values in 'capitalgain_1_log': -20.72, 0.0
all unique values in 'sex_male_workclass_state-gov_combination': 1, 2, 0
all unique values in 'hoursperweek_1_capitalloss_3_sub': 0, 1, 255
all unique values in 'marital-status_married-civ-spouse_workclass_self-emp-inc_inter': 0, 1
example unique values in 'education-num_log': 2.24, 2.59, 2.26, 2.39, 2.5, 2.29, 1.44, 2.69, 2.13, 2.25 ...
all unique values in 'age_4_marital-status_never-married_inter': 0, 1
all unique values in 'age_1_capitalgain_1_combination': 0, 1, 2
all unique values in 'age_3_capitalloss_2_sub': 0, 1, 255
all unique values in 'target': 0, 1
- *CORRELATIONS:*
correlation between 'capitalgain_1_fnlwgt_sub' and 'fnlwgt': -1.0
correlation between 'sex_male' and 'sex_female': -1.0
correlation between 'age_0_education-num_combination' and 'education-num': 0.99
correlation between 'hoursperweek_1_capitalloss_2_sub' and 'capitalloss_2': 0.97
correlation between 'hoursperweek_1_capitalloss_1_combination' and 'hoursperweek_1': 0.96
correlation between 'age_1_capitalgain_1_combination' and 'age_1': 0.95
correlation between 'education-num_log' and 'age_0_education-num_combination': 0.95
correlation between 'sex_male_workclass_state-gov_combination' and 'sex_female': -0.92
correlation between 'hoursperweek_1_capitalloss_3_sub' and 'capitalloss_3': 0.92
correlation between 'fnlwgt_quantiled_n=10_distr=uniform' and 'capitalgain_1_fnlwgt_sub': -0.91
correlation between 'marital-status_married-civ-spouse_workclass_self-emp-inc_inter' and 'workclass_self-emp-inc': 0.87
correlation between 'age_3_capitalloss_2_sub' and 'capitalloss_2': 0.87
correlation between 'age_3_capitalloss_2_sub' and 'hoursperweek_1_capitalloss_2_sub': 0.83
correlation between 'marital-status_never-married' and 'marital-status_married-civ-spouse': -0.67
correlation between 'capitalloss_2' and 'capitalloss_0': -0.59
correlation between 'sex_male' and 'relationship_husband': 0.58
correlation between 'hoursperweek_3' and 'hoursperweek_2': -0.57
correlation between 'hoursperweek_1_capitalloss_2_sub' and 'capitalloss_0': -0.57
correlation between 'capitalgain_4' and 'capitalgain_0': -0.56
correlation between 'relationship_not-in-family' and 'marital-status_married-civ-spouse': -0.55
correlation between 'capitalgain_2' and 'capitalgain_0': -0.54
correlation between 'capitalgain_1' and 'capitalgain_0': -0.5
correlation between 'hoursperweek_1_capitalloss_3_sub' and 'capitalloss_0': -0.49
correlation between 'relationship_not-in-family' and 'relationship_husband': -0.49
correlation between 'target' and 'marital-status_married-civ-spouse': 0.46
correlation between 'capitalloss_4' and 'capitalloss_0': -0.42
correlation between 'target' and 'relationship_husband': 0.41
correlation between 'relationship_own-child' and 'marital-status_married-civ-spouse': -0.41
correlation between 'sex_male' and 'marital-status_married-civ-spouse': 0.41
correlation between 'capitalloss_1' and 'capitalloss_0': -0.4
correlation between 'marital-status_married-civ-spouse_workclass_private_inter' and 'relationship_not-in-family': -0.39
correlation between 'workclass_self-emp-inc' and 'workclass_private': -0.39
correlation between 'sex_male_workclass_state-gov_combination' and 'workclass_state-gov': 0.39
correlation between 'marital-status_married-civ-spouse' and 'age_0': -0.38
correlation between 'sex_male_workclass_state-gov_combination' and 'marital-status_married-civ-spouse': 0.38
correlation between 'marital-status_married-civ-spouse' and 'marital-status_divorced': -0.37
correlation between 'relationship_husband' and 'age_0': -0.35
correlation between 'sex_female' and 'relationship_unmarried': 0.35
correlation between 'race_white' and 'race_asian-pac-islander': -0.35
correlation between 'sex_male' and 'relationship_wife': -0.35
correlation between 'age_2' and 'age_1': -0.34
correlation between 'marital-status_married-civ-spouse_workclass_self-emp-inc_inter' and 'workclass_private': -0.34
correlation between 'target' and 'marital-status_never-married': -0.33
correlation between 'workclass_state-gov' and 'workclass_private': -0.33
correlation between 'sex_male_workclass_state-gov_combination' and 'relationship_unmarried': -0.33
correlation between 'relationship_husband' and 'marital-status_divorced': -0.33
correlation between 'age_1_capitalgain_1_combination' and 'capitalgain_1': 0.31
correlation between 'marital-status_married-civ-spouse_workclass_private_inter' and 'sex_male': 0.31
correlation between 'sex_male_workclass_state-gov_combination' and 'relationship_wife': -0.31
correlation between 'relationship_not-in-family' and 'marital-status_never-married': 0.3

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: 0.00%
Score: 0.7610
Added columns: {'hoursperweek_1_capitalloss_1_combination', 'capitalgain_1_fnlwgt_sub', 'fnlwgt_quantiled_n=10_distr=uniform', 'age_1_education-num_inter'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: 0.00%
Score: 0.7610
Added columns: {'hoursperweek_1_capitalloss_2_sub', 'age_0_education-num_combination', 'sex_male_workclass_state-gov_combination', 'marital-status_married-civ-spouse_workclass_private_inter', 'capitalgain_1_log'}
Removed columns: set()
Iteration 3:
Score change relative to previous iteration: 0.39%
Score: 0.7640
Added columns: {'education-num_log', 'age_1_capitalgain_1_combination', 'marital-status_married-civ-spouse_workclass_self-emp-inc_inter', 'age_4_marital-status_never-married_inter', 'age_3_capitalloss_2_sub', 'hoursperweek_1_capitalloss_3_sub'}
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
- You create new features from existing columns to make ML Gaussian Naive Bayes Classifier model better at predicting target variable 'target' in classification problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**