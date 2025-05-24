---
layout: paper
ptype: domconf
group: knowevo
title: "모듈화된 이상 탐지 워크플로우의 조합을 위한 도구"
authors: ["김원아", "유가은", "이도현", "이예원", "박채영", "최지호", "박정현", "천세진"]
kauthors: ["김원아", "유가은", "이도현", "이예원", "박채영", "최지호", "박정현", "천세진"]
year: 2025
ref: The Korean Society of Intelligent Transport Systems
journal: "The Korean Society of Intelligent Transport Systems"
keywords: Outlier Detection, Anomaly Detection, Workflow Orchestration, Toolkits
categories: papers
---

<h4><span class="badge badge-info">Main Contribution</span></h4>
본 논문에서는 다양한 데이터 특성에서 이상 탐지를 모듈화된 워크플로우(Modularized Workflow)으로 구성하는 AnomaliFlow 프레임워크을 제안하며, 다음과 같은 주요 기여를 제공한다.  

1. 제안 프레임워크는 자동 데이터 유형 인식, 적절한 전처리와 탐지 모듈 선택을 통해 시계열, 수치형, 범주형 데이터에서 워크플로우를 재사용할 수 있는 모듈형 파이프라인을 제공한다.
2. 탐지된 이상 결과를 사용자 친화적인 시각화로 제공하여 사용자가 직관적으로 이해할 수 있도록 지원한다.
3. 각 이상에 대해 개별 피처의 기여도를 정량화하는 이상 원인 분석 점수(Root Cause Score: RCA) 점수를 도입하여 이상 원인에 대한 명확한 해석을 제공한다.
4. 마지막으로, 동적 워크플로우 관리 및 병렬 처리를 통해 대규모 데이터 처리와 다중 탐지 작업을 동시에 처리할 수 있도록 지원하며, Isolation Forest, DBSCAN, Gaussian Mixture Model의 인기 알고리즘을 통합한다.
   
<div class="alert alert-warning" role="alert">
   해당 논문은 2025년 한국ITS학회 춘계학술대회에서 우수논문상을 수상했습니다.
</div>
