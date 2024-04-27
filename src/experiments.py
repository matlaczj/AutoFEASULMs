from sklearn.metrics import (
    accuracy_score,
    mean_absolute_percentage_error,
    r2_score,
    f1_score,
    mean_absolute_error,
)
from response_schemas import schema
import copy

# Classification Models
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# Regression Models
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

# https://huggingface.co/datasets?task_categories=task_categories:tabular-regression&sort=likes

datasets = [
    {
        "origin": "sklearn",
        "predicted_variable": "",
        "type": "classification",
        "name": "wine",
        "short_description": """
**Attribute Information:**
Alcohol: Percentage of alcohol content in the wine.
Malic acid: Concentration of malic acid in the wine.
Ash: Amount of ash in the wine after combustion.
Alcalinity of ash: Measure of the basicity of ash in the wine.
Magnesium: Concentration of magnesium in the wine.
Total phenols: Total amount of phenolic compounds in the wine.
Flavanoids: Concentration of flavonoid compounds in the wine.
Nonflavanoid phenols: Concentration of non-flavonoid phenolic compounds in the wine.
Proanthocyanins: Concentration of proanthocyanins in the wine.
Color intensity: Intensity of color in the wine.
Hue: Hue or shade of the wine.
OD280/OD315 of diluted wines: Ratio of optical density at 280nm to 315nm of diluted wines.
Proline: Concentration of proline in the wine.
Target: class_0, class_1, class_2: Labels indicating the class or category of the wine samples.

""",
    },
    {
        "origin": "sklearn",
        "predicted_variable": "",
        "type": "classification",
        "name": "iris",
        "short_description": """
**Attribute Information:**
Sepal length: Length of the sepal in cm.
Sepal width: Width of the sepal in cm.
Petal length: Length of the petal in cm.
Petal width: Width of the petal in cm.
Target: class_0, class_1, class_2 - Labels indicating the class or category.

""",
    },
    {
        "origin": "sklearn",
        "predicted_variable": "",
        "type": "classification",
        "name": "breast_cancer",
        "short_description": """
**Attribute Information:**
Radius: Mean distance from the center to points on the perimeter of a tumor.
Texture: Standard deviation of gray-scale values in the tumor area.
Perimeter: Total length of the tumor perimeter.
Area: Total area covered by the tumor.
Smoothness: Local variation in the lengths of tumor radii.
Compactness: Measure of how compact the shape of the tumor is (calculated as (perimeter^2 / area) - 1).
Concavity: Severity of concave portions of the tumor contour.
Concave points: Number of concave portions of the tumor contour.
Symmetry: Symmetry of the tumor.
Fractal dimension: Measure of the complexity of the tumor's contour ("coastline approximation" - 1).
Target: Type of tumor, either malignant (WDBC-Malignant) or benign (WDBC-Benign).

""",
    },
    {
        "origin": "sklearn",
        "predicted_variable": "",
        "type": "regression",
        "name": "diabetes",
        "short_description": """
**Attribute Information:**
Age: Age of the individual in years.
Sex: Gender of the individual.
BMI: Body mass index, a measure of body fat based on height and weight.
BP: Average blood pressure of the individual.
S1 tc: Total serum cholesterol, the total amount of cholesterol in the blood.
S2 ldl: Low-density lipoproteins, a type of cholesterol often referred to as "bad" cholesterol.
S3 hdl: High-density lipoproteins, a type of cholesterol often referred to as "good" cholesterol.
S4 tch: Total cholesterol / HDL ratio, a measure of the balance between total cholesterol and HDL cholesterol.
S5 ltg: Possibly the logarithm of serum triglycerides level, a measure of fat found in the blood.
S6 glu: Blood sugar level, the concentration of glucose in the blood.
Target: A quantitative measure of disease progression one year after baseline, likely the outcome variable of interest in the dataset.

""",
    },
    {
        "origin": "huggingface",
        "predicted_variable": "body_mass_g",
        "type": "regression",
        "name": "SIH/palmer-penguins",
        "short_description": """""",
    },
    {
        "origin": "huggingface",
        "predicted_variable": "Price",
        "type": "regression",
        "name": "Ammok/laptop_price_prediction",
        "short_description": """""",
    },
    {
        "origin": "huggingface",
        "predicted_variable": "symbol",
        "type": "classification",
        "name": "edarchimbaud/earnings-forecast-stocks",
        "short_description": """**Data Fields**
symbol (string): A string representing the ticker symbol or abbreviation used to identify the company.
date (string): A string indicating the date of the forecast.
id (int64): An integer representing the unique identifier for the forecast.
fiscal_end (string): A string indicating the fiscal end date for the forecast.
consensus_eps_forecast (float64): A floating-point number representing the consensus earnings per share forecast.
high_eps_forecast (float64): A floating-point number representing the highest earnings per share forecast.
low_eps_forecast (float64): A floating-point number representing the lowest earnings per share forecast.
no_of_estimates (int64): An integer representing the number of estimates contributing to the consensus forecast.
up (int64): An integer representing the number of upward revisions to the forecast.
down (int64): An integer representing the number of downward revisions to the forecast.
""",
    },
    {
        "origin": "huggingface",
        "predicted_variable": "age",
        "type": "regression",
        "name": "imodels/credit-card",
        "short_description": """There are 25 variables:

ID: ID of each client
LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
SEX: Gender (1=male, 2=female)
EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
MARRIAGE: Marital status (1=married, 2=single, 3=others)
AGE: Age in years
PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
PAY_2: Repayment status in August, 2005 (scale same as above)
PAY_3: Repayment status in July, 2005 (scale same as above)
PAY_4: Repayment status in June, 2005 (scale same as above)
PAY_5: Repayment status in May, 2005 (scale same as above)
PAY_6: Repayment status in April, 2005 (scale same as above)
BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
default.payment.next.month: Default payment (1=yes, 0=no)
""",
    },
]

