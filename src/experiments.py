from src.tools.response_schemas import schema
import copy
from sklearn.metrics import (
    accuracy_score,
    mean_absolute_percentage_error,
)
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge


datasets = [
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "autoPrice",
        "short_description": f"**INTRODUCTION:**\nPredict the price of automobiles based on various features.\n",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "Bike_Sharing_Demand",
        "short_description": f"""**INTRODUCTION:**\nPredict the demand for shared bikes based on various features:
season : season (1:springer, 2:summer, 3:fall, 4:winter)
yr : year (0: 2011, 1:2012)
mnth : month ( 1 to 12)
hr : hour (0 to 23)
holiday : weather day is holiday or not
weekday : day of the week
workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
weathersit :
1: Clear, Few clouds, Partly cloudy, Partly cloudy
2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
temp : Normalized temperature in Celsius. The values are divided to 41 (max)
atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
hum: Normalized humidity. The values are divided to 100 (max)
windspeed: Normalized wind speed. The values are divided to 67 (max)
casual: count of casual users
registered: count of registered users
cnt: count of total rental bikes including both casual and registered\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "wine-quality-red",
        "short_description": f"""**INTRODUCTION:**\nPredict the quality of red wine based on physicochemical tests:
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
alcohol: This column represents the alcohol content of the wine, usually measured as the percentage of alcohol by volume.\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "forest_fires",
        "short_description": f"""**INTRODUCTION:**\nPredict the burned area of forest fires based on various features:
X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
month - month of the year: 'jan' to 'dec'
day - day of the week: 'mon' to 'sun'
FFMC - FFMC index from the FWI system: 18.7 to 96.20
DMC - DMC index from the FWI system: 1.1 to 291.3
DC - DC index from the FWI system: 7.9 to 860.6
ISI - ISI index from the FWI system: 0.0 to 56.10
temp - temperature in Celsius degrees: 2.2 to 33.30
RH - relative humidity in %: 15.0 to 100
wind - wind speed in km/h: 0.40 to 9.40
rain - outside rain in mm/m2 : 0.0 to 6.4
area - the burned area of the forest (in ha): 0.00 to 1090.84 (this output variable is very skewed towards 0.0, thus it may make sense to model with the logarithm transform).\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "abalone",
        "short_description": f"""**INTRODUCTION:**\nPredict the age of abalone based on physical measurements:
sex - sex of the abalone, possible values include M, F, and I (infant)
length - longest shell measurement in mm
diameter - perpendicular to length in mm
height - height with meat in shell in mm
whole_weight - whole abalone weight in grams
shucked_weight - weight of meat in grams
viscera_weight - gut weight (after bleeding) in grams
shell_weight - weight after being dried in grams
rings - the age in years of abalone, target feature\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "regression",
        "name": "UCI-student-performance-mat",
        "short_description": f"""**INTRODUCTION:**\nPredict the final grade of students in a math course based on various features:
1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira).
2 sex - student's sex (binary: 'F' - female or 'M' - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
13 traveltime - home to school travel time (numeric: 1 - <15>1 hour)
14 studytime - weekly study time (numeric: 1 - <2>10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "titanic",
        "short_description": f"""**INTRODUCTION:**\nPredict whether a passenger survived the Titanic disaster based on features:
Survived (target): This column indicates whether a passenger survived the Titanic disaster or not. It has two distinct values: 0 for not survived and 1 for survived.
Pclass: This column represents the passenger class or ticket class of the passenger. It has three distinct values, typically indicating first, second, or third class.
Sex: This column represents the gender of the passenger. It has two distinct values: male and female.
Age: This column represents the age of the passenger. It has seven distinct values, likely grouped into age ranges or categories.
Fare: This column represents the fare or price paid by the passenger for their ticket. It has six distinct values, possibly indicating different fare categories.
Embarked: This column represents the port of embarkation for the passenger. It has three distinct values, typically indicating different ports such as Southampton, Cherbourg, and Queenstown.
relatives: This column represents the number of relatives (e.g., siblings, spouse, parents, children) aboard the Titanic for the passenger. It has nine distinct values, likely representing different counts of relatives.
Title: This column represents the title or honorific of the passenger (e.g., Mr., Mrs., Miss). It has five distinct values, possibly indicating different titles or social statuses.\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "glass",
        "short_description": f"""**INTRODUCTION:**\nPredict the type of glass based on features:
binaryClass (target): This column is the target variable or the label you want to predict. It's a nominal variable with two distinct values, likely representing binary classes.
RI: This column represents the refractive index of the material. Refractive index is a measure of how light bends as it passes through the material.
Na: This column represents the sodium (Na) content of the material. Sodium content can influence various properties of the material.
Mg: This column represents the magnesium (Mg) content of the material. Magnesium can affect the material's properties such as strength and corrosion resistance.
Al: This column represents the aluminum (Al) content of the material. Aluminum is a common alloying element in many materials and can impact properties like strength and hardness.
Si: This column represents the silicon (Si) content of the material. Silicon is often present in materials like glass and ceramics and can affect properties such as transparency and thermal conductivity.
K: This column represents the potassium (K) content of the material. Potassium can influence properties like electrical conductivity and chemical reactivity.
Ca: This column represents the calcium (Ca) content of the material. Calcium is often found in materials like ceramics and can affect properties such as hardness and durability.
Ba: This column represents the barium (Ba) content of the material. Barium can be used as an additive in materials for various purposes such as improving electrical conductivity or increasing density.
Fe: This column represents the iron (Fe) content of the material. Iron is a common element in many materials and can impact properties such as strength, magnetism, and corrosion resistance.\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "iris",
        "short_description": f"""**INTRODUCTION:**\nPredict the class of iris plants based on features:
**Attribute Information**:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class: 
   -- Iris Setosa
   -- Iris Versicolour
   -- Iris Virginica\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "credit-g",
        "short_description": f"""**INTRODUCTION:**\nPredict the credit risk of individuals based on features:
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
Foreign worker (yes,no)\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "adult",
        "short_description": f"""**INTRODUCTION:**\nPredict whether an individual earns more than $50,000 a year based on features:
class (target): This column is the target variable or label that you want to predict. It's a nominal variable with two distinct values, likely representing different classes or categories.
age: This column represents the age of individuals. It's a numeric variable with 74 distinct values.
workclass: This column represents the type of employment or work class of individuals. It's a nominal variable with 8 distinct values and 2799 missing attributes.
fnlwgt: This column represents the final weight or sampling weight associated with each observation in the dataset. It's a numeric variable with 28523 distinct values.
education: This column represents the highest level of education achieved by individuals. It's a nominal variable with 16 distinct values.
education-num: This column represents the numerical encoding of education levels. It's a numeric variable with 16 distinct values.
marital-status: This column represents the marital status of individuals. It's a nominal variable with 7 distinct values.\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "mushroom",
        "short_description": f"""**INTRODUCTION:**\nPredict whether a mushroom is edible or poisonous based on features:
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
habitat: This column represents the habitat where the mushroom is typically found. It's a nominal variable with 7 distinct values.\n
""",
    },
    {
        "origin": "openml",
        "predicted_variable": "",
        "type": "classification",
        "name": "letter",
        "short_description": f"""**INTRODUCTION:**\nPredict the letter category based on features:
class (target): This column is the target variable or label that you want to predict. It's a nominal variable with 26 distinct values, representing different classes or categories.
x-box: This column represents the horizontal position of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
y-box: This column represents the vertical position of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
width: This column represents the width of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
high: This column represents the height of the bounding box for a letter-like image. It's a numeric variable with 16 distinct values.
onpix: This column represents the total number of "on" pixels (i.e., pixels that are part of the letter) in the bounding box. It's a numeric variable with 16 distinct values.
x-bar: This column represents the mean x-coordinate of "on" pixels in the bounding box. It's a numeric variable with 16 distinct values.\n
""",
    },
]

