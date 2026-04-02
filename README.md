# Student-Performance-Prediction
### Linear Regression | Machine Learning 

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6.0-orange?style=flat-square&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit)](https://student-performance-prediction-linearregression.streamlit.app/)

---

## 📌 Project Overview

This project builds a **Linear Regression model** to predict a student's final exam score
based on their study habits and lifestyle factors.

The model is trained on a dataset of **10,000 student records** and achieves an
**R² score of 0.989**, meaning it explains **98.9% of the variance** in exam scores.

A **Streamlit web application** is also built to allow users to input student details
and get an instant predicted score.

---

## 🎯 Problem Statement

> Given a student's study habits and lifestyle information,
> predict their final exam **Performance Index** (score out of 100).

---

## 📂 Project Structure

```
student-performance-regression/
│
├── student_performance.ipynb     ← Main Jupyter Notebook (ML code)
├── app.py                        ← Streamlit web application
├── student_model.pkl             ← Saved trained model
├── student_model_pipe.pkl        ← Saved pipeline (with preprocessor)
├── requirements.txt              ← Python dependencies
└── README.md                     ← Project documentation
```

---

## 📊 Dataset Description

| Column | Type | Role | Description |
|--------|------|------|-------------|
| Hours Studied | Integer (1–9) | Input | Daily hours spent studying |
| Previous Scores | Integer (40–99) | Input | Score from previous exam |
| Extracurricular Activities | Categorical (Yes/No) | Input | Participation in activities |
| Sleep Hours | Integer (4–9) | Input | Average nightly sleep hours |
| Sample Question Papers Practiced | Integer (0–9) | Input | Practice papers solved |
| Performance Index | Float (10–100) | **Output** | Final exam score to predict |

- **Total Records:** 10,000 rows
- **Missing Values:** None
- **Duplicates:** None

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| Jupyter Notebook | Development environment |
| pandas | Data loading and manipulation |
| numpy | Numerical computations |
| scikit-learn | Model building and evaluation |
| matplotlib | Data visualization |
| seaborn | Correlation heatmap |
| Streamlit | Web application |
| joblib | Model saving and loading |

---

## 🔄 Project Workflow

```
Dataset (CSV)
     ↓
Data Loading & Exploration
     ↓
Preprocessing
  ├── Check missing values
  ├── Check duplicates
  ├── Encode Extracurricular Activities (Yes→1 / No→0)
  └── Train / Test Split (80% / 20%)
     ↓
Correlation Analysis
     ↓
Model Training (Linear Regression)
     ↓
Model Evaluation (MAE, MSE, RMSE, R²)
     ↓
Visualizations
     ↓
Unseen Data Prediction (25 random rows)
     ↓
Pipeline Creation (Imputer + Encoder + Model)
     ↓
Streamlit Web App
```

---

## 📈 Correlation Analysis

| Feature | Correlation with Performance Index |
|---------|-----------------------------------|
| Previous Scores | **0.92** ← strongest |
| Hours Studied | **0.37** |
| Sleep Hours | 0.05 |
| Sample Question Papers | 0.04 |
| Extracurricular Activities | 0.02 |

> No multicollinearity detected between input features (all < 0.05).
> All 5 features are retained.

---

## ✅ Model Evaluation Results

| Metric | Value | Interpretation |
|--------|-------|----------------|
| MAE | **1.6111** | Average error of only 1.6 marks |
| MSE | **4.0826** | Very low squared error |
| RMSE | **2.0206** | Predictions within ±2 marks |
| R² Score | **0.9890** | Model explains 98.9% of variance ✅ |

---

## 📉 Visualizations

### 1. Correlation Heatmap
Shows relationships between all features and the target variable.

> <img width="758" height="590" alt="image" src="https://github.com/user-attachments/assets/e7b966ec-0dce-4d44-b31c-46cbd0188c10" />


### 2. Actual vs Predicted Plot
Scatter plot showing how close predictions are to actual scores.
Dots fall very close to the red diagonal line — confirming strong model fit.

> <img width="695" height="547" alt="image" src="https://github.com/user-attachments/assets/1a0a720c-6d9d-401b-a133-db4acb072ed2" />


### 3. Residuals Plot
Residuals are randomly scattered around 0 — confirming no pattern in errors
and that Linear Regression is appropriate for this dataset.

> <img width="690" height="547" alt="image" src="https://github.com/user-attachments/assets/3d031c90-bc20-4546-971d-b9610d929dca" />


### 4. Feature Coefficients Plot
Previous Scores has the highest coefficient — confirming it is the most
influential feature in predicting the exam score.

> <img width="887" height="547" alt="image" src="https://github.com/user-attachments/assets/3c14cf3d-ec07-4623-b36d-e49569b02e85" />

---

## 🔁 Pipeline

A **scikit-learn Pipeline** was created to bundle preprocessing and the model together:

```
Raw Data (Yes/No)
      ↓
ColumnTransformer
  ├── Numerical columns  → SimpleImputer (mean)
  └── Categorical column → SimpleImputer (most_frequent) → OrdinalEncoder
      ↓
LinearRegression Model
      ↓
Predicted Score
```

The pipeline is saved as `student_model_pipe.pkl` and can be used directly
with raw `Yes/No` input — no manual encoding required.

---

## 🔮 Unseen Data Prediction

25 random rows were sampled from the original dataset and fed to the model.

Results showed:
- Predicted scores were consistently within **±2 marks** of actual scores
- Confirms the model **generalizes well** to new unseen data

> <img width="996" height="470" alt="image" src="https://github.com/user-attachments/assets/ea0ca982-e704-467f-b29e-07c834e65070" />

---

## 🖥️ Streamlit App

A simple and clean web application was built using Streamlit.

**Features:**
- Input fields for all 5 student features
- Instant score prediction on button click
- Performance message based on predicted score
  - 🌟 Excellent (≥ 80)
  - 👍 Good (≥ 60)
  - ⚠️ Average (≥ 40)
  - ❌ Poor (< 40)

> <img width="1908" height="863" alt="image" src="https://github.com/user-attachments/assets/f538d456-99a3-40df-8f57-4ac6514d671f" />
> <img width="1891" height="794" alt="image" src="https://github.com/user-attachments/assets/6d00053a-62f6-4b5d-a322-622696c8cd52" />


### Run the app:
```bash
streamlit run app.py
```

---

## 🚀 How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/student-performance-regression.git
cd student-performance-regression
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebook
```bash
jupyter notebook student_performance.ipynb
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

---
## 🌍 Deployment
 
The app is deployed on **Streamlit Community Cloud** — free hosting for Streamlit apps.
 
| Detail | Info |
|--------|------|
| Platform | Streamlit Community Cloud |
| URL | [https://student-performance-prediction-linearregression.streamlit.app/](https://student-performance-prediction-linearregression.streamlit.app/) |
| Status | ✅ Live |
| Auto-redeploy | Yes — updates automatically on every GitHub push |
 
---
## 📦 Requirements

```
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.6.0
matplotlib==3.9.2
seaborn==0.13.2
streamlit==1.40.0
joblib==1.4.2
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 📝 Key Observations

- **Previous Scores** is by far the strongest predictor (correlation = 0.92)
- **No scaling required** — Linear Regression is scale independent (OLS formula)
- **No hyperparameter tuning needed** — Linear Regression has no hyperparameters
- **No outliers or skewness** detected in the dataset
- The model achieves near perfect R² = 0.989 on test data

---

## 🙋 Author

**Aneeta Abraham**
---
