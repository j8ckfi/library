---
id: paper:opd-skill-not-knowledge
type: paper
title: "On-Policy Distillation Teaches New Skills but Not New Knowledge"
authors:
  - "Yixuan Tang"
  - "Yi Yang"
year: 2026
month: 10
arxiv_id: "2610.09639"
url: "https://arxiv.org/abs/2610.09639"
methods:
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - opd
  - gotcha
  - opd-skill-not-knowledge
---

# On-Policy Distillation Teaches New Skills but Not New Knowledge

## Abstract Summary
Caution/evidence paper. Reverse-KL OPD transfers compositional skill across unseen reasoning structures but transfers minimal factual knowledge. Forward KL restores factual transfer; student rollouts specifically improve multi-step execution. Same asymmetry on factual QA vs competition math. Do not use reverse-KL OPD to inject facts the student does not already have. Does not retarget OPD as the matching default.

## Key Contributions
1. Reverse-KL OPD transfers compositional skill, not new facts.
2. Forward KL restores factual transfer; student rollouts help multi-step execution.
3. Factual QA vs competition math shows the same split.

## Empirical Highlights
- Controlled synthetic framework plus recent factual QA and competition math, four models from three families.
- Not a CISPO or OPD matching bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.09639`
- Code: none found as of 2026-10-09 (`code_status: none`).
