# 환경변수 호출
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI #ChatOpenAI는 대화형 답변
chat_model = ChatOpenAI()

import streamlit as st
st.title("코드 리뷰 & 분석  " + chat_model.model)

subject = st.text_area("코드 리뷰를 원하는 코드를 입력해주세요", height=200)

if st.button("리뷰하기", type="primary"):
    with st.spinner(text="In progress...", show_time=True):
        response = chat_model.invoke(subject+"의 파이썬 코드를 비전공자도 이해하기 쉽게 리뷰해줘")
        st.write(response.content)