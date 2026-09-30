# Insurance Cost Prediction

Insurance Cost Prediction is a Machine Learning project that estimates medical insurance charges based on personal and insurance-related information.

## 🚀 Live Demo

https://insurance-cost-insights.streamlit.app/

## 📌 Project Overview

This project uses Python, Data Analytics, Machine Learning and Streamlit to build an interactive application for estimating insurance charges.

The project follows a complete data workflow:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Model Training
- Model Evaluation
- Insurance Cost Prediction
- Streamlit Web Application

## 🎯 Objectives

- Clean and prepare the insurance dataset.
- Understand patterns in insurance charges through data analysis.
- Preprocess categorical and numerical data.
- Train a Linear Regression model.
- Evaluate model performance.
- Create an interactive application for insurance cost estimation.

## 📊 Dataset

The project uses the **Medical Cost Personal Dataset** from Kaggle.

The dataset contains information about individuals and their medical insurance charges.

### Features

| Feature | Description |
|---|---|
| age | Age of the individual |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of children |
| smoker | Smoking status |
| region | Residential region |
| charges | Medical insurance charges |

## ⚙️ Machine Learning

The project uses **Linear Regression** to estimate insurance charges.

The model is trained using the cleaned and preprocessed dataset.

### Model Performance

- **R² Score:** 0.807
- **MAE:** 4177.05
- **RMSE:** 5956.34

These metrics were calculated on the test dataset.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## 📂 Project Structure

```text
Insurance-Cost-Prediction/
│
├── app.py
├── insurance.csv
├── insurance_cleaned.csv
├── insurance_preprocessed.csv
├── data_cleaning.py
├── eda.py
├── preprocessing.py
├── model.py
├── insurance_model.pkl
├── model_columns.pkl
├── actual_vs_predicted.png
├── requirements.txt
└── README.md
```

## 🔄 Project Workflow

Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Data Preprocessing
     ↓
Linear Regression
     ↓
Model Evaluation
     ↓
Streamlit Application
     ↓
Insurance Cost Prediction

## 💻 Run the Project Locally
Install the required libraries:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

The application will open in the browser.

## ⚠️ Disclaimer
This application provides an estimated insurance charge based on the trained machine learning model and the information provided by the user.
The prediction is for educational and demonstration purposes only and should not be considered an actual insurance quotation.

## 👨‍💻 Author

**Varun Sharma**

BCA Student | Data Analytics & Machine Learning
