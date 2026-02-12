---
layout: paper
ptype: intjour
group: knowevo
title: "GreenAccounter: A Toolkit for Carbon-Aware Orchestration of Deep Learning Workloads in Geo-Distributed Clouds"
authors: Jeonghyeon Park, Jaekyeong Kim, Wonseok Son, Sejin Chun
kauthors: ["박정현", "김재경", "손원석", "천세진"]
year: 2026
venue: /images/papers/SoftwareX.png
image: /images/papers/SoftwareX.png
ref: SoftwareX
journal: "SoftwareX"
feature: SCIE;
doi: https://doi.org/10.1016/j.softx.2026.102550
keywords: Carbon-aware, Deep Learning, Workload migration, Multi-cloud environments
---

<h4><span class="badge badge-info">Abstract</span></h4>
Deep learning workloads generate substantial carbon emissions in data centers, driven
by long training durations and intensive energy use. To address this challenge,
previous studies have explored temporal workload shifting and spatial workload
migration. Yet, these approaches remain limited for long-running workloads, such as
large language models, because they fail to adapt to continuous fluctuations in regional
carbon intensity. We introduce GreenAccounter, a toolkit for carbon-aware
orchestration of deep learning workloads across multi-cloud environments. It integrates
real-time carbon intensity monitoring with checkpoint-based migration, allowing training
to continue seamlessly while reducing emissions. A unified dashboard visualizes
regional carbon intensity, cumulative emissions, and power consumption, providing
operators with a single pane of glass for managing distributed cloud resources.
GreenAccounter functions both as a reproducible research platform for carbon-aware
scheduling and as a practical operational toolkit for emission reduction in AI training.
Released as open source, it promotes sustainable, transparent, and data-driven
practices for deep learning at scale.


<figure>
    <img class="pull-left pad-right media-object d-none d-sm-block" src="{{ page.image }}">
    <figcaption>The screenshot of the GreenAccounter dashboard.</figcaption>
</figure>



<div class="alert alert-primary" role="alert">

    본 툴킷은 <a href="https://github.com/datascience-labs/GreenAccounter">연구실 GitHub</a>에서 확인할 수 있습니다.

</div>