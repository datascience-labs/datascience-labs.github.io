---
layout: paper
ptype: domconf
group: knowevo
title: "MCP 기반 LLM Agent를 활용한 해양 레저 추천 프레임워크"
authors: Beopgi Kim, Jeonghyeon Park, Sejin Chun
kauthors: ["김법기", "박정현", "천세진"]
year: 2026
ref: 2026년 한국ITS학회 춘계학술대회
conference: "2026년 한국ITS학회 춘계학술대회"
keywords: MCP, LLM Agent, Marine Leisure, Recommendation System, External API
---

<h4><span class="badge badge-info">Abstract</span></h4>

해양 레저 서비스는 다수의 플랫폼에 분산되어 제공되며, 사용자의 요구는 지역, 시간, 활동 유형, 예산, 인원, 접근성 등 다양한 조건을 동시에 포함한다. 그러나 기존 키워드 기반 검색 방식은 단어 단위의 매칭에 의존하기 때문에 조건 간 우선순위나 문맥적 의미를 충분히 반영하기 어렵고, 분산된 외부 플랫폼의 최신 정보를 통합하는 데에도 한계가 있다.

본 연구에서는 이러한 문제를 해결하기 위해 MCP(Model Context Protocol) 기반 LLM Agent를 활용한 해양 레저 추천 프레임워크를 제안한다. 제안하는 프레임워크는 사용자의 자연어 질의를 정형화된 구조로 변환하고, 외부 API를 통해 해양 레저 서비스 및 환경 정보를 수집한 뒤, 사용자 조건에 따라 후보군을 구성한다. 이후 LLM Agent는 제한된 후보군 내에서 의미적 적합도를 기준으로 최종 추천 항목을 선정한다.

이를 통해 본 연구는 자연어 입력의 비정형성을 처리하고, 외부 데이터 소스를 표준화된 방식으로 통합하며, LLM의 추천 범위를 후보군으로 제한함으로써 hallucination을 억제하는 구조를 제시하였다. 제안된 프레임워크는 기존 키워드 기반 검색의 문맥 처리 한계와 LLM 기반 추천의 데이터 연계 부족 문제를 동시에 보완하며, 향후 다양한 자연어 기반 추천 시스템으로 확장될 수 있다.
