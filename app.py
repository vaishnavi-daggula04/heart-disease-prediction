import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("models/logistic_model.pkl", "rb"))

# App title
st.title("❤️ Heart Disease Prediction App")
st.write("Enter the details below to check the risk of heart disease.")

# Collecting user input
age = st.number_input("Age", min_value=1, max_value=120, value=25)
sex = st.selectbox("Sex", ("Male", "Female"))
cp = st.selectbox("Chest Pain Type (0: typical angina, 1: atypical angina, 2: non-anginal pain, 3: asymptomatic)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG results", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST depression induced by exercise", value=1.0)
slope = st.selectbox("Slope of the peak exercise ST segment", [0, 1, 2])
ca = st.selectbox("Number of major vessels (0–3) colored by fluoroscopy", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (0 = normal; 1 = fixed defect; 2 = reversable defect; 3 = unknown)", [0, 1, 2, 3])

# Convert inputs to model format
sex_val = 1 if sex == "Male" else 0

input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])

# Predict and display result
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "🛑 High Risk of Heart Disease!" if prediction[0] == 1 else "✅ No Heart Disease Detected."
    st.subheader("Prediction Result:")
    st.success(result)
