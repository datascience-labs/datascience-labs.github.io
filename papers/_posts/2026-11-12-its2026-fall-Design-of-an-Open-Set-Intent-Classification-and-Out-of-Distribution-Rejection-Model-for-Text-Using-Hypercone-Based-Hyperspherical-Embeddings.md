---
layout: paper
ptype: domconf
group: knowevo
title: "Hypercone 기반 구면 임베딩을 활용한 텍스트 오픈셋 의도 분류 및 이상치 거부 모델 설계"
authors: Seongtaek Lim, Wonseok Son, Sejin Chun
kauthors: ["임성택","손원석","천세진"]
year: 2026
ref: 2026 한국ITS학회 추계학술대회
journal: "2026 한국ITS학회 추계학술대회"
keywords: 미지 의도 탐지, 자연어처리, 의도 분류, 분포 외 탐지
---

<h4><span class="badge badge-info">Abstract</span></h4>
챗봇 같은 대화 시스템에서는 학습하지 않은 미지 의도를 거부하는 것이 중요하다. 그러나 소프트맥스 기반 분류기는 미지 의도의 발화도 기존 의도 중 하나로 분류한다. 기존 분포 외 탐지 기법은 데이터셋마다 임계값을 보정해야 하고, 다양한 미지 의도를 검증 단계에서 충분히 확보하기도 어렵다. 본 연구는 알려진 의도의 문장만으로 분류 영역과 거부 영역을 구성하는 hypercone 기반 오픈셋 의도 분류 모델을 제안한다. 문장 임베딩을 단위 구면 위의 벡터로 변환하고, 각 의도를 대표 방향(중심축)과 허용 각도를 갖는 hypercone, 즉 Class Prototype으로 나타낸다. 모델은 코사인 소프트맥스 손실로 학습하고, 학습 문장과 중심축 사이 각도의 95% 분위수로 경계를 정한다. 추론 시에는 입력이 어느 Class Prototype에도 속하지 않으면 미지 의도로 거부한다. 따라서 데이터셋별 임계값 조정이 필요 없고, 수용·거부의 근거를 각도로 설명할 수 있다. 또한 경계 바로 바깥 영역에 truncated von Mises–Fisher 분포로 가상 이상치를 생성하고 경계와 네트워크를 함께 학습하는 확장 방법을 제안하여, 실제 미지 의도 문장 없이 경계 부근의 거부 성능을 보완한다. CLINC150과 BANKING77에서 학습 의도 비율을 달리한 오픈셋 설정으로 제안 방법을 평가하였다.
<div class="alert alert-warning" role="alert">
   Design of an Open-Set Intent Classification and Out-of-Distribution Rejection Model for Text Using Hypercone-Based Hyperspherical Embeddings
</div>