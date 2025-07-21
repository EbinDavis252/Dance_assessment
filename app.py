import streamlit as st
from modules import talent_evaluator, academy_analytics, recommender, knowledge_ai

st.set_page_config(page_title="Dance Intelligence Platform", layout="wide")

st.sidebar.title("DIP Navigation")
module = st.sidebar.radio("Go to Module", (
    "Talent Evaluator", "Academy Analytics", "Recommendation System", "Dance Knowledge AI"))

if module == "Talent Evaluator":
    talent_evaluator.run()

elif module == "Academy Analytics":
    academy_analytics.run()

elif module == "Recommendation System":
    recommender.run()

elif module == "Dance Knowledge AI":
    knowledge_ai.run()

st.sidebar.markdown("---")
st.sidebar.info("📍 DIP (Pose Feedback disabled for Streamlit Cloud)")
