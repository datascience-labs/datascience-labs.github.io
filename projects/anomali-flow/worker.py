from celery import Celery
from pymongo import MongoClient
import streamlit as st
import celeryconfig
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.cluster import DBSCAN, KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import MinMaxScaler
from collections import defaultdict

app = Celery('worker')
app.config_from_object(celeryconfig)

client = MongoClient('mongo', 27017)
db = client.celery_results
collection = db.results

# Celery 앱 설정
app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def run_timeseries_workflow(df, algorithm, params):
    df = pd.DataFrame(df)

    df.set_index(df.columns[0], inplace=True)
    index = df.index.tolist()
    index = [str(i) for i in index] 
    df = df.iloc[:, 0:] 
    X = df
    
    result = {}
    root_cause_scores = {}

    # Prefect 타임시리즈 워크플로우 호출
    if algorithm == 'IsolationForest':
        model = IsolationForest(max_samples=params["max_samples"], n_jobs=params["n_jobs"], contamination=params["contamination"])
        model.fit(X)
        y_pred = model.predict(X)
        outlier_indices = np.where(y_pred == -1)[0].tolist()
        outlier_scores = -model.decision_function(X)
        scaler = MinMaxScaler()
        outlier_probabilities = scaler.fit_transform(outlier_scores.reshape(-1, 1)).flatten().tolist()
    elif algorithm == 'GMM':
        model = GaussianMixture(n_init=params["n_init"], n_components=params["n_components"], random_state=params["random_state"], init_params=params["init_params"])
        model.fit(X)
        probs = model.predict_proba(X)
        prob_threshold = np.percentile(probs.max(axis=1), 5)
        outlier_indices = np.where(probs.max(axis=1) < prob_threshold)[0].tolist()
        outlier_probabilities = (1 - probs.max(axis=1)[probs.max(axis=1) < prob_threshold]).tolist()
    
    
    # 모든 인덱스에 대해 root cause score 계산
    for timestamp in X.index:
        # 각 timestamp에서 feature-wise 편차 계산
        score = np.abs(X.loc[timestamp].values - X.mean(axis=0).values)
    
        # score와 X.columns의 길이를 맞춤
        if len(score) != len(X.columns):
            # X.columns 크기에 맞게 score를 조정 (resize 사용)
            score = np.resize(score, len(X.columns))
        # 정규화 과정
        score = (score - np.min(score)) / (np.max(score) - np.min(score) + 1e-9)  # 정규화
    
        # 다시 한 번 확인해서 score가 1차원인지 확인
        if score.ndim > 1:
            score = score.flatten()  # 1차원으로 평탄화
    
        # score를 시리즈로 변환하여 root_cause_scores에 저장
        score_series = pd.Series(score, index=X.columns)
        root_cause_scores[str(timestamp)] = score_series.to_dict()  # 저장


    # MongoDB에 저장할 직렬화 가능한 결과만 저장
    result['outlier_indices'] = outlier_indices
    result['outlier_probabilities'] = outlier_probabilities
    result['root_cause_scores'] = root_cause_scores
    result['index'] = index
    
    insert_result = {
        "status": "success",
        "algorithm": algorithm,
        "params": params
    }
    
    # MongoDB에 결과 저장
    result_id = collection.insert_one(insert_result).inserted_id
    result['_id'] = str(result_id)

    return result

