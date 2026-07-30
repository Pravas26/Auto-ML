import streamlit as st
from pages.upload import upload_page

st.set_page_config(
    page_title="AutoML Studio",
    page_icon="🤖",
    layout="wide"
)

upload_page()