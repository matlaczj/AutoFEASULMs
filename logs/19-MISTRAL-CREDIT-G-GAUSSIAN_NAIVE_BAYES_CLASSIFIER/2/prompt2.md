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
 Based on the current iteration history and the available columns, here are 10 new column-tool combinations that could potentially improve the performance of the Gaussian Naive Bayes Classifier model in predicting the 'target' variable:

1. **Polynomial features**: Create interaction terms between highly correlated features such as 'age_poly_2' and 'installment_commitment_duration_inter'. Degree: 2.
    `create_interaction(column_name='age_poly_2', column_name='installment_commitment_duration_inter')`

2. **One-hot encoder**: Encode categorical features with many unique values such as 'credit_history' and 'personal_status'.
    `one_hot_encoder(column_name='credit_history')`
    `one_hot_encoder(column_name='personal_status')`

3. **Binarizer**: Convert continuous features with only a few unique values into binary features, such as 'checking_status' and 'housing'.
    `binarizer(column_name='checking_status', threshold=200)`
    `binarizer(column_name='housing', threshold=1)`

4. **Power transformer**: Apply Yeo-Johnson power transformation to features that have non-normal distribution, such as 'age_residence_since_sub' and 'existing_credits'.
    `power_transformer(column_name='age_residence_since_sub', method='yeo-johnson')`
    `power_transformer(column_name='existing_credits', method='yeo-johnson')`

5. **Linear combination**: Create a new feature by combining two features that have a high positive correlation, such as 'savings_status' and 'duration'.
    `linear_combination(column_name_1='savings_status', column_name_2='duration', weight_1=0.5, weight_2=0.5)`

6. **Subtract columns**: Create a new feature by subtracting one column from another, such as 'checking_status_<0' and 'existing_credits'.
    `subtract_columns(column_name_1='checking_status_<0>', column_name_2='existing_credits')`

7. **Ordinal encoder**: Encode ordinal features like 'employment' to create dummy variables for each category.
    `ordinal_encoder(column_name='employment')`

8. **Min-max scaler**: Scale numerical columns to a specific range, such as 'age' and 'credit_amount'.
    `min_max_scaler(column_name='age')`
    `min_max_scaler(column_name='credit_amount')`

9. **K-bins discretizer**: Discretize continuous features into bins, such as 'installment_commitment' and 'duration'.
    `k_bins_discretizer(column_name='installment_commitment', n_bins=5)`
    `k_bins_discretizer(column_name='duration', n_bins=10, strategy='quantile')`

10. **Reduce dimensionality**: Use PCA to reduce the number of features while preserving most of the variance in the data, such as 'checking_status_0<=x<200' and 'credit_history_no_credits/all_paid'.
    `reduce_dimentionality(columns=['checking_status_0<=x<200', 'credit_history_no_credits/all_paid'], method='PCA')`

**JSON:**
