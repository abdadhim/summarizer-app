# app.py

import streamlit as st
from transformers import pipeline

# Initialize summarization pipeline with the chosen language model
language_model = "t5-small"  # You can choose a model that supports language complexity
summarizer = pipeline("summarization", model=language_model)

st.title("Text Summarization App")

long_text = st.text_area("Enter your long text here:")

max_length = st.slider("Select the maximum length of the summary", min_value=30, max_value=300, value=150)

# Language complexity selection
language_complexity = st.selectbox("Select Language Complexity", ["Simple", "Intermediate", "Advanced"])

if st.button("Generate Summarized Text"):
    if long_text:
        # Adjust the language model based on the user's selection
        if language_complexity == "Simple":
            language_model = "t5-small"
        elif language_complexity == "Intermediate":
            language_model = "t5-base"
        elif language_complexity == "Advanced":
            language_model = "t5-large"

        summarizer = pipeline("summarization", model=language_model)

        summary = summarizer(long_text, max_length=max_length, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text.")
