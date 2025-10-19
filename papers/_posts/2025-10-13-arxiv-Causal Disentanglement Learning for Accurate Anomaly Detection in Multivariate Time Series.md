---
layout: paper
ptype: intconf
group: knowevo
title: "Causal Disentanglement Learning for Accurate Anomaly Detection in Multivariate Time Series"
authors: Wonah Kim, Jeonghyeon Park, Dongsan Jun, Jungkyu Han,  Sejin Chun
kauthors: ["김원아", "박정현", "전동산", "한정규", "천세진"]
keywords: Anomaly Detection, Multivariate Time Series, Causal Disentanglement, Graph Neural Network
year: 2025
ref: arXiv
journal: "arXiv"
venue: /images/papers/CDRL4AD_overview.png
image: /images/papers/CDRL4AD_overview.png
doi: https://arxiv.org/abs/2510.11084
---

<h4><span class="badge badge-info">Abstract</span></h4>
Disentangling complex causal relationships is important for accurate detection of anomalies. In multivariate time series analysis, dynamic interactions among data variables over time complicate the interpretation of causal relationships. Traditional approaches assume statistical independence between variables in unsupervised settings, whereas recent methods capture feature correlations through graph representation learning. However, their representations fail to explicitly infer the causal relationships over different time periods. To solve the problem, we propose Causally Disentangled Representation Learning for Anomaly Detection (CDRL4AD) to detect anomalies and identify their causal relationships in multivariate time series. First, we design the causal process as model input, the temporal heterogeneous graph, and causal relationships. Second, our representation identifies causal relationships over different time periods and disentangles latent variables to infer the corresponding causal factors. Third, our experiments on real-world datasets demonstrate that CDRL4AD outperforms state-of-the-art methods in terms of accuracy and root cause analysis. Fourth, our model analysis validates hyperparameter sensitivity and the time complexity of CDRL4AD. Last, we conduct a case study to show how our approach assists human experts in diagnosing the root causes of anomalies.

<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>The overview of our porposed framework</figcaption>
</figure>
