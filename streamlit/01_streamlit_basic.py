#  Streamlit Documentation  
# url: https://docs.streamlit.io/

# 01. Streamlit Basic
# url: https://docs.streamlit.io/library/get-started/create-an-app

# import necessary dependencies
import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Streamlit Basic Example")

st.write("Hello, *Streamlit!* :sunglasses:")

st.header("큰제목")
st.subheader("작은제목")

st.markdown("Markdown을 이용한 **글자 꾸미기**와 `코드 블록`을 사용할 수 있습니다.")

# st.divider("*") # 구분선

st.html("<p style='color:blue;'>HTML 태그도 사용할 수 있습니다.</p>")

# st.iframe("https://www.youtube.com/embed/dQw4w9WgXcQ", width=560, height=315) # 유튜브 영상 삽입

st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # 유튜브 영상 삽입 (자동으로 iframe으로 변환)

st.image("https://www.python.org/static/community_logos/python-logo.png", caption="Python Logo") # 이미지 삽입

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # 오디오 삽입

st.write("다양한 멀티미디어 콘텐츠를 쉽게 삽입할 수 있습니다.")

st.text_input("텍스트 입력")

st.text_area("텍스트 영역", placeholder="여기에 긴 텍스트를 입력하세요")

st.chat_input("채팅 입력")

st.number_input("숫자 입력", min_value=0, max_value=100, value=50)

st.date_input("날짜 입력")

# st.datetime_input("날짜 및 시간 입력")

st.time_input("시간 입력")

# selectbox, multiselect, slider 등 다양한 입력 위젯도 지원합니다.

st.checkbox("체크박스") 

st.radio("라디오 버튼", options=["옵션 1", "옵션 2", "옵션 3"])

st.selectbox("드롭다운 선택", options=["선택 1", "선택 2", "선택 3"])

st.multiselect("다중 선택", options=["옵션 A", "옵션 B", "옵션 C"])

st.slider("슬라이더", min_value=0, max_value=100, value=25)

st.toggle("토글 스위치")

# st.form_submit_button("폼 제출")

st.button("버튼")

# Correct syntax for pills (requires label and options)
st.pills("Pills 선택", ["Pill 1", "Pill 2", "Pill 3"])

st.link_button("링크 버튼", url="https://www.streamlit.io/")

# For external links, use link_button or markdown
st.markdown("[페이지 링크](https://www.streamlit.io/)")

# st.page_link() is for internal page navigation in multipage apps:
# st.page_link("page2.py", label="Go to Page 2")

# For menu-like functionality, use selectbox or radio:
st.selectbox("메뉴 선택", options=["메뉴 1", "메뉴 2", "메뉴 3"])

st.download_button("다운로드 버튼", data="Hello, Streamlit!", file_name="hello.txt", mime="text/plain")

st.file_uploader("파일 업로드", type=["csv", "txt"])

st.data_editor(pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
}))

st.camera_input("카메라 입력")

st.color_picker("색상 선택")

# For loading CSV files, use pandas and st.dataframe:
# df = pd.read_csv("data/iris_data.csv")
# st.dataframe(df)

# For loading Excel files, use pandas and st.dataframe:
# df = pd.read_excel("data/example_data.xlsx")
# st.dataframe(df)

# st.json("https://api.github.com/repos/streamlit/streamlit")

# For PDF display, you can use:
# st.markdown("[View PDF](https://arxiv.org/pdf/2106.14881.pdf)")

# Display logo using st.image instead (st.logo has path restrictions)
st.image("data/lion.png", width=100, caption="Logo") # Streamlit 로고
st.logo("data/lion.png") # Streamlit 로고 (st.logo는 이미지 경로 제한이 있음)
st.table(pd.DataFrame({
    'Column A': [1, 2, 3],
    'Column B': [4, 5, 6]
}))

st.dataframe(pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
}))

# Chart examples
st.line_chart(pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
}))

st.bar_chart(pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
}))

st.area_chart(pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
}))

st.scatter_chart(pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
}))


st.map(pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.41, -122.42]
}))

# st.pyplot([1, 2, 3], [4, 5, 6])

st.balloons()