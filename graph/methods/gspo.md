---
id: method:gspo
type: method
title: "GSPO (Group Sequence Policy Optimization)"
category: "rl-alignment"
status: active
superseded_by: method:sapo
sota_for: []
supersedes:
  - method:grpo
papers:
  - paper:gspo
recipes:
  - recipe:grpo-trl-training
claims:
  - benchmark: "Qwen3 MoE Reasoning RL"
    metric: "pass@1 accuracy"
    value: "State of the art on MoE reasoning RL"
    baseline: "Token-level GRPO"
    date: "2025-07"
    verified: true
    notes: "Sequence-level importance sampling ratio to stabilize RL policy updates under dynamic expert routing."
tags:
  - rl-alignment
  - reasoning
  - moe
  - gspo
---

# GSPO (Group Sequence Policy Optimization)

## Method Overview
GSPO replaces token-level importance sampling (IS) with a sequence-level importance sampling ratio. Maintained for Qwen3 / Qwen3.5-Omni Talker lineage.

## Supersession
- Superseded by `method:sapo` for Qwen MoE/VL reasoning alignment.
