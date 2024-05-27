**INTRODUCTION:**
Predict the final grade of students in a math course based on various features (these columns might not exist, use columns from COLUMNS section):
1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira).
2 sex - student's sex (binary: 'F' - female or 'M' - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
13 traveltime - home to school travel time (numeric: 1 - <15>1 hour)
14 studytime - weekly study time (numeric: 1 - <2>10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'age': 16.34, 17.74, 17.3, 18.43, 15.85, 16.99, 17.43, 17.98, 14.52, 18.75 ...
example unique values in 'medu': 2.69, 3.92, 4.07, 3.98, 1.05, 1.02, 1.26, 3.83, 2.23, 3.01 ...
example unique values in 'fedu': 3.82, 3.09, 3.98, 3.82, 2.89, 3.07, 1.71, 3.89, 3.87, 2.86 ...
example unique values in 'traveltime': 1.0, 0.97, 1.17, 0.92, 1.07, 0.83, 0.79, 1.08, 3.14, 0.87 ...
example unique values in 'studytime': 1.91, 1.89, 0.91, 2.19, 1.14, 0.89, 4.09, 3.96, 0.84, 0.82 ...
example unique values in 'failures': 0.09, -0.01, -0.02, -0.02, -0.05, 0.0, 0.03, 0.74, -0.09, 0.14 ...
example unique values in 'famrel': 4.97, 4.28, 4.24, 4.19, 3.94, 3.79, 4.12, 4.37, 4.29, 3.84 ...
example unique values in 'freetime': 3.11, 1.69, 2.78, 2.93, 4.33, 4.09, 3.71, 2.99, 3.15, 2.07 ...
example unique values in 'goout': 3.06, 4.06, 3.21, 3.04, 5.06, 1.78, 3.96, 3.17, 4.88, 4.17 ...
example unique values in 'dalc': 1.94, 3.0, 2.08, 1.36, 2.46, 1.2, 2.04, 1.38, 0.99, 4.24 ...
example unique values in 'walc': 1.97, 3.17, 4.92, 0.77, 3.81, 2.86, 1.51, 4.01, 3.42, 0.97 ...
example unique values in 'health': 5.37, 3.83, 1.26, 2.87, 3.01, 1.77, 2.86, 5.3, 2.96, 2.89 ...
example unique values in 'absences': -2.9, 3.69, -3.15, 9.16, 3.77, 14.59, 12.59, -1.73, 4.61, 57.01 ...
example unique values in 'g1': 8.17, 11.15, 6.92, 11.79, 13.23, 10.63, 10.76, 7.73, 10.45, 9.67 ...
example unique values in 'g2': 6.18, 11.44, 9.33, 16.71, 11.59, 16.13, 8.03, 9.88, 13.0, 15.12 ...
all unique values in 'school_gp': 1, 0
all unique values in 'school_ms': 0, 1
all unique values in 'sex_f': 1, 0
all unique values in 'sex_m': 0, 1
all unique values in 'address_r': 0, 1
all unique values in 'address_u': 1, 0
all unique values in 'famsize_gt3': 1, 0
all unique values in 'famsize_le3': 0, 1
all unique values in 'pstatus_a': 1, 0
all unique values in 'pstatus_t': 0, 1
all unique values in 'mjob_at_home': 1, 0
all unique values in 'mjob_health': 0, 1
all unique values in 'mjob_other': 0, 1
all unique values in 'mjob_services': 0, 1
all unique values in 'mjob_teacher': 0, 1
all unique values in 'fjob_at_home': 0, 1
all unique values in 'fjob_health': 0, 1
all unique values in 'fjob_other': 0, 1
all unique values in 'fjob_services': 0, 1
all unique values in 'fjob_teacher': 1, 0
all unique values in 'reason_course': 1, 0
all unique values in 'reason_home': 0, 1
all unique values in 'reason_other': 0, 1
all unique values in 'reason_reputation': 0, 1
all unique values in 'guardian_father': 0, 1
all unique values in 'guardian_mother': 1, 0
all unique values in 'guardian_other': 0, 1
all unique values in 'schoolsup_no': 0, 1
all unique values in 'schoolsup_yes': 1, 0
all unique values in 'famsup_no': 1, 0
all unique values in 'famsup_yes': 0, 1
all unique values in 'paid_no': 1, 0
all unique values in 'paid_yes': 0, 1
all unique values in 'activities_no': 1, 0
all unique values in 'activities_yes': 0, 1
all unique values in 'nursery_no': 0, 1
all unique values in 'nursery_yes': 1, 0
all unique values in 'higher_no': 0, 1
all unique values in 'higher_yes': 1, 0
all unique values in 'internet_no': 1, 0
all unique values in 'internet_yes': 0, 1
all unique values in 'romantic_no': 1, 0
all unique values in 'romantic_yes': 0, 1
example unique values in 'failures_poly_2': 9.45, 0.89, 0.0, 1.04, 0.54, 0.05, 0.01, 4.1, 0.0, 0.06 ...
example unique values in 'studytime_failures_sub': 1.12, 1.37, 0.05, 2.09, 1.86, 2.88, 1.57, 1.96, 2.45, 2.12 ...
all unique values in 'absences_binarized_n=5_enc=ordinal_strat=quantile': 1.0, 3.0, 0.0, 2.0, 4.0
example unique values in 'failures_studytime_absences_PCA': -2.02, -8.73, 1.2, -7.26, -3.28, -1.55, -5.19, 2.43, -16.05, -3.64 ...
example unique values in 'health_min_max_scaled': 0.14, 0.91, 0.74, 0.89, 0.87, 0.68, 0.88, 0.66, 0.95, 0.48 ...
example unique values in 'target': 3.4, 3.83, 2.95, 3.77, 2.79, 2.61, 3.94, 3.64, 4.04, 3.71 ...
- *CORRELATIONS:*
correlation between 'address_u' and 'address_r': -1.0
correlation between 'nursery_yes' and 'nursery_no': -1.0
correlation between 'paid_yes' and 'paid_no': -1.0
correlation between 'romantic_yes' and 'romantic_no': -1.0
correlation between 'activities_yes' and 'activities_no': -1.0
correlation between 'internet_yes' and 'internet_no': -1.0
correlation between 'failures_studytime_absences_PCA' and 'absences': 1.0
correlation between 'school_ms' and 'school_gp': -1.0
correlation between 'schoolsup_yes' and 'schoolsup_no': -1.0
correlation between 'pstatus_t' and 'pstatus_a': -1.0
correlation between 'health_min_max_scaled' and 'health': 1.0
correlation between 'sex_m' and 'sex_f': -1.0
correlation between 'higher_yes' and 'higher_no': -1.0
correlation between 'famsup_yes' and 'famsup_no': -1.0
correlation between 'failures_poly_2' and 'failures': 0.93
correlation between 'guardian_mother' and 'guardian_father': -0.81
correlation between 'studytime_failures_sub' and 'studytime': 0.8
correlation between 'absences_binarized_n=5_enc=ordinal_strat=quantile' and 'absences': 0.8
correlation between 'failures_studytime_absences_PCA' and 'absences_binarized_n=5_enc=ordinal_strat=quantile': 0.8
correlation between 'studytime_failures_sub' and 'failures': -0.74
correlation between 'target' and 'g2': 0.72
correlation between 'fjob_services' and 'fjob_other': -0.69
correlation between 'studytime_failures_sub' and 'failures_poly_2': -0.69
correlation between 'walc' and 'dalc': 0.61
correlation between 'fedu' and 'medu': 0.61
correlation between 'target' and 'g1': 0.56
correlation between 'reason_home' and 'reason_course': -0.47
correlation between 'mjob_teacher' and 'medu': 0.45
correlation between 'guardian_other' and 'guardian_mother': -0.44
correlation between 'mjob_services' and 'mjob_other': -0.44
correlation between 'mjob_at_home' and 'medu': -0.4
correlation between 'walc' and 'goout': 0.4
correlation between 'guardian_other' and 'age': 0.39
correlation between 'reason_reputation' and 'reason_home': -0.37
correlation between 'school_ms' and 'age': 0.36
correlation between 'school_gp' and 'age': -0.36
correlation between 'fjob_teacher' and 'fedu': 0.34
correlation between 'g2' and 'failures': -0.33
correlation between 'g1' and 'failures': -0.33
correlation between 'target' and 'failures': -0.33
correlation between 'failures_poly_2' and 'g2': -0.32
correlation between 'sex_f' and 'studytime': 0.32
correlation between 'sex_m' and 'studytime': -0.32
correlation between 'failures_poly_2' and 'g1': -0.32
correlation between 'mjob_other' and 'mjob_at_home': -0.31
correlation between 'address_u' and 'traveltime': -0.31
correlation between 'mjob_teacher' and 'mjob_other': -0.31
correlation between 'address_r' and 'traveltime': 0.31
correlation between 'mjob_teacher' and 'fedu': 0.3
correlation between 'target' and 'failures_poly_2': -0.3

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: 14.49%
Error: 0.2399
Added columns: {'health_min_max_scaled', 'studytime_failures_sub', 'absences_binarized_n=5_enc=ordinal_strat=quantile', 'failures_poly_2', 'failures_studytime_absences_PCA'}
Removed columns: set()

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

**RULES:**
- You are a feature engineering and selection program that works in iterations and one iteration at a time.
- You create new features from existing columns to make ML K-Nearest Neighbors Regressor model better at predicting target variable 'target' in regression problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**