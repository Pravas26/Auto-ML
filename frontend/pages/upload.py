import streamlit as st

from backend.main import Backend
from frontend.components.sidebar import sidebar
from frontend.pages.dashboard import dashboard


backend = Backend()


def upload_page():

    sidebar()

    st.title("Dataset Upload")

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv", "xlsx"]
    )

    if uploaded_file:

        with st.spinner("Uploading Dataset..."):

            result = backend.save_dataset(uploaded_file)

        if result["success"]:

            st.success("Dataset Uploaded Successfully!")

            dashboard(result)

        else:

            st.error(result["message"])