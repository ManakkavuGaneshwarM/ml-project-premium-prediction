import streamlit as st
from prediction_helper import predict

st.title("Shield Insurance Premium Prediction App")

categorical_option = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("Age", min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input("Income in Lakhs", min_value=0, step=1, max_value=200)

with row2[0]:
    genetical_risk= st.number_input("Genetical Risk", min_value=0, step=1, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox("Insurance Plan", categorical_option['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox("Employment Status", categorical_option['Employment Status'])

with row3[0]:
    gender = st.selectbox("Gender", categorical_option['Gender'])
with row3[1]:
    marital_status = st.selectbox("Marital Status", categorical_option['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox("BMI Category", categorical_option['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox("Smoking Status", categorical_option['Smoking Status'])
with row4[1]:
    region = st.selectbox("Region", categorical_option['Region'])
with row4[2]:
    medical_history = st.selectbox("Medical History", categorical_option['Medical History'])

input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Insurance Plan': insurance_plan,
    'Genetical Risk': genetical_risk,
    'Gender': gender,
    'Region': region,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Medical History': medical_history,
    'Employment Status': employment_status
}

if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium: {prediction}")