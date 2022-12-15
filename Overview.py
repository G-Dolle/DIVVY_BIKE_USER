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

img = Image.open("images/Divvy-bikes.jpg")
st.image(img)

#st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This App will help you to predict the arrivals and departures of bikes at each station, to find the nearest locations with Divvy Bicycle available \U0001F600
    
    # \U0001F310 Problem
    At peak hours, often impossible to find a bike (empty station) or to park it (full station) especially under rainy or cold conditions
    - Station is full: user cannot park their bike
    - Station is empty: user cannot find any bike
    
    Typical scenario in the morning to commute to work: no bike close to home, full stations in the business district. 

    # \U0001F50E Solution
    What? Being able to predict bike availability in advance depending on time of day and weather forecast
    
    How? By predicting the number of arrivals and departures of bikes at each station depending on three factors:  
    - Time of the day 
    - Weather conditions
    - Location

    # \U0001F4BB Technical Roadmap
    1️⃣ Data collection, cleaning and preprocessing \u2935

    2️⃣ Model selection and training to improve its accuracy \u2935
    
    3️⃣ Creation of a Webapp ✔️

    # \U0001F4C1 Data Collection
    Divvy bike sharing and station data from divvy website and StationAPI
    - Flows of bike rides between stations
    - Stations GPS coordinates
    - Time dimension (hour of day, day of week, month, year)
    
    Weather conditions from Open Weather API
    - Temperature
    - Humidity
    - wind speed
    - Cloudiness


    # 🔧 Data Cleaning & Preprocessing
    ✔️Slicing the city of Chicago into areas, identifying to which area bike stations belong to
    
    ✔️Computing the average number of departures and arrivals per station for a given area, for a given day and hour
    
    ✔️Selecting weather information (temperature, humidity, wind speed, cloudiness) corresponding to this day and hour 
    
    ✔️What we want to predict: avg nb or arrivals/departures for a given day and hour in a given area 
    
    ✔️Factors used for such prediction: 
    - weather information, 
    - time specific effect, 
    - geographic specific effect

    # ⚙️ Model
    TPOT’s automated Machine Learning tool is used to optimize Machine Learning Pipelines
    """
)

expander = st.expander("Click here to see the models compared in TPOT Regressor")
expander.markdown(
"""
- ElasticNetCV
- ExtraTreeRegressor
- GradientBoostingRegressor
- AdaBoostRegressor
- DecisionTreeRegressor
- KNeighborsRegressor
- LassoLarsCV
- LinearSVR
- RandomForestRegressor
- RidgeCV
- XGBRegressor
- SGDRegressor

""")

st.markdown("""
    Model of Arrival: XGBRegressor

    Model of Departure: DecisionTreeRegressor
    """)