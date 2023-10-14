from langchain.llms import OpenAI
import streamlit as st
import os

st.sidebar.title('OpenAI API Key')
openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key')

if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
else:
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    
    with st.form('question_form'):
        question = st.text_input('Ask a question:')
        submitted = st.form_submit_button('Submit')
        
        if submitted:
            result = llm.generate(
                text=f'Question: {question}\n\nAnswer:',
                max_tokens=50
            )
            st.write(result)