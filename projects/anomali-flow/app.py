import numpy as np
import streamlit as st
import requests
import pandas as pd
import time
import json
import tensorly as tl
from sklearn.preprocessing import StandardScaler
from tensorly.decomposition import parafac
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.mixture import GaussianMixture
from bokeh.plotting import figure
from bokeh.palettes import Blues256
from bokeh.models import LinearColorMapper,Spacer,Range1d, ColorBar, ColumnDataSource, Legend, HoverTool, TableColumn, DataTable, CustomJS, TapTool
from bokeh.transform import transform, jitter
from bokeh.layouts import column, row
from prefect import flow, task
from celery.result import AsyncResult
from worker import run_timeseries_workflow, run_categorical_workflow, run_numerical_workflow

# 시각화 태스크
#@task
#def create_visualizations(result, graph_type, x_column, y_column, df, selected_features):
def create_visualizations(result, graph_type, x_column, y_column, df, start_handle=None, end_handle=None):
    
    # outlier_indices 변수가 사용되기 전에 빈 리스트로 초기화
    outlier_indices = []
    
    outlier_indices = result.get('outlier_indices')
    outlier_probabilities = result.get('outlier_probabilities')
    root_cause_scores = result.get('root_cause_scores')
    index = result.get('index')
    
    # Root Cause Score 히트맵 생성
    if root_cause_scores:
        # 시각화를 위한 데이터 준비
        timestamps = list(dict.fromkeys([str(ts) for ts in index if str(ts) in root_cause_scores]))
        features = list(next(iter(root_cause_scores.values())).keys())
        # 히트맵 데이터 생성
        heatmap_data = {
            'timestamp': [],
            'feature': [],
            'score': []
        }
    
        for timestamp in timestamps:
            for feature in features:
                score = root_cause_scores.get(str(timestamp), {}).get(feature, 0)
                heatmap_data['timestamp'].append(timestamp)
                heatmap_data['feature'].append(feature)
                heatmap_data['score'].append(score)
    
        # 정규화
        scaler = MinMaxScaler(feature_range=(0, 100))
        normalized_scores = scaler.fit_transform(np.array(heatmap_data['score']).reshape(-1, 1)).flatten()
        heatmap_data['score'] = normalized_scores
    
        source = ColumnDataSource(data=heatmap_data)
    
        # 색상 매퍼 생성
        mapper = LinearColorMapper(palette="Blues256", low=100, high=0)
        
        # 히트맵 플롯 생성
        p_heatmap = figure(
            title="Root Cause Scores Heatmap",
            x_range=timestamps,
            y_range=features,
            x_axis_label='Timestamp',
            y_axis_label='Feature',
            plot_width=1000,
            plot_height=400,
            tools="pan,wheel_zoom,box_zoom,reset",
            tooltips=[('Feature', '@feature'), ('Timestamp', '@timestamp'), ('Score', '@score')],
        )
    
        p_heatmap.rect(
            x="timestamp",
            y="feature",
            width=1,
            height=1,
            source=source,
            fill_color=transform('score', mapper),
            line_color=None
        )
    
        # 색상 바 추가
        color_bar = ColorBar(color_mapper=mapper, location=(0, 0))
        p_heatmap.add_layout(color_bar, 'right')
    
        # 히트맵을 Streamlit에 표시
        st.bokeh_chart(p_heatmap)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

        
        st.markdown(
            "<p style='color:grey; font-size:12px; line-height:0.8;'>| outlier로 판별되는 근본적인 원인을 분석하고, 각 요소의 기여도를 점수로 시각화한 그래프입니다. </p>",
            unsafe_allow_html=True
        )
        
        # 여백 추가
        st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

    # 추가 그래프
    outlier_indices_all = [i for i in outlier_indices if pd.notna(i) and i in df.index]
    inlier_indices_all = [i for i in df.index if i not in outlier_indices_all]
    
    inliers_all = df.loc[inlier_indices_all] if inlier_indices_all is not None else pd.DataFrame()
    outliers_all = df.loc[outlier_indices_all] if outlier_indices_all is not None else pd.DataFrame()
    
    # 전체 Data의 ColumnDataSource 생성
    source_inliers_all = ColumnDataSource(data=dict(
        x=inlier_indices_all,
        y=inliers_all[y_column] if not inliers_all.empty else [],
    ))    
    
    source_outliers_all = ColumnDataSource(data=dict(
        x=outlier_indices_all if outlier_indices_all is not None else [],  # outlier 인덱스 사용
        y=outliers_all[y_column] if not outliers_all.empty else [],  # outlier 값
    ))
    
    p_all = figure(title="Anomaly Score Graph", x_axis_label="Index", y_axis_label="Value", 
               plot_width=1000, plot_height=400,
               tools="pan,wheel_zoom,box_zoom,reset", 
               tooltips=[("Index", "@x"), ("Value", "@y")])
    
    # y축 범위 계산 및 확장
    y_min, y_max = min(inliers_all[y_column].min(), outliers_all[y_column].min()), max(inliers_all[y_column].max(), outliers_all[y_column].max())
    y_extension = 2  # 추가하고 싶은 범위
    p_all.y_range = Range1d(y_min - y_extension, y_max + y_extension)
    
    p_all.title.align = "center"
    p_all.title.offset = 10
    p_all.title.text_font_style = "bold"
    p_all.title.text_font_size = "13pt"
    
    p_all.xaxis.axis_label_text_font_style = "italic"
    p_all.xaxis.axis_label_text_font_size = "10pt"
    
    p_all.yaxis.axis_label_text_font_style = "italic"
    p_all.yaxis.axis_label_text_font_size = "10pt"

    # 전체 데이터의 그래프에 inliers와 outliers 그리기
    p_all.line(x='x', y='y', source=source_inliers_all, line_color='#3A7CA5', line_width=2, legend_label='Inliers')
    p_all.circle(x='x', y='y', source=source_outliers_all, color='#FF6B6B', size=6, legend_label='Outliers')
    
    # Anomaly Score Graph 출력
    st.bokeh_chart(p_all)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    
    # 그래프 위에 설명 추가
    st.markdown(
        "<p style='color:grey; font-size:12px; line-height:0.8;'>| 전체 데이터에서의 outlier와 inlier의 분포를 나타내는 그래프입니다.</p>",
        unsafe_allow_html=True
    )
    
    # 여백 추가
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    
    
    # 입력 구간(start_handle, end_handle)에 해당하는 데이터만 선택
    if start_handle is None or end_handle is None:
        filtered_df = df  # 전체 데이터 사용
    else:
        # 위치 기반으로 입력된 범위에 해당하는 데이터를 필터링
        filtered_df = df.iloc[df.index.get_loc(start_handle):df.index.get_loc(end_handle) + 1]


    # 이상치와 정상 데이터 구분
    if outlier_indices is not None and len(outlier_indices) > 0:
        inliers = filtered_df.drop(outlier_indices)
        outliers = filtered_df.loc[outlier_indices]
    else:
        inliers = filtered_df
        outliers = pd.DataFrame()  # 빈 DataFrame으로 처리


    # Inliers와 Outliers에 대해 각각의 ColumnDataSource 생성
    source_inliers = ColumnDataSource(data=dict(
        x=inliers[x_column], 
        y=inliers[y_column],
        **{feature: inliers[feature] for feature in inliers.columns if feature not in [x_column, y_column]}
    ))

    if not outliers.empty:
        outliers_data = {'x': outliers[x_column], 'y': outliers[y_column]}
        for col in outliers.columns:
            if col != x_column and col != y_column:
                outliers_data[col] = outliers[col]
        source_outliers = ColumnDataSource(data=outliers_data)
    else:
        source_outliers = None

    # Graph2 설정
    p_2d = figure(title=f"{x_column} vs {y_column}", 
                tools="pan,wheel_zoom,box_zoom,reset", 
                tooltips=[("X", "@x"), ("Y", "@y")])
    
    p_2d.title.align = "left"
    p_2d.title.offset = 10
    p_2d.title.text_font_style = "bold"
    p_2d.title.text_font_size = "13pt"
    
    p_2d.xaxis.axis_label_text_font_style = "italic"
    p_2d.xaxis.axis_label_text_font_size = "10pt"
    
    p_2d.yaxis.axis_label_text_font_style = "italic"
    p_2d.yaxis.axis_label_text_font_size = "10pt"

    # 그래프 타입에 따른 그리기
    if graph_type == "Line Graph":
        p_2d.line(x='x', y='y', source=source_inliers, line_color='#3A7CA5', line_width=2, legend_label='Inliers')
        if source_outliers is not None:
            p_2d.circle(x='x', y='y', source=source_outliers, color='#FF6B6B', size=6, legend_label='Outliers')

    elif graph_type == "Scatter Plot":
        p_2d.circle(x='x', y='y', source=source_inliers, color='#3A7CA5', size=6, legend_label='Inliers')
        if source_outliers is not None:
            p_2d.circle(x='x', y='y', source=source_outliers, color='#FF6B6B', size=6, legend_label='Outliers')

    elif graph_type == "Bar Graph":
        p_2d.vbar(x='x', top='y', source=source_inliers, width=0.9, color='#3A7CA5', alpha=0.8, legend_label='Inliers')
        if source_outliers is not None:
            p_2d.circle(x='x', y='y', source=source_outliers, color='#FF6B6B', size=6, legend_label='Outliers')
        p_2d.xgrid.grid_line_color = None
        p_2d.y_range.start = 0

    if graph_type == "Scatter Plot (Jittered)":
        # Inliers 데이터로 Scatter Plot (Jittering) 생성
        p_2d.circle(x=jitter('x', width=0.1), y='y', source=source_inliers, color='#3A7CA5', size=6, legend_label='Inliers')
        # Outliers 데이터가 존재하면 Outliers도 표시
        if source_outliers is not None:
            p_2d.circle(x=jitter('x', width=0.1), y='y', source=source_outliers, color='#FF6B6B', size=6, legend_label='Outliers')
            
        # x축 레이블에 원래 값 사용 (LabelEncoder 사용)
        if x_column in label_encoders:
            x_ticks = sorted(set(inliers[x_column]))
            x_labels = label_encoders[x_column].inverse_transform(x_ticks)
            
            x_labels = pd.Series(x_labels).fillna('Unknown').tolist()
            
            p_2d.xaxis.ticker = x_ticks
            p_2d.xaxis.major_label_overrides = {tick: label for tick, label in zip(x_ticks, x_labels)}

        # y축 레이블에 원래 값 사용 (LabelEncoder 사용)
        if y_column in label_encoders:
            y_ticks = sorted(set(inliers[y_column]))
            y_labels = label_encoders[y_column].inverse_transform(y_ticks)
            p_2d.yaxis.ticker = y_ticks
            p_2d.yaxis.major_label_overrides = {tick: label for tick, label in zip(y_ticks, y_labels)}

        # x축 및 y축 레이블 설정
        p_2d.xaxis.axis_label = x_column
        p_2d.yaxis.axis_label = y_column

    # Hover tool 추가
    hover_tool_3 = HoverTool(tooltips=[('x', '@x'), ('y', '@y')], mode='vline')
    p_2d.add_tools(hover_tool_3)

    # 테이블에 출력할 데이터를 저장할 ColumnDataSource 생성 (빈 데이터로 초기화)
    selected_point_features = ColumnDataSource(data=dict(Feature=[], Value=[]))

    # 테이블 컬럼 설정
    columns = [
        TableColumn(field="Feature", title="Feature"),
        TableColumn(field="Value", title="Value"),
    ]

    # DataTable 생성
    data_table = DataTable(source=selected_point_features, columns=columns, width=400, height=280)

    # TapTool 추가 및 콜백 연결
    tap_callback = CustomJS(args=dict(source_outliers=source_outliers, source_inliers=source_inliers, selected_source=selected_point_features), code="""
    console.log("Callback triggered");

    var outlier_selected_indices = source_outliers.selected.indices;
    var inlier_selected_indices = source_inliers.selected.indices;

    var data, selected_indices;

    if (outlier_selected_indices.length > 0) {
        selected_indices = outlier_selected_indices;
        data = source_outliers.data;
        source_inliers.selected.indices = [];
    } else if (inlier_selected_indices.length > 0) {
        selected_indices = inlier_selected_indices;
        data = source_inliers.data;
        source_outliers.selected.indices = [];
    }

    if (selected_indices.length > 0) {
        var index = selected_indices[0];
        var feature_names = Object.keys(data).filter(name => name !== 'x' && name !== 'y');
        var feature_values = feature_names.map(name => data[name][index]);

        var table_data = { Feature: [], Value: [] };
        for (var i = 0; i < feature_names.length; i++) {
            table_data['Feature'].push(feature_names[i]);
            table_data['Value'].push(feature_values[i]);
        }

        selected_source.data = table_data;
        selected_source.change.emit();
        console.log("Table updated");
    }
    """)

    if source_outliers is not None and source_inliers is not None:
        tap_tool = TapTool()
        p_2d.add_tools(tap_tool)
        source_outliers.selected.js_on_change('indices', tap_callback)
        source_inliers.selected.js_on_change('indices', tap_callback)
    
    # 그래프와 설명 사이에 여백 추가 (필요 시)
    st.markdown("<br>", unsafe_allow_html=True) 
    

        
    layout = row(p_2d, data_table)
    st.bokeh_chart(layout)  
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # 두 번째 그래프와 데이터 테이블
    st.markdown(
        "<p style='color:grey;font-size:12px; line-height:0.8;'>| 앞서 선택한 두 개의 feature를 기준으로 outlier와 inlier의 분포를 시각화한 그래프입니다. </p>"
        "<p style='color:grey; font-size:12px; line-height:0.8;'>  더 자세히 확인하고 싶은 point를 클릭해보세요. 오른쪽 table에서 선택한 point에 대한 세부사항을 확인할 수 있습니다.</p>",
        unsafe_allow_html=True
    )
    
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

    


