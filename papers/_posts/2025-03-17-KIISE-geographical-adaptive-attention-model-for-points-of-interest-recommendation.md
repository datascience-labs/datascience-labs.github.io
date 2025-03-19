---
layout: paper
ptype: domjour
group: knowevo
title: "POI 추천을 위한 지리 적응형 어텐션 모델"
authors: Moyeon Jo, Sejin Chun, Jungkyu Han  
year: 2025
feature: KCI;
ref: 정보과학회논문지, 2025, vol.52, pp.217-226 
journal: "Journal of Korean Institute of Information Scientists and Engineers"
keywords: location based social network, POI recommender system, geographical influence, attention network
---

<h4><span class="badge badge-info">Abstract</span></h4>
POI 추천에 있어서 POI의 위치로 인한 지리적 영향력은 중요한 요소로 작용한다. 그에 따라 POI 추천에 관한 연구들은 거리나 위치 등과 같은 지리적 정보를 활용하여 POI 고유의 지리적 영향력을 정의하고 이를 추출하여 개인화된 추천에 반영하기 위한 연구가 주를 이룬다. 지리적 영향력을 나타내기 위한 연구는 크게 사용자와 POI사이 거리를 기반으로 선호도를 나타내는 거리 기반 영향력과 지역에 위치한 POI들의 특징을 기반으로 지역에 대한 선호도를 나타내는 지역 기반 영향력으로 나누어진다. 이전 연구들에서는 거리 기반 영향력에 초점을 맞추고 있기 때문에 지역에 대한 영향력를 활용하지 못한다. 이에 본 논문에서는 POI들의 거리 기반 영향력뿐만 아니라 POI가 위치한 지역 기반 영향력을 고려하여, 사용자가 방문한 POI들 각각이 사용자의 특징에 미치는 영향력을 적응적으로 포착할 수 있는 어텐션(Attention) 네트워크 기반 POI 추천 모델을 제안한다. 이 모델은 사용자 방문 데이터에서 특정 지역의 특성과 사용자의 POI 선호도를 학습하여, 개인화된 추천을 더욱 정확하게 제공한다. 실제 데이터셋 실험 결과, 제안된 방법이 기존 모델에 비해 Prec@10, Recall@10, HR@10 지표에서 각각 약 6∼12%, 8∼10%, 6∼7%의 성능 향상을 이루었다.

Geographical influence, stemming from the location of Points of Interest (POIs), plays a vital role in POI recommendation. Most current studies utilize geographical information such as distance and location to define and extract POI-specific geographical influences for personalized recommendations. These approaches primarily emphasize distance-based influence, which gauges user preferences based on proximity, while often overlooking area-based influence, which reflects preferences for regions with specific POI characteristics. This paper introduces a POI recommendation model based on an attention network that integrates both distance- and area-based influences. The model adaptively assesses how previously visited POIs impact the likelihood of visiting a target POI, taking into account regional characteristics and user preferences. Experiments conducted on real-world datasets indicate that the proposed method significantly outperforms baseline models, achieving improvements of approximately 6–12% in Prec@10, 8–10% in Recall@10, and 6–7% in HR@10.

<div class="alert alert-warning" role="alert">
   Geographical Adaptive Attention Model for Points of Interest Recommendation
</div>
