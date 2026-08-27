---
id: task:math-code-rl-dense
type: task
title: "Mathematical and Code RL Reasoning (Dense Policies)"
domain: "post-training"
summary: "Reinforcement learning on verifiable mathematical and coding tasks using dense transformer policies."
current_sota:
  - method: method:cispo
    as_of: "2026-08-26"
    benchmark: "MATH-500 / AIME 2024 / LiveCodeBench"
    metric: "pass@1 accuracy & training stability"
    value: "Default SOTA for Dense RL"
    notes: "CISPO via MiniMax-M1 (2506.13585) + ScaleRL (2510.13786)."
methods:
  - method:cispo
  - method:dapo
  - method:sspo
  - method:minpro
  - method:dr-grpo
  - method:grpo
tags:
  - post-training
  - reasoning
  - math
  - code
  - cispo
---

# Mathematical and Code RL Reasoning (Dense Policies)

## Problem Definition
Training dense language models to generate long chains of thought (CoT) and verifiable solutions for competitive math and coding problems.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **CISPO** (`method:cispo`, MiniMax-M1 2506.13585 + ScaleRL 2510.13786).
- **Systems Reference**: DAPO stays as systems paper reference.
