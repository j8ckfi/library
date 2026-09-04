---
id: method:verigate
type: method
title: "VeriGate (Verifier-Gated Step-Level Supervision for GRPO)"
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

# VeriGate (Verifier-Gated Step-Level Supervision for GRPO)

## Method Overview
VeriGate implements verifier-gated step-level supervision for GRPO in mathematical and logical reasoning:
1. **Verifier Gating**: Process Reward Model (PRM) step-level supervision is selectively applied only on all-zero verifier groups (where all sampled rollouts fail the outcome verifier), while mixed-reward groups remain under standard outcome GRPO.
2. **Reward Hacking Prevention**: Prevents noisy PRMs from overriding ground-truth outcome verification while supplying rich gradient signal when no positive outcome rollout exists.

## Implementation & Repository
- Repository: `https://github.com/umd-huang-lab/VeriGate`

## When to Use
- Default SOTA method for process supervision and all-zero verifier group optimization.

## Relation to Existing SOTA
- Remains the gated-PRM / all-zero-group default. `method:cliff` is an active first-mistake credit plug-in, not a PRM, and does not replace VeriGate.
