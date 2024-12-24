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
    st.markdown('House Price Prediction :chart:')
    
    # Input fields for user input
    Area = st.number_input("Enter Area in sqft", min_value=350, max_value=5000)
    Bedrooms = st.number_input("Enter Numbers of Bedrooms", min_value=0, max_value=15)
    Bathrooms = st.number_input("Enter Numbers of bathrooms", min_value=0, max_value=10)
    Floors = st.selectbox('Enter the Floor', (list(range(1, 50))))
    YearBuilt = st.selectbox('Enter the year of construction of the building', (list(range(1990, 2024))))
    Location = st.selectbox("Enter Location of the building", ('None', 'Downtown', 'Suburban', 'Rural', 'Urban'))
    if Location == 'None':
        st.warning("Please select a valid Location.")
    else:
        st.success(f"You selected: {Location}")
        
    Condition = st.selectbox("Enter the condition of the building", ('None', 'Excellent', 'Good', 'Fair', 'Poor'))
    if Condition == 'None':
        st.warning("Please select a valid condition.")
    else:
        st.success(f"You selected: {Condition}")
    
    Garage = st.selectbox("Enter if you have Garage", ('None', 'Yes', 'No'))
    if Garage == 'None':
        st.warning("Please select garage.")
    else:
        st.success(f"You selected: {Garage}")

    # Handle prediction button
    if st.button('Predict'):
        # Call the predict function and display the result
        result = predict(Area, Bedrooms, Bathrooms, Floors, YearBuilt, Location, Condition, Garage)
        st.success(f'Predicted House Price: ₹{result:,.2f}')  # Format for better readability

if __name__ == '__main__':
    main()
