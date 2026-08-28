---
id: paper:sspo
type: paper
title: "Soft Sequence Policy Optimization"
authors:
  - "Svetlana Glazyrina"
  - "Maksim Kryzhanovskiy"
  - "Roman Ischenko"
year: 2026
month: 2
arxiv_id: "2602.19327"
url: "https://arxiv.org/abs/2602.19327"
methods:
  - method:sspo
cites:
  - paper:gspo
  - paper:sapo
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - reasoning
  - sspo
---

# Soft Sequence Policy Optimization

## Abstract Summary
Soft Sequence Policy Optimization (SSPO) introduces an off-policy reinforcement learning objective within the GRPO family that unifies sequence-level coherence and token-level soft gating. By evaluating the geometric mean of token-level soft gates (defaulting to an arctan log-ratio function) inside sequence-level importance weights, SSPO mitigates variance and stabilizes policy updates, yielding consistent improvements over GRPO, GSPO, and SAPO on mathematical and coding reasoning tasks.

## Key Contributions
1. **Soft Sequence Objective**: Formulates sequence-level importance weights incorporating the geometric mean of token-level soft gates.
2. **Smooth Gating Function**: Employs an arctan transformation on token log-ratios to replace hard truncation thresholds with smooth bounds.
3. **Empirical Reasoning Gains**: Outperforms standard GRPO, GSPO, and SAPO baselines on complex reasoning tasks across math and code domains.

## Open Source Repository
- Implementation: `none found`

## Disambiguation
- Note: Soft Sequence SSPO (`arXiv:2602.19327`, Soft Sequence Policy Optimization) is distinct from subsentence SSPO (`arXiv:2511.04256`).
