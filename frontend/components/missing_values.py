import streamlit as st


def missing_table(df):

    st.subheader("Missing Values")

    st.dataframe(
        df,
        use_container_width=True
    )