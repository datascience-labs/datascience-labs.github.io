---
layout: paper
ptype: intjour
group: knowevo
title: "Graph attention-based dynamical and causal spatiotemporal learning for anomaly detection in additive manufacturing"
authors: Suk Ki Lee, Wonah Kim, Sungbeom Lee, Jeonghyeon Park, Sejin Chun, Ho Yeung & Hyunwoong Ko
kauthors: ["이석기", "김원아", "이성범", "박정현", "천세진", "Ho Yeung", "고현웅"]
year: 2025
venue: /images/papers/nvpp.png
image: /images/papers/nvpp.png
ref: Virtual and Physical Prototyping
journal: "Virtual and Physical Prototyping"
feature: SCIE; Q1;
doi: https://doi.org/10.1080/17452759.2025.2611194
keywords: Additive manufacturing, anomaly detection, graph attention networks, spatiotemporal learning, causal relationship learning, model interpretability
---

<h4><span class="badge badge-info">Abstract</span></h4>
In additive manufacturing (AM) processes, in-situ monitoring combined with machine learning (ML) approaches plays a crucial role in ensuring consistent product quality and preventing defects. However, existing ML methods for anomaly detection predominantly rely on correlation-based models that lack interpretability and fail to capture underlying spatiotemporal and causal dynamics. This study proposes an anomaly detection framework that integrates spatiotemporal dependency learning (STL) and Granger causality learning (GCL) through graph attention network mechanisms. The STL module enforces spatial consistency and temporal smoothness in learned feature representations, while the GCL module identifies causal relationships between historical process signatures and both historical and current parameters, and current states through attention-based causal aggregation and disentanglement techniques. By combining these complementary modules, our method achieves superior anomaly detection performance while providing interpretable insights through spatial-temporal dependency interpretation, causal disentanglement analysis, and causal attribution analysis. Experimental validation demonstrates improved detection accuracy compared to existing baselines, with attention-based mechanisms enabling the identification of specific process parameters and spatial regions contributing to anomalous behaviour. This framework facilitates proactive quality control in AM processes by bridging the gap between high-accuracy anomaly detection and practical interpretability requirements in manufacturing applications.

<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>An Overall Framework for Graph Attention-Based Anomaly Detection in AM Process Monitoring via Spatial-Temporal and Granger Causal Learning. Starting from the AM process phenomena (schematic adapted from [Citation9]), the proposed framework processes in-situ monitoring data, constructs graphs, and applies graph attention-based modelling with spatial-temporal dependency learning and Granger causal learning to detect anomalies in AM. Beyond anomaly detection, the framework provides interpretable insights through multiple analysis approaches: spatial-temporal dependencies interpretation via feature clustering analysis, causal disentanglement analysis via disentangled causal factor clustering analysis, and causal attribution analysis via causal pathway analysis and temporal attention distribution analysis. These capabilities enable a deeper understanding of dynamics in AM processes.</figcaption>
</figure>



<div class="alert alert-primary" role="alert">
    본 논문은 미국 NIST 및 Arizona State University와의 국제 공동연구를 통해 수행된 연구임.
</div>