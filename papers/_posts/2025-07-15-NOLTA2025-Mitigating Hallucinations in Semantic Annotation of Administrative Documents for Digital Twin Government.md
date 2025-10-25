---
layout: paper
ptype: intconf
group: knowevo
title: "Mitigating Hallucinations in Semantic Annotation of Administrative Documents for Digital Twin Government"
authors: Jeongsu Kim, Wonseok Son, Jungkyu Han, Sejin Chun
kauthors: [ "김정수", "손원석", "한정규", "천세진"]
keywords: Semantic Annotation, Hallucination Mitigation, Proposition Verification, Digital Twin Government, Administrative Documents
year: 2025
ref: NOLTA 2025
journal: "NOLTA 2025"
feature: Accepted;
---

<h4><span class="badge badge-info">Abstract</span></h4>
With the growing adoption of the digtial twin for data-driven decision-making, the accurate interpretation of massive public administrative documents has become increasingly critical. Semantic annotation, a key technique for enhancing the value of structured data, faces limitations such as ambiguity and lack of context—issues that are especially critical in the administrative domain. Recent studies on data augmentation using large language models (LLMs) have improved the performance of semantic annotation. However, the phenomenon of hallucination—where LLMs generate incorrect or fabricated content—poses a significant barrier to sensitive application domains like government. This paper proposes FACT-DT, a framework for Hallucination Control in Semantic Annotation of administrative tables. our framework leverages both tabular data and tabular context (e.g., topics, column headers, and inter-column relationships) to minimize context loss and control hallucinations during generation. It achieves this by decomposing the generated outputs into verifiable atomic propositions and extracting inter-sentential relationships to verify factuality. The effectiveness of the proposed framework in reducing hallucinations and enhancing faithfulness is quantitatively validated using LLM-based evaluation methods, such as G-Eval.