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
st.set_page_config(page_title='Contracts', page_icon=Near, layout='wide')
st.title('📑 Contracts')


# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Number of New Developer per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/502eba85-a8cf-4681-89be-2397fa9ce8b3/data/latest')
    elif query1 == 'Number of New Developer per Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/110442b4-272d-4489-96b5-ed3a5224a42c/data/latest')
    elif query1 == 'Number of New Developer per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/35ba9930-7e7b-41f2-9efe-f451cc331c82/data/latest') 
    elif query1 == 'Number of New Developer per Year':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0844772f-3428-4715-b163-d5bb5d6cd78e/data/latest')
    elif query1 == 'Number of Active Developer per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d188cbec-f8e0-407b-bcd2-89faa51c28d6/data/latest')
    elif query1 == 'Number of Active Developer per Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5b11e61e-d96c-496a-9a2a-7b28384abfb3/data/latest')
    elif query1 == 'Number of Active Developer per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/67dcbe9a-d1c1-4b29-8512-0ebcb3b32345/data/latest') 
    elif query1 == 'Number of Active Developer per Year':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/081cc634-ffaf-4521-9cd9-394e21e8c367/data/latest')
    elif query1 == 'Number of New Repositories per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f5aafb62-5657-41e5-be37-3af3dd37b708/data/latest')
    elif query1 == 'Number of New Repositories per Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2c0817fa-b9b7-48f8-a5cd-1d6ea00bac21/data/latest')
    elif query1 == 'Number of New Repositories per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8fd9b62a-9056-4af1-93e2-cf24069c7b75/data/latest') 
    elif query1 == 'Number of New Repositories per Year':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a561e309-97e7-4270-b46d-cdeb9c43eca5/data/latest')
    elif query1 == 'Total Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4c17a043-73b2-4030-9c5e-97139094b2db/data/latest')
    elif query1 == 'Top 20 Repositories With Most Pull Requests Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6a25d90b-3ead-4220-b6c6-2900e0fd08cd/data/latest')
    elif query1 == 'Top 20 Developers With Most Pull Created Requests Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/553672ed-d532-4903-a700-913b1e2a4776/data/latest') 
    elif query1 == 'Top 20 Developers With Most Repositories Count (Created Pull Requests)':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5d4d58dd-d2e3-4dab-9500-01badb0609fe/data/latest')
    elif query1 == 'Top 20 Developers With Most Closed Pull Requests Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3b598335-9a2e-4b3f-ab47-4919d26e73ec/data/latest')         
    elif query1 == 'Top 20 Developers With Most Repositories Count (Closed Pull Requests)':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cb0ba4a3-752d-464f-a87c-9534c630266b/data/latest')
    elif query1 == 'Roles of Developers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/963490f4-6fad-4645-9512-615eda781f36/data/latest') 
    elif query1 == 'Roles of Developers per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fc80cc01-b473-4a7d-a2fc-0a909f484b19/data/latest')
    elif query1 == 'Roles of Developers per Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e99e8ee0-ce98-4feb-9207-48134c7a0219/data/latest')
    elif query1 == 'Roles of Developers per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/481f5d2d-b358-4ea9-8e44-05f7ba40b10c/data/latest')
    elif query1 == 'Roles of Developers per Year':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/093e1ac2-e55c-48f7-9066-dbea564df0cd/data/latest') 
    elif query1 == 'Number of Contracts Deployed per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f8941f5e-aa5f-455b-a7f0-01c7b8b503b1/data/latest')
    elif query1 == 'Number of Contracts Deployed per Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c30661e0-cc58-4c2d-a6fe-e010343ad419/data/latest')
    elif query1 == 'Number of Contracts Deployed per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4f9070e5-7bda-4b26-8596-a112821580b8/data/latest')
    elif query1 == 'Number of Contracts Deployed per Year':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f35c7101-2cec-405b-b513-190a4e97c378/data/latest') 
    elif query1 == 'Top 20 Contracts Based on Transactions Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/14befc79-dab5-495a-94d3-be4178ece0a1/data/latest')
    elif query1 == 'Number of New Organization per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2fc4513b-8405-4c26-8dc8-bd4d33646175/data/latest')
    elif query1 == 'Number of New Organization per Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3190efda-8350-439d-90fa-66268d21a0fd/data/latest')
    elif query1 == 'Number of New Organization per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7dcd799c-9789-44b2-9021-c4f7530a83da/data/latest') 
    elif query1 == 'Number of New Organization per Year':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/41e12485-490a-474b-a6bf-7b3e34f9b4c5/data/latest')
    elif query1 == 'Top 20 Organizations Based on Developers Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/61f031e0-a0e8-46e1-a617-4022939549b8/data/latest') 
    elif query1 == 'Top 20 Organizations Based on Repository Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f908024c-e016-49c7-8469-09291457a36b/data/latest')
    elif query1 == 'Top 20 Organizations Based on Pull Request Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/00bbd2e3-4a8c-4c15-bfe3-b54a09700bfe/data/latest')
    elif query1 == 'Top 20 Developers Based on Number of Likes':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f8369bfe-a6a0-493e-bf7e-2b686b71fd70/data/latest')
    elif query1 == 'Top 20 Developers Based on Number of Days of Activity':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0b36071c-4760-4adc-927f-bf1849ad1206/data/latest') 
    elif query1 == 'Heat map':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c9e5fc31-b328-4070-a675-8acdb932f12f/data/latest') 
    elif query1 == 'Classification of Contracts Based on TXs Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/54b11f56-3207-40f9-9572-183002c21ec8/data/latest') 	
    elif query1 == 'Total Contracts Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0c390aac-8f53-4774-8ca4-f27fdebeee68/data/latest') 	
    return None

