---
layout: paper
ptype: domjour
group: knowevo
title: "추론 가속화를 위한 부가 정보 기반 조건부 플로우 매칭 콜드스타트 아이템 추천 모델"
authors: Geonhan Kim, Daro Kim, Sejin Chun, Jungkyu Han
year: 2026
feature: KCI;
ref: Smart Media Journal
journal: "Smart Media Journal"
doi: https://doi.org/10.30693/SMJ.2026.15.6.82
keywords: recommender system, cold-start, inference, flow matching, side information
---
<h4><span class="badge badge-info">Abstract</span></h4>
추천 시스템에서 신규 아이템은 사용자 상호작용 데이터 부재로 인해 협업 필터링 적용이 어려운 콜드스타트 문제를 야기한다. 최근 이를 해결하기 위해 아이템 부가 정보를 활용하는 생성형 모델, 특히 확산 모델이 주목받고 있으나, 반복적인 노이즈 제거 과정으로 인한 느린 추론 속도가 실시간 서비스 적용의 구조적 한계로 지적된다. 이에 본 논문은 확산 모델의 연산 병목을 해소하고 추론 효율성을 개선한 부가 정보 기반 조건부 플로우 매칭 추천 모델을 제안한다. 제안 모델은 아이템 콘텐츠 정보를 조건으로 목표 사용자 상호작용 벡터를 직접 예측하는 궤적을 학습함으로써, 이력 데이터가 없는 신규 아이템에 대해서도 유의미한 추천을 수행한다. 추론 스텝 조절을 통해 확산 모델 대비 약 10배 이상의 추론 속도 향상을 달성하였다. 이는 추천 품질과 연산 효율성 간의 실용적 트레이드오프를 입증한 것으로, 제안 모델이 대규모 실시간 콜드스타트 추천 환경에 보다 적합하고 확장 가능한 방법론임을 확인하였다.
In recommender systems, new items cause the Cold-Start problem due to the lack of user interaction data, making collaborative filtering difficult to apply. While generative models leveraging side information, particularly Diffusion Models, have gained attention as a solution, their iterative denoising process remains a structural bottleneck that limits real-time service deployment. To address this, we propose a side information-based Conditional Flow Matching recommendation model that resolves the computational bottleneck of Diffusion Models and improves inference efficiency. The proposed model learns trajectories that directly predict target user interaction vectors conditioned on item content, enabling meaningful recommendations even for new items without interaction history. By adjusting inference steps, the model achieves at least 10× faster inference compared to the Diffusion Model. This demonstrates a practical trade-off between recommendation quality and computational efficiency, confirming that the proposed model is a more suitable and scalable methodology for large-scale, real-time Cold-Start recommendation environments.
<div class="alert alert-warning" role="alert">
   Accelerating Inference in Cold-Start Item Recommendation Models via Side Information-Based Conditional Flow Matching
</div>
