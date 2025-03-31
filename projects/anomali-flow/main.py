from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import Dict, Union, List, Optional
from celery.result import AsyncResult
from worker import run_timeseries_workflow, run_categorical_workflow
from pymongo import MongoClient
import celeryconfig

app = FastAPI()

client = MongoClient('mongo', 27017)
db = client.celery_results
collection = db.results

# TaskRequest 모델 정의
class TaskRequest(BaseModel):
    df: Dict  # df를 딕셔너리 형태로 받음
    algorithm: str
    params: dict

# Celery 태스크를 실행하고 백그라운드에서 상태를 확인
@app.post("/tasks", response_model=dict)
def run_task(request: TaskRequest, background_tasks: BackgroundTasks):
    # Time series 또는 categorical 알고리즘에 따라 Celery 태스크를 실행
    if request.algorithm in ["DBSCAN", "KMeans"]:
        task = run_timeseries_workflow.delay(request.df, request.algorithm, request.params)
    else:
        task = run_categorical_workflow.delay(request.df, request.algorithm, request.params)
    
    # 백그라운드에서 작업 상태를 확인하도록 설정
    background_tasks.add_task(check_task_status, task.id)
    return {"task_id": task.id}

# Celery 작업의 상태를 확인하는 함수
def check_task_status(task_id: str):
    result = AsyncResult(task_id)
    if result.state == 'SUCCESS':
        # 작업이 성공적으로 완료되면 결과를 MongoDB에 저장
        collection.insert_one({"task_id": task_id, "result": result.result})
        return result.result
    return {"status": result.state}

# 작업 결과를 가져오는 엔드포인트
@app.get("/tasks/{task_id}", response_model=dict)
def get_task_result(task_id: str):
    result = AsyncResult(task_id)
    if result.state == 'SUCCESS':
        # 작업이 성공적으로 완료된 경우 결과 반환
        return {"status": result.state, "result": result.result}
    elif result.state == 'FAILURE':
        # 작업 실패 시 오류 메시지 반환
        return {"status": result.state, "result": str(result.result)}
    return {"status": result.state}

    
