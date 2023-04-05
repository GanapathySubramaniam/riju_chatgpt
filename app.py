from st_pages import Page,show_pages
import streamlit as st

show_pages([
    Page("pages/1_Home.py", "Home", " "),
    Page("pages/2_Chat_Assistant.py", "Chat Assistant", " "),
])

