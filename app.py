import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go

st.header("Data Viewer")
df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df["model"].apply(lambda x: x.split(' ')[0])
df


ckbox = st.checkbox("include manufacturers with less than 1000 ads")
if not ckbox:
    df = df.groupby("manufacturer").filter(lambda x: len(x)<= 1000).reset_index()
 
st.header('Vehicles by manufacturer')    
fig = px.histogram(df, x = 'manufacturer', color = 'type')
st.write(fig) 

st.header('Compare model year and condition')    
fig = px.histogram(df, x = 'model_year', color = 'condition')
st.write(fig) 
    
manufact_list = sorted(df['manufacturer'].unique())
manufact_list

m_1 = st.selectbox('select manufacturer #1', manufact_list, index = manufact_list.index('chrysler'))
m_2 = st.selectbox('select manufacturer #2', manufact_list,
                     index=manufact_list.index("cadillac"))
       
mask_filter = (df['manufacturer']==m_1)|(df['manufacturer']==m_2)
df_filtered = df[mask_filter]
fig = px.histogram(df_filtered, x = 'price', nbins = 30, color = 'manufacturer', barmode = 'overlay', histnorm = 'percent')
st.write(fig)
