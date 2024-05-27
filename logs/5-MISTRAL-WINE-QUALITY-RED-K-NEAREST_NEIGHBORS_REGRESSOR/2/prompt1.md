**INTRODUCTION:**
Predict the quality of red wine based on physicochemical tests (these columns might not exist, use columns from COLUMNS section):
class (target): This column is the target variable or the label that you want to predict in your dataset. It likely represents different classes or categories.
fixed_acidity: This column represents the amount of non-volatile acids in the wine. It's usually measured in grams per liter.
volatile_acidity: This column represents the amount of volatile acids in the wine, which can contribute to the vinegar-like taste. It's also measured in grams per liter.
citric_acid: This column represents the amount of citric acid in the wine. Citric acid can impart freshness and flavor to the wine. It's measured in grams per liter.
residual_sugar: This column represents the amount of sugar that remains in the wine after fermentation is complete. It's measured in grams per liter.
chlorides: This column represents the amount of salt in the wine. It's measured in grams per liter.
free_sulfur_dioxide: This column represents the amount of free sulfur dioxide in the wine, which acts as a preservative and antimicrobial agent. It's measured in parts per million (ppm).
total_sulfur_dioxide: This column represents the total amount of sulfur dioxide in the wine, including both free and bound forms. It's also measured in parts per million (ppm).
density: This column represents the density of the wine, which is influenced by the concentration of alcohol and sugar. It's usually measured in grams per milliliter.
pH: This column represents the acidity or basicity of the wine on a scale from 0 to 14, with lower values indicating higher acidity.
sulphates: This column represents the amount of sulfur dioxide added to the wine as a preservative. It's measured in grams per liter.
alcohol: This column represents the alcohol content of the wine, usually measured as the percentage of alcohol by volume.

