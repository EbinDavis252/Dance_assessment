import streamlit as st
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.header("📊 Academy Analytics")
    conn = sqlite3.connect("data/student_data.db")
    df = pd.read_sql("SELECT * FROM students", conn)

    st.dataframe(df)

    st.subheader("Enrollment by Level")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="level", ax=ax)
    st.pyplot(fig)

    st.subheader("Dropout Analysis")
    fig2, ax2 = plt.subplots()
    sns.histplot(data=df, x="dropout_risk", bins=5, ax=ax2)
    st.pyplot(fig2)
