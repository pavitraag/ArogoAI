import streamlit as st
import pickle
import numpy as np
import joblib

# Load the best model
model = joblib.load("bm.pkl")
print(type(model))

# Define UI
def main():
    st.title("Mental Health Condition Prediction")
    st.write("Enter your symptoms to receive a prediction and coping suggestions.")
    
    # User input fields
import streamlit as st
import pickle
import numpy as np

# Load the best model
with open('bm1.pkl', 'rb') as file:
    model = pickle.load(file)

# Define UI
def main():
    st.title("Mental Health Condition Prediction")
    st.write("Enter your symptoms to receive a prediction and coping suggestions.")
    
    # User input fields
    school_year = st.number_input("School Year", min_value=1, max_value=12, step=1)
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
    who_bmi = st.number_input("WHO BMI Classification", min_value=0, max_value=4, step=1)
    phq_score = st.number_input("PHQ Score", min_value=0, max_value=27, step=1)
    depression_severity = st.number_input("Depression Severity", min_value=0, max_value=3, step=1)
    gad_score = st.number_input("GAD Score", min_value=0, max_value=21, step=1)
    anxiety_severity = st.number_input("Anxiety Severity", min_value=0, max_value=3, step=1)
    epworth_score = st.number_input("Epworth Score", min_value=0.0, max_value=24.0, step=0.1)
    
    # Convert gender to numerical
    gender_map = {"Male": 0, "Female": 1, "Other": 2}
    gender_num = gender_map[gender]
    
    # Prepare input data
    input_data = np.array([[school_year, age, gender_num, bmi, who_bmi, phq_score, depression_severity, gad_score, anxiety_severity, epworth_score]])
    
    if st.button("Predict"):
        prediction = model.predict(input_data)
        
        if prediction == 0:
            st.success("No significant mental health condition detected.")
        elif prediction == 1:
            st.warning("Signs of Anxiety detected. Consider consulting a professional.")
        elif prediction == 2:
            st.warning("Signs of Depression detected. Consider seeking help.")
        else:
            st.error("Uncertain result. Please consult a specialist.")

if __name__ == "__main__":
    main()