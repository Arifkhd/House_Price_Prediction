# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:14:18 2024

@author: Dell
"""

import streamlit as st
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
model = joblib.load('Hous.pkl')

st.title('House Price Prediction')

def predict(Area, Bedrooms, Bathrooms, Floors, YearBuilt, Location, Condition, Garage):
    # Predict and extract the first element of the result to remove square brackets
    prediction = model.predict([[Area, Bedrooms, Bathrooms, Floors, YearBuilt, Location, Condition, Garage]])
    return prediction[0]  # Extract the scalar value

def main():
    st.markdown('This is a simple web app for predicting house prices :chart_with_upwards_trend:')
    
    # Input fields with validations
    area = st.number_input("Enter Area in sqft", min_value=350, max_value=5000, step=10)
    bedrooms = st.number_input("Enter Number of Bedrooms", min_value=0, max_value=15, step=1)
    bathrooms = st.number_input("Enter Number of Bathrooms", min_value=0, max_value=10, step=1)
    floors = st.selectbox('Enter the Floor', list(range(1, 50)))
    year_built = st.selectbox('Enter the Year of Construction', list(range(1990, 2024)))

# Dropdowns for categorical inputs with validation
    location = st.selectbox("Select Location of the Building", ('Select', 'Downtown', 'Suburban', 'Rural', 'Urban'))
    if location == 'Select':
        st.warning("Please select a valid location.")

    condition = st.selectbox("Select the Condition of the Building", ('Select', 'Excellent', 'Good', 'Fair', 'Poor'))
    if condition == 'Select': 
        st.warning("Please select a valid condition.")

    garage = st.selectbox("Do you have a Garage?", ('Select', 'Yes', 'No'))
    if garage == 'Select':
        st.warning("Please select a valid option for garage.")

# Check if all fields are valid before allowing prediction
    if st.button('Predict'):
        if location == 'Select' or condition == 'Select' or garage == 'Select':
            st.error("Please fill all fields with valid selections.")
        else:
            result = predict(area, bedrooms, bathrooms, floors, year_built, location, condition, garage)
            st.success(f'The Predicted House Price is: ₹{result:,.0f}')

    

if __name__ == '__main__':
    main()
