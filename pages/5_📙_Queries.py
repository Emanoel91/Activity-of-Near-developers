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
st.set_page_config(page_title='Queries', page_icon=Near, layout='wide')
st.title('📙 Queries')


# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    
    
st.info('In this dashboard, Flipside database is used to extract data. The list of all the queries used in this dashboard is available in the following links. You can click on the links to access each one.')    

