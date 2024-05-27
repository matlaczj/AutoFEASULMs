**INTRODUCTION:**
Predict whether a mushroom is edible or poisonous based on features (these columns might not exist, use columns from COLUMNS section):
class (target): This column is the target variable or label that you want to predict. It's a nominal variable with two distinct values, likely representing different classes or categories.
cap_shape: This column represents the shape of the mushroom cap. It's a nominal variable with 6 distinct values.
cap_surface: This column represents the surface texture of the mushroom cap. It's a nominal variable with 4 distinct values.
cap_color: This column represents the color of the mushroom cap. It's a nominal variable with 10 distinct values.
bruises: This column indicates whether the mushroom has bruises or not. It's a nominal variable with 2 distinct values.
odor: This column represents the odor of the mushroom. It's a nominal variable with 9 distinct values.
gill_attachment: This column represents how the gills are attached to the stem. It's a nominal variable with 2 distinct values.
gill_spacing: This column represents the spacing between gills. It's a nominal variable with 2 distinct values.
gill_size: This column represents the size of the gills. It's a nominal variable with 2 distinct values.
gill_color: This column represents the color of the gills. It's a nominal variable with 12 distinct values.
stalk_shape: This column represents the shape of the stalk. It's a nominal variable with 2 distinct values.
stalk_root: This column represents the root of the stalk. It's a nominal variable with 5 distinct values.
stalk_surface_above_ring: This column represents the surface texture of the stalk above the ring. It's a nominal variable with 4 distinct values.
stalk_surface_below_ring: This column represents the surface texture of the stalk below the ring. It's a nominal variable with 4 distinct values.
stalk_color_above_ring: This column represents the color of the stalk above the ring. It's a nominal variable with 9 distinct values.
stalk_color_below_ring: This column represents the color of the stalk below the ring. It's a nominal variable with 9 distinct values.
veil_type: This column represents the type of veil covering the gills. It's a nominal variable with 1 distinct value.
veil_color: This column represents the color of the veil. It's a nominal variable with 4 distinct values.
ring_number: This column represents the number of rings on the stalk. It's a nominal variable with 3 distinct values.
ring_type: This column represents the type of ring on the stalk. It's a nominal variable with 5 distinct values.
spore-print-color: This column represents the color of the mushroom spore print. It's a nominal variable with 9 distinct values.
population: This column represents the population density of the mushroom. It's a nominal variable with 6 distinct values.
habitat: This column represents the habitat where the mushroom is typically found. It's a nominal variable with 7 distinct values.

