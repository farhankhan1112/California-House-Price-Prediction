import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("linear_regression_california.pkl", "rb") as file:
    model = pickle.load(file)

# USD to INR Conversion Rate (Update if needed)
USD_TO_INR = 83  # Approximate exchange rate

# Streamlit UI
st.title("California House Price Prediction")
st.write("Enter the details below to predict the house price:")

# User Inputs (Only 6 features as per trained model)
median_income = st.number_input("Median Income ($1000s)", min_value=0.0, format="%.2f")
house_age = st.number_input("House Age (years)", min_value=0, max_value=100)
total_rooms = st.number_input("Total Rooms", min_value=1)
total_bedrooms = st.number_input("Total Bedrooms", min_value=1)
population = st.number_input("Population", min_value=1)
households = st.number_input("Households", min_value=1)

# Prediction
if st.button("Predict Price"):
    features = np.array([[median_income, house_age, total_rooms, total_bedrooms, population, households]])
    prediction_usd = model.predict(features)[0] * 100000  # Convert to USD
    prediction_inr = prediction_usd * USD_TO_INR  # Convert to INR
    
    # Display results
    st.success(f"Predicted House Price: ${prediction_usd:,.2f} (₹{prediction_inr:,.2f} INR)")
