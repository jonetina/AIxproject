import streamlit as st
import plotly.express as px
import pandas as pd

# Streamlit 웹앱 제목
st.title("학생 성적 시각화 대시보드")

# 제공된 데이터
data = {
    "name": ["lee", "park", "kim"],
    "grade": [2, 2, 2],
    "number": [1, 2, 3],
    "kor": [90, 88, 99],
    "eng": [91, 89, 98],
    "math": [81, 77, 100],
    "info": [100, 100, 100]
}
df = pd.DataFrame(data)

# 데이터프레임 표시
st.subheader("학생 성적 데이터")
st.dataframe(df)

# 사이드바에서 그래프 유형 선택
st.sidebar.header("그래프 설정")
graph_type = st.sidebar.selectbox("그래프 유형 선택", ["막대그래프", "선그래프"])

# 막대그래프 시각화
if graph_type == "막대그래프":
    st.subheader("학생별 과목 점수 (막대그래프)")
    fig_bar = px.bar(
        df,
        x="name",
        y=["kor", "eng", "math", "info"],
        barmode="group",
        title="학생별 국어, 영어, 수학, 정보 점수 비교",
        labels={"value": "점수", "variable": "과목", "name": "학생 이름"}
    )
    st.plotly_chart(fig_bar)

# 선그래프 시각화
elif graph_type == "선그래프":
    st.subheader("학생별 과목 점수 (선그래프)")
    fig_line = px.line(
        df,
        x="name",
        y=["kor", "eng", "math", "info"],
        title="학생별 과목 점수 추이",
        labels={"value": "점수", "variable": "과목", "name": "학생 이름"}
    )
    st.plotly_chart(fig_line)

# 사용자 데이터 업로드 기능
st.sidebar.header("사용자 데이터 업로드")
uploaded_file = st.sidebar.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file is not None:
    user_df = pd.read_csv(uploaded_file)
    st.subheader("업로드된 데이터")
    st.dataframe(user_df)
    
    # 업로드된 데이터로 막대그래프 시각화
    st.subheader("업로드된 데이터 시각화")
    columns = user_df.columns.tolist()
    x_col = st.selectbox("X축 컬럼 선택", columns)
    y_cols = st.multiselect("Y축 컬럼 선택", columns)
    
    if y_cols:
        fig_user = px.bar(
            user_df,
            x=x_col,
            y=y_cols,
            barmode="group",
            title="업로드된 데이터 막대그래프",
            labels={"value": "값", "variable": "변수"}
        )
        st.plotly_chart(fig_user)