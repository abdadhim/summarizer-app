import streamlit as st
import json
import requests
import re

API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

# <><><><><><> BEGINNING OF PAGE <><><><><><>
st.set_page_config(layout="wide")

# with st.sidebar:
#     pass

st.title("Custom Summarizer")
# st.write("Summarizer [for learning.](/What_is_CUTS-RL)")

output = []
data = [{'summary_text': ''}]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Input")

    text = st.text_area("Enter text:", height=200, placeholder="Enter text here ...", label_visibility="collapsed")
    if st.button("Submit", type="primary"):
        data = query(
            {
                "inputs": f"{text}",
                "parameters": {"do_sample": False},
            }
        )        
        # pass
    
    with st.expander("Settings", expanded=True):
        sum_to = st.radio(
            "Summarize to:",
            key="summarize_to",
            options=["Paragraphs", "Bullet Points"],
        )
        if sum_to =="Paragraphs":
            output.append(data[0]['summary_text'])
        elif sum_to =="Bullet Points":
            summary_text = data[0]['summary_text']
            sentences = re.split(r'\.\s+', summary_text)
            bullet_points = [f"- {sentence}" for sentence in sentences if sentence.strip()]

            for i in range(len(bullet_points)):
                output.append(bullet_points[i])

        st.radio(
            "Summarize into:",
            key="summarize_into",
            options=["One section", "Few sections"],
        )

        on = st.toggle('Simplify Language', value=True)
        # if on:
        #     st.write('Headings included!')
        on = st.toggle('Add Heading(s)')
        # if on:
        #     st.write('Headings included!')

        brevity = st.select_slider("Summary Length:", options=['Short', 'Medium', 'Long'])
        
        on = st.toggle("Add Quiz Section 📝")
        if on:
            # st.write('Headings included!')
            # on = st.toggle('Ask me to fill in the blanks')
            on = st.checkbox("Ask me to fill in the blanks", key="fill_blanks")
            if on:
                pass
            # on = st.toggle('Ask me to re-write the summary')
            on = st.checkbox('Ask me to re-write the summary', key='rewrite')
            if on:
                pass
    
    with st.expander("Advanced Settings"):
        option = st.selectbox(
            'Model to use:',
            ('BART', 'T5', 'Llama', 'GPT'))
        # st.write('You selected:', option)        
        
        st.radio(
            "Type of summarization:",
            key="summarize_type",
            options=["Abstractive", "Extractive"],
        )

    # Hugging Face API key
    text_input = st.text_input(
        "🤗 Hugging Face API key",
        placeholder="Enter API key", type="password"
    )

    # YouTube Summary
    # text_input = st.text_input(
    #     "Summarize YouTube video",
    #     placeholder="Enter link",
    # )

with col2:
    st.subheader("Output")
    for o in output:
        st.markdown(o)

if __name__ == "__main__":
    # Include all the UI components and functions here
    pass
