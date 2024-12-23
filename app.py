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
def predict(Area,Bedrooms,Bathrooms,Floors,YearBuilt,Location,Condition,Garage):
    prediction = model.predict([[Area,Bedrooms,Bathrooms,Floors,YearBuilt,Location,Condition,Garage]])
    return prediction 

def main():
    st.markdown('House Price Prediction :chart:')
    Area = st.number_input("Enter Area in sqft",min_value=350,max_value=5000)
    Bedrooms = st.number_input("Enter Numbers of Bedrooms",min_value=0,max_value=15)
    Bathrooms = st.number_input("Enter Numbers of bathrooms",min_value=0,max_value=10)
    Floors = st.selectbox('Enter the Floor',(list(range(1,50))))
    YearBuilt = st.selectbox('Enter the year of construction of the building',(list(range(1990,2024))))
    Location = st.selectbox("Enter Location of the building",('Downtown','Suburban','Rural','Urban'))
    Condition = st.selectbox("Enter the condition of the building",('Excellent','Good','Fair','Poor'))
    Garage = st.selectbox("Enter if you have Garage",('Yes','No'))

    if st.button('Predict'):
        result = predict(Area,Bedrooms,Bathrooms,Floors,YearBuilt,Location,Condition,Garage)
        st.success('The car price is : ₹{} '.format(result))  

if __name__ == '__main__':
    main()                         
    
    