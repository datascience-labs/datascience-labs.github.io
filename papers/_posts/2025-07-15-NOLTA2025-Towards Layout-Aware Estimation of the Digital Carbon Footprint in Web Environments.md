---
layout: paper
ptype: intconf
group: knowevo
title: "Towards Layout-Aware Estimation of the Digital Carbon Footprint in Web Environments"
authors: Ayoung Kim, Jeonghyeon Park, Jungkyu Han, Sejin Chun
kauthors: [ "김아영", "박정현", "한정규", "천세진"]
keywords: Web Carbon Emission, Energy-efficient Web Design, Layout Graph, DOM Tree Analysis 
year: 2025
ref: NOLTA 2025
journal: "NOLTA 2025"
feature: Accepted;
---

<h4><span class="badge badge-info">Abstract</span></h4>
Webpages have become a primary medium for information consumption, prompting advancements in quality assessment techniques that emphasize user experience. Recently, approaches that convert Document Object Model trees into graph structures and apply Graph Neural Networks have gained attention for quantifying layout quality. However, existing web carbon estimation tools rely solely on data transfer volume, failing to incorporate structural attributes such asDOMcomplexity or rendering costs. This study proposes a carbon emission prediction model that represents a webpage’s DOM tree as a graph and applies a Graph Attention Network to learn structural complexity and computational overhead. Each node encodes layout-related features, including tag type, size, and position, while the attention mechanism identifies components that contribute significantly to emissions. In addition, realtime carbon intensity data are integrated to enable contextaware predictions based on region and time. Model training leverages semi-supervised labels derived from existing carbon calculators and a subset of empirical measurements. By capturing structural factors overlooked in prior methods, the proposed approach enhances prediction accuracy. This structure-aware framework enables developers to assess carbon impact more precisely, supports eco-efficient design practices, and demonstrates potential as a digital indicator for carbon neutrality.
