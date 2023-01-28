# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import PIL
from PIL import Image

theme_plotly = None # None or streamlit

Near = PIL.Image.open('Near.png')

# Structure
st.set_page_config(page_title='Repository', page_icon=Near, layout='wide')
st.title('💼 Repository')


# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

