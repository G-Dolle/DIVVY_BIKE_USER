import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Recommendations",
    page_icon="👨🏼‍🔬",
    layout="centered",  # wide
    initial_sidebar_state="auto")

st.title("👨🏼‍🔬 Recommendations ")

st.markdown('''
## \U0001F4C1 Data collection
* more datapoints can be leveraged to understand the divvy bike traffic better:
   * type of users (casual vs. subscribers)
   * type of bikes (pedal bikes vs. e-bikes)
## \U0001F527 Data cleaning and preprocessing
- removing geohash
## ⚙️ Model
- leverage the most optimal TPOT model (which couldn't be run due to technical constraints)
## \U0001F522 Capacity calculations
- redesign the capacity calculations
''')
