from response_schemas import schema
import copy
from sklearn.metrics import (
    accuracy_score,
    mean_absolute_percentage_error,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression


datasets = [
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "house_prices",
        "short_description": f"Predict house prices based on various features.\n",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "autoPrice",
        "short_description": f"Predict the price of automobiles based on features.\n",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "Bike_Sharing_Demand",
        "short_description": f"Predict the demand for bike sharing based on features.\n",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "titanic",
        "short_description": f"Predict the survival of passengers on the Titanic based on features.\n",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "glass",
        "short_description": f"Predict the type of glass based on features.\n",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "yeast",
        "short_description": f"Predict the localization site of proteins in yeast cells based on features.\n",
    },
]

classical_models = [
    # Linear Models - They often require feature scaling and normalization for optimal performance. They also benefit from creating polynomial and interaction features.
    {
        "type": "classification",
        "machine_learning_model": "Logistic Regression Classifier",
        "model": LogisticRegression(max_iter=500),
    },
    {
        "type": "regression",
        "machine_learning_model": "Linear Regression",
        "model": LinearRegression(),
    },
    # Tree-based Models - They are less sensitive to the scale of the features and can handle a mix of binary and continuous features.
    {
        "type": "classification",
        "machine_learning_model": "Decision Tree Classifier (criterion='entropy', splitter='best')",
        "model": DecisionTreeClassifier(criterion="entropy", splitter="best"),
    },
    {
        "type": "regression",
        "machine_learning_model": "Decision Tree Regressor (criterion='absolute_error', splitter='best')",
        "model": DecisionTreeRegressor(criterion="absolute_error", splitter="best"),
    },
    # Distance-based Models - They require feature scaling because they rely on calculating the distance between instances.
    {
        "type": "classification",
        "machine_learning_model": "K-Nearest Neighbors Classifier (algorithm='ball_tree')",
        "model": KNeighborsClassifier(algorithm="ball_tree"),
    },
    {
        "type": "regression",
        "machine_learning_model": "K-Nearest Neighbors Regressor (algorithm='ball_tree')",
        "model": KNeighborsRegressor(algorithm="ball_tree"),
    },
    # Probabilistic Models - They often require data to be in a specific format or distribution.
    {
        "type": "classification",
        "machine_learning_model": "Gaussian Naive Bayes Classifier",
        "model": GaussianNB(),
    },
]

# Define the experiment base
experiment_base = {
    "ID": "PLACEHOLDER",
    "model": {
        "name": "MISTRAL-7B-INSTRUCT-V0.2.Q6_K",
        "chat_format": "mistral-instruct",
        "n_gpu_layers": -1,  # Meaning: Use all available GPUs.
        "n_ctx": 512 * 16,  # Meaning: Use a context window of X tokens.
        "n_batch": 512 * 8,  # Meaning: Use a batch size of X tokens.
    },
    "dataset": {
        "target_variable": "target",
        "name": "PLACEHOLDER",
        "short_description": "PLACEHOLDER",
    },
    "problem": {
        "type": "PLACEHOLDER",
        "machine_learning_model": "PLACEHOLDER",
        "model": "PLACEHOLDER",
    },
    "feature_engineering": {
        "iterations": 10,  # Meaning: Run the FE process for X iterations.
        "n_new_features": 5,  # Meaning: Suggest X new features in each iteration.
        "n_unique_values": 10,  # Meaning: Describe each column with X unique values.
        "perc_digits_after_decimal": 20,  # Meaning: Describe each column with X% of the digits after the decimal.
        "correlations_threshold": 0.4,  # Meaning: What is considered an interesting correlation to show on the prompt.
        "temperature": 0.7,  # Meaning: The higher the temperature, the more creative the FE process.
        "n_most_correlated": 30,  # Meaning: Select the X most correlated features with the target variable.
        "threshold_features": 0.95,  # Meaning: Drop features that are more than X% correlated with another feature.
        "early_stopping": 3,  # Meaning: Stop the FE process if the relative performance does not improve for X iterations.
        "delayed_deletion": 2,  # Meaning: Start dropping features after the Xnd iteration.
        "n_sampled_corr": 40,  # Meaning: Sample X correlations into prompt.
        "percentage_change_threshold": 0.05,  # Meaning: Trigger early stopping counter if the relative performance does not improve by more than X%.
    },
    "validation": {
        "kfold": 10,  # Meaning: Use 10-fold cross-validation for model evaluation.
        "scorers": {
            "classification": accuracy_score,  # Meaning: Use accuracy score for classification problems.
            "regression": mean_absolute_percentage_error,  # Meaning: Use mean absolute percentage error for regression problems.
        },
    },
    "schema": schema,  # Meaning: The schema to use for the final JSON output.
}


def prepare_experiments(datasets, classical_models, experiment_base):
    experiments = []
    i = 0
    for dataset in datasets:
        for model in classical_models:
            if dataset["type"] == model["type"]:
                experiment = copy.deepcopy(experiment_base)
                experiment["dataset"]["name"] = dataset["name"]
                experiment["dataset"]["predicted_variable"] = dataset[
                    "predicted_variable"
                ]
                experiment["dataset"]["short_description"] = dataset[
                    "short_description"
                ]
                experiment["dataset"]["origin"] = dataset["origin"]
                experiment["problem"]["type"] = model["type"]
                experiment["problem"]["machine_learning_model"] = model[
                    "machine_learning_model"
                ]
                experiment["problem"]["model"] = model["model"]
                experiment["ID"] = (
                    f'{i}-MISTRAL-{dataset["name"].replace("/","-").upper()}-{model["machine_learning_model"].upper()}'
                ).replace(" ", "_")
                experiments.append(experiment)
                i += 1
    return experiments
