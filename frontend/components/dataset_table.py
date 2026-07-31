import streamlit as st


def dataset_table(df):

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )