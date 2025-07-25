import streamlit as st
import pickle
import json
import pandas as pd

# Load trained model and features list
with open('rainfall_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('features.json', 'r') as f:
    features = json.load(f)

# Extract valid cities and months from feature columns
city_keys = [col for col in features if col.startswith('SUBDIVISION_')]
month_keys = [col for col in features if col.startswith('MONTH_')]

# User-friendly display names for dropdowns, paired with internal key names
city_display = [key.replace('SUBDIVISION_', '').replace('_', ' ') for key in city_keys]
city_map = dict(zip(city_display, city_keys))

month_display = [key.replace('MONTH_', '') for key in month_keys]
month_map = dict(zip(month_display, month_keys))

# Streamlit UI
st.title("Monthly Rainfall Prediction App")

city_name = st.selectbox("Select city/state:", city_display)
month_name = st.selectbox("Select month:", month_display)
year = st.number_input("Enter year:", min_value=1901, max_value=2100, value=2020)

# Prepare input row using only model-supported columns
row = {col: 0 for col in features}
row['YEAR'] = year

# Always valid: get internal key from selected name
row[city_map[city_name]] = 1
row[month_map[month_name]] = 1

input_df = pd.DataFrame([row])

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted rainfall in {city_name.title()}, {month_name}, {year}: {prediction:.2f} mm")

