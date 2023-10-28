import streamlit as st

st.set_page_config(layout="wide")

# with st.sidebar:
#     pass

st.title("Custom Summarizer")
# st.write("Summarizer [for learning.](/What_is_CUTS-RL)")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Input")

    text = st.text_area("Enter text:", height=200, placeholder="Enter text here", label_visibility="collapsed")
    if st.button("Submit", type="primary"):
        # Perform summarization
        # Display the summarized text
        pass
    
    with st.expander("Settings", expanded=True):
        st.radio(
            "Summarize to:",
            key="summarize_to",
            options=["Paragraphs", "Bullet Points"],
        )

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
        
        on = st.toggle("Add Quiz Section📝")
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
        placeholder="Enter API key",
    )

    # YouTube Summary
    # text_input = st.text_input(
    #     "Summarize YouTube video",
    #     placeholder="Enter link",
    # )

with col2:
    st.subheader("Output")

if __name__ == "__main__":
    # Include all the UI components and functions here
    pass
