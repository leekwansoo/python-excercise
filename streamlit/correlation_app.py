import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(
    page_title="상관성 분석 대시보드",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("📊 상관성 분석 대시보드")
st.markdown("### 정밀도 측정 데이터의 상관관계 분석")

# Function to load and clean data
@st.cache_data
def load_correlation_data():
    """Load and clean the correlation data from Excel file"""
    try:
        file_path = "data/상관성.xlsx"
        df_raw = pd.read_excel(file_path, header=None)
        
        # Extract Intraassay data (rows 4-8)
        intraassay_data = []
        for i in range(4, 9):
            if i < len(df_raw):
                row = df_raw.iloc[i]
                numeric_values = []
                for val in row[1:]:  # skip first column
                    if pd.notna(val) and isinstance(val, (int, float)):
                        numeric_values.append(val)
                if len(numeric_values) >= 5:
                    intraassay_data.append(numeric_values)
        
        # Extract Interassay data (rows 14-18)
        interassay_data = []
        for i in range(14, 19):
            if i < len(df_raw):
                row = df_raw.iloc[i]
                numeric_values = []
                for val in row[1:]:  # skip first column
                    if pd.notna(val) and isinstance(val, (int, float)):
                        numeric_values.append(val)
                if len(numeric_values) >= 5:
                    interassay_data.append(numeric_values)
        
        # Create DataFrames
        intraassay_df = pd.DataFrame(intraassay_data, 
                                   columns=['Sample', 'Measurement_1', 'Measurement_2', 'Mean', 'SD', 'CV_percent'])
        
        interassay_df = pd.DataFrame(interassay_data, 
                                   columns=['Sample', 'Day_1', 'Day_2', 'Mean', 'SD', 'CV_percent'])
        
        return intraassay_df, interassay_df
    except Exception as e:
        st.error(f"데이터 로딩 중 오류가 발생했습니다: {e}")
        return None, None

# Function to create correlation heatmap
def create_correlation_heatmap(df, title, columns_to_analyze):
    """Create interactive correlation heatmap using plotly"""
    
    corr_matrix = df[columns_to_analyze].corr()
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        text=np.around(corr_matrix.values, decimals=3),
        texttemplate="%{text}",
        textfont={"size": 12},
        colorscale='RdBu',
        zmid=0,
        colorbar=dict(title="상관계수")
    ))
    
    fig.update_layout(
        title=title,
        title_x=0.5,
        width=600,
        height=500,
        xaxis_title="변수",
        yaxis_title="변수"
    )
    
    return fig, corr_matrix

# Function to create scatter plot matrix
def create_scatter_matrix(df, columns_to_analyze, title):
    """Create scatter plot matrix"""
    
    fig = make_subplots(
        rows=len(columns_to_analyze), 
        cols=len(columns_to_analyze),
        subplot_titles=[f"{col1} vs {col2}" for col1 in columns_to_analyze for col2 in columns_to_analyze],
        vertical_spacing=0.08,
        horizontal_spacing=0.08
    )
    
    for i, col1 in enumerate(columns_to_analyze):
        for j, col2 in enumerate(columns_to_analyze):
            if i == j:
                # Diagonal: histogram
                fig.add_trace(
                    go.Histogram(x=df[col1], name=col1, showlegend=False),
                    row=i+1, col=j+1
                )
            else:
                # Off-diagonal: scatter plot
                fig.add_trace(
                    go.Scatter(
                        x=df[col2], 
                        y=df[col1], 
                        mode='markers',
                        name=f"{col1} vs {col2}",
                        showlegend=False
                    ),
                    row=i+1, col=j+1
                )
    
    fig.update_layout(
        title=title,
        title_x=0.5,
        height=800,
        width=1000
    )
    
    return fig

# Load data
intraassay_df, interassay_df = load_correlation_data()