**COLUMNS:**
- *UNIQUE VALUES:*
example unique values in 'fixed_acidity': 7.36, 7.16, 7.56, 6.13, 12.14, 6.55, 11.16, 7.28, 14.21, 8.21 ...
example unique values in 'volatile_acidity': 0.61, 0.7, 0.85, 0.29, 0.8, 0.58, 0.63, 0.65, 0.83, 0.55 ...
example unique values in 'citric_acid': 0.03, 0.22, 0.33, 0.33, 0.2, 0.42, 0.5, 0.05, 0.43, 0.32 ...
example unique values in 'residual_sugar': 3.99, 3.74, 3.41, 1.81, 2.63, 3.95, 16.11, 0.77, 2.04, 1.54 ...
example unique values in 'chlorides': 0.04, 0.09, 0.11, 0.08, 0.04, 0.14, 0.06, 0.08, 0.08, 0.13 ...
example unique values in 'free_sulfur_dioxide': 19.97, 13.85, 10.37, 15.42, 34.79, 17.61, 26.25, 27.69, 9.41, 28.25 ...
example unique values in 'total_sulfur_dioxide': 41.22, 95.03, 3.28, 97.61, 118.05, 22.93, 6.03, 17.33, 69.97, 118.88 ...
example unique values in 'density': 1.0, 1.0, 1.0, 1.0, 1.0, 0.99, 1.0, 0.99, 1.0, 1.0 ...
example unique values in 'ph': 3.23, 3.43, 3.11, 3.11, 3.54, 3.51, 3.32, 3.3, 3.5, 3.38 ...
example unique values in 'sulphates': 0.93, 0.53, 0.46, 0.51, 0.87, 0.45, 0.86, 0.74, 0.55, 0.54 ...
example unique values in 'alcohol': 15.09, 11.98, 9.48, 10.07, 12.85, 9.68, 10.38, 9.53, 10.93, 11.41 ...
example unique values in 'alcohol_min_max_scaled': 0.13, 0.38, 0.32, 0.39, 0.13, 0.21, 0.19, 0.21, 0.71, 0.3 ...
example unique values in 'total_sulfur_dioxide_volatile_acidity_inter': 26.41, 10.01, 61.56, 37.77, 53.14, 8.39, 7.67, 37.79, 13.06, 19.79 ...
example unique values in 'citric_acid_standard_scaled': 0.15, 0.16, -1.4, -0.72, 1.84, -0.01, -0.08, 0.46, 0.21, -0.06 ...
example unique values in 'total_sulfur_dioxide_ph_inter': 262.28, 346.76, 236.72, 254.19, 80.17, 290.05, 31.92, 109.11, 79.6, 86.73 ...
example unique values in 'fixed_acidity_volatile_acidity_citric_acid_residual_sugar_chlorides_free_sulfur_dioxide_total_sulfur_dioxide_density_PCA': -7.11, -37.46, -18.28, -1.95, -27.59, 114.02, 107.61, 13.05, -37.38, -43.28 ...
example unique values in 'total_sulfur_dioxide_fixed_acidity_inter': 606.8, 409.75, 242.15, 632.48, 350.15, 247.55, 145.12, 121.89, 327.52, 32.67 ...
example unique values in 'fixed_acidity_volatile_acidity_combination': 8.57, 9.08, 7.98, 10.64, 8.1, 9.96, 8.96, 14.68, 9.0, 7.4 ...
all unique values in 'target': 2.1, 2.39, 1.69, 2.61, 1.0, 2.79
- *CORRELATIONS:*
correlation between 'fixed_acidity_volatile_acidity_citric_acid_residual_sugar_chlorides_free_sulfur_dioxide_total_sulfur_dioxide_density_PCA' and 'total_sulfur_dioxide': 1.0
correlation between 'alcohol_min_max_scaled' and 'alcohol': 1.0
correlation between 'total_sulfur_dioxide_ph_inter' and 'total_sulfur_dioxide': 1.0
correlation between 'fixed_acidity_volatile_acidity_citric_acid_residual_sugar_chlorides_free_sulfur_dioxide_total_sulfur_dioxide_density_PCA' and 'total_sulfur_dioxide_ph_inter': 1.0
correlation between 'citric_acid_standard_scaled' and 'citric_acid': 1.0
correlation between 'fixed_acidity_volatile_acidity_combination' and 'fixed_acidity': 0.99
correlation between 'total_sulfur_dioxide_fixed_acidity_inter' and 'total_sulfur_dioxide': 0.95
correlation between 'total_sulfur_dioxide_fixed_acidity_inter' and 'fixed_acidity_volatile_acidity_citric_acid_residual_sugar_chlorides_free_sulfur_dioxide_total_sulfur_dioxide_density_PCA': 0.95
correlation between 'total_sulfur_dioxide_fixed_acidity_inter' and 'total_sulfur_dioxide_ph_inter': 0.94
correlation between 'total_sulfur_dioxide_ph_inter' and 'total_sulfur_dioxide_volatile_acidity_inter': 0.88
correlation between 'total_sulfur_dioxide_volatile_acidity_inter' and 'total_sulfur_dioxide': 0.88
correlation between 'fixed_acidity_volatile_acidity_citric_acid_residual_sugar_chlorides_free_sulfur_dioxide_total_sulfur_dioxide_density_PCA' and 'total_sulfur_dioxide_volatile_acidity_inter': 0.87
correlation between 'total_sulfur_dioxide_fixed_acidity_inter' and 'total_sulfur_dioxide_volatile_acidity_inter': 0.83
correlation between 'fixed_acidity_volatile_acidity_citric_acid_residual_sugar_chlorides_free_sulfur_dioxide_total_sulfur_dioxide_density_PCA' and 'free_sulfur_dioxide': 0.63
correlation between 'total_sulfur_dioxide' and 'free_sulfur_dioxide': 0.6
correlation between 'total_sulfur_dioxide_ph_inter' and 'free_sulfur_dioxide': 0.6
correlation between 'citric_acid_standard_scaled' and 'fixed_acidity': 0.59
correlation between 'citric_acid' and 'fixed_acidity': 0.59
correlation between 'fixed_acidity_volatile_acidity_combination' and 'density': 0.58
correlation between 'ph' and 'fixed_acidity': -0.58
correlation between 'fixed_acidity_volatile_acidity_combination' and 'ph': -0.57
correlation between 'density' and 'fixed_acidity': 0.57
correlation between 'total_sulfur_dioxide_fixed_acidity_inter' and 'free_sulfur_dioxide': 0.56
correlation between 'fixed_acidity_volatile_acidity_combination' and 'citric_acid_standard_scaled': 0.54
correlation between 'fixed_acidity_volatile_acidity_combination' and 'citric_acid': 0.54
correlation between 'citric_acid' and 'volatile_acidity': -0.5
correlation between 'citric_acid_standard_scaled' and 'volatile_acidity': -0.5
correlation between 'alcohol_min_max_scaled' and 'density': -0.49
correlation between 'alcohol' and 'density': -0.49
correlation between 'total_sulfur_dioxide_volatile_acidity_inter' and 'free_sulfur_dioxide': 0.48
correlation between 'citric_acid_standard_scaled' and 'ph': -0.45
correlation between 'ph' and 'citric_acid': -0.45
correlation between 'total_sulfur_dioxide_volatile_acidity_inter' and 'volatile_acidity': 0.45
correlation between 'target' and 'alcohol': 0.44
correlation between 'target' and 'alcohol_min_max_scaled': 0.44
correlation between 'target' and 'volatile_acidity': -0.35
correlation between 'citric_acid_standard_scaled' and 'density': 0.31
correlation between 'density' and 'citric_acid': 0.31
correlation between 'density' and 'residual_sugar': 0.31

**ITERATION HISTORY:**
Iteration 1:
Error change relative to previous iteration: 12.17%
Error: 0.0995
Added columns: {'fixed_acidity_volatile_acidity_combination', 'fixed_acidity_volatile_acidity_citric_acid_residual_sugar_chlorides_free_sulfur_dioxide_total_sulfur_dioxide_density_PCA', 'total_sulfur_dioxide_volatile_acidity_inter', 'total_sulfur_dioxide_ph_inter', 'alcohol_min_max_scaled', 'total_sulfur_dioxide_fixed_acidity_inter', 'citric_acid_standard_scaled'}
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