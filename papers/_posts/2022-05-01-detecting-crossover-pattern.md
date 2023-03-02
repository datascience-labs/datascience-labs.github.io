---
layout: paper
ptype: domconf
group: knowevo
title: "실시간 주식 매수를 위한 아파치 스파크 기반 크로스오버 패턴 분석"
authors: Suyeon Wang, Sejin Chun 
year: 2022
ref: 한국멀티미디어학회 춘계학술발표대회 2022.
journal: "2022년 한국멀티미디어학회 춘계학술발표대회"
---

<h4><span class="badge badge-info">Abstract</span></h4>
주식 시장에서, 크로스오버(Crossover) 패턴(이하 ‘크로스오버’)는 주식분석자가 가까운 미래의 주식이 어떻게 변화할지를 예측하는데 사용된다. 해당 패턴은 주식의 가격과 기술적 지표(Technical Indicators) 선이 교차하거나 두 지표간의 교차하는 지점을 의미한다. 따라서, 크로스오버는 주식 매수 혹은 매도의 신호를 생성하기 위한 분석에 널리 사용되는 기술적인 지표 중의 하나이다.
빠르게 생성되는 대규모의 주식 빅데이터로부터 수초내에 크로스오버 패턴을 식별하기 위해, 효율적인 실시간 데이터 처리 프레임워크가 필요하다. 본 논문은 대규모 주식 데이터의 흐름을 처리할 수 있는 인메모리(In-memory) 기반 고속 데이터 처리 연산을 지원하는 Apache Spark에 기반한 방법을 제안한다. 우리는 다른 기간을 가진 두 이동 평균(MA: Moving Average) 차이로부터 크로스오버 지점을 발견하고 강세/약세 장(Bullish/Bearish Trends) 여부를 결정한다.

<div class="alert alert-warning" role="alert">
   Detecting Crossover Patterns for Buying Stocks in Real-time using Apache Spark
</div>