import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Recommendations",
    page_icon="👨🏼‍🔬",
    layout="centered",  # wide
    initial_sidebar_state="auto")

st.title("FINAL RECOMMENDATIONS 👨🏼‍🔬")


st.header("\U0001F4C1 Data collection:")
st.markdown("   - more datapoints can be leveraged to understand the divvy bike traffic better: ")
st.markdown("       - type of users (casual vs. subscribers)")
st.markdown("       - type of bikes (pedal bikes vs. e-bikes)")

st.header("\U0001F527 Data cleaning and preprocessing:")
st.markdown("   - removing geohash")

st.header("\U0001F916 Model:")
st.markdown("   - leverage the most optimal TPOT model (which couldn't be run due to technical constraints) ")

t.header("\U0001F916 Capacity calculations:")
st.markdown("   - redesign the capacity calculations ")
