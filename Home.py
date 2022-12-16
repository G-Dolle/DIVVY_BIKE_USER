import streamlit as st
import pandas as pd
import requests
import datetime
import folium
from streamlit_folium import folium_static
from PIL import Image

st.set_page_config(
    page_title="DIViz", layout="centered"
    #page_icon="👋",
)

st.write("# Welcome to DIViz!")
st.markdown("")

img = Image.open("images/Divvy-bikes.jpg")
st.image(img)

#st.sidebar.success("Select a demo above.")
st.markdown("")
st.markdown("This App will help you to predict the arrivals and departures of bikes at each station, to find the nearest locations with Divvy Bicycle available \U0001F600")