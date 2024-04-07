import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.write('This is column 1')

    with st.expander('詳細を表示'):
        st.write('詳細情報1')
        st.write('詳細情報2')

with col2:
    st.write('This is column 2')

    # Sidebarは全体の左側に表示される
    option = st.sidebar.selectbox('選択してください', ['A', 'B', 'C'])
    st.write(f'選択した値: {option}')

st.write('---')
st.markdown('# マークダウン記法\n **強調表示**\n *斜体表示*')

st.write('---')
st.markdown("""
            <style>
            .big-font {
                font-size: 50px !important;
            }
            </style>
            """, unsafe_allow_html=True)
st.markdown('<p class="big-font">大きな文字</p>', unsafe_allow_html=True)