######## Time Series 데이터 Prefect워크플로우 and tasks ########
# 데이터 로드 및 유형 감지
def classify_dataset(df):
    num_cols = len(df.columns)
    
    # Time series: 시간 관련 열이 존재하는지 확인
    time_series_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col]) or 
                        (df[col].dtype == 'object' and pd.to_datetime(df[col], errors='coerce').notna().any())]

    if time_series_cols:
        return 'time_series'

    # Categorical: 열의 고유한 값이 일정 임계치 미만이면 categorical로 분류
    categorical_count = sum(
        (df[col].dtype == 'object' or df[col].nunique() / len(df) < 0.05)
        for col in df.columns
    )
    if categorical_count / num_cols > 0.5:
        return 'categorical'

    # Numerical: 대부분의 열이 숫자형인 경우
    numerical_count = sum(np.issubdtype(df[col].dtype, np.number) for col in df.columns)
    if numerical_count / num_cols > 0.5:
        return 'numerical' # 'numerical'
    
    return 'unknown'

# 데이터 전처리
def timeseries_preprocess(df, tensor_rank, sliding_window_size):
    # 0번째 열을 따로 저장 (원본 데이터 그대로 사용)
    first_col = df.iloc[:, 0]

    # 나머지 열만 전처리 진행
    df_processed = df.iloc[:, 1:].copy()
    
    for col in df_processed.columns:
        # 숫자 변환이 필요한 경우를 대비해 모든 열을 숫자로 변환
        df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce')  # 변환할 수 없는 값을 NaN으로 처리
        df_processed[col] = df_processed[col].fillna(df_processed[col].median())

        # 슬라이딩 윈도우 적용
        data = df_processed[col].to_numpy()
        T = len(data)
        N = T - sliding_window_size + 1

        if N <= 0:
            continue

        sliding_windows = np.array([data[i:i + sliding_window_size] for i in range(N)])
        sliding_windows = np.mean(sliding_windows, axis=1)
        df_processed[col] = pd.Series(sliding_windows, index=df_processed.index[:len(sliding_windows)])

    # NaN 값을 중앙값으로 대체
    df_processed = df_processed.fillna(df_processed.median())

    # 0번째 열을 다시 결합하여 반환
    df_processed.insert(0, first_col.name, first_col)

    return df_processed



