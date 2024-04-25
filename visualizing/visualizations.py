# %%
data = [
    {
        "mean_score": 0.8761437908496731,
        "mean_std": 0.07926369368650263,
        "columns": [
            "alcohol",
            "malic_acid",
            "ash",
            "alcalinity_of_ash",
            "magnesium",
            "total_phenols",
            "flavanoids",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "color_intensity",
            "hue",
            "od280/od315_of_diluted_wines",
            "proline",
            "target",
        ],
    },
    {
        "mean_score": 0.8931372549019606,
        "mean_std": 0.08947387763437538,
        "columns": [
            "alcohol",
            "malic_acid",
            "magnesium",
            "flavanoids",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "hue",
            "od280/od315_of_diluted_wines",
            "proline",
            "alcohol_color_intensity_interaction",
            "alcalinity_of_ash_log",
            "alcalinity_of_ash_binarized_20",
            "flavanoids_nonflavanoid_phenols_linear_combination",
        ],
    },
    {
        "mean_score": 0.9552287581699346,
        "mean_std": 0.041672753624335215,
        "columns": [
            "alcohol",
            "malic_acid",
            "magnesium",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "od280/od315_of_diluted_wines",
            "alcalinity_of_ash_log",
            "alcalinity_of_ash_binarized_20",
            "flavanoids_nonflavanoid_phenols_linear_combination",
            "alcohol_color_intensity_interaction_poly_2",
            "alcohol_color_intensity_interaction_poly_3",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "proline_bin_5_ordinal_quantile",
            "od280/od315_of_diluted_wines_hue_interaction",
        ],
    },
    {
        "mean_score": 0.9493464052287581,
        "mean_std": 0.039004058604679016,
        "columns": [
            "malic_acid",
            "magnesium",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "flavanoids_nonflavanoid_phenols_linear_combination",
            "alcohol_color_intensity_interaction_poly_3",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "proline_bin_5_ordinal_quantile",
            "od280/od315_of_diluted_wines_hue_interaction",
            "alcohol_poly_2",
            "alcohol_poly_3",
            "alcalinity_of_ash_log_quantile_transformed_5_normal",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction",
        ],
    },
    {
        "mean_score": 0.9166666666666666,
        "mean_std": 0.08695819912499181,
        "columns": [
            "malic_acid",
            "magnesium",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "alcohol_poly_3",
            "alcalinity_of_ash_log_quantile_transformed_5_normal",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_poly_2",
            "alcohol_poly_2_poly_3",
            "alcohol_poly_2_normalized_l2",
            "od280/od315_of_diluted_wines_hue_interaction_log",
        ],
    },
    {
        "mean_score": 0.9107843137254902,
        "mean_std": 0.08302261693851917,
        "columns": [
            "malic_acid",
            "magnesium",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "alcalinity_of_ash_log_quantile_transformed_5_normal",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_poly_2",
            "alcohol_poly_2_poly_3",
            "alcohol_poly_2_normalized_l2",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2",
            "alcohol_poly_3_magnesium_subtraction",
        ],
    },
    {
        "mean_score": 0.9107843137254902,
        "mean_std": 0.08302261693851917,
        "columns": [
            "malic_acid",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "alcalinity_of_ash_log_quantile_transformed_5_normal",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_poly_3",
            "alcohol_poly_2_normalized_l2",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2",
            "alcohol_poly_3_magnesium_subtraction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile",
            "magnesium_nonflavanoid_phenols_linear_combination",
        ],
    },
    {
        "mean_score": 0.9052287581699346,
        "mean_std": 0.05561319578086965,
        "columns": [
            "malic_acid",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "alcohol_poly_3_magnesium_subtraction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction",
            "magnesium_nonflavanoid_phenols_linear_combination_binarized_65",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction",
        ],
    },
    {
        "mean_score": 0.9107843137254902,
        "mean_std": 0.05071259477683134,
        "columns": [
            "malic_acid",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile",
            "alcohol_poly_3_magnesium_subtraction_log",
        ],
    },
    {
        "mean_score": 0.9104575163398693,
        "mean_std": 0.0669129118785682,
        "columns": [
            "malic_acid",
            "nonflavanoid_phenols",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile",
            "alcohol_poly_3_magnesium_subtraction_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination",
            "proanthocyanins_log",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction_bin_5_ordinal_quantile",
        ],
    },
    {
        "mean_score": 0.8761437908496731,
        "mean_std": 0.07105044148767231,
        "columns": [
            "nonflavanoid_phenols",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile",
            "alcohol_poly_3_magnesium_subtraction_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination",
            "proanthocyanins_log",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction_bin_5_ordinal_quantile_proanthocyanins_log_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_bin_5_ordinal_quantile",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_interaction",
            "malic_acid_power_transformed_box-cox",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_subtraction",
        ],
    },
    {
        "mean_score": 0.8931372549019608,
        "mean_std": 0.05882443717527601,
        "columns": [
            "nonflavanoid_phenols",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile",
            "alcohol_poly_3_magnesium_subtraction_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination",
            "proanthocyanins_log",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction_bin_5_ordinal_quantile_proanthocyanins_log_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_bin_5_ordinal_quantile",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_subtraction",
            "proanthocyanins_log_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_malic_acid_power_transformed_box-cox_interaction",
        ],
    },
    {
        "mean_score": 0.8941176470588236,
        "mean_std": 0.07200229727540083,
        "columns": [
            "nonflavanoid_phenols",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile",
            "alcohol_poly_3_magnesium_subtraction_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction_bin_5_ordinal_quantile_proanthocyanins_log_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_bin_5_ordinal_quantile",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_subtraction",
            "proanthocyanins_log_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_malic_acid_power_transformed_box-cox_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction_poly_2",
            "proanthocyanins_log_bin_5_ordinal_quantile",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_interaction_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination",
            "alcohol_poly_2_normalized_l2_proanthocyanins_log_subtraction",
        ],
    },
    {
        "mean_score": 0.9107843137254902,
        "mean_std": 0.061695503646811,
        "columns": [
            "nonflavanoid_phenols",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction",
            "alcohol_poly_3_magnesium_subtraction_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction_bin_5_ordinal_quantile_proanthocyanins_log_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_bin_5_ordinal_quantile",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_subtraction",
            "proanthocyanins_log_log",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_malic_acid_power_transformed_box-cox_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction_poly_2",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_interaction_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination",
            "alcohol_poly_2_normalized_l2_proanthocyanins_log_subtraction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_poly_2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination",
        ],
    },
    {
        "mean_score": 0.9055555555555556,
        "mean_std": 0.07049209744694176,
        "columns": [
            "nonflavanoid_phenols",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination",
            "alcohol_poly_2_normalized_l2",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction_bin_5_ordinal_quantile_proanthocyanins_log_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_bin_5_ordinal_quantile",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_subtraction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_malic_acid_power_transformed_box-cox_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction_poly_2",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_interaction_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination",
            "alcohol_poly_2_normalized_l2_proanthocyanins_log_subtraction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_poly_2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction_power_transformed_box-cox",
            "alcohol_poly_3_magnesium_subtraction_log_quantile_transformed_100_normal",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction_nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination_linear_combination",
            "proanthocyanins_log_log_poly_2",
            "proanthocyanins_log_log_poly_3",
            "proanthocyanins_log_log_normalized_l2",
        ],
    },
    {
        "mean_score": 0.8820261437908498,
        "mean_std": 0.05857700702910962,
        "columns": [
            "nonflavanoid_phenols",
            "alcalinity_of_ash_binarized_20_binarized_1.0",
            "alcohol_poly_2_normalized_l2",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_bin_5_ordinal_quantile",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_subtraction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_malic_acid_power_transformed_box-cox_interaction",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_magnesium_nonflavanoid_phenols_linear_combination_interaction_poly_2",
            "alcohol_poly_2_normalized_l2_proanthocyanins_log_subtraction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_magnesium_nonflavanoid_phenols_linear_combination_subtraction_bin_5_ordinal_quantile_poly_2",
            "flavanoids_nonflavanoid_phenols_linear_combination_alcalinity_of_ash_binarized_20_interaction_alcalinity_of_ash_log_quantile_transformed_5_normal_linear_combination_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction_power_transformed_box-cox",
            "alcohol_poly_3_magnesium_subtraction_log_quantile_transformed_100_normal",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_interaction_nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination_linear_combination",
            "proanthocyanins_log_log_poly_3",
            "proanthocyanins_log_log_normalized_l2",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_poly_2",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_poly_3",
            "nonflavanoid_phenols_proline_bin_5_ordinal_quantile_linear_combination_power_transformed_box-cox",
            "alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_interaction_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination_alcohol_color_intensity_interaction_poly_3_magnesium_subtraction_bin_10_ordinal_quantile_quantile_transformed_100_normal_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_interaction_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination_interaction",
            "od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_quantile_transformed_100_normal",
            "alcohol_poly_2_flavanoids_nonflavanoid_phenols_linear_combination_interaction_magnesium_nonflavanoid_phenols_linear_combination_interaction_bin_5_ordinal_quantile_proanthocyanins_log_linear_combination_od280/od315_of_diluted_wines_hue_interaction_log_poly_2_power_transformed_box-cox_malic_acid_linear_combination_linear_combination",
        ],
    },
]

# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from typing import List, Dict


def plot_scores(
    data: List[Dict],
    score_axis_title: str = "10-Fold Cross-Val Accuracy Score [%] With Std Dev",
    path: str = "scores.pdf",
) -> None:
    """
    Function to plot mean_score, mean_std, and num_columns.

    Parameters:
    data (List[Dict]): A list of dictionaries containing 'mean_score', 'mean_std', and 'columns'.

    Returns:
    None
    """
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Create a new column for the number of columns in each data point
    df["num_columns"] = df["columns"].apply(len)

    # Plot the mean_score, mean_std, and num_columns
    fig, ax1 = plt.subplots()

    color = "tab:blue"
    ax1.set_xlabel("Method's Iteration")
    ax1.set_ylabel(score_axis_title, color=color)
    ax1.plot(df.index, df["mean_score"], color=color)
    ax1.fill_between(
        df.index,
        df["mean_score"] - df["mean_std"],
        df["mean_score"] + df["mean_std"],
        color=color,
        alpha=0.2,
    )
    ax1.tick_params(axis="y", labelcolor=color)

    # Add lines for min, max and average of mean_score
    min_score = df["mean_score"].min()
    max_score = df["mean_score"].max()
    avg_score = df["mean_score"].mean()

    min_line = ax1.axhline(min_score, color="red", linestyle="--")
    max_line = ax1.axhline(max_score, color="green", linestyle="--")
    avg_line = ax1.axhline(avg_score, color="purple", linestyle="--")

    # Add text for min, max and average of mean_score
    ax1.text(0, min_score, f"{round(min_score,2)}", color="red", va="bottom", ha="left")
    ax1.text(
        0, max_score, f"{round(max_score,2)}", color="green", va="bottom", ha="left"
    )
    ax1.text(
        0, avg_score, f"{round(avg_score,2)}", color="purple", va="bottom", ha="left"
    )

    # Create custom legend handles
    min_handle = mlines.Line2D([], [], color="red", linestyle="--", label="Min Score")
    max_handle = mlines.Line2D([], [], color="green", linestyle="--", label="Max Score")
    avg_handle = mlines.Line2D(
        [], [], color="purple", linestyle="--", label="Avg Score"
    )

    # Find the index of the max mean_score
    max_score_index = df["mean_score"].idxmax()

    # Add a vertical line at the position of the max mean_score
    ax1.axvline(max_score_index, color="orange", linestyle="--")

    # Create a custom legend handle for the max value line
    max_value_handle = mlines.Line2D(
        [], [], color="orange", linestyle="--", label="Best Iteration"
    )

    # Add the new handle to the legend
    ax1.legend(handles=[min_handle, max_handle, avg_handle, max_value_handle])

    # Create a secondary y-axis for num_columns
    ax2 = ax1.twinx()
    ax2.set_ylabel("Total Number of Columns", color="tab:gray")
    ax2.plot(df.index, df["num_columns"], color="tab:gray", alpha=0.5)
    ax2.tick_params(axis="y", labelcolor="tab:gray")

    fig.tight_layout()
    # Save the plot as pdf file
    plt.savefig(path)
    # plt.show()


# %%
# plot_scores(data)
# %%
