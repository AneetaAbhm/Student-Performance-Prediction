import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page config
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load model
model = joblib.load('student_model_pipe.pkl')

# Header
st.markdown("## 🎓 Student Performance Predictor")
st.markdown("Fill in the student details below and click **Predict** to see the expected exam score.")

# Input section
st.markdown("### 📋 Student Details")
col1, col2 = st.columns(2)

with col1:
    hours = st.number_input(
        "📚 Hours Studied (1-9)",
        min_value=1,
        max_value=9,
        value=5,
        step=1
    )
    prev_score = st.number_input(
        "📝 Previous Score (40-99)",
        min_value=40,
        max_value=99,
        value=70,
        step=1
    )
    extra = st.selectbox(
        "🏃 Extracurricular Activities",
        options=["Yes", "No"],
        index=0
    )

with col2:
    sleep = st.number_input(
        "😴 Sleep Hours (4-9)",
        min_value=4,
        max_value=9,
        value=7,
        step=1
    )
    papers = st.number_input(
        "📄 Sample Papers Practiced (0-9)",
        min_value=0,
        max_value=9,
        value=3,
        step=1
    )


# Predict button
if st.button("🔮 Predict Score", use_container_width=True):
    input_data = pd.DataFrame({
        'Hours Studied'                    : [hours],
        'Previous Scores'                  : [prev_score],
        'Extracurricular Activities'        : [extra],
        'Sleep Hours'                      : [sleep],
        'Sample Question Papers Practiced' : [papers]
    })

    prediction = model.predict(input_data)
    score = round(float(prediction[0]), 2)

    st.divider()

    # Result display
    st.markdown("### 🎯 Prediction Result")
    col3, col4, col5 = st.columns(3)
    col3.metric("Predicted Score", f"{score} / 100")
    col4.metric("Hours Studied",   f"{hours} hrs")
    col5.metric("Previous Score",  f"{prev_score}")

    # Performance message
    if score >= 80:
        st.success(f"🌟 Excellent! Predicted Score: **{score}** — Keep it up!")
    elif score >= 60:
        st.info(f"👍 Good Performance! Predicted Score: **{score}** — Room to improve!")
    elif score >= 40:
        st.warning(f"⚠️ Average Performance! Predicted Score: **{score}** — Need more effort!")
    else:
        st.error(f"❌ Poor Performance! Predicted Score: **{score}** — Needs serious attention!")

# Footer
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with Streamlit | Student Performance Prediction | Linear Regression</p>",
    unsafe_allow_html=True
)