---
layout: paper
ptype: domjour
group: knowevo
title: 추론 가속화를 위한 부가 정보 기반 조건부 플로우 매칭 콜드스타트 아이템 추천 모델
authors: Geonhan Kim, Daro Kim, Sejin Chun, Jungkyu Han
year: 2026
ref: Smart Media Journal
doi: https://doi.org/10.30693/SMJ.2026.15.6.82
journal: Smart Media Journal
feature: KCI;
keywords: Recommender System, Cold-Start, Inference, Flow Matching, Side Information
---

<h4><span class="badge badge-info">Abstract</span></h4>
In recommender systems, new items cause the Cold-Start problem due to the lack of user interaction data, making collaborative filtering difficult to apply. While generative models leveraging side information, particularly Diffusion Models, have gained attention as a solution, their iterative denoising process remains a structural bottleneck that limits real-time service deployment. To address this, we propose a side information-based Conditional Flow Matching recommendation model that resolves the computational bottleneck of Diffusion Models and improves inference efficiency. The proposed model learns trajectories that directly predict target user interaction vectors conditioned on item content, enabling meaningful recommendations even for new items without interaction history. By adjusting inference steps, the model achieves at least 10× faster inference compared to the Diffusion Model. This demonstrates a practical trade-off between recommendation quality and computational efficiency, confirming that the proposed model is a more suitable and scalable methodology for large-scale, real-time Cold-Start recommendation environments.

<h4><span class="badge badge-info">Highlights</span></h4>

<div class="alert alert-warning" role="alert">
   Accelerating Inference in Cold-Start Item Recommendation Models via Side Information-Based Conditional Flow Matching
</div>

<h4><span class="badge badge-info">Smart Media Journal Vol. 15, No. 6, June 2026 (pp. 82-90)</span></h4>