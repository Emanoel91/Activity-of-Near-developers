# 📚 Libraries
import streamlit as st
import PIL
from PIL import Image

Near = PIL.Image.open('Near.png')

# Title
st.set_page_config(page_title='Activity of NEAR Developers', page_icon=Near, layout='wide')
st.title('Activity of NEAR Developers')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Images/near2-logo.png'))

st.subheader('📃 Introduction')


st.write(
    """
111
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
111
    """
)

st.subheader('📖 Guidance')
st.write(
    """
111
    """
)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")

with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")

with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")






