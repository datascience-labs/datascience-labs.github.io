---
layout: paper
ptype: intconf
group: knowevo
title: "Content-guided Diffusion for Cold-start Item Recommendation"
authors: Daero Kim, Sejin Chun, Jungkyu Han
kauthors: ["김대로", "천세진", "한정규"]
keywords: Cold-start Item, Diffusion, Recommendation System, Mixture of Experts, Cross-attention 
year: 2025
ref: NOLTA 2025
journal: "NOLTA 2025"
feature: Accepted;
---

<h4><span class="badge badge-info">Abstract</span></h4>
Collaborative Filtering (CF) is effective for personalized recommendation but faces critical challenges with cold-start items lacking interaction data. Existing content-based and distillation approaches struggle to capture complex semantic-to-collaborative mappings and produce suboptimal embeddings due to deterministic constraints.
To address this, we propose CGDRec (Content-Guided Diffusion model for Recommendation), which generates high-quality CF embeddings through conditional diffusion. Our hybrid backbone combines Mixture-of-Experts for adaptive content modeling and Cross-attention for aggregating collaborative signals from similar warm items.
Experiments on three dataset   ̶CiteULike, XING, and ML25M show CGDRec consistently outperforms baselines, significantly improving cold-start recommendation quality. This is the first application of conditional diffusion to cold-start item recommendation.
