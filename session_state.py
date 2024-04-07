import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('カウント'):
    st.session_state.count += 1

    st.write(f'カウント: {st.session_state.count}')

# セッション変数に保存していない情報を使い、画面更新の動作で
# 入力情報が消失しないことを保証する
user_input = st.text_input('Enter your name')

if user_input:
    st.session_state.name = user_input
    st.write(f'Hello {st.session_state.name}!')
