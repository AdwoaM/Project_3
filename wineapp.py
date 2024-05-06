import streamlit as st        
# from sklearn.ensemble import RandomForestClassifier
# import pandas as pd
import pickle
# import numpy as np
st.write("""
# Wine Quality Prediction App
This app predicts the **Wine Quality** type!
""")


## Load Models

wwine_model = pickle.load(open('wwine_quality.sav', 'rb'))
rwine_model = pickle.load(open('rwine_quality.sav', 'rb'))

st.sidebar.header('User Input Parameters')
  

fixed_acidity = st.sidebar.slider('fixed acidity: most acids involved with wine are fixed or nonvolatile', 4.6, 15.9, 8.32)
volatile_acidity = st.sidebar.slider('volatile acidity: the amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste', 0.12, 1.58 , 0.53)
citric_acid = st.sidebar.slider('citric acid: found in small quantities, citric acid can add freshness and flavor to wines', 0.0, 1.0 , 0.5)
residual_sugar = st.sidebar.slider('residual sugar:the amount of sugar remaining after fermentation stops, it is rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet', 0.9,15.5,2.54)
chlorides = st.sidebar.slider('chlorides:the amount of salt in the wine', 0.01, 0.61 , 0.09)
free_sulfur_dioxide = st.sidebar.slider('free sulfur dioxide:the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine', 1.0, 72.0,  15.9)
total_sulfur_dioxide = st.sidebar.slider('total sulfur dioxide:amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine', 6.0, 289.0 , 46.5)
density = st.sidebar.slider('density:the density of water is close to that of water depending on the percent alcohol and sugar content', 0.99, 1.0 , 0.94)
pH = st.sidebar.slider('pH: describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale', 2.74, 4.01, 3.31)
sulphates=st.sidebar.slider('sulphates:a wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial and antioxidant', 0.33,2.0,0.66 )
alcohol=st.sidebar.slider('alcohol:the percent alcohol content of the wine', 8.4, 14.9, 10.4)


st.subheader('User Input parameters')

wine_quality = ''

option = st.selectbox(
   'Which Wine Type would like to test for its Quality?',
   ('White Wine', 'Red Wine'),
   
)
if st.button('Test Quality Wine'):
    if option == 'White Wine':
        wine_quality = wwine_model.predict([[float(fixed_acidity), float(volatile_acidity), float(citric_acid), float(residual_sugar), float(chlorides), float(free_sulfur_dioxide), float(total_sulfur_dioxide), float(density), float(pH), float(sulphates), float(alcohol)]])
    elif option == 'Red Wine':
        wine_quality = rwine_model.predict([[float(fixed_acidity), float(volatile_acidity), float(citric_acid), float(residual_sugar), float(chlorides), float(free_sulfur_dioxide), float(total_sulfur_dioxide), float(density), float(pH), float(sulphates), float(alcohol)]])
st.success(wine_quality)

st.write(
    'If you get a prediction less than 7: it is a poor quality wine! An excellent wine quality should be 7 and Up!'
)

