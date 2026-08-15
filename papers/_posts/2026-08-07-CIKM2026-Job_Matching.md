---
layout: paper
ptype: intconf
group: knowevo
title: "Taxonomy-Guided Contrastive Learning with Competency-Calibrated Graphs for Job Recommendation"
authors: Wonseok Son, Haeyoon Koo, Jeonghyeon Park, Byungkook Oh, Sejin Chun  
kauthors: ["손원석", "구해윤", "박정현", "오병국", "천세진"]
year: 2026
image: /images/papers/cikm2026_job.png
ref: ACM CIKM 2026
journal: "ACM International Conference on Information and Knowledge Management (CIKM)"
keywords: Job Matching, Graph Contrastive Learning, Hierarchical Taxonomy
feature: Top-Tier;Accepted;
venue: /images/papers/cikm2026_job.png
# doi: https://ieeexplore.ieee.org/document/10643899
---

<h4><span class="badge badge-info">Abstract</span></h4>
The goal of job-skill matching is to predict appropriate job opportunities for job seekers based on their skill-sets. Prior studies encode unstructured skill data into latent representations using simple mappings within job classification systems. However, such approaches often fall short in capturing the multi-level and asymmetric associations between jobs and job-relevant competencies. To address these limitations, we propose a taxonomy-guided contrastive learning framework with competency-calibrated graph propagation for skill-based job recommendation. The proposed framework combines skill-taxonomy augmentation with degree-normalized bipartite graph propagation, where degree normalization serves as a competency calibration mechanism to mitigate generic skill bias and preserve job-specific competency signals. The model learns both skill and job representations using path/depth cues from the taxonomy and competency-aware interaction patterns in the job-skill graph. Experimental results on real-world datasets show that our method improves accuracy by +13.6%, NDCG@3 by +10.6%, and MRR@3 by +11.7%, outperforming state-of-the-art baselines.

<h4><span class="badge badge-info">Highlights</span></h4>
<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>The proposed framework</figcaption>
</figure>

<div class="alert alert-primary" role="alert">
    Acceptance Rate: 30.9% (234/764 papers accepted)
</div>