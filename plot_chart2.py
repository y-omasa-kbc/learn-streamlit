import streamlit as st
import altair as alt
import plotly.express as px

df = px.data.iris()


chart = alt.Chart(df).mark_circle(size=60).encode(
    x='sepal_width',
    y='sepal_length',
    color='species',
    tooltip=['species','sepal_length','sepal_width'])

st.altair_chart(chart, use_container_width=True)
