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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['fnlwgt', 'education-num', 'age_0', 'age_1', 'age_2', 'age_3', 'age_4', 'workclass_federal-gov', 'workclass_local-gov', 'workclass_never-worked', 'workclass_private', 'workclass_self-emp-inc', 'workclass_self-emp-not-inc', 'workclass_state-gov', 'workclass_without-pay', 'marital-status_divorced', 'marital-status_married-af-spouse', 'marital-status_married-civ-spouse', 'marital-status_married-spouse-absent', 'marital-status_never-married', 'marital-status_separated', 'marital-status_widowed', 'relationship_husband', 'relationship_not-in-family', 'relationship_other-relative', 'relationship_own-child', 'relationship_unmarried', 'relationship_wife', 'race_amer-indian-eskimo', 'race_asian-pac-islander', 'race_black', 'race_other', 'race_white', 'sex_female', 'sex_male', 'capitalgain_0', 'capitalgain_1', 'capitalgain_2', 'capitalgain_3', 'capitalgain_4', 'capitalloss_0', 'capitalloss_1', 'capitalloss_2', 'capitalloss_3', 'capitalloss_4', 'hoursperweek_0', 'hoursperweek_1', 'hoursperweek_2', 'hoursperweek_3', 'hoursperweek_4', 'hoursperweek_1_hoursperweek_0_sub', 'education-num_quantiled_n=100_distr=normal', 'workclass_self-emp-not-inc_marital-status_married-civ-spouse_inter', 'capitalgain_3_capitalloss_3_combination', 'hoursperweek_3_hoursperweek_2_sub', 'marital-status_divorced_education-num_inter', 'fnlwgt_hoursperweek_0_capitalgain_0_capitalloss_0_PCA', 'fnlwgt_min_max_scaled', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are ten new column-tool combinations that could potentially improve the ML Decision Tree Classifier model:

1. `polynomial_features(education-num, degree=2)`: Adding quadratic terms to the existing education-num feature might help capture more complex relationships with the target variable 'target'.

2. `k_bins_discretizer(fnlwgt, n_bins=5, encode='ordinal', strategy='quantile')`: Discretizing the fnlwgt column using equal width quantiles could help improve model performance by reducing the continuous nature of the data.

3. `apply_math_function(hoursperweek_1, function='square')`: Squaring hoursperweek_1 might reveal hidden relationships with other features that could be beneficial for the model.

4. `subtract_columns(age, education)`: Subtracting age from education might create a new feature revealing an interesting relationship between age and education levels.

5. `ordinal_encoder(marital-status)`: Encoding marital-status as ordinal features could help capture the inherent ordering in this nominal variable.

6. `linear_combination(hoursperweek_2, hoursperweek_3, weight_1=0.5, weight_2=0.5)`: Creating a new feature as a linear combination of hoursperweek_2 and hoursperweek_3 might capture a unique relationship not present in either column alone.

7. `min_max_scaler(capitalgain_1)`: Scaling the capitalgain_1 column using min-max normalization could help ensure that each feature is on a comparable scale for the ML Decision Tree Classifier model.

8. `create_interaction(workclass, marital-status)`: Creating interaction features between workclass and marital-status might uncover interesting relationships not present in either column alone.

9. `power_transformer(capitalloss_3, method='yeo-johnson')`: Applying Yeo-Johnson power transformation on capitalloss_3 could help normalize the distribution and reduce the skewness.

10. `one_hot_encoder(education)`: One-hot encoding the education column might help the ML Decision Tree Classifier model learn specific relationships between each unique education level and the target variable 'target'.

**JSON:**
