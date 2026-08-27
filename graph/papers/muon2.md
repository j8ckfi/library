---
id: paper:muon2
type: paper
title: "Muon2: Scaling Matrix Orthogonalization Optimizers"
authors:
  - "Muon2 Research Authors"
year: 2026
month: 4
arxiv_id: "2604.09967"
url: "https://arxiv.org/abs/2604.09967"
methods:
  - method:muon2
cites:
  - paper:muon-scalable
  - paper:muon-optimizer-paper
tags:
  - optimizer
  - pretraining
  - muon2
---

# Muon2: Scaling Matrix Orthogonalization Optimizers

## Abstract Summary
Muon2 introduces second-generation matrix orthogonalization improvements over vanilla Muon, optimizing Newton-Schulz polynomial iterations and stabilizing update scaling across deep transformer blocks during trillion-token language model pretraining.

## Key Contributions
1. **Second-Generation Orthogonalization**: Refined Newton-Schulz iterations with adaptive coefficient scheduling.
2. **Update Scaling**: Improved stability for hidden matrix representations at 7B+ parameter scale.
3. **Efficiency**: Maintains ~2x token efficiency over AdamW with reduced wall-clock overhead.

## Open Source Repository
- Implementation: `none found`
