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
all unique values in 'target': 0, 5, 4, 1, 3, 2
- *CORRELATIONS:*
correlation between 'ca' and 'ri': 0.71
correlation between 'si' and 'ri': -0.45
correlation between 'ba' and 'mg': -0.44
correlation between 'al' and 'mg': -0.44
correlation between 'ba' and 'al': 0.41
correlation between 'ca' and 'mg': -0.41
correlation between 'target' and 'mg': -0.39
correlation between 'al' and 'ri': -0.38
correlation between 'target' and 'na': 0.36
correlation between 'ba' and 'na': 0.33

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