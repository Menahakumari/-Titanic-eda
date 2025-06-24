import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("/content/Titanic-Dataset.csv")
#Generate Summary Statistics
print("Summary Statistics:\n")
print(df.describe())
print("\nSummary (including objects):\n")
print(df.describe(include='object'))
print("\nMissing Values:\n")
print(df.isnull().sum())

numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
for col in numeric_cols:
    plt.figure(figsize=(6, 5))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Histogram of {col}')
    plt.show()
for col in numeric_cols:
    plt.figure(figsize=(6, 5))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()
#Pairplot/Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
sns.pairplot(df[numeric_cols + ['Survived']], hue='Survived')
plt.show()
#Identify Patterns, Trends, or Anomalies
# Survival rate by Age Group
df['Age'].fillna(df['Age'].median(), inplace=True)  # Ensure no NaN in Age
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100],
                        labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])

plt.figure(figsize=(8, 4))
sns.barplot(x='AgeGroup', y='Survived', data=df, palette='dark', ci=None)
plt.title("Survival Rate by Age Group")
plt.ylabel("Survival Rate")
plt.xlabel("Age Group")
plt.ylim(0, 1)
plt.show()
#Fare vs Survival (outlier check)
plt.figure(figsize=(8, 4))
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title("Fare Distribution by Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Fare")
plt.show()
print("\nTop 5 Highest Fare Passengers:")
print(df[['Fare', 'Survived']].sort_values(by='Fare', ascending=False).head())

#Make Basic Feature-Level Inferences from Visuals
#Survival by Sex
plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.show()
# Survival by Passenger Class
plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival Count by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.show()
# Survival by Embarked Port
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
plt.figure(figsize=(6, 4))
sns.countplot(x='Embarked', hue='Survived', data=df)
plt.title("Survival Count by Embarkation Port")
plt.xlabel("Embarked")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.show()

# Inferences (printed out)
print("\n Feature-Level Inferences:")
print("""
1. Females had a significantly higher survival rate than males.
2. 1st class passengers had better chances of survival than 2nd and 3rd class.
3. Children and young adults survived more often than older adults.
4. Higher fare-paying passengers were more likely to survive (due to class).
5. Passengers who embarked at Cherbourg ('C') had a higher survival rate than others.
""")
