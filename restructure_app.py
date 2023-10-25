import langchain
import streamlit as st
import requests

# Define the LLM model
huggingface_model = "bart-large-cnn"

# Create a LangChain task for converting long passages into headings and bullet points
headings_and_bullet_points_task = langchain.Task(
    name="headings_and_bullet_points",
    inputs=["text"],
    outputs=["headings", "bullet_points"],
    model=huggingface_model,
    api_key="YOUR_HUGGINGFACE_API_KEY",
)

# Define a Streamlit app
@st.cache
def convert_text_to_headings_and_bullet_points(text):
    """Converts the given text into headings and bullet points using the HuggingFace Inference API."""
    response = requests.post(
        "https://api-inference.huggingface.co/models/{}/inference".format(huggingface_model),
        json={"inputs": {"text": text}},
    )
    headings = response.json()["outputs"]["headings"]
    bullet_points = response.json()["outputs"]["bullet_points"]
    return headings, bullet_points

# Create a Streamlit layout
st.title("headings and bullet points Web App")
text = st.text_area("Enter text to convert to headings and bullet points:")

# Convert the text to headings and bullet points
if st.button("Convert"):
    headings, bullet_points = convert_text_to_headings_and_bullet_points(text)

    # Display the headings and bullet points
    st.header("Headings")
    for heading in headings:
        st.markdown(f"## {heading}")

    st.header("Bullet Points")
    for bullet_point in bullet_points:
        st.markdown(f"* {bullet_point}")
