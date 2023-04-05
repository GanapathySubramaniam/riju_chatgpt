import helper
import streamlit as st
from streamlit_lottie import st_lottie






def ui():
    st.header("Welcome to Riju's Chat Assistant")
    st_lottie(helper.load_lottie('https://assets3.lottiefiles.com/packages/lf20_HwzTSCPPTj.json'))
    



ui()
helper.hide_footer()