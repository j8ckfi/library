---
id: task:label-free-test-time-reasoner
type: task
title: "Label-Free Test-Time Reasoning and Policy Optimization"
domain: "post-training"
summary: "Performing test-time adaptation and training on unlabeled problem instances to improve mathematical and logical reasoning without ground-truth labels or external verifiers."
current_sota:
  - method: method:ttpo
    as_of: "2026-08-28"
    benchmark: "AIME24 / AIME25 / AMC23 / MATH500 / OlympiadBench (TTT)"
    metric: "test-time accuracy"
    value: "Matches label-supervised OPSD; Qwen3-1.7B 38.0% -> 45.2%"
    notes: "TTPO (2608.27448) uses asymmetric OPSD on agreeing rollouts and Grouped RL on disagreeing rollouts."
methods:
  - method:ttpo
  - method:u-opsd
  - method:j-zero
  - method:opdvr
  - method:cispo
tags:
  - test-time-training
  - reasoning
  - label-free
  - ttt
---

# Label-Free Test-Time Reasoning and Policy Optimization

## Problem Definition
Adapting reasoning language models at inference / test time on unlabeled query distributions without access to ground-truth answers, external reward models, or golden verification pipelines. Standard majority-vote pseudo-labeling suffers from error propagation when incorrect consensus votes corrupt supervisory signals.

## SOTA Recommendation (as of 2026-08-28)
- **Primary Method**: **TTPO** (`method:ttpo`, `paper:ttpo` `arXiv:2608.27448`) for asymmetric test-time policy optimization (agreeing rollout OPSD + disagreeing rollout Grouped RL).
- **Complementary Work**: `method:u-opsd` for train-time unlabeled post-training; `method:opdvr` when ground-truth verifiers and external teachers exist; `method:j-zero` for data-free train-time Challenger–Solver–Judge co-evolution (not test-time).
