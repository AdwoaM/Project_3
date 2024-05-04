import streamlit as st        
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
st.write("""
# Wine Quality Prediction App
This app predicts the **Wine Quality** type!
""")
st.sidebar.header('User Input Parameters')
  
def user_input_features():
        fixed_acidity = st.sidebar.slider('fixed acidity: most acids involved with wine are fixed or nonvolatile', 4.6, 15.9, 8.32)
        volatile_acidity = st.sidebar.slider('volatile acidity: the amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste', 0.12, 1.58 , 0.53)
        citric_acid = st.sidebar.slider('citric acid: found in small quantities, citric acid can add freshness and flavor to wines', 0.0, 1.0 , 0.5)
        residual_sugar = st.sidebar.slider('residual sugar:the amount of sugar remaining after fermentation stops, it is rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet', 0.9,15.5,2.54)
        chlorides = st.sidebar.slider('chlorides:the amount of salt in the wine', 0.01, 0.61 , 0.09)
        pH = st.sidebar.slider('pH: describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale', 2.74, 4.01, 3.31)
        alcohol=st.sidebar.slider('alcohol:the percent alcohol content of the wine', 8.4, 14.9, 10.4)
        sulphates=st.sidebar.slider('sulphates:a wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial and antioxidant', 0.33,2.0,0.66 )
        data = {'fixed_acidity': fixed_acidity,
                'volatile_acidity': volatile_acidity,
                'citric_acid': citric_acid,
                'residual_sugar' : residual_sugar,
                'chlorides': chlorides,
              'pH':pH,
              'alcohol':alcohol,
                'sulphates':sulphates}
        features = pd.DataFrame(data, index=[0])
        return features
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

data=pd.read_csv("winequality-red.csv")
X =np.array(data[['fixed acidity', 'volatile acidity' , 'citric acid' ,'residual sugar','chlorides' , 'pH' , 'alcohol' , 'sulphates']])
Y = np.array(data['quality'])
clf = RandomForestClassifier()
clf.fit(X, Y)
st.subheader('Class labels and their corresponding index number')
st.write(pd.DataFrame({
   'wine quality': [3, 4, 5, 6, 7, 8 ]}))

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)
st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)