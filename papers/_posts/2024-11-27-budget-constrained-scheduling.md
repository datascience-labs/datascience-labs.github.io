---
layout: paper
ptype: intjour
group: knowevo
title: "Budget-Constrained Runtime Allocation of Linked Data Services in Stream Processing"
authors: Jungkyu Han, Sejin Chun
kauthors: ["한정규", "천세진"]
year: 2024
doi: https://doi.org/10.1007/s41019-024-00277-4
ref: Data Science and Engineering 
journal: "Data Science and Engineering"
keywords: Stream processing, Linked open data, Materialized views, Refresh budget allocation, Answer staleness
feature: SCIE;
---

<h4><span class="badge badge-info">Abstract</span></h4>
Stream processing requires integrating with background knowledge in order to become rich knowledge. As a promising approach, it is getting important to combine streaming data with linked open data. However, since linked data change dynamically, it is impossible to synchronize their distributed data sources perfectly and seamlessly. To reduce the high cost of the synchronization, the materialized views (or views) that store local copies of remote sources are used but may degrade the accuracy of stream processing. To balance response time against accuracy, recent works manage a refresh budget – that is, the limited cost allocated for updating views over remote sources. However, they fail to allocate a refresh budget and produce a low accuracy when a tight deadline is given. To solve the problem, we propose an efficient method of allocating a refresh budget to view updates. The proposed method updates views both in the background and on demand. Experimental results with real and synthetic data sets show that the proposed method achieves superiority in terms of answer staleness, resource utilization, and refresh budget usage.

