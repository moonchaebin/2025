# app.py
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="💼 MBTI 화려한 직업 추천기", page_icon="🌈", layout="wide")

# CSS 스타일 (화려한 배경 + 카드 스타일)
st.markdown("""
<style>
/* 배경 그라데이션 */
.stApp {
  background: radial-gradient(circle at 10% 10%, rgba(255,255,255,0.08), transparent 20%),
              linear-gradient(120deg, #ffecd2 0%, #fcb69f 25%, #ff7a88 50%, #b06ab3 75%);
  background-attachment: fixed;
  color: #222;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* 타이틀 */
.app-title {
  text-align: center;
  font-size: 42px;
  font-weight: 800;
  color: white;
  text-shadow: 2px 2px 12px rgba(0,0,0,0.4);
  margin-bottom: 4px;
}
.app-sub {
  text-align: center;
  color: rgba(255,255,255,0.95);
  margin-bottom: 18px;
  font-size: 16px;
}

/* 카드를 감싸는 그리드 */
.job-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.98), #ffffff);
  border-radius: 16px;
  padding: 12px;
  margin: 10px 6px;
  box-shadow: 0 12px 30px rgba(0,0,0,0.18);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  text-align: left;
  overflow: hidden;
}
.job-card:hover {
  transform: translateY(-6px) scale(1.01);
  box-shadow: 0 18px 40px rgba(0,0,0,0.25);
}

.job-img {
  width: 100%;
  height: 160px;
  object-fit: cover;
  border-radius: 10px;
  display: block;
  margin-bottom: 10px;
}

.job-label {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  background: linear-gradient(90deg,#ff8a8a,#ffd36e);
  color: #fff;
  font-weight: 700;
  font-size: 13px;
  margin-bottom: 8px;
}

.job-title {
  font-size: 18px;
  font-weight: 800;
  margin-bottom: 6px;
  color: #333;
}

.job-desc {
  color: #555;
  font-size: 14px;
  line-height: 1.3;
  margin-bottom: 8px;
}

/* 작은 메타(아이콘 등) */
.job-meta {
  font-size: 12px;
  color: #777;
}

/* 반응형 간격 보정 */
.row {
  margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)

# 페이지 타이틀
st.markdown('<div class="app-title">💼 MBTI 기반 화려한 직업 추천기</div>', unsafe_allow_html=True)
st.markdown('<div class="app-sub">MBTI를 선택하면 어울리는 직업을 카드 형태로 풍부한 이미지와 함께 보여드립니다. 바로 붙여넣고 실행하세요!</div>', unsafe_allow_html=True)

# ---------- MBTI 데이터 (16타입, 각 5개 직업: job, desc, image) ----------
# 이미지 대부분 Unsplash(무료) 이미지 링크 사용 — 필요시 직접 교체하세요.
mbti_data = {
    "INTJ": [
        {"job":"데이터 사이언티스트","desc":"데이터로 인사이트를 도출해 전략을 세우는 전문가.","img":"https://images.unsplash.com/photo-1556157382-97eda2d62296"},
        {"job":"전략 컨설턴트","desc":"기업의 장기적 방향과 실행 계획을 설계.","img":"https://images.unsplash.com/photo-1521791136064-7986c2920216"},
        {"job":"연구원","desc":"깊이 있는 탐구로 새로운 지식을 만들어 내는 직업.","img":"https://images.unsplash.com/photo-1581091012184-7b2b3b2b0b8b"},
        {"job":"소설가","desc":"복잡한 세계를 구조화하여 이야기를 만드는 창작자.","img":"https://images.unsplash.com/photo-1516979187457-637abb4f9353"},
        {"job":"기술 개발자","desc":"시스템과 제품을 설계·구현하는 기술 전문가.","img":"https://images.unsplash.com/photo-1518770660439-4636190af475"}
    ],
    "INTP": [
        {"job":"AI 연구원","desc":"인공지능 모델과 알고리즘을 설계·실험.","img":"https://images.unsplash.com/photo-1504384308090-c894fdcc538d"},
        {"job":"시스템 분석가","desc":"복잡한 IT 시스템을 분석하고 최적화.","img":"https://images.unsplash.com/photo-1526378722484-bd91ca387e72"},
        {"job":"철학자/연구자","desc":"개념과 이론을 깊게 성찰하고 글로 표현.","img":"https://images.unsplash.com/photo-1522202176988-66273c2fd55f"},
        {"job":"프로그래머","desc":"논리적 문제해결로 소프트웨어를 구축.","img":"https://images.unsplash.com/photo-1555066931-4365d14bab8c"},
        {"job":"과학 작가","desc":"과학적 아이디어를 대중에게 쉽게 전달.","img":"https://images.unsplash.com/photo-1532012197267-da84d127e765"}
    ],
    "ENTJ": [
        {"job":"CEO/경영자","desc":"조직을 비전으로 이끌고 성장시키는 리더.","img":"https://images.unsplash.com/photo-1542744173-8e7e53415bb0"},
        {"job":"프로젝트 매니저","desc":"팀과 자원을 관리하며 목표를 완수.","img":"https://images.unsplash.com/photo-1517245386807-bb43f82c33c4"},
        {"job":"전략 컨설턴트","desc":"문제의 핵심을 파악해 실행 가능한 방안을 제시.","img":"https://images.unsplash.com/photo-1559526324-593bc073d938"},
        {"job":"정치/정책 리더","desc":"정책을 만들고 공공을 설득하는 역할.","img":"https://images.unsplash.com/photo-1527261834078-9bbc9aaee5d8"},
        {"job":"영업 이사","desc":"시장과 매출을 책임지는 전략적 영업 리더.","img":"https://images.unsplash.com/photo-1519389950473-47ba0277781c"}
    ],
    "ENTP": [
        {"job":"기업가","desc":"문제에서 기회를 찾아 새로운 사업을 만드는 사람.","img":"https://images.unsplash.com/photo-1525182008055-f88b95ff7980"},
        {"job":"마케팅 디렉터","desc":"창의적 캠페인으로 브랜드를 성장시킴.","img":"https://images.unsplash.com/photo-1507679799987-c73779587ccf"},
        {"job":"방송인/퍼포머","desc":"생동감 있게 아이디어를 전달하고 소통.","img":"https://images.unsplash.com/photo-1515377905703-c4788e51af15"},
        {"job":"제품 기획자","desc":"사용자 문제를 정의하고 솔루션을 설계.","img":"https://images.unsplash.com/photo-1522071820081-009f0129c71c"},
        {"job":"광고 크리에이티브 디렉터","desc":"광고 방향을 총괄하여 큰 임팩트 창출.","img":"https://images.unsplash.com/photo-1503602642458-232111445657"}
    ],
    "INFJ": [
        {"job":"상담가/심리치료사","desc":"개인의 내면을 이해하고 성장을 돕는 역할.","img":"https://images.unsplash.com/photo-1494790108377-be9c29b29330"},
        {"job":"작가","desc":"깊은 통찰을 글로 풀어내는 창작자.","img":"https://images.unsplash.com/photo-1516979187457-637abb4f9353"},
        {"job":"인권/사회 변호사","desc":"약자 편에서 사회 정의를 실현.","img":"https://images.unsplash.com/photo-1488998527040-85054a85150b"},
        {"job":"교사/교육자","desc":"학생의 성장을 돕는 헌신적 교육자.","img":"https://images.unsplash.com/photo-1503676260728-1c00da094a0b"},
        {"job":"연구 심리학자","desc":"심층 연구로 사람의 마음을 이해.","img":"https://images.unsplash.com/photo-1588774067804-3a4f9c7a7e8f"}
    ],
    "INFP": [
        {"job":"소설가/스토리텔러","desc":"감성을 바탕으로 사람의 마음을 흔드는 글을 씀.","img":"https://images.unsplash.com/photo-1495446815901-a7297e633e8d"},
        {"job":"시인/창작가","desc":"언어로 섬세한 감정을 표현.","img":"https://images.unsplash.com/photo-1504384308090-c894fdcc538d"},
        {"job":"사회운동가","desc":"가치에 따라 세상을 바꾸려 노력.","img":"https://images.unsplash.com/photo-1495121605193-b116b5b09c1b"},
        {"job":"심리상담사","desc":"개인의 이야기를 경청하고 회복을 돕음.","img":"https://images.unsplash.com/photo-1580281657521-8b85d0c5d719"},
        {"job":"예술가","desc":"시각·음악 등으로 자기 세계를 표현.","img":"https://images.unsplash.com/photo-1504198453319-5ce911bafcde"}
    ],
    "ENFJ": [
        {"job":"교육자/리더","desc":"사람을 이끌고 동기를 부여하는 역할.","img":"https://images.unsplash.com/photo-1531297484001-80022131f5a1"},
        {"job":"홍보/PR 전문가","desc":"조직의 이야기를 매력적으로 전달.","img":"https://images.unsplash.com/photo-1520975917837-7f3d8b6b2b8f"},
        {"job":"커뮤니티 매니저","desc":"사람들을 연결하고 활력을 불어넣음.","img":"https://images.unsplash.com/photo-1504384308090-c894fdcc538d"},
        {"job":"강연가/연설가","desc":"영감을 주는 메시지로 청중을 움직임.","img":"https://images.unsplash.com/photo-1503676260728-1c00da094a0b"},
        {"job":"HR/조직개발 전문가","desc":"사람 중심의 조직문화를 설계.","img":"https://images.unsplash.com/photo-1542744173-8e7e53415bb0"}
    ],
    "ENFP": [
        {"job":"크리에이터","desc":"다양한 매체로 아이디어를 자유롭게 표현.","img":"https://images.unsplash.com/photo-1503387762-592deb58ef4e"},
        {"job":"광고 기획자","desc":"감성을 자극하는 캠페인을 설계.","img":"https://images.unsplash.com/photo-1492724441997-5dc865305da7"},
        {"job":"작가/콘텐츠 제작자","desc":"사람의 공감을 끄는 콘텐츠 창작.","img":"https://images.unsplash.com/photo-1522202176988-66273c2fd55f"},
        {"job":"여행 작가/여행 기획자","desc":"새로운 경험을 기획하고 공유.","img":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"},
        {"job":"연예 기획 PD","desc":"창의적 콘텐츠로 스타와 작품을 만드는 직무.","img":"https://images.unsplash.com/photo-1515378791036-0648a3ef77b2"}
    ],
    "ISTJ": [
        {"job":"회계사/감사","desc":"숫자와 규정을 통해 안정성을 지키는 직업.","img":"https://images.unsplash.com/photo-1559526324-593bc073d938"},
        {"job":"법률 사무원","desc":"법적 절차를 정확히 수행하고 문서화.","img":"https://images.unsplash.com/photo-1488998527040-85054a85150b"},
        {"job":"군인/공무원","desc":"책임과 규율로 공공의 임무를 수행.","img":"https://images.unsplash.com/photo-1532634896-26909d0d3b14"},
        {"job":"프로젝트 매니저","desc":"체계적으로 일을 계획하고 완수.","img":"https://images.unsplash.com/photo-1517245386807-bb43f82c33c4"},
        {"job":"엔지니어","desc":"사실과 원리를 적용해 문제를 해결.","img":"https://images.unsplash.com/photo-1518770660439-4636190af475"}
    ],
    "ISFJ": [
        {"job":"간호사","desc":"세심한 돌봄으로 환자의 회복을 돕는 직업.","img":"https://images.unsplash.com/photo-1515378791036-0648a3ef77b2"},
        {"job":"사회복지사","desc":"사람들의 일상과 복지를 지원.","img":"https://images.unsplash.com/photo-1521737604893-d14cc237f11d"},
        {"job":"행정직/사무","desc":"정확하고 신뢰성 있는 행정 처리.","img":"https://images.unsplash.com/photo-1519222970733-f546218fa6d7"},
        {"job":"교사","desc":"학생 개개인에 대한 배려와 교육적 지원.","img":"https://images.unsplash.com/photo-1503676260728-1c00da094a0b"},
        {"job":"보건 전문가","desc":"지역 건강과 예방을 책임지는 역할.","img":"https://images.unsplash.com/photo-1558655146-dc3d3b1cd3a7"}
    ],
    "ESTJ": [
        {"job":"경영 관리자","desc":"실행 중심으로 조직 운영을 이끄는 역할.","img":"https://images.unsplash.com/photo-1521737604893-d14cc237f11d"},
        {"job":"재무 분석가","desc":"재무 데이터를 분석해 의사결정을 지원.","img":"https://images.unsplash.com/photo-1559526324-593bc073d938"},
        {"job":"군 장교/공공리더","desc":"책임감 있는 리더십으로 조직을 관리.","img":"https://images.unsplash.com/photo-1532634896-26909d0d3b14"},
        {"job":"생산/운영 관리자","desc":"생산성과 품질을 동시에 관리.","img":"https://images.unsplash.com/photo-1503602642458-232111445657"},
        {"job":"영업 관리자","desc":"팀을 조직해 목표 매출을 달성.","img":"https://images.unsplash.com/photo-1519389950473-47ba0277781c"}
    ],
    "ESFJ": [
        {"job":"교사/유치원 교사","desc":"사람 중심의 돌봄과 교육을 제공.","img":"https://images.unsplash.com/photo-1494790108377-be9c29b29330"},
        {"job":"간호사/헬스케어","desc":"환자와 가족을 세심히 돌보는 역할.","img":"https://images.unsplash.com/photo-1515378791036-0648a3ef77b2"},
        {"job":"이벤트 플래너","desc":"사람들이 즐길 수 있는 경험을 기획.","img":"https://images.unsplash.com/photo-1503602642458-232111445657"},
        {"job":"영업/고객 관리자","desc":"고객관계 관리와 서비스 향상 담당.","img":"https://images.unsplash.com/photo-1519389950473-47ba0277781c"},
        {"job":"고객 서비스 매니저","desc":"고객 만족을 최우선으로 조직을 운영.","img":"https://images.unsplash.com/photo-1520975917837-7f3d8b6b2b8f"}
    ],
    "ISTP": [
        {"job":"기계공/정비사","desc":"손으로 문제를 해결하고 즉시 수리하는 전문가.","img":"https://images.unsplash.com/photo-1518770660439-4636190af475"},
        {"job":"파일럿/항공 관련","desc":"기술적으로 정교한 조작을 담당.","img":"https://images.unsplash.com/photo-1508614999368-9260051290f4"},
        {"job":"응급구조사/소방관","desc":"위기 상황에서 침착히 대처하는 직업.","img":"https://images.unsplash.com/photo-1503602642458-232111445657"},
        {"job":"보안/사이버 보안 전문가","desc":"시스템을 방어하고 침해를 차단.","img":"https://images.unsplash.com/photo-1542223616-1b0f44b9a9a1"},
        {"job":"건축가/실무 엔지니어","desc":"실용적이면서 창의적인 공간 설계.","img":"https://images.unsplash.com/photo-1491567858451-5a3bbea3dfb9"}
    ],
    "ISFP": [
        {"job":"사진작가","desc":"순간을 예술로 포착하는 비주얼 아티스트.","img":"https://images.unsplash.com/photo-1504198453319-5ce911bafcde"},
        {"job":"패션 디자이너","desc":"개성과 미감을 옷으로 표현.","img":"https://images.unsplash.com/photo-1520975917837-7f3d8b6b2b8f"},
        {"job":"요리사/푸드 크리에이터","desc":"감각으로 맛과 경험을 만들어내는 직업.","img":"https://images.unsplash.com/photo-1504674900247-0877df9cc836"},
        {"job":"공예가/수공예","desc":"손으로 만드는 아름다운 오브제를 창조.","img":"https://images.unsplash.com/photo-1496317899792-9d7dbcd928a1"},
        {"job":"작곡가/음악가","desc":"감성으로 소리를 빚어내는 창작가.","img":"https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4"}
    ],
    "ESTP": [
        {"job":"영업 전문가","desc":"즉흥적 설득력으로 거래를 성사시키는 사람.","img":"https://images.unsplash.com/photo-1519389950473-47ba0277781c"},
        {"job":"스타트업 창업가","desc":"짧은 사이클로 빠르게 실험하고 성장.","img":"https://images.unsplash.com/photo-1525182008055-f88b95ff7980"},
        {"job":"프로 운동선수/트레이너","desc":"에너지와 경쟁심으로 성과를 만드는 직업.","img":"https://images.unsplash.com/photo-1517649763962-0c623066013b"},
        {"job":"경찰/보안 실무자","desc":"현장에서 직접 대응하며 안전을 지킴.","img":"https://images.unsplash.com/photo-1520975917837-7f3d8b6b2b8f"},
        {"job":"이벤트 프로듀서","desc":"현장 운영과 즉흥적 문제해결에 강함.","img":"https://images.unsplash.com/photo-1503602642458-232111445657"}
    ],
    "ESFP": [
        {"job":"배우/퍼포머","desc":"사람들 앞에서 즉흥성과 감정 표현으로 소통.","img":"https://images.unsplash.com/photo-1515378791036-0648a3ef77b2"},
        {"job":"여행 가이드/관광업","desc":"사람들과의 상호작용을 즐기는 직업.","img":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"},
        {"job":"가수/뮤지션","desc":"무대에서 에너지로 청중을 매료.","img":"https://images.unsplash.com/photo-1506152983158-9f30b7b2b4f1"},
        {"job":"방송 진행자","desc":"즉흥적 재치와 호감으로 프로그램을 이끔.","img":"https://images.unsplash.com/photo-1515377905703-c4788e51af15"},
        {"job":"홍보/이벤트 홍보 담당","desc":"공간과 사람을 연결해 화제를 만드는 역할.","img":"https://images.unsplash.com/photo-1520975917837-7f3d8b6b2b8f"}
    ],
}

# ---------- UI: 선택창, 버튼 ----------
mbti_list = sorted(mbti_data.keys())
left_col, center_col, right_col = st.columns([1,2,1])

with center_col:
    selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list, index=0, help="예: INTJ, ENFP 등")

# 재미 요소: 카드 크기 조절 또는 이미지 모드
with left_col:
    cols_count = st.selectbox("카드 열 갯수", options=[2,3,4], index=1, help="카드가 몇 열로 보여질지 선택하세요.")
with right_col:
    show_meta = st.checkbox("직업 설명 보이기", value=True)

st.write("")  # 여백

if st.button("✨ 추천받기 ✨", key="recommend"):
    jobs = mbti_data.get(selected_mbti, [])
    if not jobs:
        st.warning("해당 MBTI 데이터가 없습니다.")
    else:
        st.markdown(f"### 🔍 {selected_mbti} 타입 추천 직업 ({len(jobs)}개)")
        # 카드 레이아웃: cols_count로 나누기
        cols = st.columns(cols_count)
        for i, j in enumerate(jobs):
            col = cols[i % cols_count]
            with col:
                # 카드 HTML
                job_html = f"""
                <div class="job-card">
                    <img class="job-img" src="{j['img']}?auto=format&fit=crop&w=1000&q=60" alt="{j['job']}">
                    <div class="job-label">{selected_mbti}</div>
                    <div class="job-title">{j['job']}</div>
                    <div class="job-desc">{"<em>"+j['desc']+"</em>" if show_meta else ""}</div>
                    <div class="job-meta">추천 이유: MBTI 특성과 직무 적합성 기반</div>
                </div>
                """
                st.markdown(job_html, unsafe_allow_html=True)

        st.markdown("---")
        st.info("이미지를 직접 바꾸고 싶다면 `mbti_data`의 'img' 값을 원하는 이미지 URL로 바꿔주세요. Unsplash에서 'query' 검색 후 공유 URL을 사용하면 예쁩니다.")

# 추가 하단 설명
st.markdown("""
<div style="padding:8px;border-radius:8px;background:rgba(255,255,255,0.12);">
<p style="color:rgba(255,255,255,0.95);margin:6px 8px;">
이 추천기는 MBTI의 일반적 성향(예: 외향/내향, 감각/직관, 사고/감정, 판단/인식)을 기반으로 직무 예시를 제공하는 참고용 자료입니다. 
직업 선택은 개인의 가치관, 능력, 경험에 따라 달라지므로 다양한 정보와 체험을 통해 결정하세요.
</p>
</div>
""", unsafe_allow_html=True)