classical_models = [
    {
        "type": "classification",
        "machine_learning_model": "Support Vector Machine Classifier",
        "model": SVC(),
    },
    {
        "type": "classification",
        "machine_learning_model": "Random Forest Classifier",
        "model": RandomForestClassifier(),
    },
    {
        "type": "classification",
        "machine_learning_model": "K-Nearest Neighbors Classifier",
        "model": KNeighborsClassifier(),
    },
    {
        "type": "classification",
        "machine_learning_model": "Gaussian Naive Bayes Classifier",
        "model": GaussianNB(),
    },
    {
        "type": "classification",
        "machine_learning_model": "Decision Tree Classifier",
        "model": DecisionTreeClassifier(),
    },
    {
        "type": "regression",
        "machine_learning_model": "Support Vector Machine Regressor",
        "model": SVR(),
    },
    {
        "type": "regression",
        "machine_learning_model": "Random Forest Regressor",
        "model": RandomForestRegressor(),
    },
    {
        "type": "regression",
        "machine_learning_model": "K-Nearest Neighbors Regressor",
        "model": KNeighborsRegressor(),
    },
    {
        "type": "regression",
        "machine_learning_model": "Decision Tree Regressor",
        "model": DecisionTreeRegressor(),
    },
    {
        "type": "regression",
        "machine_learning_model": "Linear Regression",
        "model": LinearRegression(),
    },
]

# Define the experiment base
experiment_base = {
    "ID": "PLACEHOLDER",
    "model": {
        "name": "MISTRAL-7B-INSTRUCT-V0.2.Q6_K",
        "chat_format": "mistral-instruct",
        "n_gpu_layers": -1,
        "n_ctx": 512 * 16,
        "n_batch": 512 * 8,
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
        "iterations": 100,
        "n_new_features": 5,
        "n_unique_values": 10,
        "perc_digits_after_decimal": 20,
        "correlations_threshold": 0.5,
        "temperature": 1.5,
        "n_most_correlated": 20,
        "threshold_features": 0.8,
        "early_stopping": 4,
        "delayed_deletion": 2,
        "n_sampled_corr": 40,
        "percentage_change_threshold": 0.05,
    },
    "validation": {
        "kfold": 10,
        "scorers": {
            "classification": accuracy_score,
            "regression": mean_absolute_percentage_error,
        },
    },
    "schema": schema,
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
