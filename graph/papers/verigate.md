---
id: paper:verigate
type: paper
title: "VeriGate: Gated Process Supervision for Mathematical Reasoning"
authors:
  - "VeriGate Research Authors"
year: 2026
month: 5
arxiv_id: "2605.30451"
url: "https://arxiv.org/abs/2605.30451"
methods:
  - method:verigate
cites: []
tags:
  - post-training
  - reasoning
  - verigate
  - process-supervision
---

# VeriGate: Gated Process Supervision for Mathematical Reasoning

## Abstract Summary
VeriGate demonstrates that un-gated Process Reward Models (PRMs) introduce severe reward hacking, proving that process supervision must be strictly gated behind trusted deterministic outcome verifiers.

## Key Contributions
1. **Gated Process Supervision**: Verifier gating mechanism preventing noisy PRM rewards from overriding ground-truth outcome checks.
2. **All-Zero Group Handling**: Robust policy gradient formulation when all candidate rollouts in a verifier group fail.

## Open Source Repository
- Implementation: `none found`
