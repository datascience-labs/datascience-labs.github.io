---
layout: paper
ptype: domconf
group: knowevo
title: "벤치마크 데이터 무결성 검증을 통한 MLLM의 표 이해 성능 분석"
authors: Donghyeon Kim, Ayoung Kim, Jungkyu Han, Sejin Chun
kauthors: ["김동현", "김아영", "한정규", "천세진"]
keywords: TableVQA, Multimodal Large Language Models, Table Understanding, Benchmark Data Integrity, Ground Truth Correction, Evaluation Reliability
year: 2026
ref: 한국정보과학회 한국컴퓨터종합학술대회 2026
journal: "2026 한국컴퓨터종합학술대회"
venue: /images/papers/KCC2026.png
image: /images/papers/KCC2026.png
---

<h4><span class="badge badge-info">Abstract</span></h4>
표는 다양한 분야에서 핵심적인 정보 전달 수단으로 활용되며, 최근에는 문서 이미지 형태의 표를 대상으로 한 TableVQA의 중요성이 커지고 있다. 그러나 이 과제는 문자 인식을 넘어 표 구조와 셀 간 관계, 수치 비교를 포함한 추론까지 요구하므로 여전히 어려운 문제로 남아 있다. 기존 연구는 이미지 표에서의 성능 저하를 모델의 한계로 해석해 왔지만, 정답지 품질과 평가 기준의 영향은 충분히 검토하지 않았다. 이에 본 연구는 최신 멀티모달 대규모 언어모델을 활용해 TableVQA-Bench를 대상으로 재현 실험을 수행하고, 여러 도메인의 문항과 오답 사례를 중심으로 정답지와 평가 과정의 한계를 검토하였다. 그 결과, 일부 성능 저하는 모델 자체보다 정답지 오류와 평가 기준의 경직성에서 비롯된 것으로 나타났다. 이는 TableVQA 평가에서 모델 성능뿐 아니라 데이터 무결성과 평가 체계의 신뢰성도 함께 고려해야 함을 보여준다.

<figure>
<img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
<figcaption>제안 프레임워크</figcaption>
</figure>

<div class="alert alert-warning" role="alert">
An Analysis of MLLM Table Understanding Performance through Benchmark Data Integrity Assessment
</div>
