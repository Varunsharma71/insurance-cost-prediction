import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("insurance_cleaned.csv")

print("Dataset Shape: - eda.py:8", df.shape)
print("\nBasic Statistics: - eda.py:9")
print(df.describe())

# 1. Distribution of insurance charges
plt.figure(figsize=(8, 5))
sns.histplot(df["charges"], kde=True)
plt.title("Distribution of Insurance Charges")
plt.xlabel("Insurance Charges")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 2. Age vs Charges
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="age", y="charges", hue="smoker")
plt.title("Age vs Insurance Charges")
plt.xlabel("Age")
plt.ylabel("Insurance Charges")
plt.tight_layout()
plt.show()

# 3. BMI vs Charges
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="bmi", y="charges", hue="smoker")
plt.title("BMI vs Insurance Charges")
plt.xlabel("BMI")
plt.ylabel("Insurance Charges")
plt.tight_layout()
plt.show()

# 4. Smoker vs Charges
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="smoker", y="charges")
plt.title("Smoker Status vs Insurance Charges")
plt.xlabel("Smoker")
plt.ylabel("Insurance Charges")
plt.tight_layout()
plt.show()

# 5. Region vs Charges
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="region", y="charges")
plt.title("Region vs Insurance Charges")
plt.xlabel("Region")
plt.ylabel("Insurance Charges")
plt.tight_layout()
plt.show()

# 6. Sex vs Charges
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="sex", y="charges")
plt.title("Gender vs Insurance Charges")
plt.xlabel("Gender")
plt.ylabel("Insurance Charges")
plt.tight_layout()
plt.show()

print("\nEDA completed successfully! - eda.py:66")