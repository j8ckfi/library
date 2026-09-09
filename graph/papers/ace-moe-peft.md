---
id: paper:ace-moe-peft
type: paper
title: "ACE: Adapter Consolidation across Experts for Parameter-Efficient Fine-Tuning of MoE LLMs"
authors:
  - "Ahin Lee"
  - "Sehyun Yun"
  - "Joonha Park"
  - "Taesik Gong"
year: 2026
month: 9
arxiv_id: "2609.06072"
url: "https://arxiv.org/abs/2609.06072"
methods:
  - method:ace-moe-peft
cites: []
tags:
  - peft
  - moe
  - ace-moe-peft
---

# ACE: Adapter Consolidation across Experts for Parameter-Efficient Fine-Tuning of MoE LLMs

## Abstract Summary
Expert-wise LoRA on MoE splits capacity, sparse-routes gradients, and launches many small GEMMs. ACE (Adapter Consolidation across Experts) groups redundant experts and replaces per-expert adapters with group-shared higher-rank LoRA under the same PEFT budget, then runs grouped adapter GEMMs. Across 12 datasets and four MoE backbones (EMNLP 2026), ACE has the highest observed mean accuracy among parameter-matched PEFT methods on the three backbones with complete baseline coverage, with 1.31×–1.48× wall-clock training speedup over expert-wise LoRA and no extra peak memory. Distinct from `method:ace` (Agentic Context Engineering).

## Key Contributions
1. **Expert-adapter redundancy**: subsets of expert LoRAs become functionally similar.
2. **Group-shared higher-rank LoRA** under a fixed PEFT budget.
3. **Grouped GEMMs** instead of many tiny expert-wise kernels.

## Empirical Highlights
- Highest mean accuracy among parameter-matched PEFT on three of four MoE backbones with complete baselines.
- 1.31× to 1.48× training speedup vs expert-wise LoRA; peak memory not increased.

## Open Source Repository & Resources
- Code: `https://github.com/UbiquitousAILab/ACE` (EMNLP 2026).
