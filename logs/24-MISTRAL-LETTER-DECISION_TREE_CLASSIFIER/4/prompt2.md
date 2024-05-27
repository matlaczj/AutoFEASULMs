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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['x-box', 'y-box', 'width', 'high', 'onpix', 'x-bar', 'y-bar', 'x2bar', 'y2bar', 'xybar', 'x2ybr', 'xy2br', 'x-ege', 'xegvy', 'y-ege', 'yegvx', 'x-bar_y-bar_sub', 'x-box_y-box_combination', 'onpix_log', 'x-ege_width_inter', 'high_min_max_scaled', 'x-box_power_transformed_yeo-johnson', 'width_high_inter', 'onpix_quantiled_n=100_distr=uniform', 'x-bar_y-box_inter', 'onpix_width_high_TruncatedSVD', 'x-ege_abs', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the given data and previous iterations, here are my suggested 10 new column-tool combinations for this iteration:

1. `power_transformer(column_name='onpix', method='yeo-johnson')`
2. `create_interaction(column_name_1='x-box', column_name_2='y-ege')`
3. `reduce_dimentionality(columns=['width', 'high'], method='PCA')`
4. `subtract_columns(column_name_1='x-box', column_name_2='y-box')`
5. `normalizer(column_name='onpix', norm='l2')`
6. `k_bins_discretizer(column_name='high', n_bins=4, encode='ordinal', strategy='quantile')`
7. `apply_math_function(column_name='x-ege', function='abs')`
8. `polynomial_features(column_name='width', degree=2)`
9. `min_max_scaler(column_name='onpix')`
10. `ordinal_encoder(column_name='class')`

Justification: I suggest transforming the 'onpix' column using Yeo-Johnson power transformation since it was previously found to have a high correlation with the target variable but had low performance when used directly in the previous iteration. Creating an interaction feature between 'x-box' and 'y-ege' may help capture any existing non-linear relationship between these features. Principal Component Analysis (PCA) can be applied to 'width' and 'high' columns as they have high correlations with each other, which could potentially result in reducing dimensionality without losing much information. Subtracting 'y-box' from 'x-box' might help create a new feature that represents the horizontal difference between them. Normalizing the 'onpix' column using L2 norm may improve performance since it was found to have a correlation with the target variable and had a moderate performance when scaled previously. Discretizing the 'high' column into 4 bins using an ordinal encoder could help capture any non-linear relationship and potentially improve model performance. Applying absolute values to 'x-ege' could capture both positive and negative values, which may be important for the model. Polynomial features with degree 2 can be applied to the 'width' column as it has a moderate correlation with the target variable and adding polynomial terms might help capture any non-linear relationship. Min-max scaling on 'onpix' was suggested earlier but this time I suggest using it after normalization to check if it provides better performance. Finally, encoding the 'class' column as ordinal may help the model understand the inherent order in the target variable.

**JSON:**
