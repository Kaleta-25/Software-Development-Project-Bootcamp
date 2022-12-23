import pandas as pd
import streamlit as st
import plotly.express as px

st.title = {"Software Development Project"}
st.title

vehicles_df = pd.read_csv('vehicles_us.csv')
vehicles_df.info()

vehicles_df['cylinders'] = vehicles_df['cylinders'].fillna(0).astype(int)
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0).astype(int)
vehicles_df['odometer'] = vehicles_df['odometer'].fillna(0).astype(int)
vehicles_df['paint_color'] = vehicles_df['paint_color'].fillna('Unknown')

st.header=("Exploratory Data Analysis of Car Advertisements") 
st.header

scatter_list = ['model' , 'days_listed' , 'odometer']
factors = st.selectbox('Options:',scatter_list)
figure = px.scatter(vehicles_df, x = factors,y='price')
figure.update_layout(title = '<b>Price based on {}</b>'.format(factors))

show_scatter = st.checkbox("Show scatter plot")
if show_scatter:
    st.plotly_chart(figure)

histogram_list = ['model' , 'condition' , 'paint_color']
factors2 = st.selectbox('Options:',histogram_list, key = 'count')
figure2 = px.histogram(vehicles_df, x=factors2, y='price')
figure2.update_layout(title = '<b>Price based on {}</b>'.format(factors2))

show_scatter = st.checkbox("Show scatter plot")
if show_scatter:
    st.plotly_chart(figure2)