---
layout: paper
ptype: intjour
group: knowevo
title: "Proactive policy for efficiently updating join views on continuous queries over data streams and linked data"
authors: Sejin Chun, Jooik Jung, Kyong-Ho Lee
year: 2021
ref: IEEE Access
journal: IEEE Access, 7, 86226-86241.
doi: 10.1109/ACCESS.2019.2923414
---

<h4><span class="badge badge-info">Abstract</span></h4>
Modern data analytic systems benefit from the fusion of streaming data and linked data distributed on the Web. Accessing the linked data at query time is prohibited as usual due to its expensive cost. To reduce the high cost, most of the database systems have used a materialized view (a view) that stores local copies of the data. However, views by conventional maintenance policies such as immediate, deferred, and periodic fail to achieve high accuracy of answers to queries on data streams and linked data. To cope with the limitations, we propose a maintenance policy that releases expensive jobs of copying the latest version of linked data into views at the idle time. In other words, we pre-fetch a portion of linked data in advance according to their update pattern and query evaluation semantics. Our multiple maintenance policies that take into account changes of linked data alleviate the degradation of performance at run-time. Using real-world datasets we report that the proposed method has a significant improvement in terms of the response time, compared to the state-of-the-art methods.