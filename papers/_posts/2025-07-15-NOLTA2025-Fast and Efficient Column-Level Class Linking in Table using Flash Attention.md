---
layout: paper
ptype: intconf
group: knowevo
title: "Fast and Efficient Column-Level Class Linking in Table using Flash Attention"
authors: Wonseok Son, Yewon Lee, Jungkyu Han, Sejin Chun
kauthors: [ "손원석", "이예원", "한정규", "천세진"]
keywords: Semantic Table Interpretation, FlashAttention, Knowledge Graph Linking, Column Type Annotation
year: 2025
ref: NOLTA 2025
journal: "NOLTA 2025"
feature: Accepted;
---

<h4><span class="badge badge-info">Abstract</span></h4>
Semantic Table Interpretation (STI) is essential for understanding and analyzing structured tabular data, with column-level entity prediction being a key subtask. Recent studies have actively explored Transformer-based architectures for this purpose. However, these methods often incur substantial computational overhead due to the complexity of their attention mechanisms, resulting in prolonged inference times. In this study, we propose a highly efficient column-level entity prediction model that leverages FlashAttention to mitigate these limitations. Our approach structurally captures the relationships between table cells and their corresponding headers, enabling effective semantic representation of each column. Experimental results show that the proposed model achieves up to 2.1× faster inference compared to existing methods, without sacrificing prediction accuracy.