**COLUMNS:**
- *UNIQUE VALUES:*
all unique values in 'cap-shape_b': 0, 1
all unique values in 'cap-shape_c': 0, 1
all unique values in 'cap-shape_f': 0, 1
all unique values in 'cap-shape_k': 0, 1
all unique values in 'cap-shape_s': 0, 1
all unique values in 'cap-shape_x': 1, 0
all unique values in 'cap-surface_f': 1, 0
all unique values in 'cap-surface_g': 0
all unique values in 'cap-surface_s': 0, 1
all unique values in 'cap-surface_y': 0, 1
all unique values in 'cap-color_b': 0, 1
all unique values in 'cap-color_c': 0, 1
all unique values in 'cap-color_e': 0, 1
all unique values in 'cap-color_g': 1, 0
all unique values in 'cap-color_n': 0, 1
all unique values in 'cap-color_p': 0, 1
all unique values in 'cap-color_r': 0, 1
all unique values in 'cap-color_u': 0, 1
all unique values in 'cap-color_w': 0, 1
all unique values in 'cap-color_y': 0, 1
all unique values in 'bruises%3f_f': 1, 0
all unique values in 'bruises%3f_t': 0, 1
all unique values in 'odor_a': 0, 1
all unique values in 'odor_c': 1, 0
all unique values in 'odor_f': 0, 1
all unique values in 'odor_l': 0, 1
all unique values in 'odor_m': 0, 1
all unique values in 'odor_n': 0, 1
all unique values in 'odor_p': 0, 1
all unique values in 'odor_s': 0, 1
all unique values in 'odor_y': 0, 1
all unique values in 'gill-attachment_a': 0, 1
all unique values in 'gill-attachment_f': 1, 0
all unique values in 'gill-spacing_c': 1, 0
all unique values in 'gill-spacing_w': 0, 1
all unique values in 'gill-size_b': 0, 1
all unique values in 'gill-size_n': 1, 0
all unique values in 'stalk-shape_e': 1, 0
all unique values in 'stalk-shape_t': 0, 1
all unique values in 'stalk-root_b': 1, 0
all unique values in 'stalk-root_c': 0, 1
all unique values in 'stalk-root_e': 0, 1
all unique values in 'stalk-root_r': 0, 1
all unique values in 'stalk-surface-above-ring_f': 0, 1
all unique values in 'stalk-surface-above-ring_k': 0, 1
all unique values in 'stalk-surface-above-ring_s': 1, 0
all unique values in 'stalk-surface-above-ring_y': 0, 1
all unique values in 'stalk-surface-below-ring_f': 0, 1
all unique values in 'stalk-surface-below-ring_k': 0, 1
all unique values in 'stalk-surface-below-ring_s': 1, 0
all unique values in 'stalk-surface-below-ring_y': 0, 1
all unique values in 'stalk-color-above-ring_b': 0, 1
all unique values in 'stalk-color-above-ring_c': 0, 1
all unique values in 'stalk-color-above-ring_e': 0, 1
all unique values in 'stalk-color-above-ring_g': 0, 1
all unique values in 'stalk-color-above-ring_n': 0, 1
all unique values in 'stalk-color-above-ring_o': 0, 1
all unique values in 'stalk-color-above-ring_p': 0, 1
all unique values in 'stalk-color-above-ring_w': 1, 0
all unique values in 'stalk-color-above-ring_y': 0, 1
all unique values in 'stalk-color-below-ring_b': 0, 1
all unique values in 'stalk-color-below-ring_c': 0, 1
all unique values in 'stalk-color-below-ring_e': 0, 1
all unique values in 'stalk-color-below-ring_g': 0, 1
all unique values in 'stalk-color-below-ring_n': 0, 1
all unique values in 'stalk-color-below-ring_o': 0, 1
all unique values in 'stalk-color-below-ring_p': 0, 1
all unique values in 'stalk-color-below-ring_w': 1, 0
all unique values in 'stalk-color-below-ring_y': 0, 1
all unique values in 'veil-type_p': 1
all unique values in 'veil-color_n': 0, 1
all unique values in 'veil-color_o': 0, 1
all unique values in 'veil-color_w': 1, 0
all unique values in 'veil-color_y': 0, 1
all unique values in 'ring-number_n': 0, 1
all unique values in 'ring-number_o': 1, 0
all unique values in 'ring-number_t': 0, 1
all unique values in 'ring-type_e': 0, 1
all unique values in 'ring-type_f': 0, 1
all unique values in 'ring-type_l': 0, 1
all unique values in 'ring-type_n': 0, 1
all unique values in 'ring-type_p': 1, 0
all unique values in 'spore-print-color_b': 0, 1
all unique values in 'spore-print-color_h': 0, 1
all unique values in 'spore-print-color_k': 0, 1
all unique values in 'spore-print-color_n': 1, 0
all unique values in 'spore-print-color_o': 0, 1
all unique values in 'spore-print-color_r': 0, 1
all unique values in 'spore-print-color_u': 0, 1
all unique values in 'spore-print-color_w': 0, 1
all unique values in 'spore-print-color_y': 0, 1
all unique values in 'population_a': 0, 1
all unique values in 'population_c': 0, 1
all unique values in 'population_n': 0, 1
all unique values in 'population_s': 0, 1
all unique values in 'population_v': 1, 0
all unique values in 'population_y': 0, 1
all unique values in 'habitat_d': 1, 0
all unique values in 'habitat_g': 0, 1
all unique values in 'habitat_l': 0, 1
all unique values in 'habitat_m': 0, 1
all unique values in 'habitat_p': 0, 1
all unique values in 'habitat_u': 0, 1
all unique values in 'habitat_w': 0, 1
all unique values in 'stalk-color-below-ring_p_stalk-color-above-ring_p_sub': 0, 1, 255
all unique values in 'cap-shape_k_population_c_combination': 0.0, 0.5, 1.0
all unique values in 'veil-color_w_log': 0.0, -20.72
all unique values in 'stalk-surface-above-ring_k_stalk-surface-below-ring_s_sub': 255, 0, 1
all unique values in 'bruises%3f_f_power_transformed_yeo-johnson': 0.83, -1.21
all unique values in 'gill-attachment_f_gill-spacing_w_combination': 0.6, 1.0, 0.0
all unique values in 'population_a_log': -20.72, 0.0
all unique values in 'cap-shape_x_gill-attachment_f_inter': 1, 0
all unique values in 'bruises%3f_f_log': 0.0, -20.72
all unique values in 'veil-type_p_veil-color_n_habitat_d_PCA': 0.63, -0.37, 0.63, 0.63, -0.38
all unique values in 'ring-number_o_log': 0.0, -20.72
all unique values in 'stalk-root_c_population_v_combination': -0.5, 0.0, 0.5
all unique values in 'stalk-color-below-ring_w_cap-color_r_sub': 1, 0
all unique values in 'odor_n_power_transformed_yeo-johnson': -0.84, 1.19
all unique values in 'stalk-surface-above-ring_f_stalk-surface-below-ring_s_sub': 255, 0, 1
all unique values in 'gill-attachment_a_PCA': -0.02, -0.02, 0.98
all unique values in 'cap-shape_k_cap-surface_s_combination': 0.0, 0.2, 0.8, 1.0
all unique values in 'gill-spacing_w_quantiled_n=100_distr=normal': -5.2, 5.2
all unique values in 'target': 1, 0
- *CORRELATIONS:*
correlation between 'ring-number_o_log' and 'ring-number_o': 1.0
correlation between 'gill-size_n' and 'gill-size_b': -1.0
correlation between 'veil-color_y' and 'stalk-color-above-ring_y': 1.0
correlation between 'spore-print-color_h' and 'ring-type_l': 0.86
correlation between 'stalk-surface-above-ring_f_stalk-surface-below-ring_s_sub' and 'stalk-surface-above-ring_k_stalk-surface-below-ring_s_sub': 0.79
correlation between 'gill-attachment_a_PCA' and 'veil-color_o': 0.72
correlation between 'stalk-surface-above-ring_k_stalk-surface-below-ring_s_sub' and 'stalk-surface-below-ring_k': -0.7
correlation between 'ring-type_l' and 'stalk-surface-below-ring_k': 0.69
correlation between 'spore-print-color_o' and 'stalk-color-above-ring_o': 0.66
correlation between 'spore-print-color_w' and 'gill-size_b': -0.64
correlation between 'stalk-surface-above-ring_f_stalk-surface-below-ring_s_sub' and 'spore-print-color_h': -0.54
correlation between 'stalk-surface-below-ring_k' and 'bruises%3f_f': 0.53
correlation between 'ring-type_p' and 'stalk-surface-below-ring_k': -0.5
correlation between 'stalk-color-below-ring_w_cap-color_r_sub' and 'ring-type_l': -0.5
correlation between 'stalk-color-below-ring_w' and 'stalk-color-above-ring_w': 0.5
correlation between 'population_v' and 'stalk-root_b': 0.46
correlation between 'target' and 'ring-type_l': 0.44
correlation between 'stalk-color-above-ring_w' and 'stalk-surface-above-ring_k': -0.43
correlation between 'odor_n_power_transformed_yeo-johnson' and 'gill-size_b': 0.42
correlation between 'population_v' and 'population_s': -0.42
correlation between 'population_c' and 'gill-attachment_f': -0.42
correlation between 'odor_n_power_transformed_yeo-johnson' and 'gill-size_n': -0.42
correlation between 'spore-print-color_w' and 'odor_y': 0.41
correlation between 'gill-attachment_f_gill-spacing_w_combination' and 'stalk-surface-above-ring_f': 0.4
correlation between 'cap-shape_k_population_c_combination' and 'stalk-color-above-ring_e': 0.4
correlation between 'stalk-root_b' and 'cap-color_w': -0.39
correlation between 'habitat_l' and 'ring-type_e': 0.37
correlation between 'stalk-color-above-ring_n' and 'stalk-surface-below-ring_k': 0.37
correlation between 'odor_n_power_transformed_yeo-johnson' and 'gill-spacing_w': 0.37
correlation between 'gill-attachment_f_gill-spacing_w_combination' and 'stalk-color-below-ring_w': 0.37
correlation between 'target' and 'gill-spacing_w': -0.36
correlation between 'target' and 'stalk-surface-above-ring_f_stalk-surface-below-ring_s_sub': -0.36
correlation between 'gill-spacing_w_quantiled_n=100_distr=normal' and 'stalk-color-below-ring_w': 0.35
correlation between 'stalk-color-below-ring_w_cap-color_r_sub' and 'cap-color_w': 0.35
correlation between 'gill-spacing_w_quantiled_n=100_distr=normal' and 'cap-color_w': 0.34
correlation between 'spore-print-color_n' and 'odor_f': -0.34
correlation between 'gill-attachment_a_PCA' and 'spore-print-color_b': 0.34
correlation between 'stalk-color-below-ring_c' and 'cap-color_c': 0.33
correlation between 'habitat_g' and 'cap-color_w': 0.33
correlation between 'stalk-surface-below-ring_f' and 'stalk-surface-above-ring_f': 0.33
correlation between 'stalk-color-above-ring_b' and 'cap-color_y': 0.33
correlation between 'odor_m' and 'cap-color_c': 0.33
correlation between 'ring-type_n' and 'cap-color_c': 0.33
correlation between 'cap-shape_x' and 'cap-shape_k': -0.32
correlation between 'stalk-color-below-ring_g' and 'bruises%3f_f': -0.32
correlation between 'ring-number_o_log' and 'odor_n': -0.32
correlation between 'gill-attachment_f_gill-spacing_w_combination' and 'cap-color_w': 0.32
correlation between 'spore-print-color_n' and 'stalk-surface-above-ring_s': 0.31
correlation between 'population_v' and 'stalk-color-below-ring_p': 0.3
correlation between 'stalk-color-above-ring_p' and 'stalk-root_b': 0.3

