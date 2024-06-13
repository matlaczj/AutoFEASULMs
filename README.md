# Automated Feature Engineering And Selection Using Language Model

<img src="logo.jpg" alt="logo" width="350" style="display: block; margin-left: auto; margin-right: auto; border-radius: 20px;"/>


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

- **6 sets and 2 models for regression**
- **7 sets and 2 models for classification**

This made a total of **26 experiments**. For regression, the **Mean Absolute Percentage Error** (MAPE) was measured, and for classification, the **Accuracy Score** was measured.

## Results

- In up to**58% of the experiments**, the method improved the results.
- The average improvement, in the experiments in which it occurred, was around**2.84%**.

### Notable Gains

- **Regression:** The largest gain was for the combination of the**Abalone** set and the**Ridge Regression** model, where the error fell by more than**8.7%** relative to no feature engineering, just by using the method.
- **Classification:** The combination of the**Glass** set and the**Decision Tree Classifier** model had a nearly**4.5%** higher accuracy score, thanks to the method.

## Comparison

The results were also compared with the **featurewiz** library and **CAAFE** paper.

## Keywords

Automated Feature Engineering, Feature Selection, Optimization, LLM, Open-Source, Mistral 7B, Tabular-Numeric Data
