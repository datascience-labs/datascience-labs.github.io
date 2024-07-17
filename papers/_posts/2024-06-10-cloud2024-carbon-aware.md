---
layout: paper
ptype: intconf
group: knowevo
title: "Carbon-Aware and Fault-Tolerant Migration of Deep Learning Workloads in the Geo-distributed Cloud"
authors: Jeonghyeon Park, Daero Kim, Jiseon Kim, Jungkyu Han, Sejin Chun  
year: 2024
image: /images/papers/cloud2024.png
ref: IEEE CLOUD 2024
journal: "IEEE International Conference on Cloud Computing (CLOUD)"
keywords: carbon-aware, fault-tolerant, geo-distributed, cloud, deep learning, task migration
feature: Top-Tier;Accepted;
venue: /images/papers/cloud2024.png
---

<h4><span class="badge badge-info">Abstract</span></h4>
Recently, many deep learning models have been trained in geographically distributed data centers. The carbon emissions produced by training the models may pose a significant threat to climate change like increasing temperatures. Existing studies have a hardship in shifting the workload of training models to a data center with low carbon emissions. So, they fail to ensure low emissions of the workload during training, especially when long-term workloads like Large Language Models~(LLMs) are trained. To cope with this problem, we propose a method that shifts the workload to a cloud with low carbon emissions while enduring a lack of computational resources. Specifically, we define a task scheduler that includes states and their transitions to migrate mini-batches dynamically. Next, we present a fault-tolerant control that optimizes a GPU frequency to adapt to workload variations of training models while guaranteeing its power consumption. Last, we conducted exhaustive experiments using real-world data in terms of carbon emissions, transfer time, and power consumption compared to state-of-the-art methods.

<h4><span class="badge badge-info">Highlights</span></h4>
<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>CAFTM method</figcaption>
</figure>