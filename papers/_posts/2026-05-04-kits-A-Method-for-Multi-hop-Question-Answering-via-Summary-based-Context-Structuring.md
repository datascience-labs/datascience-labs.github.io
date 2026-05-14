---
layout: paper
ptype: conf
group: knowevo
title: "A Method for Multi-hop Question Answering via Summary-based Context Structuring"
authors: Taei Yoon, Taehee Kim, Sejin Chun
kauthors: ["윤태이", "김태희", "천세진"]
year: 2026
ref: 2026년 한국ITS학회 춘계학술대회
conference: "2026년 한국ITS학회 춘계학술대회"
keywords: Retrieval-Augmented Generation, Multi-hop Question Answering, Large Language Model, Summary-based Context Structuring, GraphRAG
---
<h4><span class="badge badge-info">Abstract</span></h4>
대규모 언어모델(LLM) 기반의 RAG는 텍스트 유사도 중심의 검색 방식을 사용하기 때문에, 여러 문서에 흩어진 정보를 연결해야 하는 Multi-hop 질의에서 관계 정보를 충분히 활용하지 못하는 한계가 있다. 기존 GraphRAG는 이를 보완하지만, 그래프 재구성 비용과 관계 누락에 따른 오류 전파 문제가 존재한다. 본 논문에서는 이를 해결하기 위해 요약 기반 문맥 구조화를 통한 RAG 방법론을 제안한다. 제안 방법은 문서별 공통 엔티티와 조건-결과 관계를 요약으로 사전에 추출하고, 검색된 청크와 해당 요약을 인접하게 배치하는 인터리브 구조를 적용한다. 이를 통해 모델이 명시적인 연결 단서를 바탕으로 복합적인 추론을 수행하도록 유도하며, 향후 요약의 품질이 전체 응답 성능에 미치는 영향을 실험적으로 검증할 계획이다.
