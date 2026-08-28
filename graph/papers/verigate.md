---
id: paper:verigate
type: paper
title: "VeriGate: Verifier-Gated Step-Level Supervision for GRPO"
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

# VeriGate: Verifier-Gated Step-Level Supervision for GRPO

## Abstract Summary
VeriGate demonstrates that un-gated Process Reward Models (PRMs) introduce severe reward hacking, proposing verifier-gated step-level supervision for GRPO where PRM guidance is activated only on all-zero verifier groups while mixed-reward groups use standard outcome GRPO.

## Key Contributions
1. **Verifier-Gated Step Supervision**: Applies PRM step-level guidance exclusively when all rollouts fail verification, preserving outcome-level GRPO for mixed groups.
2. **Mitigating Reward Hacking**: Eliminates reward gaming from noisy intermediate PRM steps.

## Open Source Repository
- Implementation: `https://github.com/umd-huang-lab/VeriGate`
