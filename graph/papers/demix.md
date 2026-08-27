---
id: paper:demix
type: paper
title: "DeMix: Dynamic Data Mixture Optimization for Language Model Pretraining"
authors:
  - "Lucius LSR et al."
year: 2026
month: 2
arxiv_id: "2602.00747"
url: "https://arxiv.org/abs/2602.00747"
methods:
  - method:demix
cites: []
tags:
  - pretraining
  - data-curriculum
  - demix
---

# DeMix: Dynamic Data Mixture Optimization for Language Model Pretraining

## Abstract Summary
DeMix dynamically rebalances domain mixtures throughout language model pretraining by monitoring validation gradient alignments across domain checkpoints, improving sample efficiency over static token mixes.

## Key Contributions
1. **Dynamic Domain Weighting**: Continuous adjustment of domain proportions during training.
2. **Gradient Alignment Metric**: Uses inner-product gradient signals to detect diminishing returns on web corpora.

## Open Source Repository
- Implementation: `https://github.com/Lucius-lsr/DeMix`
