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
    
    
st.info('🟢 In this dashboard, Flipsidecrypto database is used to extract data. The list of all the queries used in this dashboard is available in the following links. You can click on the links to access each one.')    

st.write(
   """
 Project link on GitHub: [Click here](https://github.com/Emanoel91/L2Chains)      
   """
  )
c1, c2, c3 = st.columns(3)
with c1:
    st.write(
       """
     - [Total Contracts Count](https://app.flipsidecrypto.com/velocity/queries/0c390aac-8f53-4774-8ca4-f27fdebeee68)
     - [Classification of Contracts Based on TXs Count](https://app.flipsidecrypto.com/velocity/queries/54b11f56-3207-40f9-9572-183002c21ec8) 
     - [Top 20 Developers Based on Number of Days of Activity](https://app.flipsidecrypto.com/velocity/queries/0b36071c-4760-4adc-927f-bf1849ad1206)
     - [Top 20 Developers Based on Number of Likes](https://app.flipsidecrypto.com/velocity/queries/f8369bfe-a6a0-493e-bf7e-2b686b71fd70)
     - [Top 20 Organizations Based on Pull Request Count](https://app.flipsidecrypto.com/velocity/queries/00bbd2e3-4a8c-4c15-bfe3-b54a09700bfe)
     - [Top 20 Organizations Based on Repository Count](https://app.flipsidecrypto.com/velocity/queries/f908024c-e016-49c7-8469-09291457a36b)
     - [Top 20 Organizations Based on Developers Count](https://app.flipsidecrypto.com/velocity/queries/61f031e0-a0e8-46e1-a617-4022939549b8) 
     - [Number of New Organization per Month](https://app.flipsidecrypto.com/velocity/queries/7dcd799c-9789-44b2-9021-c4f7530a83da)
     - [Number of New Organization per Week](https://app.flipsidecrypto.com/velocity/queries/3190efda-8350-439d-90fa-66268d21a0fd)
     - [Number of New Organization per Day](https://app.flipsidecrypto.com/velocity/queries/2fc4513b-8405-4c26-8dc8-bd4d33646175)       
       """
      )
with c2:
    st.write(
       """ 
     - [Top 20 Contracts Based on Transactions Count](https://app.flipsidecrypto.com/velocity/queries/14befc79-dab5-495a-94d3-be4178ece0a1)
     - [Number of Contracts Deployed per Year](https://app.flipsidecrypto.com/velocity/queries/f35c7101-2cec-405b-b513-190a4e97c378) 
     - [Roles of Developers per Year](https://app.flipsidecrypto.com/velocity/queries/093e1ac2-e55c-48f7-9066-dbea564df0cd)
     - [Roles of Developers per Month](https://app.flipsidecrypto.com/velocity/queries/481f5d2d-b358-4ea9-8e44-05f7ba40b10c)
     - [Roles of Developers per Week](https://app.flipsidecrypto.com/velocity/queries/e99e8ee0-ce98-4feb-9207-48134c7a0219)
     - [Roles of Developers per Day](https://app.flipsidecrypto.com/velocity/queries/fc80cc01-b473-4a7d-a2fc-0a909f484b19)
     - [Roles of Developers](https://app.flipsidecrypto.com/velocity/queries/963490f4-6fad-4645-9512-615eda781f36) 
     - [Top 20 Developers With Most Repositories Count (Created Pull Requests)](https://app.flipsidecrypto.com/velocity/queries/5d4d58dd-d2e3-4dab-9500-01badb0609fe)
     - [Top 20 Developers With Most Pull Created Requests Count](https://app.flipsidecrypto.com/velocity/queries/553672ed-d532-4903-a700-913b1e2a4776)
     - [Number of New Repositories per Year](222)      
       """
      )

with c3:
    st.write(
       """
     - [Number of New Repositories per Month](https://app.flipsidecrypto.com/velocity/queries/8fd9b62a-9056-4af1-93e2-cf24069c7b75)
     - [Number of New Repositories per Week](https://app.flipsidecrypto.com/velocity/queries/2c0817fa-b9b7-48f8-a5cd-1d6ea00bac21) 
     - [Number of New Repositories per Day](https://app.flipsidecrypto.com/velocity/queries/f5aafb62-5657-41e5-be37-3af3dd37b708)
     - [Number of Active Developer per Year](https://app.flipsidecrypto.com/velocity/queries/081cc634-ffaf-4521-9cd9-394e21e8c367)
     - [Number of Active Developer per Month](https://app.flipsidecrypto.com/velocity/queries/67dcbe9a-d1c1-4b29-8512-0ebcb3b32345)
     - [Number of Active Developer per Week](https://app.flipsidecrypto.com/velocity/queries/5b11e61e-d96c-496a-9a2a-7b28384abfb3)
     - [Number of Active Developer per Day](https://app.flipsidecrypto.com/velocity/queries/d188cbec-f8e0-407b-bcd2-89faa51c28d6) 
     - [Number of New Developer per Year](https://app.flipsidecrypto.com/velocity/queries/0844772f-3428-4715-b163-d5bb5d6cd78e)
     - [Number of New Developer per Month](https://app.flipsidecrypto.com/velocity/queries/35ba9930-7e7b-41f2-9efe-f451cc331c82)
     - [Number of New Developer per Week](https://app.flipsidecrypto.com/velocity/queries/110442b4-272d-4489-96b5-ed3a5224a42c)     
       """
      )	





