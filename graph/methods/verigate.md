---
id: method:verigate
type: method
title: "VeriGate (Gated Process Supervision)"
category: "rl-alignment"
status: sota
sota_for:
  - task:all-zero-verifier-groups
papers:
  - paper:verigate
recipes:
  - recipe:verigate
claims:
  - benchmark: "Process Supervision & Mathematical Reasoning"
    metric: "reward hacking prevention & pass@1 accuracy"
    value: "Default SOTA for verifier-gated process reward modeling"
    baseline: "Un-gated PRM / Outcome-Only Reward"
    date: "2026-08-26"
    verified: true
    notes: "Strictly gates PRM signals behind trusted deterministic outcome verifiers to safeguard reasoning alignment."
tags:
  - post-training
  - reasoning
  - verigate
  - process-supervision
  - sota
---

# VeriGate (Gated Process Supervision)

## Method Overview
VeriGate implements gated process supervision for mathematical and logical reasoning:
1. **Verifier Gating**: Process Reward Model (PRM) scores are gated behind deterministic outcome verification, ensuring PRMs cannot reward incorrect reasoning traces.
2. **All-Zero Group Handling**: Robust advantage estimation when all candidate rollouts in a verification group fail.

## When to Use
- Default SOTA method for process supervision and all-zero verifier group optimization.
