---
layout: paper
ptype: intconf 
group: knowevo
title: "Geographic Area Analysis by Using VAE based Area Embeddings on LBSN data"
authors: Muyeon Jo, Sejin Chun, Jungkyu Han
kauthors: ["조무연", "천세진", "한정규"]
year: 2023
ref: RACS 2023
journal: "Proceedings of the 2023 International Conference on Research in Adaptive and Convergent Systems"
image: /images/papers/RACS-Geographic-Area-Analysis.png
doi: 10.1145/3599957.3606245
keywords: Geographical Influence, Point of Interest, Area Characteristics, Location-based Social Network
---

<h4><span class="badge badge-info">Abstract</span></h4>
Location-Based1 Social Networks (LBSNs) are social networking services that allow users to share the Points of Interest (POIs) they have visited. The data from LBSNs are used for personalized place recommendations and the analysis of user mobility. In this study, we propose a method to analyze LBSN data from two perspectives: the functionalities provided by different areas in a city and the mobility of users visiting those areas. Specifically, we employ the Variational Auto Encoder (VAE) to embed the distribution of user visits over POI categories and the distribution of user visits over areas for each area. We then use these embeddings to analyze the similarity of areas. The analysis reveals that user visits are concentrated in relatively nearby areas, while areas with similar functionalities are distributed widely across the entire city. Furthermore, we found that user visits have a stronger influence than the visited categories in determining the characteristics of areas.

<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>The proposed model</figcaption>
</figure>


<div class="alert alert-warning" role="alert">
   Geographic Area Analysis by Using VAE based Area Embeddings on LBSN data
</div>

<h4><span class="badge badge-info">published</span></h4>