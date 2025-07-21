import streamlit as st
import joblib

def run():
    st.header("💃 Talent Evaluator")
    model = joblib.load("models/dropout_predictor.pkl")

    age = st.slider("Age", 5, 25)
    attendance = st.slider("Attendance (%)", 50, 100)
    scores = st.slider("Dance Score (out of 100)", 0, 100)

    if st.button("Evaluate"):
        pred = model.predict([[age, attendance, scores]])
        st.success("🎯 Likely to Continue" if pred[0] == 0 else "⚠️ At Risk of Dropping Out")
