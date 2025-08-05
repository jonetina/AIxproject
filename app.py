import streamlit as st   # streamlit 패키지를 설치해줘야 한다.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/mydata.csv')

url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'

urls = {
    "정보" : ['1', '2'],
    "수학" : ['3', '4']
}

st.title("This is my first webAPP!!")

col1, col2 = st.columns((4, 1))

with col1:
    with st.expander("SubContent1..."):
        st.subheader("SubContent1...")
        st.video(url)
        
    with st.expander("SubContent2..."):
        st.subheader("Image Content...")
        st.image('./images/catdog.png')
        
    with st.expander("SubContent3..."):
        st.subheader("HTML Content...")
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index.html', 'r', encoding='utf-8') as f:
            html1 = f.read()
            f.close()
        htmlviewer.html(html1, height=800)
        
    with st.expander("SubContent4..."):
        st.subheader("Data App Content...")
        st.table(df)
        st.write(df.describe()) # 기술적 통계를 보여줌
        fig, ax = plt.subplots(figsize=(20,10))
        df.plot(ax = ax)
        plt.savefig('./images/mygraph.png') # 이미지 저장
        st.image('./images/mygraph.png')
        
with col2:
    with st.expander("Tips..."):
        st.info("Tips......")