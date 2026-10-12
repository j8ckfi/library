---
id: paper:cv-opd
type: paper
title: 'CV-OPD: Contrastive Vision On-policy Distillation'
authors:
- Haowei Wang
- Hao Lin
- Qi Zhu
- Jiayi Ji
- Deyi Ji
- Liujuan Cao
- Rongrong Ji
year: 2026
month: 10
arxiv_id: '2610.13264'
url: https://arxiv.org/abs/2610.13264
methods:
- method:cv-opd
cites:
- paper:opd
- paper:where-opd
tags:
- post-training
- distillation
- opd
- vlm
- cv-opd
---

# CV-OPD: Contrastive Vision On-policy Distillation

## Abstract Summary
Vanilla VLM OPD lets the student answer from the answer hint even when visual regions are masked. CV-OPD contrasts teacher distributions on positive vs negative crops under the same student prefix, adds a margin Contrastive Divergence Loss, and gates tokens with token- and sample-level discrepancy so only visually relevant tokens are optimized.

## Key Contributions
1. Documents the visual shortcut in answer-hinted OPD.
2. Positive/negative crop teachers + CDL + discrepancy-aware gate.
3. Gains on fine-grained visual benches vs vanilla OPD.

## Empirical Highlights
- See `method:cv-opd` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13264`
- Code: `none found` (`code_status: none`).
