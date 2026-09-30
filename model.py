import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

import numpy as np


# 1. Preprocessed data load
df = pd.read_csv("insurance_preprocessed.csv")

print("Data loaded successfully! - model.py:13")
print("Shape: - model.py:14", df.shape)


# 2. Input (X) aur Target (y) alag karo
X = df.drop("charges", axis=1)
y = df["charges"]


# 3. Training aur Testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining data: - model.py:30", X_train.shape)
print("Testing data: - model.py:31", X_test.shape)


# 4. Linear Regression model
model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel trained successfully! - model.py:39")


# 5. Test data par prediction
y_pred = model.predict(X_test)


# 6. Model performance
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n Model Performance - model.py:51")
print("R2 Score : - model.py:52", round(r2, 3))
print("MAE      : - model.py:53", round(mae, 2))
print("RMSE     : - model.py:54", round(rmse, 2))


# 7. Kuch actual vs predicted values
result = pd.DataFrame({
    "Actual Charges": y_test.values,
    "Predicted Charges": y_pred
})

print("\nActual vs Predicted: - model.py:63")
print(result.head(10))

import matplotlib.pyplot as plt

# Actual vs Predicted graph
plt.figure(figsize=(7, 5))

plt.scatter(y_test, y_pred, alpha=0.6)

# Perfect prediction line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)

plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Insurance Charges")

plt.tight_layout()
plt.savefig("actual_vs_predicted.png", dpi=150)

plt.show()

print("\nEvaluation graph saved successfully! - model.py:89")

import joblib

# Model save
joblib.dump(model, "insurance_model.pkl")

# Model ke required columns save
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("\nModel saved successfully! - model.py:99")
print("insurance_model.pkl created - model.py:100")
print("model_columns.pkl created - model.py:101")