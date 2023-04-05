import yaml
from yaml.loader import SafeLoader
import streamlit as st
import requests
import openai

def generate(content,messages):
    api_key=read_yaml('secrets.yaml')['api_key']
    openai.api_key =api_key
    messages.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    chat_response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})
    return chat_response,messages
     


     


def load_lottie(url): 
    response = requests.get(url)
    lottie_data = response.json()
    return lottie_data

def hide_footer():
        
        hide_streamlit_style = """
                        <style>
                                footer {visibility: hidden;}
                        </style>
                        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def read_yaml(file_path):
    with open(file_path) as f:
        config_dict = yaml.load(f, Loader=SafeLoader)
    return config_dict