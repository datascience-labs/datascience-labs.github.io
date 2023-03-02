---
layout: paper
ptype: domjour
group: recsys
title: 유사 아이템 정보를 이용한 콜드 아이템 추천성능 개선
authors: 한정규, 천세진
year: 2021
ref: 멀티미디어학회논문지 2021.
journal: "멀티미디어학회논문지, 2021, vol.24, no.12, pp. 1673-1681"
---

<h4><span class="badge badge-info">Abstract</span></h4>
Item cold start is a well studied problem in the research field of recommender systems. Still, many existing collaborative filters cannot recommend items accurately when only a few user-item interaction data are available for newly introduced items (Cold items). We propose a interaction feature prediction method to mitigate item cold start problem. The proposed method predicts the interaction features that collaborative filters can calculate for the cold items. For prediction, in addition to content features of the cold-items used by state-of-the-art methods, our method exploits the interaction features of k-nearest content neighbors of the cold-items. An attention network is adopted to extract appropriate information from the interaction features of the neighbors by examining the contents feature similarity between the cold-item and its neighbors. Our evaluation on a real dataset CiteULike shows that the proposed method outperforms state-of-the-art methods 0.027 in Recall@20 metric and 0.023 in NDCG@20 metric.

<div class="alert alert-warning" role="alert">
  Addressing the Item Cold-Start in Recommendation Using Similar Warm Items
</div>