**ITERATION HISTORY:**
Iteration 1:
Score change relative to previous iteration: 1.54%
Score: 0.9870
Added columns: {'stalk-color-below-ring_p_stalk-color-above-ring_p_sub', 'gill-attachment_f_gill-spacing_w_gill-size_b_stalk-root_r_PCA', 'cap-shape_k_population_c_combination', 'veil-color_w_log'}
Removed columns: set()
Iteration 2:
Score change relative to previous iteration: -0.81%
Score: 0.9790
Added columns: {'gill-attachment_f_gill-spacing_w_combination', 'population_a_log', 'bruises%3f_f_power_transformed_yeo-johnson', 'stalk-surface-above-ring_k_stalk-surface-below-ring_s_sub'}
Removed columns: set()
Iteration 3:
Score change relative to previous iteration: 1.12%
Score: 0.9900
Added columns: {'cap-shape_x_gill-attachment_f_inter', 'stalk-root_c_population_v_combination', 'ring-number_o_log', 'stalk-color-below-ring_w_cap-color_r_sub', 'veil-type_p_veil-color_n_habitat_d_PCA', 'odor_n_power_transformed_yeo-johnson', 'bruises%3f_f_log'}
Removed columns: {'gill-attachment_f_gill-spacing_w_gill-size_b_stalk-root_r_PCA'}
Iteration 4:
Score change relative to previous iteration: 0.10%
Score: 0.9910
Added columns: {'stalk-surface-above-ring_f_stalk-surface-below-ring_s_sub', 'cap-shape_k_cap-surface_s_combination', 'gill-spacing_w_quantiled_n=100_distr=normal', 'gill-attachment_a_PCA'}
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
- You create new features from existing columns to make ML Gaussian Naive Bayes Classifier model better at predicting target variable 'target' in classification problem.
- Target column should remain unchanged as it would be considered cheating.
- Every iteration you suggest 10 new column-tool combinations.
- You don't write code. Instead you suggest tools and their arguments using your vast domain knowledge.
- You create columns that are highly correlated with target feature.
- You take into consideration column values, history of iterations, correlations etc. to make better judgements.
- You don't repeat the same mistake twice expecting different results.

**CURRENT ITERATION:**