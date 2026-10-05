---
id: paper:scad
type: paper
title: "SCAD: Structured Credit Assignment and Distillation for Long-Horizon Agents"
authors:
  - "Shangyang Wu"
  - "Shuai Zhao"
  - "Ziyue Zhu"
  - "Jinyang Wu"
  - "Anh Tuan Luu"
  - "Haoran Luo"
year: 2026
month: 10
arxiv_id: "2610.03372"
url: "https://arxiv.org/abs/2610.03372"
methods:
  - method:scad
cites:
  - paper:canopy
  - paper:pivotopd
  - paper:foldgrpo
tags:
  - post-training
  - rl-alignment
  - agentic
  - distillation
  - scad
---

# SCAD: Structured Credit Assignment and Distillation for Long-Horizon Agents

## Abstract Summary
Long-horizon agents mix sparse terminal rewards with on-policy distillation that loses teacher signal as student histories grow. SCAD splits planning from bounded subtask execution: distill execution in local contexts, score planning with cross-rollout subtask-prefix trees, give planning signed terminal credit, and give execution only the positive terminal part plus local teacher guidance. Active plug-in beside CANOPY / PivotOPD. No public code as of 2026-10-05.

## Key Contributions
1. **Subtask-local distillation** so teacher feedback is computed in the same bounded context the student uses.
2. **Cross-rollout planning credit** from subtask–report prefix trees.
3. **Qwen3-4B text macro-average 46.10** vs ATOD 41.62 / HiPER 41.49 / FoldGRPO 39.60 (+4.48 vs strongest baseline). Multimodal +4.19 vs strongest baseline.

## Empirical Highlights
- ATOD / HiPER are paper baselines, not library methods.
- FoldGRPO remains the folding first hop; SCAD does not retarget it.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.03372`
- Code: none found as of 2026-10-05 (`code_status: none`). Homepage/code/model/data buttons in the HTML were not a public GitHub as of ingest.
