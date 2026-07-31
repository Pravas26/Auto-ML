import streamlit as st

from frontend.components.summary_card import summary_card
from frontend.components.dataset_table import dataset_table
from frontend.components.statistics import statistics_table
from frontend.components.missing_values import missing_table


def dashboard(result):

    summary_card(result)

    st.divider()

    dataset_table(result["preview"])

    st.divider()

    statistics_table(result["statistics"])

    st.divider()

    missing_table(result["missing"])