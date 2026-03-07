import streamlit as st
import pandas as pd
import pickle
import os
import joblib

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def load_data():
    csv_path = os.path.join(BASE_DIR, "quikr_car.csv")
    df = pd.read_csv(csv_path)
    df['model'] = df['name'].str.split().str[1]
    df = df.dropna(subset=['model'])
    return df

df = load_data()

@st.cache_resource
def load_model():
    model_path = os.path.join(BASE_DIR, "car_price_model.pkl")
    return joblib.load(model_path)

pipe = load_model()

st.title("🚗 Car Price Prediction System")
st.write("Enter the car details below to estimate the price.")

st.markdown("### 🚘 Car Details")

col1, col2 = st.columns(2)

valid_brands = [ "Audi","BMW","Chevrolet","Datsun","Fiat","Force","Ford", "Hindustan","Honda","Hyundai","Jaguar","Jeep","Land", "Mahindra","Maruti","Mercedes","Mini","Mitsubishi", "Nissan","Renault","Skoda","Tata","Toyota","Volkswagen","Volvo" ]

with col1:
    company = st.selectbox("Company", valid_brands)

    models = sorted(df[df['company'] == company]['model'].unique())
    car_model = st.selectbox("Model", models)

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol","Diesel","CNG"])

    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        max_value=300000,
        step=1000,
        value=30000
    )

year = st.slider("Year", 2005, 2025, 2015)


st.sidebar.title("About this App")

st.sidebar.info(
"""
This ML model predicts used car prices based on:

• Company  
• Model  
• Year  
• Kilometers Driven  
• Fuel Type
"""
)


def format_price(price):
    return f"₹ {price/100000:.2f} Lakh"

if st.button("🚀 Predict Price"):

    input_df = pd.DataFrame({
        "company":[company],
        "model":[car_model],
        "year":[year],
        "kms_driven":[kms_driven],
        "fuel_type":[fuel_type]
    })

    with st.spinner("Calculating price..."):
        prediction = pipe.predict(input_df)

    st.markdown("## Prediction Result")

    col1, col2 = st.columns(2)

    # LEFT COLUMN → Car Details
    with col1:
        st.markdown("### 🚘 Car Details")
        st.write(f"**Company:** {company}")
        st.write(f"**Model:** {car_model}")
        st.write(f"**Year:** {year}")
        st.write(f"**Fuel Type:** {fuel_type}")
        st.write(f"**Kilometers Driven:** {kms_driven:,} km")

    # RIGHT COLUMN → Price Card
    with col2:
        st.markdown(f"""
        <div style="
        padding:30px;
        border-radius:12px;
        background-color:#f5f7fa;
        border:1px solid #ddd;
        text-align:center;
        font-size:24px;
        font-weight:bold;
        color:#2c3e50;
        ">
        🚗 Estimated Car Price<br><br>
        <span style="font-size:40px;color:#27ae60;">
        {format_price(prediction[0])}
        </span>
        </div>
        """, unsafe_allow_html=True)