import streamlit as st
import numpy as np
import joblib
import pandas as pd

# -----------------------------
# Load model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("random_forest")

model = load_model()

# -----------------------------
# Helper functions
# -----------------------------
def encode_yes_no(value):
    return 1 if value == "Yes" else 0

def scale(value, min_val, max_val):
    """Min-Max Scaling"""
    return (value - min_val) / (max_val - min_val)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📊 Customer Churn Prediction")

st.write("Enter details to predict churn .")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (0–72 months)", min_value=0, max_value=72, value=12)
    monthly_charges = st.number_input("Monthly Charges (0–120)", min_value=0.0, max_value=120.0, value=50.0)
    total_charges = st.number_input("Total Charges (0–9000)", min_value=0.0, max_value=9000.0, value=600.0)

with col2:
    senior = st.selectbox("Senior Citizen", ["Yes", "No"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependent = st.selectbox("Dependent", ["Yes", "No"])

# -----------------------------
# Encode + Scale
# -----------------------------
senior_enc = encode_yes_no(senior)
partner_enc = encode_yes_no(partner)
dependent_enc = encode_yes_no(dependent)

tenure_scaled = scale(tenure, 0, 72)
monthly_scaled = scale(monthly_charges, 0, 120)
total_scaled = scale(total_charges, 0, 9000)

# Prepare input row
input_data = pd.DataFrame([{
    "SeniorCitizen": senior_enc,
    "tenure": tenure_scaled,
    "MonthlyCharges": monthly_scaled,
    "TotalCharges": total_scaled,
    "Partner": partner_enc,
    "Dependent": dependent_enc
}])
# -----------------------------
# Predict
# -----------------------------
if st.button("Predict"):
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if pred == 1:
        st.error(f"⚠️ High Churn Risk — Probability: {prob:.2f}")
    else:
        st.success(f"✔️ Not Likely to Churn — Probability: {prob:.2f}")

    st.progress(float(prob))
