import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model

# Function to preprocess user input data
def preprocess_input(data):
    data['gender'] = data['gender'].apply(lambda x: 1 if x == 'Male' else 0)
    categorical_columns = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
                           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                           'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
    for col in categorical_columns:
        data[col] = data[col].apply(lambda x: 1 if x == 'Yes' else 0 if x == 'No' else 2)
    return data

# Load your ANN model here
final_model = load_model('Model_folder/churn_prediction.h5')

# Streamlit UI
st.title("Churn Prediction App")

st.write("Enter customer information:")

# Create input fields for user input
gender = st.selectbox("Gender", ['Male', 'Female'])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ['Yes', 'No'])
dependents = st.selectbox("Dependents", ['Yes', 'No'])
tenure = st.number_input("Tenure", min_value=0)
phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No'])
internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.number_input("Monthly Charges", min_value=0)
total_charges = st.number_input("Total Charges", min_value=0)

# Create a dictionary with user input
user_input = {
    'gender': gender,
    'SeniorCitizen': senior_citizen,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'PhoneService': phone_service,
    'MultipleLines': multiple_lines,
    'InternetService': internet_service,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'Contract': contract,
    'PaperlessBilling': paperless_billing,
    'PaymentMethod': payment_method,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges
}


# Preprocess user input
input_data = preprocess_input(pd.DataFrame([user_input]))
reshaped_input = input_data.values[:, :11]
# Make prediction
prediction = final_model.predict(reshaped_input)
single_prediction = prediction[0]
churn_prediction = "Churn" if single_prediction > 0.5 else "Not Churn"

st.write("Prediction:", churn_prediction)