def categorical_preprocess(df):
    # 0번째 열을 따로 저장 (원본 데이터 그대로 사용)
    first_col = df.iloc[:, 0]

    # 나머지 열만 전처리 진행
    df_processed = df.iloc[:, 1:].copy()
    
    label_encoders = {}
    for column in df_processed.columns:
        # Categorical 열인지 확인
        if df_processed[column].dtype == 'object' or pd.api.types.is_categorical_dtype(df_processed[column]):
            # LabelEncoder를 사용해 범주형 데이터를 숫자로 변환
            le = LabelEncoder()
            df_processed[column] = le.fit_transform(df_processed[column])
            label_encoders[column] = le  # 나중에 변환할 때 사용할 수 있도록 저장

    # 0번째 열을 다시 결합하여 반환
    df_processed.insert(0, first_col.name, first_col)

    return df_processed, label_encoders

def numerical_preprocess(df, tensor_rank):
    # 0번째 열을 따로 저장 (원본 데이터 그대로 사용)
    first_col = df.iloc[:, 0]

    # 나머지 열만 전처리 진행
    df_processed = df.iloc[:, 1:].copy()
    scaler = StandardScaler()

    for col in df_processed.columns:
        # 작은 따옴표로 묶인 문자열을 처리하여 float으로 변환
        if df_processed[col].dtype == object:  # 문자열로 인식되는 경우
            df_processed[col] = df_processed[col].str.replace("'", "").astype(float)

        # 열이 numerical인지 확인 (숫자형 열만 텐서 분해 적용)
        if np.issubdtype(df_processed[col].dtype, np.number):
            data = df_processed[col].to_numpy().reshape(-1, 1)

            # 데이터 스케일링 적용
            scaled_data = scaler.fit_transform(data)

            # 텐서 분해 적용
            tensor = tl.tensor(scaled_data)
            factors = parafac(tensor, rank=tensor_rank)
            reconstructed_tensor = tl.kruskal_to_tensor(factors)
            df_processed[col] = pd.Series(reconstructed_tensor.flatten(), index=df_processed.index)

        # NaN 값 중앙값으로 대체 (숫자형 열만)
        df_processed[col] = df_processed[col].fillna(df_processed[col].median())

    # 0번째 열을 다시 결합하여 반환
    df_processed.insert(0, first_col.name, first_col)

    return df_processed


