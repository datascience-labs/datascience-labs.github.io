---
layout: paper
ptype: intconf
group: knowevo
title: "Real-time Stock Market Analytics for Improving Deployment and Accessibility using PySpark and Docker"
image: /images/papers/debs2022-framework.png
authors: Suyeon Wang, Jaekyong Kim, Yoonsang Yang, Jinseong Hwang, Jungkyu Han, Sejin Chun
year: 2022
ref: ACM DEBS 2022
journal: "DEBS '22: Proceedings of the 16th ACM International Conference on Distributed and Event-Based SystemsJune 2022 Pages 171–175"
doi: 10.1145/3524860.3539652
---

<h4><span class="badge badge-info">Abstract</span></h4>
Making timely-decisions amid the massive influx of financial data is one of the essential features of stock market analytics. Many stock market analytics should provide functionalities that compute multiple technical indicators simultaneously and detect breakout situations. The DEBS 2022 Grand Challenge (DEBS22 GC) competition requires to answering two types of queries: technical trend indicators and detection of crossover patterns. In response to the competition, we propose a real-time stock market analytic solution using PySpark and Docker. Our solution calculates the technical trend indicator---Exponential Moving Average(EMA)---in real-time with the window function. With the technical indicators computed, we detect the breakout pattern that helps determine either buy or sell stocks. Our solution not only improves the speed of deploying applications using a Docker container image but also can be accessed easily via a web-based Jupyter notebook.

<h4><span class="badge badge-info">Highlights</span></h4>
<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>The Architecture of StockInflux</figcaption>
</figure>