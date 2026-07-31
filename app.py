import streamlit as st

from frontend.pages.upload import upload_page

st.set_page_config(
    page_title="DeepArchitect",
    page_icon="🤖",
    layout="wide"
)

upload_page()