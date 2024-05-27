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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x', 'y', 'ffmc', 'dmc', 'dc', 'isi', 'temp', 'rh', 'wind', 'rain', 'target', 'day_fri', 'day_mon', 'day_sat', 'day_sun', 'day_thu', 'day_tue', 'day_wed']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are ten new column-tool combinations that could potentially improve the performance of the K-Nearest Neighbors Regressor model for predicting the 'target' variable in the forest fire burned area problem:

1. `polynomial_features(x, degree=3)`: Add polynomial features up to degree 3 for both spatial coordinates (x and y) to capture complex non-linear relationships with the target.
2. `power_transformer(temp, method='box-cox')`: Apply a Box-Cox power transformation on the temperature column since it has a skewed distribution.
3. `subtract_columns(df['X'], df['Y'])`: Create a new feature by subtracting the spatial coordinate X from Y to find the difference between the two and potentially discover any spatial patterns.
4. `min_max_scaler(wind)`: Scale the wind speed column to bring all features to a similar range for easier comparison.
5. `create_interaction(df['temp'], df['rh'])`: Create an interaction term between temperature and relative humidity since they have a negative correlation with each other and might affect the fire risk differently in combination.
6. `k_bins_discretizer(temp, n_bins=5, strategy='quantile')`: Discretize the temperature column using equal-width bins based on quantiles to create more meaningful bins for forest fires.
7. `one_hot_encoder(day_fri)`: One-hot encode the day_fri column since it's a categorical variable.
8. `linear_combination(ffmc, dmc, weight_1=0.5, weight_2=0.5)`: Create a new feature by taking a linear combination of FFMC and DMC indices to capture their combined influence on forest fires.
9. `apply_math_function(isi, function='log')`: Apply a logarithmic transformation to the ISI index since it is highly skewed towards 0 and might have an exponential relationship with the target variable.
10. `reduce_dimentionality(columns=['ffmc', 'dc', 'isi', 'temp'], method='PCA')`: Perform Principal Component Analysis on these columns to find a lower-dimensional representation that retains most of the information and reduces overfitting.

**JSON:**
