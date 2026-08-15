---
layout: paper
ptype: intconf
group: knowevo
title: "Cross-Modal Attribute Consistency Verification for E-Commerce Products via Relational Graph Embedding"
authors: Ayoung Kim, Jeonghyeon Park, Wonseok Son, Sejin Chun  
kauthors: ["김아영", "박정현", "손원석", "천세진"]
year: 2026
image: /images/papers/cikm2026_short.png
ref: ACM CIKM 2026
journal: "ACM International Conference on Information and Knowledge Management (CIKM)"
keywords: e-commerce, cross-modal attribute consistency, relation classification, structural triples, relational graph embedding
feature: Top-Tier;Accepted;
venue: /images/papers/cikm2026_short.png
# doi: https://ieeexplore.ieee.org/document/10643899
---

<h4><span class="badge badge-info">Abstract</span></h4>
Product attributes on e-commerce pages are often distributed across two modalities, textual content and embedded images. Such crossmodal presentation can introduce inconsistencies in wording, units, values, and attribute presence. Existing approaches match representations across modalities, but such alignment only indicates correspondence and cannot determine the relation type between paired attributes, such as equivalence and value conflict.We propose a framework that verifies attribute consistency at the attribute-pair level. First, it aligns cross-modal attributes by combining representation normalization with semantic embedding matching. Second, it classifies each aligned pair into four relation types. Third, it represents the inferred relations as typed triples in a relational graph for relational embedding learning. Finally, we evaluate the proposed framework on a real-world dataset in terms of relation classification, link prediction, and structural triple injection.

<h4><span class="badge badge-info">Highlights</span></h4>
<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>The proposed framework</figcaption>
</figure>

<div class="alert alert-primary" role="alert">
    Acceptance Rate: 30.9% (234/764 papers accepted)
</div>