classical_models = [
    # Linear Models - They often require feature scaling and normalization for optimal performance. They also benefit from creating polynomial and interaction features.
    {
        "type": "regression",
        "machine_learning_model": "Ridge Regression",
        "model": Ridge(),
        "param_grid": {
            "alpha": [0.001, 0.01, 0.1, 1.0, 10.0, 100.0],
            "fit_intercept": [True, False],
            "max_iter": [100, 500, 1000, 2000],
            "tol": [0.0001, 0.001, 0.01, 0.1],
        },
    },
    # Tree-based Models - They are less sensitive to the scale of the features and can handle a mix of binary and continuous features.
    {
        "type": "classification",
        "machine_learning_model": "Decision Tree Classifier",
        "model": DecisionTreeClassifier(),
        "param_grid": {
            "max_depth": [None, 5, 10, 15, 20],
            "min_samples_split": [2, 5, 10, 20],
            "min_samples_leaf": [1, 2, 5, 10],
        },
    },
    # Distance-based Models - They require feature scaling because they rely on calculating the distance between instances.
    {
        "type": "regression",
        "machine_learning_model": "K-Nearest Neighbors Regressor",
        "model": KNeighborsRegressor(),
        "param_grid": {
            "n_neighbors": [1, 3, 5, 7, 9, 11, 13, 15],
            "weights": ["uniform", "distance"],
            "p": [1, 2],
        },
    },
    # Probabilistic Models - They often require data to be in a specific format or distribution.
    {
        "type": "classification",
        "machine_learning_model": "Gaussian Naive Bayes Classifier",
        "model": GaussianNB(),
        "param_grid": {"var_smoothing": [1e-9, 1e-8, 1e-7, 1e-6, 1e-5]},
    },
]