# Prefect 태스크: Celery에 작업을 넘기는 함수
@task(log_prints=True)
def submit_to_celery(df, algorithm, params, workflow_type):
    if workflow_type == 'timeseries':
        task = run_timeseries_workflow.apply_async(args=[df, algorithm, params])
    elif workflow_type == 'categorical':
        task = run_categorical_workflow.apply_async(args=[df, algorithm, params])
    elif workflow_type == 'numerical':
        task = run_numerical_workflow.apply_async(args=[df, algorithm, params])
    
    return task.id  # 작업 ID 반환

# Prefect 태스크: Celery 작업의 결과를 가져오는 함수
@task(log_prints=True)
def get_celery_result(task_id):
    task_result = AsyncResult(task_id)
    if task_result.ready():
        return task_result.result
    else:
        return "Task is still running..."

######## Time Series  데이터 Prefect 워크플로우 ########
@flow(log_prints=True)
def timeseries_workflow(df, algorithm, param):
    # Celery worker에 작업을 넘김
    task_id = submit_to_celery(df, algorithm, params, 'timeseries')
    # Celery 작업의 결과를 가져옴
    result = get_celery_result(task_id)
    return result

######## Categorical  데이터 Prefect 워크플로우 ########
@flow(log_prints=True)
def categorical_workflow(df, algorithm, params):
    # Celery worker에 작업을 넘김
    task_id = submit_to_celery(df, algorithm, params, 'categorical')
    # Celery 작업의 결과를 가져옴
    result = get_celery_result(task_id)
    return result

