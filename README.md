# Depression and Anxiety 

Depression and Anxiety Dataset is a machine learning-based system for predicting mental health conditions like depression and anxiety. The model is trained using real-world mental health survey data and employs feature engineering, preprocessing, and model selection techniques to ensure high accuracy.

---

## 📂 Dataset Preprocessing

### 1️⃣ Data Cleaning
- Missing values in `depression_diagnosis` and `anxiety_diagnosis` were replaced with `0`.
- Categorical values (e.g., `depression_severity`, `anxiety_severity`) were converted to numerical values using predefined mappings.
- Boolean-like categorical columns were transformed into numerical binary values (`0` and `1`).

### 2️⃣ Feature Engineering
- **Encoding**: Label Encoding was applied to categorical features (`gender`, `who_bmi`).
- **Scaling**: Numerical features were normalized using `StandardScaler`.
- **Feature Selection**: Used `SelectKBest` with an ANOVA F-test to pick the most relevant features.

### 3️⃣ Splitting the Dataset
- The dataset was split into **80% training** and **20% testing** using `train_test_split`, ensuring stratified sampling.

---

## 🎯 Model Selection Rationale

ArogoAI uses **Random Forest** and **XGBoost** classifiers for predicting depression and anxiety diagnoses. Both models were trained and evaluated using:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **ROC-AUC Score**

After evaluating both models, the best-performing one was **selected dynamically** based on **F1-score performance**.

---

## 🚀 Running the Inference Script

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/pavitraag/ArogoAI
cd ArogoAI
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Inference
```bash
python inference.py --input "sample_data.csv"
```

---

## 🖥️ UI/CLI Usage Instructions

### 1️⃣ Command-Line Interface (CLI)
Run the following command to get predictions:
```bash
python inference.py --input "sample_data.csv"
```
The script will output:
```yaml
Predicted Depression Diagnosis: 1 (Yes)
Predicted Anxiety Diagnosis: 0 (No)
```

### 2️⃣ Web Interface (Optional)
Start the UI using:
```bash
streamlit run app.py
```
Upload your dataset and get mental health predictions.

---

## 🏆 Model and Artifacts
- `bm1.pkl` - The best-trained model.
- `scaler.pkl` - The scaler used for normalization.

---

## 🚀 Running the Streamlit Web App

ArogoAI provides a **web-based interface** using **Streamlit** to help users easily input their symptoms and get mental health condition predictions.

### 1️⃣ Install Dependencies
Ensure you have Streamlit installed:
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Web App
```bash
streamlit run app.py
```

### 3️⃣ Using the Web Interface
- Open the displayed **local URL** in your browser.
- Enter the following details:
  - **School Year** (1-12)
  - **Age** (10-100)
  - **Gender** (Male, Female, Other)
  - **BMI** (10.0 - 50.0)
  - **WHO BMI Classification** (0-4)
  - **PHQ Score** (0-27)
  - **Depression Severity** (0-3)
  - **GAD Score** (0-21)
  - **Anxiety Severity** (0-3)
  - **Epworth Score** (0.0 - 24.0)

---

This project aims to help early detection of mental health conditions using AI-based insights. 🚀💡

