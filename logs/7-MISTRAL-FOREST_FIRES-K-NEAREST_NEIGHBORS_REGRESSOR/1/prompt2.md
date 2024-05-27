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
 Based on the given dataset and considering the current iteration, here are my suggested column-tool combinations for creating new features:

1. Apply log transformation using `apply_math_function` on 'area': This is due to the skewed nature of the target variable (area). Logarithmic transformation can help normalize the distribution.
2. Create interaction between 'FFMC' and 'DC' using `create_interaction`: FFMC and DC are correlated, creating an interaction term may help capture more complex relationships between the two features.
3. Polynomial features of degree 2 on 'temp' using `polynomial_features`: Nonlinear relationship between temperature and burned area is common in forest fire data, thus polynomial features can help model this relationship better.
4. Subtract 'rain' from 'ISI' using `subtract_columns`: Rain affects the ISI index significantly; subtracting rain from it may help capture more precise information about the vegetation condition.
5. Binarize 'day_fri' and 'day_mon' using `binarizer`: Some forest fires might have specific trends related to weekdays or weekends, binarizing these columns will allow the model to capture this information directly.
6. One-hot encode 'month' using `one_hot_encoder`: The month of the year may influence the burned area; one-hot encoding will ensure that each month is considered as a separate feature.
7. Create interaction between 'rh' and 'temp' using `create_interaction`: Relative humidity and temperature have a strong inverse correlation, creating an interaction term can help capture more complex relationships between these two features.
8. Apply min-max scaling on 'FFMC', 'DMC', 'DC', and 'ISI' using `min_max_scaler`: These columns are on different scales; normalizing them may help improve model performance by ensuring equal weightage to all input features.
9. Power transform 'rh' using `power_transformer` with the box-cox method: The distribution of relative humidity is not normally distributed, and Box-Cox power transformation can help make it more symmetrical and normal, which could improve model performance.
10. Create interaction between 'wind' and 'temp' using `create_interaction`: Wind speed and temperature are known factors influencing the burned area; their interaction term may provide important information for modeling forest fires accurately.

**JSON:**
