import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="오늘의 점심 메뉴 추천", page_icon="🍱", layout="centered"
)

# 카테고리별 점심 메뉴 데이터
menus = {
    "한식": [
        "김치찌개",
        "된장찌개",
        "제육볶음",
        "순대국밥",
        "비빔밥",
        "불고기백반",
        "칼국수",
        "냉면",
    ],
    "중식": ["짜장면", "짬뽕", "탕수육 세트", "마라탕", "볶음밥", "마파두부덮밥"],
    "일식": ["돈까스", "초밥", "라멘", "우동", "규동(소고기덮밥)", "가츠동"],
    "양식/기타": [
        "파스타",
        "수제버거",
        "쌀국수",
        "타코",
        "샌드위치 & 샐러드",
        "커리",
    ],
}

st.title("🍱 오늘 점심 뭐 먹지?")
st.write(
    "카테고리를 선택하고 버튼을 누르면 오늘의 점심 메뉴를 추천해 드립니다."
)

# 카테고리 선택 (기본값: 전체)
category = st.selectbox(
    "원하는 음식 종류를 선택하세요:", ["전체"] + list(menus.keys())
)

# 선택된 카테고리에 따라 후보 메뉴 리스트 구성
if category == "전체":
    candidate_menus = [menu for sublist in menus.values() for menu in sublist]
else:
    candidate_menus = menus[category]

st.divider()

# 버튼 클릭 시 랜덤 추천 실행
if st.button(
    "🎲 오늘의 메뉴 추천받기", use_container_width=True, type="primary"
):
    selected_menu = random.choice(candidate_menus)
    st.balloons()
    st.success(f"오늘의 추천 점심 메뉴는 **'{selected_menu}'** 입니다! 🎉")
