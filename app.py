import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# Custom Styling
# -------------------------------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="💰",
    layout="wide"
)


# -------------------------------------------------
# Load Model and Columns
# -------------------------------------------------
model = joblib.load("insurance_model.pkl")
model_columns = joblib.load("model_columns.pkl")


# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown(
    '<div class="main-title">💰 Insurance Cost Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Estimate insurance charges based on personal and insurance details</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# Input Section
# -------------------------------------------------
st.subheader("👤 Personal & Insurance Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

with col2:
    sex = st.selectbox(
        "Sex",
        ["male", "female"]
    )

with col3:
    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1
    )


col4, col5, col6 = st.columns(3)

with col4:
    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=0
    )

with col5:
    smoker = st.selectbox(
        "Smoker",
        ["no", "yes"]
    )

with col6:
    region = st.selectbox(
        "Region",
        [
            "northeast",
            "northwest",
            "southeast",
            "southwest"
        ]
    )


st.divider()


# -------------------------------------------------
# Prediction
# -------------------------------------------------
if st.button("🔮 Predict Insurance Cost", use_container_width=True):

    # Empty row with exactly the same columns
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )

    # Fill user values
    input_data["age"] = age
    input_data["sex"] = 0 if sex == "male" else 1
    input_data["bmi"] = bmi
    input_data["children"] = children
    input_data["smoker"] = 1 if smoker == "yes" else 0

    # Region
    region_column = f"region_{region}"

    if region_column in input_data.columns:
        input_data[region_column] = True


    # Prediction
    prediction = model.predict(input_data)[0]


    # Result
    st.success("Prediction completed successfully!")

    st.metric(
        label="Estimated Insurance Charges",
        value=f"{prediction:,.2f}"
    )

    st.info(
        "This estimate is generated using the trained Linear Regression model."
    )


# -------------------------------------------------
# Footer
# -------------------------------------------------
st.divider()

st.caption(
    "Insurance Cost Prediction | Python + Data Analytics + Machine Learning"
)