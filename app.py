# streamlit_app.py
import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.title("Student Performance Prediction")

# Inputs
gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
education = st.selectbox("Parental Level of Education", [...])
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score", 0, 100)
writing_score = st.number_input("Writing Score", 0, 100)

if st.button("Predict"):
    data = CustomData(gender, ethnicity, education, lunch, prep, reading_score, writing_score)
    pred_df = data.get_data_as_data_frame()
    pipeline = PredictPipeline()
    result = pipeline.predict(pred_df)
    st.success(f"Predicted Score: {result[0]}")
