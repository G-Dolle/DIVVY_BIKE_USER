import streamlit as st
from streamlit_folium import folium_static
from PIL import Image

st.set_page_config(page_title="Team", layout="centered", initial_sidebar_state="auto")

st.markdown("# Our Team")

col1, col2 = st.columns(2)

img = Image.open("images/Guillaume.png")
col1.image(img, width=200)

col1.markdown("##### Guillaume Dollé")
col1.write("🔗Contact: [Github](https://github.com/G-Dolle/) [Linkedin](https://www.linkedin.com/in/guillaume-doll%C3%A9-585174a9/)")

#.markdown("***")

img = Image.open("images/Mario.jpg")
col1.image(img, width=200, use_column_width = 'bool')

col1.markdown("##### Mario Fernandez")
col1.write("🔗Contact: [Github](https://github.com/fernandez-7m) [Linkedin](https://www.linkedin.com/in/mario-fernandez-42722927/)")

st.markdown("***")

img = Image.open("images/Anson.png")
col2.image(img, width=200)

col2.markdown("##### Hon Fai Chow Anson")
col2.write("🔗Contact: [Github](https://github.com/ansonchf) [Linkedin](https://www.linkedin.com/in/hon-fai-chow/)")

#col1.markdown("***")

img = Image.open("images/Joachim.jpg")
col2.image(img, width=200)

col2.markdown("##### Joachim Clodic")
col2.write("🔗Contact: [Github](https://github.com/Jo8467) [Linkedin](https://www.linkedin.com/in/joachimclodic/)")
