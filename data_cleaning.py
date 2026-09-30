# ==========================================================
# Data Cleaning - insurance.csv
# Run: python data_cleaning.py
# ==========================================================

import pandas as pd

# 1. File load karo
df = pd.read_csv("insurance.csv")
print("Original shape: - data_cleaning.py:10", df.shape)

# 2. Pehli 5 rows dekho
print("\nFirst 5 rows:\n - data_cleaning.py:13", df.head())

# 3. Columns ka data type aur info
print("\nData types:\n - data_cleaning.py:16", df.dtypes)

# 4. Missing (null) values check
print("\nMissing values:\n - data_cleaning.py:19", df.isnull().sum())

# 5. Duplicate rows check aur hatao
print("\nDuplicate rows: - data_cleaning.py:22", df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)

# 6. Text columns ko saaf karo (extra space / capital letters)
for col in ["sex", "smoker", "region"]:
    df[col] = df[col].str.strip().str.lower()

# 7. Galat values check (age, bmi, charges)
print("\nStatistical summary:\n - data_cleaning.py:30", df.describe())
print("\nUnique values: - data_cleaning.py:31")
for col in ["sex", "smoker", "region"]:
    print(col, "> - data_cleaning.py:33", df[col].unique())

# 8. Outliers check (BMI aur charges me IQR method se)
for col in ["bmi", "charges"]:
    q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    count = ((df[col] < low) | (df[col] > high)).sum()
    print(f"\n{col}: outliers = {count} (range {low:.2f} to {high:.2f}) - data_cleaning.py:41")

# 9. Cleaned file save karo
df.to_csv("insurance_cleaned.csv", index=False)
print("\nCleaned shape: - data_cleaning.py:45", df.shape)
print("Cleaned file saved: insurance_cleaned.csv - data_cleaning.py:46")