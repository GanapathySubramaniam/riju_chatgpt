import streamlit as st
import requests
import helper
from streamlit_lottie import st_lottie

if 'messages' not in st.session_state.keys():
    st.session_state['messages']= []

def callback(button_name):
    st.session_state[button_name]=True


def add_to_session_state(key,value):
    if key not in st.session_state.keys():
        st.session_state[key]=value
    
add_to_session_state('Submit',False)
add_to_session_state('Restart Chat',False)


def ui():
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Riju's Chat Assistant")
    with col2:
        st_lottie(helper.load_lottie('https://assets10.lottiefiles.com/packages/lf20_jh9gfdye.json'))
    with col3:
        st_lottie(helper.load_lottie('https://assets9.lottiefiles.com/packages/lf20_jAaRKGyuDD.json'))
    
        
    prompt=st.text_area("Enter the Prompt")

    if st.button('Submit',on_click=callback,args=['Submit']) or st.session_state['Submit']:     
        with st.spinner('Loading'):
            messages=st.session_state['messages']
            response,messages=helper.generate(prompt,messages)
            st.session_state['messages']=messages
            st.write(response)
            
            

    

    


ui()
helper.hide_footer()