---
id: paper:htmuon
type: paper
title: "HTmuon: Heavy-Tailed Momentum Orthogonalization for Large-Scale Training"
authors:
  - "HTmuon Research Authors"
year: 2026
month: 3
arxiv_id: "2603.10067"
url: "https://arxiv.org/abs/2603.10067"
methods:
  - method:htmuon
cites:
  - paper:muon-scalable
tags:
  - optimizer
  - pretraining
  - htmuon
---

# HTmuon: Heavy-Tailed Momentum Orthogonalization for Large-Scale Training

## Abstract Summary
HTmuon addresses gradient noise in extreme-scale pretraining by introducing heavy-tailed noise filtering into matrix-orthogonalizing momentum optimizers.

## Key Contributions
1. **Heavy-Tailed Noise Robustness**: Mitigates gradient spikes in non-stationary data mixes.
2. **Matrix Stability**: Preserves spectral norm properties during batch transitions.

## Open Source Repository
- Implementation: `https://github.com/TDCSZ327/HTmuon`
