import streamlit as st
from transformers import pipeline

# Define a function to summarize text
def summarize_text(text):
    """Summarizes the given text using the Bart summarization pipeline from Transformers."""
    summarizer = pipeline("summarization", device=0)
    summary = summarizer(text, max_length=100)
    return summary

# Create a Streamlit layout
st.title("Text Summarization App")
text = st.text_area("Enter text to summarize:")

# Summarize the text
if st.button("Summarize"):
    summary = summarize_text(text)
    st.write(summary)
