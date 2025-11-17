---
layout: project
title: CarbonAwareLab
project: carbon-aware-lab
repo: datascience-labs/carbon-aware-lab
permalink: /:path/:basename:output_ext
published: false
---

# CarbonAwareLab
CarbonAwareLab은 탄소 인지형 클라우드 워크로드를 설계·실험하기 위한 내부 도구 모음입니다. FastAPI, Apache Airflow, Streamlit을 활용해 실시간 배출량 데이터를 수집하고, 모델 학습·재배포 의사결정을 자동화합니다.

## Features
- 실시간 전력 배출량 API 수집 및 캐싱
- 모델 학습 작업의 배출량 기반 우선순위 조정
- 실험 결과 대시보드 및 알림

## Tech Stack
- Backend: FastAPI, PostgreSQL, Redis
- Workflow: Apache Airflow, Prefect
- Frontend: Streamlit, Tailwind CSS
- Infra: Docker Compose, GitHub Actions

## Run
```bash
docker compose up --build -d
```

## Access
- Streamlit UI: http://localhost:8501
- API Docs: http://localhost:8000/docs
- Dashboard: http://localhost:3000

## Roadmap
- [ ] 지역별 배출량 모델 추가
- [ ] GPU 워크로드 스케줄러 연동
- [ ] Slack/Teams 알림 채널 지원
