import streamlit as st


def sidebar():

    with st.sidebar:

        st.title("🤖 AutoML Studio")

        st.markdown("---")

        st.write("### Supported Datasets")

        st.success("CSV")
        st.success("Excel")
        st.success("Text")
        st.success("Image Folder")

        st.markdown("---")

        st.write("Developer Version 1.0")