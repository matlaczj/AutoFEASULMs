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
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['duration', 'credit_amount', 'installment_commitment', 'residence_since', 'age', 'existing_credits', 'num_dependents', 'checking_status_0<=x<200', 'checking_status_<0', 'checking_status_>=200', 'checking_status_no_checking', 'credit_history_all_paid', 'credit_history_critical/other_existing_credit', 'credit_history_delayed_previously', 'credit_history_existing_paid', 'credit_history_no_credits/all_paid', 'purpose_business', 'purpose_domestic_appliance', 'purpose_education', 'purpose_furniture/equipment', 'purpose_new_car', 'purpose_other', 'purpose_radio/tv', 'purpose_repairs', 'purpose_retraining', 'purpose_used_car', 'savings_status_100<=x<500', 'savings_status_500<=x<1000', 'savings_status_<100', 'savings_status_>=1000', 'savings_status_no_known_savings', 'employment_1<=x<4', 'employment_4<=x<7', 'employment_<1', 'employment_>=7', 'employment_unemployed', 'personal_status_female_div/dep/mar', 'personal_status_male_div/sep', 'personal_status_male_mar/wid', 'personal_status_male_single', 'other_parties_co_applicant', 'other_parties_guarantor', 'other_parties_none', 'property_magnitude_car', 'property_magnitude_life_insurance', 'property_magnitude_no_known_property', 'property_magnitude_real_estate', 'other_payment_plans_bank', 'other_payment_plans_none', 'other_payment_plans_stores', 'housing_for_free', 'housing_own', 'housing_rent', 'job_high_qualif/self_emp/mgmt', 'job_skilled', 'job_unemp/unskilled_non_res', 'job_unskilled_resident', 'own_telephone_none', 'own_telephone_yes', 'foreign_worker_no', 'foreign_worker_yes', 'credit_amount_poly_2', 'credit_history_delayed_previously_credit_history_existing_paid_sub', 'age_quantiled_n=100_distr=normal', 'employment_1<=x<4_personal_status_female_div/dep/mar_inter', 'residence_since_binarized_n=5_enc=ordinal_strat=quantile', 'installment_commitment_max_abs_scaled', 'age_checking_status_>=200_combination', 'credit_history_all_paid_credit_history_delayed_previously_credit_history_critical/other_existing_credit_existing_credits_PCA', 'target']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current iteration history and the available columns, here are 10 new column-tool combinations that could potentially improve the ML Decision Tree Classifier model for predicting 'target':

1. `polynomial_features(checking_status, degree=3)` - Create polynomial features up to degree 3 from the 'checking_status' column to capture more complex relationships with the target variable.
2. `min_max_scaler(credit_history_delayed_previously)` - Normalize the 'credit_history_delayed_previously' column using Min-Max Scaler to bring all values to a comparable scale and avoid bias towards large values.
3. `create_interaction(employment, personal_status)` - Create interaction features between 'employment' and 'personal_status' columns to account for the influence of employment status on credit risk based on individual circumstances.
4. `reduce_dimentionality(existing_credits:, method='PCA')` - Use Principal Component Analysis (PCA) to reduce the dimensionality of the 'existing_credits' column and keep only the most significant components that explain maximum variance in the data.
5. `log(installment_commitment)` - Apply log transformation on 'installment_commitment' to make the distribution more normal, as it might be skewed towards larger values and negatively impact model performance.
6. `binarizer(other_debtors_guarantors, threshold=1)` - Convert the binary 'other_debtors_guarantors' column into dummy variables using Binarizer to help the decision tree classifier learn the difference between having and not having debtors/guarantors.
7. `quantile_transformer(age, n_quantiles=10, output_distribution='normal')` - Apply quantile normalization on 'age' column and output normalized values following a normal distribution to bring age values into a more uniform scale.
8. `subtract_columns(credit_amount, duration)` - Subtract the 'duration' column from the 'credit_amount' column to calculate the difference between the loan amount requested and loan tenure, which might be an important factor in determining credit risk.
9. `power_transformer(personal_status, method='yeo-johnson')` - Apply Yeo-Johnson power transformation on 'personal_status' column to adjust for non-linearity and improve the model's ability to learn complex relationships between personal status and credit risk.
10. `one_hot_encoder(purpose)` - Encode the 'purpose' column into one-hot encoded dummy variables to provide separate binary features for each purpose category, making it easier for the decision tree classifier to identify patterns specific to each purpose type.

**JSON:**
