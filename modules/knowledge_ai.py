import streamlit as st
import json
import random

def run():
    st.header("🧠 Dance Knowledge AI")

    with open("data/dance_knowledge.json", "r") as f:
        knowledge = json.load(f)

    question = st.text_input("Ask a dance-related question")

    if question:
        answer = None
        for q, a in knowledge.items():
            if q.lower() in question.lower():
                answer = a
                break

        if not answer:
            answer = random.choice(list(knowledge.values()))

        st.success(f"💡 {answer}")
