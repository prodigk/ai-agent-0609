
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI() 

import streamlit as st
st.title("디지털 글쓰기  " + chat_model.model)
subject = st.text_input("궁금한 내용을 입력해주세요")

if st.button("질문하기", type="primary"):
    with st.spinner(text="In progress...", show_time=True):
        response = chat_model.invoke(subject+"에 대해 설명해줘")
        st.success("답변이 생성되었습니다!")
        st.write(response.content)
