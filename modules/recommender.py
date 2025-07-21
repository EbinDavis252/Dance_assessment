import streamlit as st
import pandas as pd

def run():
    st.header("🤖 Choreography Recommender")

    df = pd.read_csv("data/choreography_data.csv")
    genre = st.selectbox("Select Genre", df["genre"].unique())

    recommendations = df[df["genre"] == genre].sample(3)
    st.write("Top Recommendations:")
    st.table(recommendations[["title", "difficulty", "duration"]])
