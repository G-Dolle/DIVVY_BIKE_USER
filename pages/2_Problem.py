import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Problem")

st.title("\U0001F310 Problem")
st.markdown("")

col1, col2 = st.columns(2)

img1 = Image.open("images/Empty.jpg")
col1.image(img1, width=300)

img2 = Image.open("images/Full.png")
col2.image(img2, width=310)

st.markdown("")
st.markdown("""
    At peak hours, often impossible to find a bike (empty station) or to park it (full station) especially under rainy or cold conditions
    - Station is full: user cannot park their bike
    - Station is empty: user cannot find any bike
""")
