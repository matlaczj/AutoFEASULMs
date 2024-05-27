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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'sex_f', 'sex_i', 'sex_m', 'height_diameter_inter', 'height_diameter_inter_standard_scaled', 'viscera_weight_quantiled_n=100_distr=normal', 'viscera_weight_quantiled_n=4_distr=normal', 'height_log', 'shell_weight_square', 'height_diameter_sub', 'length_diameter_sub', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given information, I suggest the following 10 column-tool combinations for this iteration:

1. `height_diameter_inter: create_interaction(height:, diameter:)`: Creating an interaction feature between height and diameter as they have a strong correlation with each other (-0.87). This new feature might contain valuable information that can help improve the model's prediction of 'target'.
2. `viscera_weight_log: apply_math_function(viscera_weight:, function='log')`: Taking the natural logarithm of viscera_weight as it has a correlation with whole_weight and target (-0.76, -0.39 respectively). This transformation could help to linearize the relationship between these variables and improve model performance.
3. `diameter_sqrt: apply_math_function(diameter:, function='sqrt')`: Applying a square root transformation on diameter as it has a strong correlation with length and target (0.92, -0.42 respectively). This could help to capture any hidden patterns or relationships that the model may not be able to detect using the raw data.
4. `whole_weight_normalized_l1: normalizer(whole_weight:, norm='l1')`: Normalizing whole_weight using L1 norm to ensure equal importance of each feature and help the model to focus on the most significant factors influencing the target variable.
5. `height_diameter_inter_quantile_n=4: k_bins_discretizer(height_diameter_inter:, n_bins=4)`: Discretizing the interaction feature 'height_diameter_inter' into 4 equal bins using a uniform strategy. This transformation might help to capture any non-linear relationships between height and diameter that the model may not be able to detect using the raw or scaled data.
6. `viscera_weight_quantile_n=100_distr=normal: quantile_transformer(viscera_weight:, n_quantiles=100, output_distribution='normal')`: Performing quantile normalization on viscera_weight as it has a weak correlation with the target feature but is important for modeling due to its relationship with whole_weight (-0.53). This transformation will ensure that the data follows a normal distribution which could help improve model performance.
7. `shell_weight_square: apply_math_function(shell_weight:, function='square')`: Applying the square transformation on shell_weight as it has a strong correlation with whole_weight and target (0.88, 0.84 respectively). This could help to capture any hidden patterns or relationships that the model may not be able to detect using the raw data.
8. `height_diameter_inter_standard_scaled: standard_scaler(height_diameter_inter:)`: Scaling 'height_diameter_inter' using StandardScaler as it has a strong correlation with height, diameter, and target (-0.59, 0.87, -0.44 respectively). This transformation will help the model to compare features on an equal scale and improve its ability to identify patterns in the data.
9. `viscera_weight_log_shell_weight: create_interaction(viscera_weight_log:, shell_weight:)`: Creating an interaction feature between viscera_weight_log and shell_weight as they have a moderate correlation (-0.68). This new feature might contain valuable information that can help improve the model's prediction of 'target'.
10. `height_diameter_inter_standard_scaled_abs: apply_math_function(height_diameter_inter_standard_scaled:, function='abs')`: Taking the absolute value of 'height_diameter_inter_standard_scaled' as it is a scaled feature and applying the absolute transformation could help capture any positive or negative relationships with other features that might be important for modeling.

**JSON:**
