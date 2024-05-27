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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'species']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given dataset and columns, here are ten potential feature engineering ideas for improving the performance of a K-Nearest Neighbors Regressor model in predicting the target variable 'class':

1. Create a new feature named `acidity_score` using a weighted sum of `fixed_acidity` and `volatile_acidity`, with weights determined by their correlation with the target. For instance: `linear_combination(fixed_acidity, volatile_acidity, 0.44, -0.35)`.
2. Apply a power transformation (Box-Cox method) to the 'density' column to make it more normally distributed and reduce skewness, which might help improve model performance: `power_transformer(density, method='box-cox')`.
3. Create interaction features between 'total_sulfur_dioxide' and 'fixed_acidity', 'volatile_acidity', and 'pH' to capture potential non-linear relationships: `create_interaction(total_sulfur_dioxide, fixed_acidity)`, `create_interaction(total_sulfur_dioxide, volatile_acidity)`, and `create_interaction(total_sulfur_dioxide, pH)`.
4. Use a polynomial degree of 2 to capture non-linear relationships between 'residual_sugar' and other features: `polynomial_features(residual_sugar, degree=2)`.
5. Create a new feature named 'acidity_ratio' by dividing `fixed_acidity` by `volatile_acidity` to better understand the relationship between these two factors.
6. Standardize 'citric_acid', 'chlorides', and 'sulphates' columns using z-score normalization: `standard_scaler(citric_acid)`, `standard_scaler(chlorides)`, and `standard_scaler(sulphates)`.
7. Use MinMaxScaler on the 'alcohol' column to make sure all values are within a specific range, which might help improve model performance: `min_max_scaler(alcohol)`.
8. Discretize 'pH' into five bins using equal width encoding strategy: `k_bins_discretizer(pH, n_bins=5, encode='ordinal', strategy='uniform')`.
9. Use OneHotEncoder on 'class' column to create binary indicator features for each unique class: `one_hot_encoder(class)`.
10. Perform Principal Component Analysis (PCA) to reduce the dimensionality of the dataset and improve model performance while retaining most of the important information: `reduce_dimentionality(columns=['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density'], method='PCA')`.

**JSON:**
