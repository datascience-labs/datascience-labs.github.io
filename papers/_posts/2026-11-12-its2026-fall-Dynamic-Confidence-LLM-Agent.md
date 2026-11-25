---
layout: paper
ptype: domconf
group: knowevo
title: "제조분야 LLM 에이전트의 선택적 실행을 위한 작업 복잡도와 행동 위험도 기반 동적 신뢰도 계산"
authors: Yuri Jeon, Jeonghyun Park, Sejin Chun
kauthors: ["전유리", "박정현", "천세진"]
year: 2026
ref: 2026 한국ITS학회 추계학술대회
journal: "2026 한국ITS학회 추계학술대회"
keywords: LLM 에이전트, 선택적 실행, 동적 신뢰도, 작업 복잡도, 행동 위험도, 제조
---

<h4><span class="badge badge-info">Abstract</span></h4>
LLM 에이전트에서 경량 모델이 신뢰도 높은 행동을 직접 실행하고 불확실한 행동을 상위 모델에 위임하려면, 동일한 신뢰도라도 작업의 복잡도와 잘못된 실행의 피해에 따라 실행 기준을 달리해야 한다. 본 연구는 행동의 신뢰도(c), 작업 복잡도(q), 행동 위험도(r)를 정규화하고, 복잡도와 위험도에 따라 임계값 τ(q,r) = min{1, τ0 + α·q + β·r}을 조절하는 동적 신뢰도 기반 선택적 실행 방법을 제안한다. 신뢰도가 임계값 이상이고 실행 조건을 충족하면 행동을 직접 실행하고, 신뢰도가 부족하면 상위 모델에 위임하며, 필수 정보나 승인이 부족하면 사용자 확인을 요청한다. 설비 고장에 따른 부품 제조기업의 생산 일정 변경 시나리오를 대상으로, 강력한 모델 단독 사용 및 고정 임계값 방식과 작업 성공률, 오류 실행률, 상위 모델 호출 비율, 평균 추론 비용을 비교할 계획이다.
<div class="alert alert-warning" role="alert">
  Dynamic Confidence Computation for Selective Action Execution in LLM Agents Based on Task Complexity and Action Risk
</div>
