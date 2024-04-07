import streamlit as st
from PIL import Image

image = Image.open('test_image.jpg')
st.image(image, caption='サンプルイメージ')

st.write('---')

video_file = open('test_movie.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
