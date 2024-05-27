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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['age', 'medu', 'fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'dalc', 'walc', 'health', 'absences', 'g1', 'g2', 'school_gp', 'school_ms', 'sex_f', 'sex_m', 'address_r', 'address_u', 'famsize_gt3', 'famsize_le3', 'pstatus_a', 'pstatus_t', 'mjob_at_home', 'mjob_health', 'mjob_other', 'mjob_services', 'mjob_teacher', 'fjob_at_home', 'fjob_health', 'fjob_other', 'fjob_services', 'fjob_teacher', 'reason_course', 'reason_home', 'reason_other', 'reason_reputation', 'guardian_father', 'guardian_mother', 'guardian_other', 'schoolsup_no', 'schoolsup_yes', 'famsup_no', 'famsup_yes', 'paid_no', 'paid_yes', 'activities_no', 'activities_yes', 'nursery_no', 'nursery_yes', 'higher_no', 'higher_yes', 'internet_no', 'internet_yes', 'romantic_no', 'romantic_yes', 'failures_poly_2', 'studytime_failures_sub', 'absences_binarized_n=5_enc=ordinal_strat=quantile', 'failures_studytime_absences_PCA', 'traveltime_studytime_sub', 'studytime_poly_3', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current iteration history and unique values provided, here are 10 suggested column-tool combinations for creating new features in this math grade prediction problem:

1. `min_max_scaler('age')` - Scale the 'age' feature using Min-Max Scaler to bring all values within a standard range.
2. `quantile_transformer('failures', n_quantiles=5, output_distribution='normal')` - Normalize the 'failures' feature using Quantile Transformer with 5 quantiles.
3. `polynomial_features('studytime', degree=3)` - Add polynomial terms of degree 3 to the 'studytime' feature.
4. `k_bins_discretizer('health', n_bins=5, encode='ordinal', strategy='uniform')` - Discretize the 'health' feature into 5 bins using equal width binning.
5. `create_interaction(X, 'traveltime', 'studytime')` - Create interaction features between 'traveltime' and 'studytime'.
6. `subtract_columns('studytime', 'failures')` - Subtract 'failures' from 'studytime' to create a new column.
7. `power_transformer('health_log', method='yeo-johnson')` - Apply Yeo-Johnson power transformation on log transformed 'health' feature.
8. `binarizer('guardian', threshold=0.5)` - Binarize the 'guardian' column based on a threshold value of 0.5.
9. `one_hot_encoder(X, columns=['reason'])` - One-hot encode the 'reason' feature to create separate binary columns for each unique value.
10. `reduce_dimentionality(X, method='PCA', n_components=2)` - Apply Principal Component Analysis (PCA) to reduce dimensionality of the dataset while preserving most of the variance.

**JSON:**
