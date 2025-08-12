import streamlit as st

# MBTI별 직업 추천 데이터 예시
mbti_jobs = {
    "INTJ": ["데이터 사이언티스트", "전략 컨설턴트", "연구원", "소설가"],
    "ENTP": ["기업가", "마케터", "방송인", "제품 기획자"],
    "INFJ": ["상담가", "작가", "인권 변호사", "교사"],
    "ESFP": ["배우", "이벤트 플래너", "영업직", "여행 가이드"],
    # 필요한 만큼 추가
}

st.set_page_config(page_title="MBTI 직업 추천기", page_icon="💼", layout="centered")

# 제목
st.title("💼 MBTI 기반 직업 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# MBTI 선택
selected_mbti = st.selectbox("MBTI를 선택하세요", list(mbti_jobs.keys()))

# 추천 버튼
if st.button("추천받기"):
    jobs = mbti_jobs.get(selected_mbti, [])
    if jobs:
        st.subheader(f"🔍 {selected_mbti} 타입 추천 직업")
        for job in jobs:
            st.write(f"- {job}")
    else:
        st.warning("아직 데이터가 없습니다. 다른 MBTI를 선택해 주세요.")

