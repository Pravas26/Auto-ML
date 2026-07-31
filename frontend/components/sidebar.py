import streamlit as st


def sidebar():

    with st.sidebar:

        st.title("🤖 DeepArchitect")

        st.markdown("---")

        st.subheader("📂 Supported Datasets")

        st.success("CSV")
        st.success("Excel (.xlsx)")
        st.success("Text (.txt)")
        st.success("Image Folder (.zip)")

        st.markdown("---")

        st.subheader("⚙️ Workflow")

        st.write("1️⃣ Upload Dataset")
        st.write("2️⃣ Analyze Dataset")
        st.write("3️⃣ Train Models")
        st.write("4️⃣ Compare Results")
        st.write("5️⃣ Best Model")

        st.markdown("---")

        st.info("Version 1.0")

        st.caption("Built with ❤️ using Streamlit")