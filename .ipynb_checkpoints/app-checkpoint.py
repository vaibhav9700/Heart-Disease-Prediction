import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Heart Health AI", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: black;
}
.main {
    background: linear-gradient(to right, #000000, #1a1a1a);
}
.hero {
    background-image: url("https://images.unsplash.com/photo-1588776814546-ec7e6c9a9c75");
    background-size: cover;
    padding: 120px;
    text-align: center;
    color: white;
}
.hero h1 {
    font-size: 50px;
    color: #ff4b4b;
}
.section {
    background-color: #f2f2f2;
    padding: 50px;
    border-radius: 15px;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<div class="hero">
    <h1>❤️ EXAMINING YOUR HEART'S HEALTH</h1>
    <h3>AI Powered Heart Disease Prediction System</h3>
</div>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
model = pickle.load(open("heart_model.pkl", "rb"))

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("## 🫀 Enter Patient Data")

# ---------- INPUT SECTION ----------
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")
        sex = st.selectbox("Sex", ["Female", "Male"])
        cp = st.number_input("Chest Pain Type")

    with col2:
        trestbps = st.number_input("Resting Blood Pressure")
        chol = st.number_input("Cholesterol")
        fbs = st.selectbox("Fasting Blood Sugar >120", ["No", "Yes"])

    with col3:
        thalach = st.number_input("Max Heart Rate")
        exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
        oldpeak = st.number_input("Oldpeak")

    slope = st.number_input("Slope")
    ca = st.number_input("Number of Major Vessels")
    thal = st.number_input("Thal")

sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0

if st.button("🔍 Predict Now"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            0, thalach, exang, oldpeak,
                            slope, ca, thal]])

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("💚 Patient is Healthy")
    else:
        st.error("💔 High Risk of Heart Disease")
