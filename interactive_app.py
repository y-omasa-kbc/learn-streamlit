import streamlit as st

st.title('Interactive Streamlit app')
user_input = st.text_input('文字列を入力してください:')
if user_input:
    st.write(f'あなたが入力した文字列は"{user_input}"です。')
