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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['class', 'age', 'sex', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current iteration history and available columns, here are ten new column-tool combinations that could potentially improve the performance of the Gaussian Naive Bayes Classifier for predicting the 'target' variable:

1. **Create interaction**: ('Pclass', 'sex')
This combination will create a new binary feature indicating the interaction between Pclass and Sex, as they are known to have a correlation with the target.
2. **Polynomial features**: ('age')
Adding polynomial terms up to degree 3 for the Age column could help capture non-linear relationships between age and the target.
3. **Ordinal encoder**: ('title')
Encoding categorical titles as ordinal numbers can be beneficial for some machine learning models, especially when dealing with ordered categories like 'Mr.', 'Mrs.', etc.
4. **K_bins_discretizer**: ('age', strategy='quantile', n_bins=5)
Discretizing Age using quantiles could help capture more meaningful information and reduce the impact of outliers on the model.
5. **Subtract columns**: (['Pclass', 'Fare'], 'age')
Subtracting Pclass and Fare from Age may help uncover any hidden relationships or patterns with the target variable.
6. **Binarizer**: ('relatives')
Creating binary features for different categories of relatives aboard the Titanic could provide valuable information about passenger demographics.
7. **Max_abs_scaler**: ('age_sex_combination')
Scaling 'age_sex_combination' using max_abs_scaler can help ensure all features have similar scales and prevent any dominance of high-magnitude features in the model.
8. **Power transformer**: ('fare', method='yeo-johnson')
Yeo-Johnson power transformation on Fare might help improve the normality of the distribution, making it more suitable for Gaussian Naive Bayes Classifier.
9. **Create interaction**: ('sex_class_inter', 'age_quantiled_n=10_distr=normal')
The interaction between 'sex_class_inter' and 'age_quantiled_n=10_distr=normal' could provide valuable insights into how age and social class combine to influence the target variable.
10. **Quantile transformer**: ('fare', n_quantiles=5, output_distribution='uniform')
Transforming Fare using a uniform quantile distribution can help reduce skewness in the data and make it more uniformly distributed, which is often preferred by Gaussian Naive Bayes Classifier.

**JSON:**
