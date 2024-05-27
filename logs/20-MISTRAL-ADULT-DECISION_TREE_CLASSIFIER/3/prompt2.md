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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['fnlwgt', 'education-num', 'age_0', 'age_1', 'age_2', 'age_3', 'age_4', 'workclass_federal-gov', 'workclass_local-gov', 'workclass_never-worked', 'workclass_private', 'workclass_self-emp-inc', 'workclass_self-emp-not-inc', 'workclass_state-gov', 'workclass_without-pay', 'marital-status_divorced', 'marital-status_married-af-spouse', 'marital-status_married-civ-spouse', 'marital-status_married-spouse-absent', 'marital-status_never-married', 'marital-status_separated', 'marital-status_widowed', 'relationship_husband', 'relationship_not-in-family', 'relationship_other-relative', 'relationship_own-child', 'relationship_unmarried', 'relationship_wife', 'race_amer-indian-eskimo', 'race_asian-pac-islander', 'race_black', 'race_other', 'race_white', 'sex_female', 'sex_male', 'capitalgain_0', 'capitalgain_1', 'capitalgain_2', 'capitalgain_3', 'capitalgain_4', 'capitalloss_0', 'capitalloss_1', 'capitalloss_2', 'capitalloss_3', 'capitalloss_4', 'hoursperweek_0', 'hoursperweek_1', 'hoursperweek_2', 'hoursperweek_3', 'hoursperweek_4', 'hoursperweek_1_hoursperweek_0_sub', 'education-num_quantiled_n=100_distr=normal', 'workclass_self-emp-not-inc_marital-status_married-civ-spouse_inter', 'capitalgain_3_capitalloss_3_combination', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are my recommendations for creating 10 new feature columns using existing ones:

1. Capital gain and loss interaction: 'capitalgain_3_capitalloss_4_combination'
Create an interaction term between capital gain (column 'capitalgain_3') and capital loss (column 'capitalloss_4').
2. Workclass and marital status combination: 'workclass_marital-status_inter'
Create a new column by combining 'workclass' and 'marital-status' columns, which can provide more context for the model.
3. Hours per week squared: 'hoursperweek_sq'
Add the square of 'hoursperweek' to capture non-linear relationships between hours worked and income.
4. Education number and relationship status intersection: 'education-num_relationship_inter'
Create an interaction term between 'education-num' and 'relationship' columns, which might provide insight into the impact of education level on specific relationship types.
5. Log transformation of fnlwgt: 'ln_fnlwgt'
Apply a logarithmic transformation to the 'fnlwgt' column as it may help normalize extreme values and make the distribution more Gaussian, making models perform better.
6. Marital status encoding: 'marital-status_encoded'
Apply one-hot encoding on 'marital-status' to convert categorical variables into binary indicators.
7. Age and workclass combination: 'age_workclass_inter'
Create an interaction term between 'age' and 'workclass' columns as they might be related to income.
8. Capital gain and hour per week interaction: 'capitalgain_hoursperweek_inter'
Create an interaction term between 'capitalgain_3' and 'hoursperweek' columns, which could provide insight into the impact of hours worked on capital gains.
9. Race encoding: 'race_encoded'
Apply one-hot encoding on 'race' column to convert categorical variables into binary indicators.
10. Age group based on decade: 'age_decade'
Create a new column with age groups defined by decades (e.g., 0 for age under 10, 1 for age between 10-20, etc.) to help capture trends in income related to age groups.

**JSON:**