@app.task
def run_categorical_workflow(df, algorithm, params):
    df = pd.DataFrame(df)
    # NaN 값을 중앙값으로 대체 (또는 dropna로 제거)
    imputer = SimpleImputer(strategy='median')
    df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    
    # 0번째 열을 문자열 그대로 인덱스로 설정
    df.set_index(df.columns[0], inplace=True)
    index = df.index.tolist()
    index = [str(i) for i in index] 
    df = df.iloc[:, 0:] 
    X = df
    
    result = {}
    root_cause_scores = {}
    
    # Prefect 카테고리 워크플로우 호출
    if algorithm == 'LOF':
        model = LocalOutlierFactor(n_neighbors=params["n_neighbors"], n_jobs=params["n_jobs"], contamination=params["contamination"])
        y_pred = model.fit_predict(X)
        outlier_indices = np.where(y_pred == -1)[0].tolist()
        outlier_scores = -model.negative_outlier_factor_
        scaler = MinMaxScaler()
        outlier_probabilities = scaler.fit_transform(outlier_scores.reshape(-1, 1)).flatten().tolist()
    
    elif algorithm == 'DBSCAN':
        model = DBSCAN(eps=params["eps"], min_samples=params["min_samples"], n_jobs=params["n_jobs"])
        y_pred = model.fit_predict(X)
        outlier_indices = np.where(y_pred == -1)[0].tolist()
        
        # Check if there are any core samples and outliers
        core_sample_indices = model.core_sample_indices_
        if len(core_sample_indices) == 0 or len(outlier_indices) == 0:
            # If there are no core samples or no outliers, avoid calculating distances
            outlier_scores = [0] * len(outlier_indices)  # Assign a default score of 0 for all outliers
            outlier_probabilities = [0] * len(outlier_indices)  # Assign a default probability of 0
        else:
            core_samples = X.iloc[core_sample_indices]
            outlier_samples = X.iloc[outlier_indices]

        
            distances = pairwise_distances(outlier_samples, core_samples, metric='euclidean')
            outlier_scores = np.min(distances, axis=1)
        
            scaler = MinMaxScaler()
            outlier_probabilities = scaler.fit_transform(outlier_scores.reshape(-1, 1)).flatten().tolist()
    

    # 모든 인덱스에 대해 root cause score 계산
    for timestamp in X.index:
        # 각 timestamp에서 feature-wise 편차 계산
        score = np.abs(X.loc[timestamp].values - X.mean(axis=0).values)
    
        # score와 X.columns의 길이를 맞춤
        if len(score) != len(X.columns):
            # X.columns 크기에 맞게 score를 조정 (resize 사용)
            score = np.resize(score, len(X.columns))
        # 정규화 과정
        score = (score - np.min(score)) / (np.max(score) - np.min(score) + 1e-9)  # 정규화
    
        # 다시 한 번 확인해서 score가 1차원인지 확인
        if score.ndim > 1:
            score = score.flatten()  # 1차원으로 평탄화
    
        # score를 시리즈로 변환하여 root_cause_scores에 저장
        score_series = pd.Series(score, index=X.columns)
        root_cause_scores[str(timestamp)] = score_series.to_dict()  # 저장

        
    # MongoDB에 저장할 직렬화 가능한 결과만 저장
    result['outlier_indices'] = outlier_indices
    result['outlier_probabilities'] = outlier_probabilities
    result['root_cause_scores'] = root_cause_scores
    result['index'] = index

    
    insert_result = {
        "status": "success",
        "algorithm": algorithm,
        "params": params
    }
    
    # MongoDB에 결과 저장
    result_id = collection.insert_one(insert_result).inserted_id
    result['_id'] = str(result_id)

    return result

