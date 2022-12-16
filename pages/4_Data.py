import streamlit as st

st.set_page_config(
    page_title="Data",
    layout="wide",  # wide
    initial_sidebar_state="auto")

col1, col2 = st.columns(2)
col1.markdown("""
            # \U0001F4C1 Data Collection

            * Divvy website and Station API: bike sharing history and station data 
                * Flows of bike rides between stations
                * Stations GPS coordinates
                * Time dimension (hour of day, day of week, month, year)
            * Weather conditions from Open Weather API
                * Temperature
                * Humidity
                * wind speed
        """)
        
col2.markdown("""
            # 🔧 Data Cleaning & Preprocessing

            * Geohash
            * Hourly intervals 
            * Merging the two datasets → Bike sharing and weather data  
            * Using avg. number of Arrivals / Departures per hour per area as proxy for availability
            * Factors used for such prediction: 
                * weather information, 
                * time specific effect, 
                * geographic specific effect
        """)
        