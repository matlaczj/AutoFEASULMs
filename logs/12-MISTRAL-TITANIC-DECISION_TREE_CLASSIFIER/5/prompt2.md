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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['class', 'age', 'sex', 'sex_class_inter', 'age_age_sub', 'age_log', 'age_min_max_scaled', 'class_exp', 'class_age_sub', 'age_max_abs_scaled', 'age_log_class_sex_age_PCA_age_min_max_scaled_PCA', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are ten new column-tool combinations that could potentially improve the ML Decision Tree Classifier model for predicting the 'target' variable:

1. `log(class)` using `apply_math_function()`
2. `sex * 2` using `apply_math_function()` and `multiply(columns=['sex'], axes=0)()`
3. `interaction(age, class)` using `create_interaction()`
4. `title.isin(['Mr.', 'Mrs.']) * 1` using `apply_math_function()`, `one_hot_encoder()`, and `element_wise_multiply()`
5. `relatives.quartile(0.75)` using `quantile_transformer()`
6. `class_exp.abs()` using `apply_math_function()`
7. `min(age, fare)` using `min()` and `apply_generic()`
8. `max_abs_scaled('age') * max_abs_scaled('fare')` using `max_abs_scaler()` and `multiply()`
9. `class_exp * (relatives + 1)` using `linear_combination()` and `add(columns=['class_exp', 'relatives'])`
10. `PolynomialFeatures(degree=2, input_features=[columns['age'], columns['class']], interaction_only=False)` using `polynomial_features()`

**JSON:**
