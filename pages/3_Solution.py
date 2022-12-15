import streamlit as st

st.set_page_config(
    page_title="Solution")

st.title("\U0001F50E Solution")
st.markdown("")

st.markdown("""
    What? Being able to predict bike availability in advance depending on time of day and weather forecast
    
    How? By predicting the number of arrivals and departures of bikes at each station depending on three factors:  
    - Time of the day 
    - Weather conditions
    - Location

    # \U0001F4BB Technical Roadmap
""")

st.markdown("")
expander = st.expander("Click here to see the roadmap")
expander.markdown(
"""
1️⃣ Data collection, cleaning and preprocessing \u2935

2️⃣ Model selection and training to improve its accuracy \u2935
    
3️⃣ Creation of a Webapp ✔️
""")
