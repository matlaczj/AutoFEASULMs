from sklearn.metrics import accuracy_score, mean_absolute_percentage_error, r2_score
from response_schemas import schema
import copy

# Classification Models
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Regression Models
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor


datasets = [
    {
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
        "n_sampled_corr": 100,
    },
    "validation": {
        "kfold": 5,
        "scorers": {
            "classification": accuracy_score,
            "regression": r2_score,  # mean_absolute_percentage_error
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
                experiment["dataset"]["short_description"] = dataset[
                    "short_description"
                ]
                experiment["problem"]["type"] = model["type"]
                experiment["problem"]["machine_learning_model"] = model[
                    "machine_learning_model"
                ]
                experiment["problem"]["model"] = model["model"]
                experiment["ID"] = (
                    f'{i}-MISTRAL-{dataset["name"].upper()}-{model["machine_learning_model"].upper()}'
                ).replace(" ", "_")
                experiments.append(experiment)
                i += 1
    return experiments
