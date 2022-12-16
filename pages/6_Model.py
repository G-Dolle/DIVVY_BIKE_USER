import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Model")

st.title("⚙️ Model")
st.markdown("")

st.markdown("""
    TPOT’s automated Machine Learning tool is used to optimize Machine Learning Pipelines
""")

st.markdown("")

img = Image.open("images/tpot.png")
st.image(img)

st.markdown("")

st.markdown("""
    Model of Arrival- XGBRegressor

    Model of Departure- DecisionTreeRegressor
    """)