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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['age', 'medu', 'fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'dalc', 'walc', 'health', 'absences', 'g1', 'g2', 'target', 'school_gp', 'school_ms', 'sex_f', 'sex_m', 'address_r', 'address_u', 'famsize_gt3', 'famsize_le3', 'pstatus_a', 'pstatus_t', 'mjob_at_home', 'mjob_health', 'mjob_other', 'mjob_services', 'mjob_teacher', 'fjob_at_home', 'fjob_health', 'fjob_other', 'fjob_services', 'fjob_teacher', 'reason_course', 'reason_home', 'reason_other', 'reason_reputation', 'guardian_father', 'guardian_mother', 'guardian_other', 'schoolsup_no', 'schoolsup_yes', 'famsup_no', 'famsup_yes', 'paid_no', 'paid_yes', 'activities_no', 'activities_yes', 'nursery_no', 'nursery_yes', 'higher_no', 'higher_yes', 'internet_no', 'internet_yes', 'romantic_no', 'romantic_yes']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and previous iteration history, here are my suggested feature engineering and selection steps for the next iteration:

1. Polynomial Features (degree=2) on 'age': Create a new set of columns based on squared and interaction terms between existing 'age' column to capture non-linear relationships with the target variable.
   - polynomial\_features('age', degree=2)

2. One Hot Encoder for 'reason': Convert categorical 'reason' column into binary indicator columns (one for each category).
   - one_hot_encoder('reason')

3. Interaction between 'studytime' and 'famsup': Create a new feature by multiplying the existing 'studytime' and 'famsup' columns to capture their interaction effect on the target variable.
   - create_interaction('studytime', 'famsup')

4. Subtracting 'traveltime' from 'studytime': Create a new feature by subtracting 'traveltime' from 'studytime'. This could help capture the net study time available for students after adjusting for travel time.
   - subtract_columns('studytime', 'traveltime')

5. Bin Discretizer on 'health': Divide the continuous 'health' column into 5 equal bins and create new indicator columns for each bin to capture health status distribution.
   - k_bins_discretizer('health', n_bins=5, encode='ordinal')

6. Interaction between 'sex' and 'school': Create a new feature by multiplying the existing 'sex' and 'school' columns to capture any potential interaction effect on the target variable.
   - create_interaction('sex', 'school')

7. Min-Max Scaler on 'studytime_traveltime_sub': Scale 'studytime_traveltime_sub' feature using a Min-Max scaler to ensure all features have a similar range for the Ridge Regression model.
   - min_max_scaler('studytime_traveltime_sub')

8. Log Transform on 'health_log': Apply log transformation on 'health_log' feature to normalize its distribution and improve model performance.
   - apply_math_function('health_log', function='log')

9. Linear Combination between 'famsize_gt3' and 'schoolsup_yes': Create a new feature by multiplying the existing 'famsize_gt3' and 'schoolsup_yes' columns to capture their interaction effect on the target variable, then apply a normalizer to ensure it has similar scale as other features.
   - linear_combination('famsize_gt3', 'schoolsup_yes')
   - normalizer(column='linear_combination_famsize_gt3_schoolsup_yes', norm='l2')

10. Interaction between 'reason_course' and 'address_u': Create a new feature by multiplying the existing 'reason_course' and 'address_u' columns to capture any potential interaction effect on the target variable.
    - create_interaction('reason_course', 'address_u')

**JSON:**
