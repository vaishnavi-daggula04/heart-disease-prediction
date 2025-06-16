# ❤️ Heart Disease Prediction App

A web-based machine learning app built using **Streamlit** that predicts the likelihood of heart disease based on medical parameters.

---

## 📊 About the Project

This project uses a **Logistic Regression model** trained on the **Cleveland Heart Disease dataset** to predict whether a patient has heart disease. Users can input health data using the Streamlit interface and get real-time predictions.

---

## 🔍 Features

- 🔢 Input fields for 13 medical parameters like age, cholesterol, blood pressure, etc.
- 🧠 Model trained using scikit-learn's Logistic Regression
- 📈 Model Accuracy: ~73%
- 💻 Interactive Web UI using Streamlit
- 🧾 Clean, minimal design with dark theme

---

## 🗃 Dataset Used

- **Name**: Cleveland Heart Disease dataset  
- **Source**: UCI Machine Learning Repository  
- **Samples**: 297  
- **Features**: 13  
- **Target**: 0 = No Heart Disease, 1 = Heart Disease  

---

## 🏗 Project Structure

heart-disease-prediction/
├── app.py # Streamlit web app
├── logistic_model.pkl # Trained ML model
├── heart_cleveland_upload.csv # Dataset used
├── README.md # Project description
├── requirements.txt # Python packages

---

## 🚀 How to Run the App Locally

1. Clone the repo:
git clone https://github.com/vaishnavi-daggula04/heart-disease-prediction.git
cd heart-disease-prediction

2. Create a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install required packages:
pip install -r requirements.txt

4.Run the app:
streamlit run app.py

🧠 Model Input Features

| Feature                   | Description                                         |
| ------------------------- | --------------------------------------------------- |
| Age                       | Age in years                                        |
| Sex                       | 0 = Female, 1 = Male                                |
| Chest Pain Type (cp)      | 0–3 categorical                                     |
| Resting Blood Pressure    | in mm Hg                                            |
| Cholesterol               | in mg/dl                                            |
| Fasting Blood Sugar > 120 | 1 = True, 0 = False                                 |
| Resting ECG Results       | 0–2 categorical                                     |
| Max Heart Rate Achieved   | Numeric value                                       |
| Exercise Induced Angina   | 1 = Yes, 0 = No                                     |
| ST Depression (oldpeak)   | Numeric value                                       |
| Slope of ST Segment       | 0 = upsloping, 1 = flat, 2 = downsloping            |
| Number of Major Vessels   | 0–3                                                 |
| Thalassemia               | 1 = normal, 2 = fixed defect, 3 = reversible defect |

👩‍💻 Author
Vaishnavi Daggula

GitHub: vaishnavi-daggula04

✅ Final Layout Example (Snipped)
...

---

## 🚀 How to Run the App Locally
(...steps...)

---

## ✅ Optional: Deploy on Streamlit Cloud (FREE Hosting)

To make your project live online:

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Click **"New App"**
4. Select your repo: `vaishnavi-daggula04/heart-disease-prediction`
5. Set the **main file path** as: `app.py`
6. Click **"Deploy"**

It will host your app at `https://yourname.streamlit.app` 🎉

---

## 📌 License

This project is open source and available under the [MIT License](LICENSE).