Number_of_New_Developer_per_Day = get_data('Number of New Developer per Day')
Number_of_New_Developer_per_Week = get_data('Number of New Developer per Week')
Number_of_New_Developer_per_Month = get_data('Number of New Developer per Month')
Number_of_New_Developer_per_Year = get_data('Number of New Developer per Year')
Number_of_Active_Developer_per_Day = get_data('Number of Active Developer per Day')
Number_of_Active_Developer_per_Week = get_data('Number of Active Developer per Week')
Number_of_Active_Developer_per_Month = get_data('Number of Active Developer per Month')
Number_of_Active_Developer_per_Year = get_data('Number of Active Developer per Year')
Number_of_New_Repositories_per_Day = get_data('Number of New Repositories per Day')
Number_of_New_Repositories_per_Week = get_data('Number of New Repositories per Week')
Number_of_New_Repositories_per_Month = get_data('Number of New Repositories per Month')
Number_of_New_Repositories_per_Year = get_data('Number of New Repositories per Year')
Total_Data = get_data('Total Data')
Top_20_Repositories_With_Most_Pull_Requests_Count = get_data('Top 20 Repositories With Most Pull Requests Count ')
Top_20_Developers_With_Most_Pull_Created_Requests_Count = get_data('Top 20 Developers With Most Pull Created Requests Count')
Top_20_Developers_With_Most_Repositories_Count_Created_Pull_Requests = get_data('Top 20 Developers With Most Repositories Count (Created Pull Requests)')
Top_20_Developers_With_Most_Closed_Pull_Requests_Count = get_data('Top 20 Developers With Most Closed Pull Requests Count')
Top_20_Developers_With_Most_Repositories_Count_Closed_Pull_Requests = get_data('Top 20 Developers With Most Repositories Count (Closed Pull Requests)')
Roles_of_Developers = get_data('Roles of Developers')
Roles_of_Developers_per_Day = get_data('Roles of Developers per Day')
Roles_of_Developers_per_Week = get_data('Roles of Developers per Week')
Roles_of_Developers_per_Month = get_data('Roles of Developers per Month')
Roles_of_Developers_per_Year = get_data('Roles of Developers per Year')
Number_of_Contracts_Deployed_per_Day = get_data('Number of Contracts Deployed per Day')
Number_of_Contracts_Deployed_per_Week = get_data('Number of Contracts Deployed per Week')
Number_of_Contracts_Deployed_per_Month = get_data('Number of Contracts Deployed per Month')
Number_of_Contracts_Deployed_per_Year = get_data('Number of Contracts Deployed per Year')
Top_20_Contracts_Based_on_Transactions_Count = get_data('Top 20 Contracts Based on Transactions Count')
Number_of_New_Organization_per_Day = get_data('Number of New Organization per Day')
Number_of_New_Organization_per_Week = get_data('Number of New Organization per Week')
Number_of_New_Organization_per_Month = get_data('Number of New Organization per Month')
Number_of_New_Organization_per_Year = get_data('Number of New Organization per Year')
Top_20_Organizations_Based_on_Developers_Count = get_data('Top 20 Organizations Based on Developers Count')
Top_20_Organizations_Based_on_Repository_Count = get_data('Top 20 Organizations Based on Repository Count')
Top_20_Organizations_Based_on_Pull_Request_Count = get_data('Top 20 Organizations Based on Pull Request Count')
Top_20_Developers_Based_on_Number_of_Likes = get_data('Top 20 Developers Based on Number of Likes')
Top_20_Developers_Based_on_Number_of_Days_of_Activity = get_data('Top 20 Developers Based on Number of Days of Activity')
Heat_map = get_data('Heat map')
Classification_of_Contracts_Based_on_TXs_Count = get_data('Classification of Contracts Based on TXs Count')
Total_Contracts_Count = get_data('Total Contracts Count')

