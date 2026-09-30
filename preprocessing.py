import pandas as pd

# Cleaned dataset load
df = pd.read_csv("insurance_cleaned.csv")

print("Original data: - preprocessing.py:6")
print(df.head())

# Text values ko numbers mein convert
df["sex"] = df["sex"].map({
    "male": 0,
    "female": 1
})

df["smoker"] = df["smoker"].map({
    "no": 0,
    "yes": 1
})

# Region ko numerical columns mein convert
df = pd.get_dummies(df, columns=["region"], drop_first=True)

print("\nPreprocessed data: - preprocessing.py:23")
print(df.head())

print("\nColumns: - preprocessing.py:26")
print(df.columns)

# Preprocessed dataset save
df.to_csv("insurance_preprocessed.csv", index=False)

print("\nPreprocessing completed! - preprocessing.py:32")
print("File saved: insurance_preprocessed.csv - preprocessing.py:33")