import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'data1': [10, 20, 30, 40, 50],
    'data2': [10, 30, 20, 60, 50]
})

st.bar_chart(data, width=500, height=500)
