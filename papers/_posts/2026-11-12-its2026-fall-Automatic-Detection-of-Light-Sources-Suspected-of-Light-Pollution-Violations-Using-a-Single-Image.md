---
layout: paper
ptype: domconf
group: knowevo
title: "단일 이미지를 이용한 빛공해 위반 의심 광원 자동 탐지"
authors: Taeseung Jo, Seungju Kim, Jeongsu Kim, Sejin Chun
kauthors: ["조태승", "김승주", "김정수", "천세진"]
year: 2026
ref: 2026 한국ITS학회 추계학술대회
journal: "2026 한국ITS학회 추계학술대회"
keywords: 빛공해, 광원 탐지, 단일 이미지, YOLOv8, 이미지 기반 분석
---

<h4><span class="badge badge-info">Abstract</span></h4>

과도한 인공조명은 수면 장애와 생태계 교란을 유발하며, 도로 조명과 옥외광고물의 눈부심은 운전자 시인성을 저하시켜 교통안전에도 영향을 미친다. 「인공조명에 의한 빛공해 방지법」은 조명환경관리구역별로 조명 유형별 허용 기준을 규정하고 있으나, 기존 단속은 전문 인력이 휘도계·조도계를 이용하여 현장에서 직접 측정하는 절차에 의존한다. 본 연구에서는 촬영 이미지 한 장을 이용하여 빛공해 위반이 의심되는 광원을 자동으로 탐지하고 분석하는 시스템을 제안한다. 야간 저조도 환경을 고려하여 Gray-World 화이트밸런스, 양방향 필터, LAB 색공간 L채널 CLAHE를 적용하고, 전이학습한 YOLOv8 모델을 이용해 간판·장식조명·가로등 세 유형의 광원을 탐지한다. 탐지 영역은 sRGB 선형화와 Rec.709 계수를 이용해 상대휘도로 변환하고 고휘도 픽셀 비율을 산출하며, EXIF의 기종·ISO·노출시간·촬영각 정보를 이용하여 촬영 조건에 따른 편차를 보정한다. 또한 GPS 역지오코딩을 통해 조명환경관리구역을 판별하고 조명 유형별 법정 기준과 비교하여 위반 단계를 산출하며, 분석 결과를 침입광·눈부심·산란광·군집된빛의 네 유형으로 분류하여 제시한다. 실험에서는 간판·장식조명·가로등으로 구성된 야간 이미지 데이터셋을 구축하고 YOLOv8n을 전이학습하여 단일 이미지 기반 빛공해 분석 가능성을 확인하였다.

<div class="alert alert-warning" role="alert">
  Automatic Detection of Light Sources Suspected of Light Pollution Violations Using a Single Image
</div>