
"""
Complete Exploratory Data Analysis (EDA) Script
Author: Dr. Didar Murad

Topics Covered:
1. Introduction to EDA
2. Missing Value Analysis
3. Data Consistency Checking
4. Binning and Discretization
5. Outlier Detection and Handling
6. Feature Selection
7. Data Wrangling
8. Hypothesis Testing
9. Data Visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier

print("Loading Dataset...")
data = pd.read_csv("eda_sample_dataset.csv")

print("\nFirst 5 Rows")
print(data.head())

print("\nDataset Info")
print(data.info())

print("\nSummary Statistics")
print(data.describe())

print("\n-----------------------------")
print("Missing Value Analysis")
print("-----------------------------")

print(data.isnull().sum())

numeric_columns = data.select_dtypes(include=np.number).columns
categorical_columns = data.select_dtypes(include='object').columns

# Handle missing numeric values
for col in numeric_columns:
    data[col].fillna(data[col].mean(), inplace=True)

# Handle missing categorical values
for col in categorical_columns:
    data[col].fillna(data[col].mode()[0], inplace=True)

print("\nMissing values handled.")

print("\n-----------------------------")
print("Data Consistency Cleaning")
print("-----------------------------")

if "Gender" in data.columns:
    data["Gender"] = data["Gender"].replace({
        "M": "Male",
        "F": "Female",
        "male": "Male",
        "female": "Female"
    })
    print("Unique Gender values:", data["Gender"].unique())

print("\n-----------------------------")
print("Binning Continuous Variables")
print("-----------------------------")

if "Age" in data.columns:
    data["Age_Group"] = pd.cut(
        data["Age"],
        bins=[0,18,35,60,100],
        labels=["Teen","Young Adult","Adult","Senior"]
    )
    print(data[["Age","Age_Group"]].head())

print("\n-----------------------------")
print("Outlier Detection")
print("-----------------------------")

if "Salary" in data.columns:
    z_scores = np.abs(stats.zscore(data["Salary"]))
    data = data[z_scores < 3]
    print("Dataset shape after removing outliers:", data.shape)

print("\n-----------------------------")
print("Encoding Categorical Variables")
print("-----------------------------")

encoder = LabelEncoder()

for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

print(data.head())

print("\n-----------------------------")
print("Feature Selection")
print("-----------------------------")

if "Purchased" in data.columns:
    X = data.drop("Purchased", axis=1)
    y = data["Purchased"]

    selector = SelectKBest(score_func=chi2, k=2)
    selector.fit(X, y)

    print("Feature Scores:", selector.scores_)

    model = RandomForestClassifier()
    model.fit(X, y)

    print("Feature Importance:", model.feature_importances_)

print("\n-----------------------------")
print("Visualization")
print("-----------------------------")

sns.set(style="whitegrid")

plt.figure()
data["Age"].hist()
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure()
sns.boxplot(x=data["Salary"])
plt.title("Salary Boxplot")
plt.show()

plt.figure()
sns.scatterplot(x="Age", y="Salary", hue="Purchased", data=data)
plt.title("Age vs Salary")
plt.show()

plt.figure()
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

print("\n-----------------------------")
print("Hypothesis Testing")
print("-----------------------------")

if "Purchased" in data.columns:
    group1 = data[data["Purchased"] == 0]["Salary"]
    group2 = data[data["Purchased"] == 1]["Salary"]

    t_stat, p_value = stats.ttest_ind(group1, group2)

    print("T-Test Statistic:", t_stat)
    print("P-value:", p_value)

if "Gender" in data.columns:
    contingency = pd.crosstab(data["Gender"], data["Purchased"])
    chi2_stat, p, dof, expected = stats.chi2_contingency(contingency)

    print("Chi-square:", chi2_stat)
    print("P-value:", p)

print("\nEDA Completed Successfully")