if intraassay_df is not None and interassay_df is not None:
    
    # Sidebar for analysis options
    st.sidebar.header("분석 옵션")
    analysis_type = st.sidebar.selectbox(
        "분석 유형을 선택하세요:",
        ["전체 분석", "Intraassay만", "Interassay만"]
    )
    
    visualization_type = st.sidebar.selectbox(
        "시각화 유형을 선택하세요:",
        ["상관관계 히트맵", "산점도 행렬", "둘 다"]
    )
    
    # Main content
    if analysis_type in ["전체 분석", "Intraassay만"]:
        st.header("🔍 Intraassay 분석")
        
        # Display data
        with st.expander("Intraassay 데이터 보기"):
            st.dataframe(intraassay_df)
        
        # Statistics
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📈 기본 통계")
            st.dataframe(intraassay_df.describe())
        
        with col2:
            st.subheader("📊 상관계수 요약")
            intra_columns = ['Measurement_1', 'Measurement_2', 'Mean', 'SD', 'CV_percent']
            intra_corr = intraassay_df[intra_columns].corr()
            st.dataframe(intra_corr)
        
        # Visualizations
        if visualization_type in ["상관관계 히트맵", "둘 다"]:
            st.subheader("🔥 Intraassay 상관관계 히트맵")
            intra_heatmap, _ = create_correlation_heatmap(
                intraassay_df, 
                "Intraassay 상관관계 히트맵", 
                intra_columns
            )
            st.plotly_chart(intra_heatmap, use_container_width=True)
        
        if visualization_type in ["산점도 행렬", "둘 다"]:
            st.subheader("📈 Intraassay 산점도 행렬")
            intra_scatter = create_scatter_matrix(
                intraassay_df, 
                intra_columns[:3],  # Limit to avoid overcrowding
                "Intraassay 산점도 행렬"
            )
            st.plotly_chart(intra_scatter, use_container_width=True)
    
    if analysis_type in ["전체 분석", "Interassay만"]:
        st.header("🔍 Interassay 분석")
        
        # Display data
        with st.expander("Interassay 데이터 보기"):
            st.dataframe(interassay_df)
        
        # Statistics
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📈 기본 통계")
            st.dataframe(interassay_df.describe())
        
        with col2:
            st.subheader("📊 상관계수 요약")
            inter_columns = ['Day_1', 'Day_2', 'Mean', 'SD', 'CV_percent']
            inter_corr = interassay_df[inter_columns].corr()
            st.dataframe(inter_corr)
        
        # Visualizations
        if visualization_type in ["상관관계 히트맵", "둘 다"]:
            st.subheader("🔥 Interassay 상관관계 히트맵")
            inter_heatmap, _ = create_correlation_heatmap(
                interassay_df, 
                "Interassay 상관관계 히트맵", 
                inter_columns
            )
            st.plotly_chart(inter_heatmap, use_container_width=True)
        
        if visualization_type in ["산점도 행렬", "둘 다"]:
            st.subheader("📈 Interassay 산점도 행렬")
            inter_scatter = create_scatter_matrix(
                interassay_df, 
                inter_columns[:3],  # Limit to avoid overcrowding
                "Interassay 산점도 행렬"
            )
            st.plotly_chart(inter_scatter, use_container_width=True)
    
    # Comparative analysis
    if analysis_type == "전체 분석":
        st.header("⚖️ 비교 분석")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("CV% 비교")
            comparison_df = pd.DataFrame({
                'Intraassay_CV': intraassay_df['CV_percent'],
                'Interassay_CV': interassay_df['CV_percent']
            })
            
            fig_cv = px.scatter(
                comparison_df, 
                x='Intraassay_CV', 
                y='Interassay_CV',
                title='Intraassay vs Interassay CV% 비교',
                labels={'Intraassay_CV': 'Intraassay CV%', 'Interassay_CV': 'Interassay CV%'}
            )
            fig_cv.add_shape(
                type="line", line=dict(dash="dash"),
                x0=0, x1=comparison_df.max().max(), 
                y0=0, y1=comparison_df.max().max()
            )
            st.plotly_chart(fig_cv, use_container_width=True)
        
        with col2:
            st.subheader("정밀도 지표 요약")
            summary_stats = pd.DataFrame({
                'Metric': ['Mean CV%', 'Max CV%', 'Min CV%', 'Std CV%'],
                'Intraassay': [
                    intraassay_df['CV_percent'].mean(),
                    intraassay_df['CV_percent'].max(),
                    intraassay_df['CV_percent'].min(),
                    intraassay_df['CV_percent'].std()
                ],
                'Interassay': [
                    interassay_df['CV_percent'].mean(),
                    interassay_df['CV_percent'].max(),
                    interassay_df['CV_percent'].min(),
                    interassay_df['CV_percent'].std()
                ]
            })
            st.dataframe(summary_stats)
    
    # Download section
    st.header("💾 데이터 다운로드")
    col1, col2 = st.columns(2)
    
    with col1:
        csv_intra = intraassay_df.to_csv(index=False)
        st.download_button(
            label="📥 Intraassay 데이터 다운로드 (CSV)",
            data=csv_intra,
            file_name='intraassay_data.csv',
            mime='text/csv'
        )
    
    with col2:
        csv_inter = interassay_df.to_csv(index=False)
        st.download_button(
            label="📥 Interassay 데이터 다운로드 (CSV)",
            data=csv_inter,
            file_name='interassay_data.csv',
            mime='text/csv'
        )

else:
    st.error("데이터를 불러올 수 없습니다. '상관성.xlsx' 파일이 data 폴더에 있는지 확인해주세요.")
    
    # Sample data creation for demonstration
    st.info("샘플 데이터로 데모를 실행합니다.")
    
    # Create sample data
    np.random.seed(42)
    sample_intra = pd.DataFrame({
        'Sample': range(1, 6),
        'Measurement_1': np.random.normal(5, 2, 5),
        'Measurement_2': np.random.normal(5, 2, 5),
        'Mean': np.random.normal(5, 2, 5),
        'SD': np.random.uniform(0.1, 0.5, 5),
        'CV_percent': np.random.uniform(1, 10, 5)
    })
    
    st.subheader("샘플 데이터 상관관계 분석")
    fig_sample, _ = create_correlation_heatmap(
        sample_intra,
        "샘플 데이터 상관관계",
        ['Measurement_1', 'Measurement_2', 'Mean', 'SD', 'CV_percent']
    )
    st.plotly_chart(fig_sample, use_container_width=True)