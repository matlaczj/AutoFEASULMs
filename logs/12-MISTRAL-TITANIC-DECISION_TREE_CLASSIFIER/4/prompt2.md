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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['class', 'age', 'sex', 'sex_class_inter', 'age_age_sub', 'age_log', 'class_age_combination', 'age_min_max_scaled', 'class_sex_age_PCA', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current iteration history and unique values provided, here are 10 new column-tool combinations that could potentially improve the ML Decision Tree Classifier model for predicting 'target':

1. `min_max_scaler('age')`: To normalize age values.
2. `create_interaction(class, sex)`: To create interaction features between passenger class and gender.
3. `one_hot_encoder(embarked)`: To convert the categorical 'embarked' column into one-hot encoded columns.
4. `subtract_columns(age, fare)`: To find the difference between age and fare, which might be relevant for survival chances.
5. `k_bins_discretizer(fare, 3, encode='ordinal', strategy='quantile')`: Discretize 'fare' column into three equal quantiles.
6. `reduce_dimentionality(columns=['class_age_sub', 'age_min_max_scaled'], method='PCA')`: Perform PCA on the combination of 'class_age_sub' and 'age_min_max_scaled' columns to reduce dimensionality.
7. `polynomial_features(relatives, degree=3)`: Create polynomial features up to degree 3 for the 'relatives' column.
8. `ordinal_encoder(title)`: Encode ordinal values in 'title' into integers or dummy variables.
9. `linear_combination(class_exp, age, weight_1=0.5, weight_2=0.5)`: Create a linear combination of 'class_exp' and 'age'.
10. `power_transformer('title', method='yeo-johnson')`: Apply Yeo-Johnson power transformation on the 'title' column to improve normal distribution for better feature engineering performance.

**JSON:**
