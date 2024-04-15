import streamlit as st
import pandas as pd

df = pd.read_csv('sampledata.csv')
st.write("DataFrame", df)
