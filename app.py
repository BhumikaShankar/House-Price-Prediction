import streamlit as st
import joblib
import numpy as np

st.title("House Price Prediction Model")

# Load the model
model = joblib.load("model.pkl")

st.divider()

st.write(
    "This app uses ML for predicting house price with given features of the house. "
    "For using this app, you can enter the inputs from this UI interface and use the predict button."
)

st.divider()

# Inputs
bedrooms = st.number_input("Number of bedrooms", min_value=0, value=0)
bathrooms = st.number_input("Number of bathrooms", min_value=0, value=0)
livingarea = st.number_input("Living area", min_value=0, value=2000)

# Fixing selectbox issue
condition = st.selectbox(
    "Condition of the house", 
    options=[0, 1, 2, 3, 4, 5],  # Ensuring the minimum value is 0
    index=3  # Default selection (3rd index)
)

numberofschools = st.number_input("Number of schools nearby", min_value=0, value=0)

st.divider()

# Feature array
X = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]

predictbutton = st.button("Predict")

if predictbutton:
    st.balloons()  # Corrected spelling from `st.ballons()` to `st.balloons()`

    X_array = np.array(X)

    prediction = model.predict(X_array)

    st.write(f"Price prediction is {prediction[0]:,.2f}")  # Formatting the price

else:
    st.write("Please use the Predict button after entering values.")
