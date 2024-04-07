import io
import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader("ファイルを選択してください。")
if uploaded_file is not None:
    string_data = uploaded_file.read().decode('utf-8')
    df = pd.read_csv(io.StringIO(string_data))
    st.write(df)