# Define the experiment base
experiment_base = {
    "ID": "PLACEHOLDER",
    "model": {
        "name": "MISTRAL-7B-INSTRUCT-V0.2.Q4_0",  # "MISTRAL-7B-INSTRUCT-V0.2.Q6_K",  # Meaning: The model name.
        "chat_format": "mistral-instruct",  # Meaning: The chat format to use. Improper chat formats can lead to unexpected results.
        "n_gpu_layers": -1,  # Meaning: Use all available GPUs.
        "n_ctx": 512 * 16,  # Meaning: Use a context window of X tokens.
        "n_batch": 512 * 8,  # Meaning: Use a batch size of X tokens.
    },
    "dataset": {
        "noise_perc_of_range": 0.05,  # Meaning: Percent of range of column values to add as noise.
        "target_variable": "target",  # Target column name will be changed to this name.
        "max_records": 1000,  # Meaning: Maximum number of records to sample from the dataset.
        "origin": "PLACEHOLDER",
        "predicted_variable": "PLACEHOLDER",
        "type": "PLACEHOLDER",
        "name": "PLACEHOLDER",
        "short_description": "PLACEHOLDER",
    },
    "problem": {
        "type": "PLACEHOLDER",
        "machine_learning_model": "PLACEHOLDER",
        "model": "PLACEHOLDER",
    },
    "feature_engineering": {
        "iterations": 15,  # Meaning: Run the FE process for X iterations.
        "early_stopping": 3,  # Meaning: Stop the FE process if the relative performance does not improve for X iterations.
        "percentage_change_threshold": 0,  # Meaning: Tolerance. Trigger early stopping counter if the relative performance drops by over X% in all early_stopping iterations.
        "n_new_features": 10,  # Meaning: Suggest X new features in each iteration.
        "n_unique_values": 5,  # Meaning: Describe each column with X unique values.
        "perc_digits_after_decimal": 10,  # Meaning: Describe each column with X% of the digits after the decimal.
        "correlations_threshold": 0.3,  # Meaning: What is considered an interesting correlation to show on the prompt.
        "temperature": 0.8,  # Meaning: The higher the temperature, the more creative the FE process.
        "n_most_correlated": 50,  # Meaning: Select the X most correlated features with the target variable.
        "threshold_features": 0.95,  # Meaning: Drop features that are more than X% correlated with another feature.
        "delayed_deletion": 2,  # Meaning: Start dropping features after the Xnd iteration.
        "n_sampled_corr": 50,  # Meaning: Sample X correlations into prompt.
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
                experiment["dataset"]["type"] = dataset["type"]
                experiment["problem"]["type"] = model["type"]
                experiment["problem"]["machine_learning_model"] = model[
                    "machine_learning_model"
                ]
                experiment["problem"]["model"] = model["model"]
                experiment["problem"]["param_grid"] = model["param_grid"]
                experiment["ID"] = (
                    f'{i}-MISTRAL-{dataset["name"].replace("/","-").upper()}-{model["machine_learning_model"].upper()}'
                ).replace(" ", "_")
                experiments.append(experiment)
                i += 1
    return experiments
