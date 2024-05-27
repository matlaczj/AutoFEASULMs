**TASK:**
Turn the content into valid json like on the schema.
Remember to put values of arguments in correct lists.
Tool called `apply_math_function` expects `categorical_arguments` to be filled with one of accepted string values and `numerical_arguments` to be empty! Same goes for `normalizer` etc. Look at TOOLS section for accepted values.

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

**SCHEMA:**
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['fnlwgt', 'education-num', 'age_0', 'age_1', 'age_2', 'age_3', 'age_4', 'workclass_federal-gov', 'workclass_local-gov', 'workclass_never-worked', 'workclass_private', 'workclass_self-emp-inc', 'workclass_self-emp-not-inc', 'workclass_state-gov', 'workclass_without-pay', 'marital-status_divorced', 'marital-status_married-af-spouse', 'marital-status_married-civ-spouse', 'marital-status_married-spouse-absent', 'marital-status_never-married', 'marital-status_separated', 'marital-status_widowed', 'relationship_husband', 'relationship_not-in-family', 'relationship_other-relative', 'relationship_own-child', 'relationship_unmarried', 'relationship_wife', 'race_amer-indian-eskimo', 'race_asian-pac-islander', 'race_black', 'race_other', 'race_white', 'sex_female', 'sex_male', 'capitalgain_0', 'capitalgain_1', 'capitalgain_2', 'capitalgain_3', 'capitalgain_4', 'capitalloss_0', 'capitalloss_1', 'capitalloss_2', 'capitalloss_3', 'capitalloss_4', 'hoursperweek_0', 'hoursperweek_1', 'hoursperweek_2', 'hoursperweek_3', 'hoursperweek_4', 'capitalgain_1_fnlwgt_sub', 'age_1_education-num_inter', 'fnlwgt_quantiled_n=10_distr=uniform', 'hoursperweek_1_capitalloss_1_combination', 'hoursperweek_1_capitalloss_2_sub', 'marital-status_married-civ-spouse_workclass_private_inter', 'age_0_education-num_combination', 'capitalgain_1_log', 'sex_male_workclass_state-gov_combination', 'hoursperweek_1_capitalloss_3_sub', 'marital-status_married-civ-spouse_workclass_self-emp-inc_inter', 'education-num_log', 'age_4_marital-status_never-married_inter', 'age_1_capitalgain_1_combination', 'age_3_capitalloss_2_sub', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iterations, here are ten new column-tool combinations that could potentially improve the performance of the Gaussian Naive Bayes Classifier for predicting the target variable 'target':

1. `quantile_transformer(fnlwgt, n_quantiles=50, output_distribution='uniform')`: As 'fnlwgt' is a continuous numeric variable, this transformation could help normalize its distribution and reduce skewness, making it more suitable for the classifier model.

2. `one_hot_encoder(workclass)`: Since 'workclass' is a nominal categorical feature with missing attributes, encoding it as one-hot would convert each unique category into a new binary column, enabling the classifier to consider each workclass type separately.

3. `linear_combination(hoursperweek_1, capitalloss_2, weight_1=0.5, weight_2=-0.5)`: Based on the high correlation between 'hoursperweek_1' and 'capitalloss_2' (-0.57), creating a new feature by linearly combining these two columns could potentially help in capturing their joint effect on the target variable.

4. `k_bins_discretizer(age, n_bins=5, encode='ordinal', strategy='quantile')`: Discretizing the 'age' column into five equally-sized bins using quantile binning could help in capturing non-linear relationships or trends present within the data.

5. `polynomial_features(education_num, degree=2)`: As 'education_num' is a continuous numeric variable, creating polynomial features up to the second degree could potentially help capture any underlying curvilinear relationships with the target variable.

6. `subtract_columns(capitalgain_1, capitalloss_4)`: Since the correlation between 'capitalgain_1' and 'capitalloss_4' is -0.42, creating a new feature by subtracting these two columns could help in capturing the difference between capital gains and losses, which might be significant for predicting the target variable.

7. `apply_math_function(marital_status_married_civ_spouse, function='log')`: Taking the logarithm of 'marital_status_married_civ_spouse' could help in reducing skewness and making it more amenable to the classifier model.

8. `ordinal_encoder(marital_status)`: Encoding 'marital_status' as ordinal variables would convert each unique category into a new integer value, which could potentially improve the classifier's ability to learn from categorical data.

9. `min_max_scaler(education)`: Scaling the 'education' column using Min-Max scaling could help normalize its values within a specific range and reduce any potential bias towards certain education levels.

10. `power_transformer(sex, method='box-cox')`: As 'sex' is a binary categorical feature, applying a Box-Cox power transformation could potentially help improve the classifier's ability to capture any underlying non-linear relationships between sex and the target variable.

**JSON:**
