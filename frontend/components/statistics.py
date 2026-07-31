import streamlit as st


def statistics_table(df):

    st.subheader("Statistics")

    st.dataframe(
        df,
        use_container_width=True
    )