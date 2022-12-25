import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


vehicles_df = pd.read_csv('vehicles_us.csv')
vehicles_df.info()

vehicles_df['cylinders']= vehicles_df['cylinders'].fillna(vehicles_df['cylinders'].mean())
vehicles_df['odometer'] = vehicles_df['odometer'].fillna(vehicles_df['odometer'].mean())
# The mean is used to replace missing values because just because there is a NaN value, does not mean there are 0 cyclinders or No Distance in the odometer columns. Mean is used to represent a number that is possibly close to what the car may have. 
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0).astype(int)
# 0 represents 'No' and 1 represents 'Yes'
vehicles_df['paint_color'].fillna('Unknown', inplace=True)
vehicles_df['model_year'].fillna('Unknown', inplace=True)
# All cars have a paint color and model year, but for this datatset, there is no way to know. 


vehicles_df['cylinders'] = vehicles_df['cylinders'].astype(np.int64)
vehicles_df['odometer'] = vehicles_df['odometer'].astype(np.int64)
vehicles_df.info()


st.header("Exploratory Data Analysis of Car Advertisements") 

st.dataframe(vehicles_df)


scatter_list = ['model','days_listed', 'odometer']
factors = st.selectbox('Options:',scatter_list)
figure = px.scatter(vehicles_df, x = factors,y='price' , color='model', hover_name='model') 
figure.update_layout(title = '<b>Price based on {}</b>'.format(factors))

show_scatter = st.checkbox("Show scatter plot")
if show_scatter:
    st.plotly_chart(figure)

histogram_list = ['model','type' , 'condition' , 'paint_color']
factors2 = st.selectbox('Options:',histogram_list, key = 'count')
figure2 = px.histogram(vehicles_df, x=factors2, color='model', hover_name='model')
figure2.update_layout(title = '<b>Price based on {}</b>'.format(factors2))

show_histogram = st.checkbox("Show histogram", key="show-histogram")
if show_histogram:
    st.plotly_chart(figure2)