######## Numerical  데이터 Prefect 워크플로우 ########
@flow(log_prints=True)
def numerical_workflow(df, algorithm, params):
    # Celery worker에 작업을 넘김
    task_id = submit_to_celery(df, algorithm, params, 'numerical')
    # Celery 작업의 결과를 가져옴
    result = get_celery_result(task_id)
    return result

######## 시각화 ########
@flow
def visualization_flow(result, graph_type, x_column, y_column, df, start_handle=None, end_handle=None):
    create_visualizations(result, graph_type, x_column, y_column, df, start_handle, end_handle)

st.set_page_config(layout="wide")  # 화면을 넓게 사용

# 세션 상태 유지 (CSV 파일 및 모델 실행 상태 관리)
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# 쿼리 파라미터 확인
if 'model_run' not in st.session_state:
    st.session_state.model_run = False

# 기본적으로는 Configuration 탭만 존재
if st.session_state.model_run:
    tabs = st.tabs(["Configuration Page", "Visualization Page"])
else:
    tabs = st.tabs(["Configuration Page"])

if __name__ == "__main__":
    with tabs[0]:
        # Streamlit 인터페이스
        col1, col2 = st.columns(2)
        with col1:
            # st.set_page_config(page_title="AnomaliFlow: Distributed Execution of Reusable ML Workflows", page_icon=":material/edit:")
            st.title("AnomaliFlow")
            
            st.markdown("""
                        AnomaliFlow는 분산 환경에서 재사용 가능한 머신러닝 워크플로우를 실행하기 위한 강력한 도구입니다. 이 플랫폼은 복잡한 머신러닝 파이프라인을 손쉽게 구성하고, 이를 여러 컴퓨팅 노드에 분산하여 빠르게 처리할 수 있도록 돕습니다. 다양한 데이터셋과 머신러닝 모델을 효과적으로 결합하고, 유연한 실행을 가능하게 하여 사용자에게 높은 생산성을 제공합니다.

                        주요 기능:
                        - **분산 컴퓨팅 지원**: 여러 노드에서 병렬 처리를 통해 대용량 데이터 및 복잡한 모델도 빠르게 처리 가능합니다.
                        - **워크플로우 재사용성**: 반복적인 작업을 자동화하고, 다양한 환경에서도 동일한 워크플로우를 쉽게 재사용할 수 있습니다.
                        - **확장성**: 다양한 ML 프레임워크 및 툴과의 통합을 지원하여 확장성과 유연성을 제공합니다.

                        이 플랫폼을 통해 보다 효율적이고 간편한 머신러닝 개발을 경험해보세요.
                        """)
            # sidebar
            with st.sidebar:
                st.title("AnomaliFlow")
                st.markdown("""
                            Distributed Execution of Reusable ML Workflows
                            """)
                st.divider()
                st.header("💻 주요 기능")
                stage = st.sidebar.button('About')
                                        
                st.header("⚙ ML Models") 
                stage = st.sidebar.button('Supported ML Models')

                # http://localhost:4200/dashboard 와의 연동
                st.header("📊 Workflow Management")
                stage = st.sidebar.radio("Choose Step", ['Home', 'Saved Workflows', 'Monitor Workflows'])

                st.header("만든 사람")
                stage = st.sidebar.button('Our team')
                

            st.header("Data import" )
            uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

            st.header("Jobs for Executing Distributed Task", divider=True)
            n_jobs = st.slider("Select n_jobs", min_value=1, max_value=6, value=2)

            st.write(f"n_jobs: {n_jobs}")

            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file, encoding="UTF-8")
                st.write(df)

                # Detect data types
                data_type = classify_dataset(df)
                st.write(data_type)
                with col2:        
                    st.header(f"Type of the Dataset: {data_type.capitalize()}", divider=True)
                    
                    model_selections = {}

                    # Time Series Data
                    if data_type == 'time_series':
                        
                        st.subheader(f"Model Configuration", divider=True)
                        # Hyper-parameters for Tensor Decomposition and Window Operation
                        tensor_rank = st.slider("Tensor Rank", min_value=1, max_value=10, value=3)
                        sliding_window_size = st.slider("Sliding Window Size", min_value=2, max_value=50, value=5)

                        # Data Preprocessing
                        df = timeseries_preprocess(df, tensor_rank, sliding_window_size)

                        # Model Selection
                        time_series_model = st.selectbox("Select a Model", ["IsolationForest", "GMM"])
                        
                        
                        # # 양방향 슬라이더
                        # preview_handle_range = st.slider(
                        #     "Filtering range for data points", 
                        #     1, len(df), 
                        #     value=(1, 1500)  # 초기값 범위 설정 (시작점, 끝점)
                        # )

                        # # 타임 필터링
                        # start_handle, end_handle = map(int, preview_handle_range)
                        # selected_data = df[start_handle:end_handle]

                        # # threshold_handle = st.slider("Threshold", 0.0, 1.0, value=0.5)
                        
                        params = {}
                        if time_series_model == "IsolationForest":
                            params['max_samples'] = st.number_input("The maximum number of samples", 1, len(df))
                            params['n_estimators'] = st.number_input("The number of estimators", 1, 1000, value=100)
                            params['contamination'] = st.number_input("The contamination parameter", 0.0, 0.5, value=0.1)
                            params['n_jobs'] = n_jobs
                        elif time_series_model == "GMM":
                            params['n_init'] = st.slider("The number of times for the GMM execution with different certroid seeds", min_value=1, max_value=10, value=1)
                            params['n_components'] = st.number_input("The number of components", 1, len(df), value=2)
                            # params['covariance_type'] = st.selectbox("Covariance type", ["full", "tied", "diag", "spherical"], index=0)
                            params['random_state'] = st.number_input("Random state", 0, 1000, value=42)
                            params['init_params'] = 'kmeans'
                        
                        st.subheader(f"Visualization", divider=True)
                        graph_type = st.selectbox("Select a Graph Type", ["Line Graph", "Scatter Plot", "Bar Graph"])
                        columns = df.columns.tolist()
                        columns = [col for col in df.columns if col != 'date']
                        x_column = st.selectbox("Select X-axis Feature", columns)
                        y_column = st.selectbox("Select Y-axis Feature", columns)
                        
                        if st.button("Run your workflow"):
                            st.session_state.model_run = True
                            if len(tabs) > 1 and st.session_state.model_run:
                                with tabs[1]:
                                    st.title("AnomaliFlow Visualization")
                                    # Celery worker에 비동기 작업 요청
                                    df_dict = df.to_dict(orient='records')
                                    result = run_timeseries_workflow(df_dict, time_series_model, params)
                                    
                                    # Visualization step
                                    if result:
                                        st.write("Workflow Completed! Visualizing Results...")
                                        # Call visualization function
                                        visualization_flow(result, graph_type, x_column, y_column, df, None, None)
                                        st.write(result)
                                        #visualization_flow(result, graph_type, x_column, y_column, df, start_handle, end_handle)    
                    
                    # Categorical Data
                    elif data_type == 'categorical':
                        
                        st.subheader(f"Model Configuration", divider=True)
                        # Data Preprocessing
                        df, label_encoders = categorical_preprocess(df)

                        # Algorithm select (데이터 유형별로 다르게)
                        algorithm = st.selectbox("Select a Model", ["DBSCAN", "LOF"])

                        # threshold_handle = st.slider("Threshold", 0.0, 1.0, value=0.5)

                        # parameters
                        params = {}
                        if algorithm == "DBSCAN":
                            eps = st.slider("epsilon(Ɛ)", min_value=0.01, max_value=10.00, value=0.05)
                            min_samples = st.slider("The mininum number of samples", min_value=1, max_value=100, value=5)
                            params = {"eps": eps, "min_samples": min_samples, "n_jobs" : n_jobs}
                        elif algorithm == "LOF":
                            params['n_neighbors'] = st.number_input("The number of neighbors", 1, 100, value=20)
                            params['contamination'] = st.number_input("The contamination parameter", 0.0, 0.5, value=0.1)
                            params['n_jobs'] = n_jobs


                        st.subheader(f"Visualization", divider=True)
                        graph_type = st.selectbox("Select a Type of Chart ", ["Line Graph", "Scatter Plot", "Bar Graph", "Scatter Plot (Jittered)"])
                        columns = df.columns.tolist()
                        x_column = st.selectbox("Select X-axis Feature", columns)
                        y_column = st.selectbox("Select Y-axis Feature", columns)

                        if st.button("Run your workflow"):
                            st.session_state.model_run = True
                            if st.session_state.model_run:
                                with tabs[1]:
                                    st.title("AnomaliFlow Visualization")
                                    # Celery worker에 비동기 작업 요청
                                    df_dict = df.to_dict(orient='records')
                                    result = run_categorical_workflow(df_dict, algorithm, params)
                                    
                                    # Visualization step
                                    if result:
                                        st.write("Workflow Completed! Visualizing Results...")
                                        st.write(result)
                                        # Call visualization function
                                        visualization_flow(result, graph_type, x_column, y_column, df, None, None)

                    # Numerical Data
                    if data_type == 'numerical':
                        
                        st.subheader(f"Model Configuration", divider=True)
                        # Hyper-parameters for Tensor Decomposition 
                        tensor_rank = st.slider("Tensor Rank", min_value=1, max_value=10, value=1)

                        # Data Preprocessing
                        df = numerical_preprocess(df, tensor_rank)

                        # Model Selection
                        numerical_model = st.selectbox("Select a Model", ["IsolationForest", "GMM", "DBSCAN", "LOF", "KMeans"])

                        # threshold_handle = st.slider("Threshold", 0.0, 1.0, value=0.5)
                        
                        params = {}
                        if numerical_model == "IsolationForest":
                            params['max_samples'] = st.number_input("The maximum number of samples", 1, len(df))
                            params['n_estimators'] = st.number_input("The number of estimators", 1, 1000, value=100)
                            params['contamination'] = st.number_input("The contamination parameter", 0.0, 0.5, value=0.1)
                            params['n_jobs'] = n_jobs
                        elif numerical_model == "GMM":
                            params['n_init'] = st.slider("The number of times for the GMM execution with different certroid seeds", min_value=1, max_value=10, value=1)
                            params['n_components'] = st.number_input("The number of components", 1, len(df), value=2)
                            # params['covariance_type'] = st.selectbox("Covariance type", ["full", "tied", "diag", "spherical"], index=0)
                            params['random_state'] = st.number_input("Random state", 0, 1000, value=42)
                            params['init_params'] = 'kmeans'
                        elif numerical_model == "DBSCAN":
                            eps = st.slider("epsilon(Ɛ)", min_value=0.01, max_value=10.00, value=0.05)
                            min_samples = st.slider("The mininum number of samples", min_value=1, max_value=100, value=5)
                            params = {"eps": eps, "min_samples": min_samples, "n_jobs" : n_jobs}
                        elif numerical_model == "LOF":
                            params['n_neighbors'] = st.number_input("The number of neighbors", 1, 100, value=20)
                            params['contamination'] = st.number_input("The contamination parameter", 0.0, 0.5, value=0.1)
                            params['n_jobs'] = n_jobs
                        elif numerical_model == "KMeans":
                            n_clusters = st.slider("The number of clusters", min_value=2, max_value=20, value=3)
                            n_init = st.slider("The number of times for the KMeans execution with different certroid seeds", min_value=1, max_value=20, value=10)
                            params = {"n_clusters": n_clusters, "n_init": n_init, "n_jobs" : n_jobs}

                    
                        
                        st.subheader(f"Visualization", divider=True)
                        graph_type = st.selectbox("Select a Graph Type", ["Line Graph", "Scatter Plot", "Bar Graph"])
                        columns = df.columns.tolist()
                        x_column = st.selectbox("Select X-axis Feature", columns)
                        y_column = st.selectbox("Select Y-axis Feature", columns)
                        
                        if st.button("Run your workflow"):
                            st.session_state.model_run = True
                            if st.session_state.model_run:
                                with tabs[1]:
                                    st.title("AnomaliFlow Visualization")
                                    # Celery worker에 비동기 작업 요청
                                    df_dict = df.to_dict(orient='records')
                                    result = run_numerical_workflow(df_dict, numerical_model, params)
                                    
                                    # Visualization step
                                    if result:
                                        st.write("Workflow Completed! Visualizing Results...")
                                        st.write(result)
                                        # Call visualization function
                                        visualization_flow(result, graph_type, x_column, y_column, df, None, None)
