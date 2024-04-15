import streamlit as st
import pandas as pd

df = pd.read_csv('sampledata.csv')
st.write("DataFrame", df)

user_input = st.sidebar.text_input("検索キーワード(Last namne)")
filered_df = df[df['Last Name'].str.contains(user_input)]

st.write("検索結果", filered_df)