# Analysis

df = Total_Contracts_Count
c1, c2 = st.columns(2)
             
with c1:
      st.metric(label='**Total Number of Contracts**', value=df['Contracts Count'])

df = Classification_of_Contracts_Based_on_TXs_Count
c1, c2 = st.columns(2)
             
with c1:
     fig = px.pie(df, values='Number of Contracts', names='Group', title='Classification of Contracts Based on TXs Count')
     fig.update_layout(legend_title='Group', legend_y=0.5)
     fig.update_traces(textinfo='percent', textposition='inside')
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with c2:
     fig = px.bar(df, x='Group', y='Number of Contracts', color='Group', title='', log_y=False)
     fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='Contracts Count', xaxis={'categoryorder':'total ascending'})
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Top_20_Contracts_Based_on_Transactions_Count
fig = px.bar(df, x='New Contract', y='TXs Count', color='New Contract', title='Top 20 Contracts Based on Transactions Count', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Contracts Analysis
subtab_Daily, subtab_Weekly, subtab_Monthly, subtab_Yearly = st.tabs(['Daily', 'Weekly', 'Monthly','Yearly'])

with subtab_Daily:
            df = Number_of_Contracts_Deployed_per_Day
            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=df['Day'], y=df['Contracts Count'], name='Contracts Count'), secondary_y=False)
            fig.add_trace(go.Line(x=df['Day'], y=df['Cummulative Contracts Count'], name='Cummulative Contracts Count'), secondary_y=True)
            fig.update_layout(title_text='Number of Contracts')
            fig.update_yaxes(title_text='', secondary_y=False)
            fig.update_yaxes(title_text='', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
	
	
	
# -------------------------------------------------Weekly------------------------------------------------------------------------------------------
with subtab_Weekly:
            df = Number_of_Contracts_Deployed_per_Week
            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=df['Week'], y=df['Contracts Count'], name='Contracts Count'), secondary_y=False)
            fig.add_trace(go.Line(x=df['Week'], y=df['Cummulative Contracts Count'], name='Cummulative Contracts Count'), secondary_y=True)
            fig.update_layout(title_text='Number of Contracts')
            fig.update_yaxes(title_text='', secondary_y=False)
            fig.update_yaxes(title_text='', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
                   
	

# --------------------------------------------------Monthly----------------------------------------------------------------------------------------
with subtab_Monthly:
            df = Number_of_Contracts_Deployed_per_Month
            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=df['Month'], y=df['Contracts Count'], name='Contracts Count'), secondary_y=False)
            fig.add_trace(go.Line(x=df['Month'], y=df['Cummulative Contracts Count'], name='Cummulative Contracts Count'), secondary_y=True)
            fig.update_layout(title_text='Number of Contracts')
            fig.update_yaxes(title_text='', secondary_y=False)
            fig.update_yaxes(title_text='', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)



# --------------------------------------------------Yearly----------------------------------------------------------------------------------------
with subtab_Yearly:

            df = Number_of_Contracts_Deployed_per_Year
            c1, c2 = st.columns(2)
             
            with c1:
                fig = px.pie(df, values='Contracts Count', names='Year', title='Share of Contracts in Each Year')
                fig.update_layout(legend_title='Year', legend_y=0.5)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
            with c2:
                fig = px.bar(df, x='Year', y='Contracts Count', color='Year', title='Total Number of Contracts', log_y=False)
                fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='Contracts Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.subheader('🔎 Observations')
st.write(
    """
- **Most contracts have between 10 and 100 transactions.**
- **The least number of contracts have recorded only one transaction.**
- **The three contracts with the highest number of transactions are:**
🥇 **token.sweat 👉 20.8M TXs**

🥈 **tge.lockup.sweat 👉 4.4M TXs**

🥉 **v2.nearapps.near 👉 3.5M TXs**
- **On some days, we see a significant growth in the number of active contracts.**
- **The maximum number of active contracts has been recorded on June 7, 2022.**
- **In 2021, the number of contracts has been increasing every month.**
- **The highest number of active contracts is related to 2022.**
- **The number of active contracts in 2022 has increased by 130% compared to 2021.**
    """
)




