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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x-box', 'y-box', 'width', 'high', 'onpix', 'x-bar', 'y-bar', 'x2bar', 'y2bar', 'xybar', 'x2ybr', 'xy2br', 'x-ege', 'xegvy', 'y-ege', 'yegvx', 'x-box_y-box_inter', 'width_high_sub', 'onpix_log', 'width_min_max_scaled', 'x-box_min_max_scaled', 'onpix_width_combination', 'x-ege_standard_scaled', 'x-ege_quantiled_n=100_distr=uniform', 'x-box_y-box_sub', 'x2ybr_abs', 'x-bar_y-bar_inter', 'width_high_PCA', 'onpix_sqrt', 'width_log', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given information, I suggest the following 10 column-tool combinations for this iteration:

1. `width_power_transformed_yeo-johnson(width)`: Since the correlation between 'width' and 'width_power_transformed_yeo-johnson' is relatively high (0.88), applying a power transformation to 'width' using the Yeo-Johnson method could help improve the model's performance.
2. `x-box_min_max_scaled(x-box)`: Since the correlation between 'x-box' and 'x-box_min_max_scaled' is quite strong (0.92), normalizing 'x-box' using MinMaxScaler could be beneficial for the model.
3. `onpix_quantiled_n=100_distr=uniform(onpix)`: Given that the correlation between 'onpix' and 'width' is 0.7, we can try quantile normalization on 'onpix' using Uniform distribution to help improve the model.
4. `x-box_y-box_sub(x-box, y-box)`: With a moderate negative correlation between 'x-box' and 'y-box' (-0.69), creating a new feature by subtracting 'y-box' from 'x-box' could help reveal any interesting patterns or relationships in the data.
5. `width_high_combination(width, high)`: As the correlation between 'width' and 'high' is quite high (0.87), creating a new feature by combining these two columns using a linear combination might be helpful for the model.
6. `x-box_y-box_inter(x-box, y-box)`: Given that 'x-box' and 'y-box' have a strong positive correlation (0.92), creating an interaction feature between these two columns could potentially reveal more complex relationships in the data.
7. `onpix_log(onpix)`: Based on the correlation between 'onpix_log' and 'width' (0.65), applying a logarithmic transformation to 'onpix' might help improve the model by making the relationship between these two features more linear.
8. `x-bar_y-bar_inter(x-bar, y-bar)`: Since there is a moderate positive correlation between 'x-bar' and 'y-bar' (0.52), creating an interaction feature between these two columns could be beneficial for the model.
9. `width_high_sub(width, high)`: Considering the strong negative correlation between 'width' and 'high' (-0.59), subtracting 'high' from 'width' might help reveal any interesting patterns or relationships in the data.
10. `x-ege_standard_scaled(x-ege)`: As 'x-ege' is highly correlated with its standardized version (correlation = 1), we can apply StandardScaler to normalize 'x-ege' to make the model more robust and efficient.

**JSON:**
