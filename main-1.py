# 환경변수 호출
from dotenv import load_dotenv
load_dotenv()

#from langchain_openai import OpenAI #OpenAI는 한번의 답변
from langchain_openai import ChatOpenAI #ChatOpenAI는 대화형 답변

#1. 모델 객체 생성
#llm = OpenAI()
chat_model = ChatOpenAI() 

#2. LLM 호출
# llm_response = llm.invoke("오늘 6시 서울 송파구 날씨는 어때?")
# print(llm_response)
chat_model_response = chat_model.invoke("오늘 6시 서울 송파구 날씨는 어때?")
print(chat_model_response.content)