@app.task
def run_numerical_workflow(df, algorithm, params):
    df = pd.DataFrame(df)
    # NaN 값을 중앙값으로 대체 (또는 dropna로 제거)
    imputer = SimpleImputer(strategy='median')
    df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    # 0번째 열을 문자열 그대로 인덱스로 설정
    df.set_index(df.columns[0], inplace=True)

    index = df.index.tolist()
    index = [str(i) for i in index] 
    df = df.iloc[:, 0:] 
    X = df

    result = {}
    root_cause_scores = {}
    
    # Prefect 카테고리 워크플로우 호출
    if algorithm == 'IsolationForest':
        model = IsolationForest(max_samples=params["max_samples"], n_jobs=params["n_jobs"], contamination=params["contamination"])
        model.fit(X)
        y_pred = model.predict(X)
        outlier_indices = np.where(y_pred == -1)[0].tolist()
        outlier_scores = -model.decision_function(X)
        scaler = MinMaxScaler()
        outlier_probabilities = scaler.fit_transform(outlier_scores.reshape(-1, 1)).flatten().tolist()
    elif algorithm == 'GMM':
        model = GaussianMixture(n_init=params["n_init"], n_components=params["n_components"], random_state=params["random_state"], init_params=params["init_params"])
        model.fit(X)
        probs = model.predict_proba(X)
        prob_threshold = np.percentile(probs.max(axis=1), 5)
        outlier_indices = np.where(probs.max(axis=1) < prob_threshold)[0].tolist()
        outlier_probabilities = (1 - probs.max(axis=1)[probs.max(axis=1) < prob_threshold]).tolist()
    elif algorithm == 'DBSCAN':
        model = DBSCAN(eps=params["eps"], min_samples=params["min_samples"], n_jobs=params["n_jobs"])
        y_pred = model.fit_predict(X)
        outlier_indices = np.where(y_pred == -1)[0].tolist()
        
        # Check if there are any core samples and outliers
        core_sample_indices = model.core_sample_indices_
        if len(core_sample_indices) == 0 or len(outlier_indices) == 0:
            # If there are no core samples or no outliers, avoid calculating distances
            outlier_scores = [0] * len(outlier_indices)  # Assign a default score of 0 for all outliers
            outlier_probabilities = [0] * len(outlier_indices)  # Assign a default probability of 0
        else:
            core_samples = X.iloc[core_sample_indices]
            outlier_samples = X.iloc[outlier_indices]

        
            distances = pairwise_distances(outlier_samples, core_samples, metric='euclidean')
            outlier_scores = np.min(distances, axis=1)
        
            scaler = MinMaxScaler()
            outlier_probabilities = scaler.fit_transform(outlier_scores.reshape(-1, 1)).flatten().tolist()
    elif algorithm == 'LOF':
        model = LocalOutlierFactor(n_neighbors=params["n_neighbors"], n_jobs=params["n_jobs"], contamination=params["contamination"])
        y_pred = model.fit_predict(X)
        outlier_indices = np.where(y_pred == -1)[0].tolist()
        outlier_scores = -model.negative_outlier_factor_
        scaler = MinMaxScaler()
        outlier_probabilities = scaler.fit_transform(outlier_scores.reshape(-1, 1)).flatten().tolist()
    elif algorithm == 'KMeans':
        model = KMeans(n_init=params["n_init"], n_clusters=params["n_clusters"])
        model.fit(X)
        y_pred = model.predict(X)
        
        distances = np.min(model.transform(X), axis=1)
        threshold = np.percentile(distances, 95)
        outlier_indices = np.where(distances > threshold)[0].tolist()
        outlier_scores = distances[distances > threshold]
        
        scaler = MinMaxScaler()
        outlier_probabilities = scaler.fit_transform(outlier_scores.reshape(-1, 1)).flatten().tolist()

        
    for timestamp in X.index:
        # 각 timestamp에서 feature-wise 편차 계산
        score = np.abs(X.loc[timestamp].values - X.mean(axis=0).values)
    
        # score와 X.columns의 길이를 맞춤
        if len(score) != len(X.columns):
            # X.columns 크기에 맞게 score를 조정 (resize 사용)
            score = np.resize(score, len(X.columns))
        # 정규화 과정
        score = (score - np.min(score)) / (np.max(score) - np.min(score) + 1e-9)  # 정규화
    
        # 다시 한 번 확인해서 score가 1차원인지 확인
        if score.ndim > 1:
            score = score.flatten()  # 1차원으로 평탄화
    
        # score를 시리즈로 변환하여 root_cause_scores에 저장
        score_series = pd.Series(score, index=X.columns)
        root_cause_scores[str(timestamp)] = score_series.to_dict()  # 저장
        
    # MongoDB에 저장할 직렬화 가능한 결과만 저장
    result['outlier_indices'] = outlier_indices
    result['outlier_probabilities'] = outlier_probabilities
    result['root_cause_scores'] = root_cause_scores
    result['index'] = index

    
    insert_result = {
        "status": "success",
        "algorithm": algorithm,
        "params": params
    }
    
    # MongoDB에 결과 저장
    result_id = collection.insert_one(insert_result).inserted_id
    result['_id'] = str(result_id)

    return result
