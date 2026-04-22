# 상관성 분석 도구 (Correlation Analysis Tools)

이 폴더에는 상관성.xlsx 파일을 기반으로 한 상관성 분석을 위한 두 가지 도구가 포함되어 있습니다.

## 📁 파일 구조

```
streamlit/
├── correlation_app.py          # Streamlit 웹 대시보드
├── correlation_analysis.py     # 독립실행형 분석 스크립트
├── requirements.txt            # 필요한 라이브러리 목록
├── run_correlation_app.bat     # Streamlit 앱 실행 배치파일
├── README_CORRELATION.md       # 이 파일
└── data/
    └── 상관성.xlsx            # 분석 대상 데이터 파일
```

## 🚀 사용 방법

### 방법 1: Streamlit 웹 대시보드 (권장)

#### 자동 실행 (Windows)
```bash
# 배치파일을 더블클릭하거나 명령프롬프트에서 실행
run_correlation_app.bat
```

#### 수동 실행
```bash
# 1. 필요한 라이브러리 설치
pip install -r requirements.txt

# 2. Streamlit 앱 실행
streamlit run correlation_app.py
```

#### 웹 대시보드 특징:
- 📊 **인터랙티브 상관관계 히트맵**: 마우스 호버로 상세 정보 확인
- 📈 **산점도 행렬**: 변수간 관계를 시각적으로 표현
- 🔍 **분석 옵션**: Intraassay, Interassay, 또는 전체 분석 선택
- 📥 **데이터 다운로드**: 분석 결과를 CSV 형태로 다운로드
- 📱 **반응형 디자인**: 다양한 화면 크기에 대응

### 방법 2: 독립실행형 분석 스크립트

```bash
# Python 스크립트 직접 실행
python correlation_analysis.py
```

#### 독립실행형 스크립트 특징:
- 🖼️ **고품질 이미지 생성**: PNG 형태로 분석 결과 저장
- 📊 **종합 분석 리포트**: 콘솔에 상세한 통계 정보 출력
- 💾 **CSV 데이터 저장**: 정제된 데이터를 파일로 저장
- 🎯 **강한 상관관계 하이라이트**: |r| > 0.7인 상관관계 자동 식별

## 📊 분석 내용

### 1. Intraassay 분석 (재현성)
- **데이터**: 동일한 배치에서 2회 측정
- **변수**: Measurement_1, Measurement_2, Mean, SD, CV%
- **목적**: 측정의 재현성 평가

### 2. Interassay 분석 (정밀도)
- **데이터**: 서로 다른 날짜에 측정
- **변수**: Day_1, Day_2, Mean, SD, CV%
- **목적**: 측정의 정밀도 평가

### 3. 비교 분석
- **CV% 비교**: Intraassay vs Interassay 변동계수 비교
- **상관관계 강도**: 각 분석 유형별 변수간 상관관계
- **정밀도 지표**: 평균, 최대, 최소, 표준편차

## 📈 생성되는 시각화

1. **상관관계 히트맵**: 변수간 상관계수를 색상으로 표현
2. **산점도 행렬**: 모든 변수 쌍의 산점도
3. **CV% 비교 차트**: Intraassay vs Interassay CV% 산점도
4. **측정값 비교**: 각 측정 세트의 산점도
5. **SD vs CV% 관계**: 표준편차와 변동계수의 관계

## 🛠️ 요구사항

### Python 라이브러리
- pandas (데이터 처리)
- numpy (수치 계산)
- matplotlib (기본 시각화)
- seaborn (고급 시각화)
- plotly (인터랙티브 시각화)
- streamlit (웹 대시보드)
- openpyxl (Excel 파일 읽기)
- scipy (통계 분석)

### 시스템 요구사항
- Python 3.7 이상
- Windows/Mac/Linux 지원
- 웹 브라우저 (Streamlit 앱용)

## 📄 데이터 형식

`상관성.xlsx` 파일은 다음 구조를 따라야 합니다:

```
Row 4-8:   Intraassay 데이터 (Sample, Measurement_1, Measurement_2, Mean, SD, CV%)
Row 14-18: Interassay 데이터 (Sample, Day_1, Day_2, Mean, SD, CV%)
```

## 🔧 문제 해결

### 일반적인 문제들:

1. **파일을 찾을 수 없음**
   - `data/상관성.xlsx` 파일이 올바른 위치에 있는지 확인
   - 파일명이 정확한지 확인 (한글 인코딩 문제 주의)

2. **라이브러리 설치 오류**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Streamlit 실행 오류**
   ```bash
   # Streamlit 재설치
   pip uninstall streamlit
   pip install streamlit
   ```

4. **한글 폰트 문제**
   - matplotlib에서 한글이 깨질 경우, 시스템 폰트 설정 필요
   - Windows: 맑은 고딕, Mac: Apple SD Gothic Neo

## 📞 추가 지원

- 데이터 형식 변경이 필요한 경우 `correlation_analysis.py`의 데이터 로딩 부분 수정
- 추가 분석이 필요한 경우 새로운 함수 추가 가능
- 시각화 스타일 변경은 matplotlib/seaborn/plotly 설정에서 조정

## 📝 사용 예시

### Streamlit 대시보드 사용법:
1. 배치파일 실행 또는 `streamlit run correlation_app.py` 명령 실행
2. 웹 브라우저에서 자동으로 열린 페이지에서 분석 옵션 선택
3. 사이드바에서 원하는 분석 유형과 시각화 옵션 선택
4. 결과 확인 및 필요시 데이터 다운로드

### 독립실행형 스크립트 사용법:
1. `python correlation_analysis.py` 실행
2. 콘솔에서 분석 결과 확인
3. 생성된 PNG 이미지 파일 및 CSV 파일 확인