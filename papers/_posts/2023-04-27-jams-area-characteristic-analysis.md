---
layout: paper
ptype: domconf
group: knowevo
title: "LBSN 데이터와 VAE로 학습한 특징 임베딩을 활용한 지역 특징 분석"
authors: Muyeon Jo, Sejin Chun, Jungkyu Han
year: 2023
ref: 한국스마트미디어학회 종합학술대회 2023.
journal: "한국스마트미디어학회 2023년 종합학술대회"
image: /images/papers/jams-area-characteristic-analysis.png
keywords: Geographical Influence, Point of Interest, Area Characteristics, Location-based Social Network
feature: RESEARCH;
---

<h4><span class="badge badge-info">Abstract</span></h4>
사용자가 방문한 장소(POI: Point-Of-Interest)를 공유하는 사회관계망 서비스인 LBSN(Location Based Social Network)은 사용자의 취향에 맞는 개인화된 장소 추천 및 사용자의 이동패턴 분석의 연구에 사용된다. 본 연구에서는 LBSN 데이터를 활용하여 도시의 각 지역이 사용자에게 제공하는 기능의 관점과 지역에 방문하는 사용자의 이동 패턴의 관점에서 분석하는 방법을 제안한다. 구체적으로는 사용자가 방문하는 POI의 카테고리에 대한 지역별 분포와 사용자의 방문 비율을 VAE (Variational Auto Encoder) 알고리즘을 사용하여 임베딩한 후 이를 비교하여 임베딩이 유사한 지역의 위치에 대해 분석한다. 분석 결과, 사용자의 방문은 비교적 가까운 지역에 집중되어 있는 반면에, 유사한 역할을 가진 지역은 도시 전체에 넓게 분포됨을 보였다.

<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>거리에 따른 시각화 결과</figcaption>
</figure>

<div class="alert alert-primary" role="alert">
    본 논문은 <strong>2023년 한국스마트미디어학회 종합학술대회 우수논문상</strong> 수상하였습니다
</div>

<div class="alert alert-warning" role="alert">
   Area Characteristic Analysis by Using VAE-learned Embedding with LBSN Data
</div>