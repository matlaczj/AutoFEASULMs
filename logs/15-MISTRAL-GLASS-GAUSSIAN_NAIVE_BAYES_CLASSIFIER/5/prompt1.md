**INTRODUCTION:**
Predict the type of glass based on features (these columns might not exist, use columns from COLUMNS section):
binaryClass (target): This column is the target variable or the label you want to predict. It's a nominal variable with two distinct values, likely representing binary classes.
RI: This column represents the refractive index of the material. Refractive index is a measure of how light bends as it passes through the material.
Na: This column represents the sodium (Na) content of the material. Sodium content can influence various properties of the material.
Mg: This column represents the magnesium (Mg) content of the material. Magnesium can affect the material's properties such as strength and corrosion resistance.
Al: This column represents the aluminum (Al) content of the material. Aluminum is a common alloying element in many materials and can impact properties like strength and hardness.
Si: This column represents the silicon (Si) content of the material. Silicon is often present in materials like glass and ceramics and can affect properties such as transparency and thermal conductivity.
K: This column represents the potassium (K) content of the material. Potassium can influence properties like electrical conductivity and chemical reactivity.
Ca: This column represents the calcium (Ca) content of the material. Calcium is often found in materials like ceramics and can affect properties such as hardness and durability.
Ba: This column represents the barium (Ba) content of the material. Barium can be used as an additive in materials for various purposes such as improving electrical conductivity or increasing density.
Fe: This column represents the iron (Fe) content of the material. Iron is a common element in many materials and can impact properties such as strength, magnetism, and corrosion resistance.

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'ri': 1.52, 1.52, 1.52, 1.52, 1.52, 1.52, 1.53, 1.52, 1.52, 1.52 ...
example unique values in 'na': 13.05, 13.1, 13.06, 12.1, 13.21, 13.11, 12.67, 13.45, 13.14, 12.71 ...
example unique values in 'mg': 3.28, 3.83, 3.35, 0.06, 3.49, 0.18, 2.71, 0.02, 4.26, 3.97 ...
example unique values in 'al': 2.19, 2.24, 0.98, 1.31, 1.57, 1.31, 1.3, 0.6, 1.18, 1.46 ...
example unique values in 'si': 72.19, 72.59, 72.93, 73.14, 73.91, 71.89, 73.57, 72.51, 72.23, 72.1 ...
example unique values in 'k': 0.43, 0.61, 0.09, -0.57, 0.53, 0.1, 0.32, 1.15, -0.35, -0.11 ...
example unique values in 'ca': 8.15, 7.9, 9.28, 10.12, 7.83, 7.43, 8.37, 8.35, 8.78, 8.27 ...
example unique values in 'ba': 0.17, -0.3, 0.21, -0.06, 1.49, 0.16, -0.2, 0.22, 0.09, 0.12 ...
example unique values in 'fe': 0.02, 0.53, 0.24, -0.02, -0.03, 0.05, 0.03, 0.04, 0.04, 0.2 ...
example unique values in 'ri_na_inter': 20.45, 21.96, 21.49, 16.14, 21.19, 19.81, 19.64, 16.36, 20.42, 20.15 ...
all unique values in 'mg_binarized_n=5_enc=ordinal_strat=quantile': 2.0, 4.0, 1.0, 0.0, 3.0
example unique values in 'si_poly_2': 5364.46, 5293.57, 5298.81, 5229.7, 5289.92, 5327.84, 5309.94, 5373.33, 5187.71, 4972.99 ...
example unique values in 'ri_ca_sub': -6.2, -6.69, -4.09, -6.15, -5.83, -13.66, -7.06, -6.87, -8.43, -6.64 ...
example unique values in 'al_min_max_scaled': 0.4, 0.12, 0.68, 0.71, 0.63, 0.18, 0.39, 0.48, 0.45, 0.36 ...
example unique values in 'k_quantiled_n=10_distr=uniform': 0.58, 0.1, 0.83, 0.9, 0.24, 0.51, 0.22, 0.89, 0.27, 0.22 ...
example unique values in 'ri_mg_combination': -0.31, 0.36, -0.35, -0.33, -0.16, 0.65, 0.82, -0.07, -0.26, -0.39 ...
example unique values in 'mg_min_max_scaled': 0.76, 0.78, 0.3, 0.03, 0.88, 0.11, 0.77, 0.88, 0.84, 0.08 ...
example unique values in 'ca_poly_2': 77.05, 68.42, 77.07, 161.14, 59.32, 120.0, 206.95, 105.01, 69.74, 79.13 ...
example unique values in 'ri_si_sub': -71.4, -70.61, -71.25, -71.5, -70.7, -71.72, -71.8, -71.09, -72.85, -71.48 ...
example unique values in 'al_power_transformed_yeo-johnson': 0.74, -1.16, -0.62, -0.18, 0.67, -0.84, 0.72, 0.45, 0.2, -0.65 ...
example unique values in 'ri_ca_inter': 16.05, 13.02, 12.56, 17.23, 13.87, 13.07, 14.48, 12.25, 14.53, 11.64 ...
all unique values in 'ri_binarized_n=5_enc=ordinal_strat=quantile': 1.0, 0.0, 2.0, 4.0, 3.0
example unique values in 'ri_mg_sub': -1.9, -1.88, -1.96, -2.02, -1.52, -1.76, -2.2, 1.53, -0.16, 1.73 ...
example unique values in 'al_power_transformed_box-cox': -0.88, 0.35, 1.2, -0.89, -1.8, 0.38, 0.47, -0.06, -0.32, 0.53 ...
example unique values in 'si_ca_PCA': -0.64, -1.55, -0.61, -0.21, -0.99, -0.95, 1.28, 0.15, -0.25, 2.83 ...
example unique values in 'na_quantiled_n=100_distr=uniform': 0.04, 0.8, 0.44, 0.16, 0.31, 0.65, 0.85, 0.94, 0.3, 0.62 ...
example unique values in 'ri_si_combination': 29.85, 30.11, 29.98, 29.85, 29.82, 29.68, 30.27, 29.75, 30.23, 29.86 ...
example unique values in 'fe_min_max_scaled': 0.14, 0.17, 0.19, 0.52, 0.45, 0.0, 0.08, 0.07, 0.05, 0.31 ...
example unique values in 'ri_mg_inter': 4.9, -0.08, 6.92, 5.4, 4.7, -0.03, 4.22, 1.55, 5.17, 4.52 ...
example unique values in 'si_ca_sub': 56.31, 65.02, 63.05, 64.08, 66.44, 62.48, 64.25, 65.1, 65.67, 62.11 ...
example unique values in 'na_quantiled_n=100_distr=normal': -0.46, 0.37, 1.23, -1.69, -0.17, -0.39, -1.83, -1.47, 0.21, -0.94 ...
example unique values in 'si_ca_inter': 867.23, 572.21, 569.93, 1042.45, 757.8, 569.69, 740.64, 673.15, 666.99, 594.91 ...
example unique values in 'ri_poly_2': 2.31, 2.3, 2.3, 2.3, 2.3, 2.32, 2.31, 2.3, 2.29, 2.31 ...
example unique values in 'si_ca_mg_PCA_PCA': -0.96, 1.22, -1.59, -0.05, -0.88, -1.11, 2.07, -1.01, -0.93, 1.94 ...
all unique values in 'ri_mg_combination_binarized_th=0.5': 0.0, 1.0
all unique values in 'target': 0, 5, 4, 1, 3, 2
- *CORRELATIONS:*
correlation between 'ri_mg_sub' and 'mg_min_max_scaled': -1.0
correlation between 'si_ca_inter' and 'ri_ca_sub': -1.0
correlation between 'ri_mg_sub' and 'ri_mg_combination': 1.0
correlation between 'ri_mg_combination' and 'mg': -1.0
correlation between 'ri_mg_inter' and 'mg_min_max_scaled': 1.0
correlation between 'ri_na_inter' and 'na': 1.0
correlation between 'al_power_transformed_yeo-johnson' and 'al': 0.99
correlation between 'si_ca_inter' and 'ca_poly_2': 0.99
correlation between 'na_quantiled_n=100_distr=normal' and 'ri_na_inter': 0.98
correlation between 'ri_mg_combination_binarized_th=0.5' and 'ri_mg_combination': 0.93
correlation between 'si_ca_sub' and 'ca': -0.89
correlation between 'si_ca_sub' and 'ca_poly_2': -0.89
correlation between 'si_ca_sub' and 'ri_ca_sub': 0.89
correlation between 'mg_binarized_n=5_enc=ordinal_strat=quantile' and 'mg': 0.86
correlation between 'ri_mg_combination' and 'mg_binarized_n=5_enc=ordinal_strat=quantile': -0.86
correlation between 'mg_min_max_scaled' and 'mg_binarized_n=5_enc=ordinal_strat=quantile': 0.86
correlation between 'si_ca_mg_PCA_PCA' and 'ri_mg_sub': 0.83
correlation between 'ri_mg_combination_binarized_th=0.5' and 'si_ca_mg_PCA_PCA': 0.75
correlation between 'ri_poly_2' and 'ca_poly_2': 0.72
correlation between 'si_ca_mg_PCA_PCA' and 'si_ca_sub': -0.69
correlation between 'si_ca_inter' and 'ri': 0.68
correlation between 'ri_si_combination' and 'ri': -0.45
correlation between 'ri_poly_2' and 'ri_si_sub': 0.45
correlation between 'ri_poly_2' and 'ri_si_combination': -0.45
correlation between 'ri_mg_combination' and 'ba': 0.44
correlation between 'ri_mg_combination' and 'al': 0.44
correlation between 'ri_mg_sub' and 'al': 0.44
correlation between 'ri_mg_combination' and 'al_min_max_scaled': 0.44
correlation between 'si_ca_inter' and 'ri_mg_sub': 0.42
correlation between 'si_ca_inter' and 'ri_mg_inter': -0.42
correlation between 'si_ca_inter' and 'mg': -0.42
correlation between 'al_power_transformed_yeo-johnson' and 'mg_min_max_scaled': -0.41
correlation between 'al_power_transformed_box-cox' and 'ri_binarized_n=5_enc=ordinal_strat=quantile': -0.41
correlation between 'al_power_transformed_box-cox' and 'mg_binarized_n=5_enc=ordinal_strat=quantile': -0.4
correlation between 'ri_binarized_n=5_enc=ordinal_strat=quantile' and 'al_min_max_scaled': -0.4
correlation between 'ri_binarized_n=5_enc=ordinal_strat=quantile' and 'al': -0.4
correlation between 'ri_mg_sub' and 'ri_ca_inter': 0.4
correlation between 'target' and 'ri_mg_inter': -0.39
correlation between 'target' and 'ri_mg_sub': 0.39
correlation between 'ri_poly_2' and 'al_power_transformed_box-cox': -0.39
correlation between 'al' and 'ri': -0.38
correlation between 'ri_poly_2' and 'al': -0.38
correlation between 'si_ca_PCA' and 'mg_min_max_scaled': -0.38
correlation between 'ri_mg_combination_binarized_th=0.5' and 'al': 0.38
correlation between 'ri_mg_inter' and 'si_ca_PCA': -0.38
correlation between 'ri_binarized_n=5_enc=ordinal_strat=quantile' and 'si': -0.36
correlation between 'ri_mg_combination_binarized_th=0.5' and 'ri_ca_inter': 0.36
correlation between 'target' and 'na_quantiled_n=100_distr=normal': 0.35
correlation between 'target' and 'mg_binarized_n=5_enc=ordinal_strat=quantile': -0.34
correlation between 'ri_ca_sub' and 'mg_binarized_n=5_enc=ordinal_strat=quantile': 0.32

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: 1.94%
Score: 0.4768
Added columns: {'mg_binarized_n=5_enc=ordinal_strat=quantile', 'si_ca_mg_PCA', 'si_poly_2', 'ri_na_inter', 'ri_mg_combination', 'k_quantiled_n=10_distr=uniform', 'al_min_max_scaled', 'ri_ca_sub'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: -3.95%
Score: 0.4580
Added columns: {'mg_min_max_scaled', 'al_power_transformed_yeo-johnson', 'ri_ca_inter', 'ca_poly_2', 'ri_si_sub', 'na_quantiled_n=10_distr=uniform'}
Removed columns: set()
Iteration 3:
Score change relative to previous iteration: 0.24%
Score: 0.4591
Added columns: {'ri_binarized_n=5_enc=ordinal_strat=quantile', 'si_ca_PCA', 'ri_mg_inter', 'al_power_transformed_box-cox', 'fe_min_max_scaled', 'ri_si_combination', 'ri_mg_sub', 'na_quantiled_n=100_distr=uniform'}
Removed columns: {'na_quantiled_n=10_distr=uniform'}
Iteration 4:
Score change relative to previous iteration: -0.05%
Score: 0.4589
Added columns: {'ri_poly_2', 'ri_mg_combination_binarized_th=0.5', 'na_quantiled_n=100_distr=normal', 'si_ca_mg_PCA_PCA', 'si_ca_sub', 'si_ca_inter'}
Removed columns: {'si_ca_mg_PCA'}

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
- You create new features from existing columns to make ML Gaussian Naive Bayes Classifier model better at predicting target variable 'target' in classification problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**