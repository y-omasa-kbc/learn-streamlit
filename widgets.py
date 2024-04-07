import streamlit as st

user_input = st.text_input("Enter your name", "愛媛 太郎")
st.write(f"Hello {user_input}!")

if st.button("Click me!"):
    st.write("You clicked me!")

age = st.slider("年齢を選択してください", 0, 100, 25)
st.write(f"あなたの年齢は{age}歳です")

show_info = st.checkbox("詳細情報を表示する")
if show_info:
    st.write("詳細情報を表示します")
