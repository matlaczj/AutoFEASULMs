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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['duration', 'credit_amount', 'installment_commitment', 'residence_since', 'age', 'existing_credits', 'num_dependents', 'target', 'checking_status_0<=x<200', 'checking_status_<0', 'checking_status_>=200', 'checking_status_no_checking', 'credit_history_all_paid', 'credit_history_critical/other_existing_credit', 'credit_history_delayed_previously', 'credit_history_existing_paid', 'credit_history_no_credits/all_paid', 'purpose_business', 'purpose_domestic_appliance', 'purpose_education', 'purpose_furniture/equipment', 'purpose_new_car', 'purpose_other', 'purpose_radio/tv', 'purpose_repairs', 'purpose_retraining', 'purpose_used_car', 'savings_status_100<=x<500', 'savings_status_500<=x<1000', 'savings_status_<100', 'savings_status_>=1000', 'savings_status_no_known_savings', 'employment_1<=x<4', 'employment_4<=x<7', 'employment_<1', 'employment_>=7', 'employment_unemployed', 'personal_status_female_div/dep/mar', 'personal_status_male_div/sep', 'personal_status_male_mar/wid', 'personal_status_male_single', 'other_parties_co_applicant', 'other_parties_guarantor', 'other_parties_none', 'property_magnitude_car', 'property_magnitude_life_insurance', 'property_magnitude_no_known_property', 'property_magnitude_real_estate', 'other_payment_plans_bank', 'other_payment_plans_none', 'other_payment_plans_stores', 'housing_for_free', 'housing_own', 'housing_rent', 'job_high_qualif/self_emp/mgmt', 'job_skilled', 'job_unemp/unskilled_non_res', 'job_unskilled_resident', 'own_telephone_none', 'own_telephone_yes', 'foreign_worker_no', 'foreign_worker_yes']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and the correlation table provided, here are 10 new column-tool combinations that could potentially improve the ML Decision Tree Classifier model for predicting the 'target' variable:

1. `poly_features('duration', degree=3)`: Creating polynomial features up to degree 3 for the 'duration' column might capture non-linear relationships between duration and credit risk.
2. `binarizer('employment_>=7')`: Binarizing the employment status into two categories: employed (1) or unemployed/not employed (-1), as employment status is strongly correlated with credit risk.
3. `min_max_scaler('installment_commitment')`: Scaling the 'installment_commitment' column to bring all values within a standard range, which could help improve model performance and reduce dimensionality.
4. `k_bins_discretizer('age', n_bins=5, encode='ordinal', strategy='quantile')`: Discretizing the 'age' column into 5 bins using quantiles to simplify data representation and capture non-linear relationships with credit risk.
5. `create_interaction(['employment_>=7', 'personal_status_male_single'])`: Creating an interaction feature between employment status and personal status, as these two factors may influence each other's impact on credit risk.
6. `one_hot_encoder('credit_history_delayed_previously')`: One-hot encoding the 'credit_history_delayed_previously' column to handle categorical data and improve model interpretability.
7. `linear_combination('age', 'installment_commitment', weight_1=0.6, weight_2=-0.3)`: Combining age and installment commitment linearly, as they are moderately correlated with credit risk (-0.54 correlation).
8. `subtract_columns('property_magnitude_real_estate', 'savings_status_>=1000')`: Subtracting the value of property magnitude from savings status, as having a substantial difference might indicate better financial management and lower credit risk.
9. `ordinal_encoder('employment_<1')`: One-hot encoding employment status (-1) into a new column 'employment_-1' to simplify data representation for the model.
10. `power_transformer('credit_history_existing_paid', method='yeo-johnson')`: Applying the Yeo-Johnson power transformation to the 'credit_history_existing_paid' column to normalize its distribution and improve model performance.

**JSON:**
