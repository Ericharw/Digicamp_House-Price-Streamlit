import streamlit as st
import joblib
import pandas as pd

st.title("Predict House Price")

try:
    model = joblib.load("house_price_model.pkl")
    columns = joblib.load("feature_columns.pkl")
except Exception as e:
    st.error(e)
    st.stop()

inputs = {}
inputs["GrLivArea"] = st.number_input("Luas Bangunan (sqft)", min_value=0)
inputs["LotArea"] = st.number_input("Luas Tanah (sqft)", min_value=0)
inputs["TotalBsmtSF"] = st.number_input("Luas Basement (sqft)", min_value=0)
inputs["BedroomAbvGr"] = st.number_input("Jumlah Kamar Tidur", min_value=0)
inputs["FullBath"] = st.number_input("Jumlah Kamar Mandi", min_value=0)
inputs["TotRmsAbvGrd"] = st.number_input("Total Ruangan", min_value=0)
inputs["OverallQual"] = st.slider("Kualitas Rumah", 1, 10, 5)
inputs["OverallCond"] = st.slider("Kondisi Rumah", 1, 10, 5)
inputs["KitchenQual"] = st.slider("Kualitas Dapur", 1, 5, 3)
inputs["GarageCars"] = st.number_input("Kapasitas Garasi", min_value=0)
inputs["GarageArea"] = st.number_input("Luas Garasi (sqft)", min_value=0)

neighborhood_mapping = {
    "Blmngtn": 0, "Blueste": 1, "BrDale": 2, "BrkSide": 3,
    "ClearCr": 4, "CollgCr": 5, "Crawfor": 6, "Edwards": 7,
    "Gilbert": 8, "IDOTRR": 9, "MeadowV": 10, "Mitchel": 11,
    "NAmes": 12, "NPkVill": 13, "NWAmes": 14, "NoRidge": 15,
    "NridgHt": 16, "OldTown": 17, "SWISU": 18, "Sawyer": 19,
    "SawyerW": 20, "Somerst": 21, "StoneBr": 22, "Timber": 23,
    "Veenker": 24
}

inputs["Neighborhood"] = neighborhood_mapping[
    st.selectbox("Lokasi / Neighborhood", neighborhood_mapping.keys())
]

if st.button("Predict"):
    df = pd.DataFrame([inputs])
    df = df[columns]
    prediction = model.predict(df)[0]
    st.success(f"Prediksi Harga Rumah: {prediction:,.2f}")
