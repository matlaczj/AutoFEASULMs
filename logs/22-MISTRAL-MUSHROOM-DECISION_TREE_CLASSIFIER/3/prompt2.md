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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['cap-shape_b', 'cap-shape_c', 'cap-shape_f', 'cap-shape_k', 'cap-shape_s', 'cap-shape_x', 'cap-surface_f', 'cap-surface_g', 'cap-surface_s', 'cap-surface_y', 'cap-color_b', 'cap-color_c', 'cap-color_e', 'cap-color_g', 'cap-color_n', 'cap-color_p', 'cap-color_r', 'cap-color_u', 'cap-color_w', 'cap-color_y', 'bruises%3f_f', 'bruises%3f_t', 'odor_a', 'odor_c', 'odor_f', 'odor_l', 'odor_m', 'odor_n', 'odor_p', 'odor_s', 'odor_y', 'gill-attachment_a', 'gill-attachment_f', 'gill-spacing_c', 'gill-spacing_w', 'gill-size_b', 'gill-size_n', 'stalk-shape_e', 'stalk-shape_t', 'stalk-root_b', 'stalk-root_c', 'stalk-root_e', 'stalk-root_r', 'stalk-surface-above-ring_f', 'stalk-surface-above-ring_k', 'stalk-surface-above-ring_s', 'stalk-surface-above-ring_y', 'stalk-surface-below-ring_f', 'stalk-surface-below-ring_k', 'stalk-surface-below-ring_s', 'stalk-surface-below-ring_y', 'stalk-color-above-ring_b', 'stalk-color-above-ring_c', 'stalk-color-above-ring_e', 'stalk-color-above-ring_g', 'stalk-color-above-ring_n', 'stalk-color-above-ring_o', 'stalk-color-above-ring_p', 'stalk-color-above-ring_w', 'stalk-color-above-ring_y', 'stalk-color-below-ring_b', 'stalk-color-below-ring_c', 'stalk-color-below-ring_e', 'stalk-color-below-ring_g', 'stalk-color-below-ring_n', 'stalk-color-below-ring_o', 'stalk-color-below-ring_p', 'stalk-color-below-ring_w', 'stalk-color-below-ring_y', 'veil-type_p', 'veil-color_n', 'veil-color_o', 'veil-color_w', 'veil-color_y', 'ring-number_n', 'ring-number_o', 'ring-number_t', 'ring-type_e', 'ring-type_f', 'ring-type_l', 'ring-type_n', 'ring-type_p', 'spore-print-color_b', 'spore-print-color_h', 'spore-print-color_k', 'spore-print-color_n', 'spore-print-color_o', 'spore-print-color_r', 'spore-print-color_u', 'spore-print-color_w', 'spore-print-color_y', 'population_a', 'population_c', 'population_n', 'population_s', 'population_v', 'population_y', 'habitat_d', 'habitat_g', 'habitat_l', 'habitat_m', 'habitat_p', 'habitat_u', 'habitat_w', 'stalk-color-below-ring_e_stalk-color-above-ring_c_sub', 'bruises%3f_t_power_transformed_yeo-johnson', 'population_n_log', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iterations, here are my suggested 10 column-tool combinations for this iteration:

1. `power_transformer(cap-color_g, method='yeo-johnson')`: The correlation between cap-color_g and target is moderate (0.43), so applying a power transformation with the Yeo-Johnson method could potentially improve model performance.
2. `k_bins_discretizer(bruises%3f, n_bins=5)`: This discretization can help create new binary or multi-class features from the existing 'bruises%3f' feature to provide better separation between classes.
3. `subtract_columns(gill-size_b, stalk-color-below-ring_w)`: The correlation between gill-size_b and stalk-color-below-ring_w is moderate (-0.43). Subtracting these columns could create a new feature that might be helpful for the model.
4. `create_interaction(cap-shape_x, cap-surface_y)`: This interaction feature could capture the relationship between these two features that may not be evident when looking at them separately.
5. `linear_combination(gill-spacing_w, stalk-root_e, 0.5, -0.5)`: Based on the correlation of 0.52 between gill-spacing_w and stalk-root_e, creating a linear combination might lead to useful information for the model.
6. `one_hot_encoder(veil-color_y)`: Since veil-color_y is a nominal variable with 4 distinct values, encoding it using One Hot Encoding would create new binary features, potentially providing more clarity to the model.
7. `polynomial_features(odor_n, degree=2)`: Applying polynomial features with a degree of 2 could help capture non-linear relationships between odor_n and the target variable.
8. `reduce_dimentionality(columns=['cap-color_g', 'stalk-shape_t', 'gill-size_b'], method='PCA')`: Principal Component Analysis (PCA) can be applied to these three features to create new features from the existing ones that capture most of their variances.
9. `min_max_scaler(gill-attachment_a)`: Scaling the gill-attachment_a column using Min-Max normalization might help improve model performance by standardizing the feature values across a similar range.
10. `binarizer(habitat_w, threshold=0.5)`: This binary transformation can be applied to the habitat_w column if it is currently a nominal variable with more than two distinct classes. If it is already binary or has only two classes, this step should be skipped.

**JSON:**
