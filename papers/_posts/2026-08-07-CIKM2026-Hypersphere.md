---
layout: paper
ptype: intconf
group: knowevo
title: "Table-Guided Hyperspherical Diffusion for Preserving Semantic Dependencies in Column Type Annotation"
authors: Wonseok Son, Jeonghyeon Park, Sejin Chun  
kauthors: ["손원석", "박정현", "천세진"]
year: 2024
image: /images/papers/cikm2026_full.png
ref: ACM CIKM 2026
journal: "ACM International Conference on Information and Knowledge Management (CIKM)"
keywords: Semantic Table Interpretation, Column Type Annotation, Hyperspherical Diffusion
feature: Top-Tier;Accepted;
venue: /images/papers/cikm2026_full.png
# doi: https://ieeexplore.ieee.org/document/10643899
---

<h4><span class="badge badge-info">Abstract</span></h4>
Column Type Annotation (CTA) is a fundamental task in Semantic Table Interpretation that assigns semantic types to table columns. In real-world tables, column meanings are often ambiguous because schemas are heterogeneous and metadata is limited. Therefore, the type of a column depends not only on its own cell values but also on its relationships with other columns. Recent Transformer-based CTA methods capture such contextual information during encoding. However, they rely on discriminative classification, where each column is independently assigned to a predefined type through a softmax classifier. As a result, semantic dependencies among column types are not explicitly preserved during inference. This limits accurate type prediction for context-dependent columns, such as ambiguous numerical columns and long-tail types.

We propose a novel CTA framework that combines diffusion-based iterative denoising with hyperspherical representation learning to generate column type representations. The framework first learns table-guided signals from categorical and numerical columns to capture contextual relationships within a table. It then uses the signals to guide the iterative denoising process, allowing semantic dependencies to be progressively reflected in the generated representations. By modeling the representations in hyperspherical space, the framework preserves semantic dependencies through angular similarity rather than vector scale. Experiments on four benchmark datasets show that our framework outperforms state-of-the-art discriminative and LLM-based baselines.

<h4><span class="badge badge-info">Highlights</span></h4>
<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>The proposed framework</figcaption>
</figure>

<div class="alert alert-primary" role="alert">
    Acceptance Rate: 27%
</div>