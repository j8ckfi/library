---
id: task:distill-reasoner-verifier
type: task
title: "Distill a Reasoner with Verifiable Reward"
domain: "post-training"
summary: "Combining dense token-level on-policy distillation guidance with task-level verifiable reward (RLVR) correctness for reasoning models."
current_sota:
  - method: method:opdvr
    as_of: "2026-08-27"
    benchmark: "AIME24 / AIME25 / AMC / GSM8K"
    metric: "avg@16 accuracy"
    value: "SOTA for OPD + RLVR integration"
    notes: "OPDVR (2608.24696) with zero-extra-hyperparameter ReLU correctness gating."
methods:
  - method:opdvr
  - method:opd
  - method:cispo
  - method:verigate
  - method:tulu3-rlvr
tags:
  - post-training
  - distillation
  - rlvr
  - reasoning
---

# Distill a Reasoner with Verifiable Reward

## Problem Definition
Distilling multi-step reasoning capabilities from strong teacher models into compact students while utilizing ground-truth verifiers (math outcomes, unit tests, formal checks) to prevent hallucinated teacher distributions from propagating to the student.

## SOTA Recommendation (as of 2026-08-27)
- **Primary Method**: **OPDVR** (`method:opdvr`, `paper:opdvr` `arXiv:2608.24696`) for zero-extra-hyperparameter ReLU-gated on-policy distillation.
- **Related Benchmarks**: AIME 2024/2025, AMC, GSM8K, MATH-500.
