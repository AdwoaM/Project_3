import streamlit as st 
import pickle

## Load Models

wwine_model = pickle.load(open('wwine_quality.sav', 'rb'))
rwine_model = pickle.load(open('rwine_quality.sav', 'rb'))

st.write("""
# Wine Quality Prediction App
This app predicts the **Wine Quality** type!
""")

st.text('Select the Wine Quality Value: Range 1 - 10')

# Create Columns
col1, col2, col3 = st.columns(3)

with col1 :
    fixed_acidity = st.number_input ('Input Fixed Acidity Value')
    volatile_acidity = st.number_input ('Input Volatile Acidity Value')
    citric_acid = st.number_input ('Input Ciytic Acid Value')
    residual_sugar = st.number_input ('Input Residual Sugar Value')
with col2 :
    chlorides = st.number_input ('Input Chlorides Value')
    free_sulfur_dioxide = st.number_input ('Input Free Sulfur Dioxide Value')
    total_sulfur_dioxide = st.number_input ('Input Total Sulfur Dioxide Value')
    density = st.number_input ('Input Density value')
with col3 :
    pH = st.number_input ('Input pH value')
    sulphates = st.number_input ('Input Sulphates Value')
    alcohol = st.number_input ('Input Alcohol Value')

# Predictions
wine_quality = ''

option = st.selectbox(
   'Which Wine Type would like to test for its Quality?',
   ('White Wine', 'Red Wine'),
    # index=None,
    # placeholder ="Select The Wine Type"
    # "Select The Wine Type You Would like to test for its Quality", ["White Wine", "Red Wine"]
)

if st.button('Test Quality Wine'):
    if option == 'White Wine':
        wine_quality = wwine_model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
    elif option == 'Red Wine':
        wine_quality = rwine_model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
st.success(wine_quality)
