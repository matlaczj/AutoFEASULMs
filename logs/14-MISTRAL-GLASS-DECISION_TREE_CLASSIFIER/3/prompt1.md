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
example unique values in 'ri_poly_2': 2.28, 2.32, 2.32, 2.34, 2.29, 2.3, 2.3, 2.31, 2.3, 2.3 ...
example unique values in 'mg_al_combination': 1.02, 2.77, 4.91, 5.01, 4.66, 1.9, 4.18, 2.11, 4.38, 2.98 ...
example unique values in 'mg_power_transformed_yeo-johnson': -1.73, 0.51, -0.01, -1.73, -1.77, -1.73, 0.34, 0.09, 1.26, 0.37 ...
example unique values in 'fe_abs': 0.01, 0.02, 0.0, 0.11, 0.05, 0.05, 0.06, 0.11, 0.05, 0.02 ...
example unique values in 'ri_si_PCA': -0.42, -0.58, 0.06, -0.42, 0.69, -0.44, -0.35, -1.07, -0.14, -0.03 ...
example unique values in 'ca_quantiled_n=100_distr=normal': -1.51, -0.98, -0.03, 0.21, -0.32, -1.14, -1.74, 1.31, 0.74, -1.9 ...
example unique values in 'ri_al_inter': 2.15, 1.35, 3.0, 3.35, 2.14, 2.33, 2.39, 2.37, 1.41, 3.05 ...
example unique values in 'na_poly_2': 163.89, 169.16, 171.57, 193.32, 193.67, 172.24, 171.95, 177.57, 167.18, 173.35 ...
example unique values in 'ri_power_transformed_yeo-johnson': -0.0, 0.0, -0.0, 0.0, 0.0, 0.0, -0.0, -0.0, -0.0, -0.0 ...
example unique values in 'mg_al_sub': 1.9, 1.5, 2.98, 2.54, -1.73, 1.87, -1.84, 1.6, 1.86, 2.46 ...
example unique values in 'si_ca_sub_quantiled_n=100_distr=uniform': 0.08, 0.61, 0.73, 0.2, 0.39, 0.36, 0.18, 0.6, 0.22, 0.9 ...
all unique values in 'fe_binarized_n=5_enc=ordinal_strat=quantile': 3.0, 0.0, 4.0, 1.0, 2.0
example unique values in 'ri_mg_combination': 2.47, 2.46, 2.5, 2.53, 2.28, 2.4, 2.62, 0.75, 1.6, 0.64 ...
example unique values in 'ca_min_max_scaled': 0.31, 0.46, 0.22, 0.35, 0.05, 0.46, 0.36, 0.29, 0.28, 0.24 ...
example unique values in 'ri_mg_inter': 4.81, 5.87, 5.66, 5.51, 5.1, 5.61, 1.59, -0.33, 5.31, 2.52 ...
example unique values in 'si_ca_sub_mg_power_transformed_yeo-johnson_PCA': -1.16, 0.16, 0.27, -0.23, -1.57, 1.35, 1.5, -0.51, -0.86, -0.09 ...
all unique values in 'target': 0, 5, 4, 1, 3, 2
- *CORRELATIONS:*
correlation between 'ca_min_max_scaled' and 'ca': 1.0
correlation between 'ri_power_transformed_yeo-johnson' and 'ri_poly_2': 1.0
correlation between 'ri_mg_inter' and 'ri_mg_combination': 1.0
correlation between 'ri_power_transformed_yeo-johnson' and 'ri': 1.0
correlation between 'mg_power_transformed_yeo-johnson' and 'mg': 0.99
correlation between 'ri_mg_combination' and 'mg_power_transformed_yeo-johnson': 0.99
correlation between 'mg_al_sub' and 'mg': 0.96
correlation between 'ri_mg_combination' and 'mg_al_sub': 0.96
correlation between 'ri_mg_inter' and 'mg_al_combination': 0.94
correlation between 'mg_al_combination' and 'mg': 0.94
correlation between 'si_ca_sub_mg_power_transformed_yeo-johnson_PCA' and 'ca_min_max_scaled': 0.91
correlation between 'si_ca_sub_mg_power_transformed_yeo-johnson_PCA' and 'si_ca_sub_quantiled_n=100_distr=uniform': -0.87
correlation between 'si_ca_sub_mg_power_transformed_yeo-johnson_PCA' and 'ri_poly_2': 0.77
correlation between 'ca_min_max_scaled' and 'si_ca_sub_quantiled_n=100_distr=uniform': -0.77
correlation between 'si_ca_sub_mg_power_transformed_yeo-johnson_PCA' and 'ri': 0.77
correlation between 'ca_min_max_scaled' and 'ri_poly_2': 0.71
correlation between 'ri_power_transformed_yeo-johnson' and 'ca': 0.7
correlation between 'si_ca_sub_quantiled_n=100_distr=uniform' and 'ri': -0.61
correlation between 'si_ca_sub_quantiled_n=100_distr=uniform' and 'ri_si_PCA': -0.57
correlation between 'mg_al_combination' and 'ca': -0.54
correlation between 'ca_min_max_scaled' and 'mg_al_combination': -0.54
correlation between 'mg_al_sub' and 'ba': -0.49
correlation between 'ri_al_inter' and 'mg_power_transformed_yeo-johnson': -0.45
correlation between 'mg_power_transformed_yeo-johnson' and 'al': -0.45
correlation between 'ri_si_PCA' and 'ri': 0.45
correlation between 'ca_quantiled_n=100_distr=normal' and 'mg_al_combination': -0.44
correlation between 'ri_mg_inter' and 'ri_al_inter': -0.44
correlation between 'ri_mg_inter' and 'al': -0.44
correlation between 'ri_power_transformed_yeo-johnson' and 'ri_si_PCA': 0.44
correlation between 'ri_mg_combination' and 'ri_al_inter': -0.44
correlation between 'ri_mg_combination' and 'al': -0.44
correlation between 'mg_power_transformed_yeo-johnson' and 'ba': -0.43
correlation between 'ri_al_inter' and 'ba': 0.42
correlation between 'ca' and 'mg': -0.41
correlation between 'target' and 'mg_al_sub': -0.4
correlation between 'ca_min_max_scaled' and 'mg_power_transformed_yeo-johnson': -0.4
correlation between 'target' and 'mg_power_transformed_yeo-johnson': -0.4
correlation between 'ca_min_max_scaled' and 'ri_mg_combination': -0.4
correlation between 'ri_mg_combination' and 'ca': -0.4
correlation between 'target' and 'ri_mg_combination': -0.39
correlation between 'target' and 'mg': -0.39
correlation between 'ri_poly_2' and 'al': -0.38
correlation between 'al' and 'ri': -0.38
correlation between 'ri_al_inter' and 'ri_poly_2': -0.38
correlation between 'target' and 'na': 0.36
correlation between 'target' and 'mg_al_combination': -0.34
correlation between 'ba' and 'na': 0.33
correlation between 'mg_al_combination' and 'ba': -0.33
correlation between 'ca_quantiled_n=100_distr=normal' and 'k': -0.32
correlation between 'ri_mg_combination' and 'ca_quantiled_n=100_distr=normal': -0.31

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: 4.48%
Score: 0.5706
Added columns: {'ri_poly_2', 'ri_si_PCA', 'ca_quantiled_n=100_distr=normal', 'si_ca_sub', 'fe_abs', 'mg_power_transformed_yeo-johnson', 'mg_al_combination', 'ri_al_inter'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: -0.83%
Score: 0.5658
Added columns: {'ri_mg_inter', 'fe_binarized_n=5_enc=ordinal_strat=quantile', 'si_ca_sub_mg_power_transformed_yeo-johnson_PCA', 'ca_min_max_scaled', 'mg_al_sub', 'si_ca_sub_quantiled_n=100_distr=uniform', 'ri_mg_combination', 'na_poly_2', 'ri_power_transformed_yeo-johnson'}
Removed columns: {'si_ca_sub'}

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
- You create new features from existing columns to make ML Decision Tree Classifier model better at predicting target variable 'target' in classification problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**