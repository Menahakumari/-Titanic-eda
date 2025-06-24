# -Titanic-eda

# Titanic Data Analysis & Visualization

This project focuses on understanding the Titanic dataset using descriptive statistics and visualizations. The goal is to extract patterns, detect anomalies, and draw inferences from the data to support survival prediction in future modeling tasks.

---

## Objectives

- Generate summary statistics (mean, median, std, etc.)
- Create histograms and boxplots for numeric features
- Use correlation matrix and pairplots to explore feature relationships
- Identify patterns, trends, and anomalies
- Make feature-level inferences from visuals

---

## Project Structure

```
titanic-analysis/
├── Titanic-Dataset.csv           # Raw dataset
├── titanic_analysis.ipynb        # Jupyter notebook with analysis & visualizations
└── README.md                     # Project documentation
```

---

## 🛠️ Tools & Libraries Used

- **Python** – Programming language
- **Pandas** – Data analysis
- **Matplotlib / Seaborn** – Visualization
- **Jupyter Notebook** – Code and plots

---

##  Analysis Overview

### Summary Statistics
- Used `df.describe()` to understand distribution of numeric values
- Checked for missing values and filled where necessary

### Visualizations
- **Histograms** to inspect distributions (Age, Fare, SibSp, Parch)
- **Boxplots** to detect outliers
- **Correlation Matrix** to understand numerical relationships
- **Pairplot** to visualize multiple features against survival
- **Bar plots** to explore trends in categorical features like Sex, Pclass, Embarked

### Trend & Pattern Discovery
- Survival rate varies by age group, fare paid, and class
- Higher fare and 1st class passengers had better chances of survival
- Children and young adults had higher survival rates
- Females had significantly better survival outcomes than males

---

##  Key Inferences

- **Sex**: Females were more likely to survive than males
- **Pclass**: Passengers in 1st class survived more often than those in 2nd or 3rd
- **Age**: Children (<12) and young adults (<35) had higher survival rates
- **Fare**: Higher fare correlated with survival (likely due to class)
- **Embarked**: Port C (Cherbourg) passengers had better survival odds

---

##  Dataset Source

[Titanic Dataset – Kaggle](https://www.kaggle.com/competitions/titanic/data)

---

## Contact

Feel free to connect or contribute to the project.
