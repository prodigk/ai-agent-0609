import random
from datetime import datetime
import streamlit as st

def generate_lotto_numbers():
    """
    1부터 45 사이에서 중복되지 않는 로또 번호 6개를 생성하고,
    생성된 시각을 함께 출력합니다.
    """
    # 1. 로또 번호 생성 (1~45 범위, 중복 제거)
    numbers = random.sample(range(1, 46), 6)
    
    # 오름차순으로 정렬하여 보기 좋게 만듭니다.
    numbers.sort()
    
    # 2. 현재 시간 기록
    current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    
    st.write("================================================================================")
    st.title("🏆 로또 번호 생성기 결과 🎰")
    st.write("================================================================================")
    st.subheader(f"✨ 생성 일시: {current_time}")
    st.write("----------------------------------------")
    # 보기 좋게 쉼표로 구분하여 출력
    st.header(f"🍀 행운의 로또 번호: {numbers[0]:<2} | {numbers[1]:<2} | {numbers[2]:<2} | {numbers[3]:<2} | {numbers[4]:<2} | {numbers[5]:<2}")
    st.write("================================================================================")

if st.button("로또 번호 생성하기", type="primary"):
    generate_lotto_numbers()
