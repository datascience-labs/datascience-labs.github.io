---
layout: paper
ptype: domconf
group: knowevo
title: "건물 메쉬 데이터에서의 효율적 외피 구조 인식 알고리즘"
authors: Geonhan Kim, Daero Kim, Sejin Chun, Jungkyu Han
kauthors: ["김건한", "김대로", "천세진", "한정규"]
year: 2025
ref: 한국멀티미디어학회 추계학술발표대회 2025.
journal: "2025년 한국멀티미디어학회 추계학술발표대회"
Key Words : 건물 외피 추출, 평면 피팅, 계산 복잡도
---

<h4><span class="badge badge-info">Abstract</span></h4>
본 연구는 건물 메쉬 데이터로부터 외피(facade) 구조를 효율적으로 인식하기 위한 2단계 알고리즘을 제안한다. 1단계에서는 DFS 기반 인접 탐색을 통해 삼각형 면을 빠르게 그룹화하고, 2단계에서는 Convex Hull, RANSAC 기반 Plane Fitting, Normal 기반 Region Growing을 적용·비교하여 외피를 단일 평면 구조로 환원한다. 시간 복잡도 분석에 근거한 이론적 검토 결과, Convex Hull은 , RANSAC Plane Fitting은 , Normal 기반 Region Growing은 의 계산 복잡도를 갖는 것으로 분석된다. 이에 따라 Region Growing이 선형 복잡도로 가장 효율적일 가능성이 높으며, RANSAC은 이상치 보정에 유리하고, Convex Hull은 외곽 단순화에 적합함을 확인하였다. 제안된 접근법은 건물 외피 인식의 효율적 구조 분석과 시뮬레이션 응용에 이론적 근거를 제공한다.
<div class="alert alert-warning" role="alert">
  Efficient Envelope Structure Recognition Algorithm for Building Mesh Data
</div>
