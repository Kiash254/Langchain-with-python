import streamlit as st
from langchain.llms import open_weather_api_client
st.title('🦜🔗 Quickstart App')
#Want to use langchain with OpenWeather API? Get your API key here: https://openweathermap.org/api and after checking the weather using langchain we can be able to tell the user the condtion of the weather in their location.
openweather_api_key = st.sidebar.text_input('OpenWeather API Key')

def generate_response(input_text):
    llm = open_weather_api_client(temperature=0.7, openweather_api_key=openweather_api_key)
    st.info(llm(input_text))
    
with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is the weather like in my location?')
    submitted = st.form_submit_button('Submit')
    if not openweather_api_key.startswith('sk-'):
        st.warning('Please enter your OpenWeather API key!', icon='⚠')
    if submitted and openweather_api_key.startswith('sk-'):
        generate_response(text)
           