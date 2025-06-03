---
layout: paper
ptype: domconf
group: knowevo
title: "ReAct 기반 추론-행동 연계를 활용한 온톨로지 지향 질문 생성 기법 "
authors: Yewon Lee, Wonseok Son, Jeongsu Kim, Jungkyu Han, Sejin Chun
kauthors: ["이예원", "손원석", "김정수", "한정규", "천세진"]
keywords: Large Language Model, Competency Question Generation, ReAct, Re-ranking, NeOn Methodology, Ontology Automation
year: 2025
ref: 한국정보과학회 한국컴퓨터종합학술대회 2025
journal: "2025 한국컴퓨터종합학술대회"
venue: /images/papers/KCC2025.png
image: /images/papers/KCC2025.png
---

<h4><span class="badge badge-info">Abstract</span></h4>
최근 대규모 언어모델(Large Language Model, LLM)의 발전은 지식 획득 및 온톨로지 구축의 자동화를 가속화하고 있다. 그러나 기존의 연구는 온톨로지 개발 과정의 일부만 자동화하며, 역량질문(Competency Questions, CQs)의 생성은 논리적 정합성과 도메인 특화성이 부족한 경우가 많다. 본 연구는 이러한 한계를 극복하기 위해 ReAct 기반 추론 및 재순위화 기법을 활용한 온톨로지 지향 CQ 생성 프레임워크를 제안한다. 제안 프레임워크는 NeOn 방법론을 기반으로, 페르소나 기반 프롬프트를 통해 도메인 설명과 사용자 역할을 반영한 개념 및 관계를 자동으로 생성하고, 이를 기반으로 CQ를 생성하며 RDF 형식으로 변환 후 검증까지 자동화한다. 제안된 프레임워크는 공개적으로 구현되었으며 해당 소스코드는 공개적으로 활용 및 접근가능하다.

<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>제안 프레임워크</figcaption>
</figure>

<div class="alert alert-warning" role="alert">
    Ontology-Driven Competency Question Generationusing ReAct-Based Reasoning and Action Framework
</div>