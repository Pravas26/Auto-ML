import streamlit as st
import os

from components.sidebar import sidebar


def upload_page():

    sidebar()

    st.title("🤖 AutoML Studio")

    st.write(
        "Upload your dataset and let AutoML build the best Machine Learning pipeline automatically."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv", "xlsx", "txt", "zip"]
    )

    dataset_name = st.text_input("Dataset Name")

    prompt = st.text_area(
        "Optional Prompt",
        placeholder="Example: Predict employee salary..."
    )

    if uploaded_file:

        st.success("Dataset Uploaded Successfully")

        st.subheader("Dataset Information")

        st.write("**File Name :**", uploaded_file.name)

        st.write(
            "**File Size :**",
            round(uploaded_file.size / 1024, 2),
            "KB"
        )

        extension = os.path.splitext(uploaded_file.name)[1]

        st.write("**File Type :**", extension)

    if st.button("🚀 Run AutoML"):

        if uploaded_file is None:

            st.error("Please upload a dataset first.")

        else:

            st.success("Dataset Ready!")

            from backend.main import Backend

            backend = Backend()

            result = backend.save_dataset(uploaded_file)

            if result["success"]:

                st.success("Dataset Saved Successfully!")

                st.write(result)

            else:

                st.error(result["message"])