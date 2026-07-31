import streamlit as st


def summary_card(result):

    st.header("Dataset Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", result["rows"])

    c2.metric("Columns", result["columns"])

    c3.metric("File Type", result["extension"])

    c4.metric("Size (KB)", result["size"])