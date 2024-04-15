import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'numbers': [1, 2, 3, 4, 5],
    'values': [10, 30, 20, 60, 50]
})

st.line_chart(data)
