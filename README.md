# Automated Feature Engineering And Selection Using Language Model

<div style="text-align: center;">
    <img src="logo.jpg" alt="logo" width="350"/>
</div>

## Abstract

The aim of the study was to create an efficient tool for automated feature engineering and selection for tabular-numeric data, using a small-local open-source language model. Tests were performed on the **Mistral-7B-Instruct-v0.2** model, with a quantization method of **Q5_K_M**, whose size is **5.13 GB**. The results were calculated using the **RTX 2070 Super** graphics card.

## Methodology

The context for the language model is generated automatically, with an optional manual description of the dataset whose feature set is to be changed. The context includes:

- A random sample of column values
- Relevant feature correlations
- An iteration history with results and added/removed attributes
- A set of tools that the model can use, along with acceptable argument values
- Rules of conduct for the model describing its task and approach to solving the problem

In response, the model reasons and indicates what new attributes are worth creating with the tools. This response is turned into a JSON file that conforms to the defined schema, using one of the **JSON Schema Mode** type algorithms, ensuring a correct interface with the model. The transformations are then performed, altering the original set.

## Experiments

The result is measured for a given combination of dataset and classical machine learning model, e.g., **AutoPrice** and **kNN**. The classical model has selected hyperparameters and is then validated using cross-validation, with the result being the average of the splits.

Experiments were performed for:

- **6 sets and 2 models for regression.**
- **7 sets and 2 models for classification.**

This made a total of **26 experiments**. For regression, the **Mean Absolute Percentage Error** (MAPE) was measured, and for classification, the **Accuracy Score** was measured.

## Results

- In up to **58% of the experiments**, the method improved the results.
- The average improvement, in the experiments in which it occurred, was around **2.84%**.

<div style="text-align: center;">
    <img src="8-Abalone-Ridge Regression_scores-1.png" alt="logo" width="500"/>
    <img src="8-Abalone-Ridge Regression_columns-1.png" alt="logo" width="500"/>
</div>

| Experiment |           Dataset           |         ML Model         | Best Iter. | Best Metric [%] | Metric w/o FE [%] | Metric Imp. [%] |
| :--------: | :-------------------------: | :----------------------: | :--------: | :-------------: | :---------------: | :-------------: |
|     8     |           abalone           |     Ridge Regression     |     5     |      48.65      |       53.31       |      -8.74      |
|     7     |        forest_fires        |      K-NN Regressor      |     5     |      89.1      |       94.71       |      -5.92      |
|     14     |            glass            | Decision Tree Classifier |     1     |      57.06      |       54.61       |      4.48      |
|     4     |      wine-quality-red      |     Ridge Regression     |     1     |      6.98      |        7.3        |      -4.43      |
|     0     |          autoPrice          |     Ridge Regression     |     1     |      1.47      |       1.52       |      -3.72      |
|     21     |            adult            |      GNB Classifier      |     5     |      78.3      |       76.1       |      2.89      |
|     23     |          mushroom          |      GNB Classifier      |     5     |      99.5      |       97.2       |      2.37      |
|     19     |          credit-g          |      GNB Classifier      |     1     |      74.8      |       73.1       |      2.33      |
|     2     |     Bike_Sharing_Demand     |     Ridge Regression     |     5     |      17.97      |       18.32       |      -1.96      |
|     15     |            glass            |      GNB Classifier      |     1     |      47.68      |       46.77       |      1.94      |
|     16     |            iris            | Decision Tree Classifier |     2     |      97.33      |       96.0       |      1.39      |
|     6     |        forest_fires        |     Ridge Regression     |     4     |      76.77      |       77.52       |      -0.96      |
|     17     |            iris            |      GNB Classifier      |     1     |      96.0      |       95.33       |       0.7       |
|     13     |           titanic           |      GNB Classifier      |     1     |      78.3      |       77.8       |      0.64      |
|     9     |           abalone           |      K-NN Regressor      |     4     |      54.35      |       54.45       |      -0.18      |
|     1     |          autoPrice          |      K-NN Regressor      |     0     |       2.2       |        2.2        |       0.0       |
|     12     |           titanic           | Decision Tree Classifier |     0     |      79.9      |       79.9       |       0.0       |
|     11     | UCI-student-performance-mat |      K-NN Regressor      |     0     |      20.96      |       20.96       |       0.0       |
|     10     | UCI-student-performance-mat |     Ridge Regression     |     0     |      20.92      |       20.92       |       0.0       |
|     18     |          credit-g          | Decision Tree Classifier |     0     |      71.2      |       71.2       |       0.0       |
|     20     |            adult            | Decision Tree Classifier |     0     |      85.4      |       85.4       |       0.0       |
|     5     |      wine-quality-red      |      K-NN Regressor      |     0     |      8.87      |       8.87       |       0.0       |
|     22     |          mushroom          | Decision Tree Classifier |     0     |      99.6      |       99.6       |       0.0       |
|     3     |     Bike_Sharing_Demand     |      K-NN Regressor      |     0     |      21.25      |       21.25       |       0.0       |
|     24     |           letter           | Decision Tree Classifier |     0     |      45.8      |       45.8       |       0.0       |
|     25     |           letter           |      GNB Classifier      |     0     |      56.9      |       56.9       |       0.0       |

### Notable Gains

- **Regression:** The largest gain was for the combination of the **Abalone** set and the **Ridge Regression** model, where the error fell by more than **8.7%** relative to no feature engineering, just by using the method.
- **Classification:** The combination of the **Glass** set and the **Decision Tree Classifier** model had a nearly **4.5%** higher accuracy score, thanks to the method.

## Comparison

The results were also compared with the **featurewiz** library and **CAAFE** paper.

## Keywords

Automated Feature Engineering, Feature Selection, Optimization, LLM, Open-Source, Mistral 7B, Tabular-Numeric Data
