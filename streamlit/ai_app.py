import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import requests
import json

# ==========================================
# 웹앱 설정
# ==========================================
st.set_page_config(page_title="Gemma 4 Data Analyzer", page_icon="📊", layout="wide")
st.title("📊 CSV 데이타 분석 및 Gemma 4 AI 챗봇")
st.markdown("Streamlit 기반으로 CSV 데이터를 추출/시각화 하고, 현재 실행 중인 **Gemma 4** (`gemma4:e4b`) 모델에게 데이터와 관련된 질문을 할 수 있습니다.")

# ==========================================
# 사이드바: 데이터 업로드
# ==========================================
st.sidebar.header("📁 데이터 업로드")
uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

# 샘플 데이터 다운로드 링크
sample_file_path = "data/sample_data.csv"
if os.path.exists(sample_file_path):
    with open(sample_file_path, "r", encoding="utf-8") as file:
        st.sidebar.markdown("---")
        st.sidebar.markdown("**샘플 데이터 제공**")
        st.sidebar.download_button(
            label="📥 테스트용 샘플 데이터 다운로드",
            data=file,
            file_name="sample_data.csv",
            mime="text/csv"
        )
        st.sidebar.caption("다운로드 후 위 업로드 공간에 드래그&드롭 하세요.")

# ==========================================
# 메인: 데이터 처리 및 시각화
# ==========================================
data_summary = ""
columns_info = ""

if uploaded_file is not None:
    try:
        # 데이터프레임으로 읽기
        df = pd.read_csv(uploaded_file)
        
        st.subheader("📝 데이터 미리보기 (Pandas DataFrame)")
        st.dataframe(df, use_container_width=True)
        
        # 수치형 데이터만 선택 (시각화용)
        numeric_df = df.select_dtypes(include=['float64', 'int64'])

        if numeric_df.shape[1] >= 2:
            st.divider()
            col1, col2 = st.columns(2)

            # 1. 산점도 (Scatter Graph)
            with col1:
                st.subheader("📈 산점도 (Scatter Plot)")
                st.markdown("두 변수 간의 관계를 보여줍니다.")
                x_axis = st.selectbox("X축 선택", numeric_df.columns, index=0)
                y_axis = st.selectbox("Y축 선택", numeric_df.columns, index=1)
                
                fig_scatter, ax_scatter = plt.subplots()
                sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax_scatter, color="#4A90E2")
                ax_scatter.grid(True, linestyle="--", alpha=0.6)
                st.pyplot(fig_scatter)

            # 2. 상관관계 히트맵 (Correlation Heatmap)
            with col2:
                st.subheader("🔥 상관관계 히트맵")
                st.markdown("수치형 변수들 간의 상관계수를 보여줍니다.")
                fig_heat, ax_heat = plt.subplots()
                corr_matrix = numeric_df.corr()
                sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax_heat, linewidths=0.5)
                st.pyplot(fig_heat)
        else:
            st.warning("시각화를 수행하기에 충분한 수치형 컬럼이 없습니다. (최소 2개 필요)")

        # AI 챗봇 컨텍스트 용 데이터 메타데이터 생성
        data_summary = df.describe().to_string()
        columns_info = ", ".join(df.columns.tolist())
    
    except Exception as e:
        st.error(f"CSV 파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.info("👈 왼쪽 사이드바에서 CSV 파일을 업로드하여 데이터 분석을 시작하세요.")

st.divider()

# ==========================================
# Gemma 4 AI 챗봇 (Ollama 연동)
# ==========================================
st.subheader("🤖 데이터 어시스턴트 (Gemma 4)")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma4:e4b"

# 대화 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 대화 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
if prompt := st.chat_input("업로드된 데이터에 대해 질문해보세요! (예: 이 데이터에서 가장 눈에 띄는 특징은 뭐야?)"):
    # 사용자 메시지 표시
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI 컨텍스트 주입용 시스템 프롬프트
    system_prompt = "당신은 데이터 분석 전문가 AI입니다. "
    if columns_info and data_summary:
        system_prompt += f"""
        현재 사용자가 분석 중인 데이터의 컬럼은 [{columns_info}] 입니다.
        기본적인 요약 통계는 다음과 같습니다.
        {data_summary}
        이 정보를 바탕으로 사용자의 질문에 명확하고 친절하게 한국어로 답변해주세요.
        """
    else:
        system_prompt += "현재 사용자가 업로드한 데이터가 없습니다. 먼저 데이터를 업로드하도록 안내하거나, 일반적인 데이터 분석 질문에 한국어로 답변해주세요."
    
    # 메시지 리스트 구성
    full_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    payload = {
        "model": MODEL_NAME,
        "messages": full_messages,
        "stream": True
    }

    # AI 응답 출력 (스트리밍)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            response = requests.post(OLLAMA_URL, json=payload, stream=True)
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        if "message" in chunk and "content" in chunk["message"]:
                            full_response += chunk["message"]["content"]
                            message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            else:
                st.error(f"응답 오류: 코드는 {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Ollama 서버에 연결할 수 없습니다. 터미널에서 'ollama serve'가 실행 중인지 확인해주세요.")
        except Exception as e:
            st.error(f"알 수 없는 오류 발생: {e}")
