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
from sklearn.linear_model import LogisticRegression

# Regression Models
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

# https://huggingface.co/datasets?task_categories=task_categories:tabular-regression&sort=likes

datasets1 = [
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
        "origin": "arff",
        "predicted_variable": "class",
        "type": "classification",
        "name": "credit_data",
        "short_description": """Attribute description
Status of existing checking account, in Deutsche Mark.
Duration in months
Credit history (credits taken, paid back duly, delays, critical accounts)
Purpose of the credit (car, television,...)
Credit amount
Status of savings account/bonds, in Deutsche Mark.
Present employment, in number of years.
Installment rate in percentage of disposable income
Personal status (married, single,...) and sex
Other debtors / guarantors
Present residence since X years
Property (e.g. real estate)
Age in years
Other installment plans (banks, stores)
Housing (rent, own,...)
Number of existing credits at this bank
Job
Number of people being liable to provide maintenance for
Telephone (yes,no)
Foreign worker (yes,no)
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
]

datasets = (
    [
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
            "origin": "huggingface",
            "predicted_variable": "price",
            "type": "regression",
            "name": "gauss314/bitcoin_daily",
            "short_description": """Daily Bitcoin price data. The dataset contains the following columns:
- date: The date of the data point.
- price: The price of Bitcoin on that date.
- market_caps: The market capitalization of Bitcoin on that date.
- total_volumes: The total volume of Bitcoin traded on that date.""",
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
    + datasets1
)

classical_models = [
    # Linear Models - They often require feature scaling and normalization for optimal performance. They also benefit from creating polynomial and interaction features.
    {
        "type": "classification",
        "machine_learning_model": "Logistic Regression",
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
        "machine_learning_model": "Decision Tree Classifier",
        "model": DecisionTreeClassifier(criterion="entropy", splitter="best"),
    },
    {
        "type": "regression",
        "machine_learning_model": "Decision Tree Regressor",
        "model": DecisionTreeRegressor(criterion="absolute_error", splitter="best"),
    },
    # Distance-based Models - They require feature scaling because they rely on calculating the distance between instances.
    {
        "type": "classification",
        "machine_learning_model": "K-Nearest Neighbors Classifier",
        "model": KNeighborsClassifier(algorithm="ball_tree"),
    },
    {
        "type": "regression",
        "machine_learning_model": "K-Nearest Neighbors Regressor",
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
        "n_new_features": 6,  # Meaning: Suggest X new features in each iteration.
        "n_unique_values": 8,  # Meaning: Describe each column with X unique values.
        "perc_digits_after_decimal": 20,  # Meaning: Describe each column with X% of the digits after the decimal.
        "correlations_threshold": 0.4,  # Meaning: What is considered an interesting correlation to show on the prompt.
        "temperature": 0.5,  # Meaning: The higher the temperature, the more creative the FE process.
        "n_most_correlated": 30,  # Meaning: Select the X most correlated features with the target variable.
        "threshold_features": 0.9,  # Meaning: Drop features that are more than X% correlated with another feature.
        "early_stopping": 3,  # Meaning: Stop the FE process if the relative performance does not improve for X iterations.
        "delayed_deletion": 1,  # Meaning: Start dropping features after the Xnd iteration.
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
