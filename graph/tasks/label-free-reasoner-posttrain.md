---
id: task:label-free-reasoner-posttrain
type: task
title: "Unlabeled Reasoner Post-Training without Ground Truth"
domain: "post-training"
summary: "Post-training reasoning language models on unlabeled problems without ground-truth labels, verifiers, or external teacher models."
current_sota:
  - method: method:u-opsd
    as_of: "2026-08-28"
    benchmark: "AIME24 / AIME25 / HMMT25 / MATH500 / AMC23 (Unlabeled)"
    metric: "avg accuracy"
    value: "+8.5% to +10.7% over base; beats supervised OPSD by +2.3% to +3.2% on non-thinking"
    notes: "u-OPSD (2608.06296) majority-votes own rollouts and distills pseudo-solution-conditioned distribution onto disagreeing paths."
methods:
  - method:u-opsd
  - method:ttpo
  - method:opdvr
  - method:cispo
tags:
  - post-training
  - distillation
  - label-free
  - reasoning
---

# Unlabeled Reasoner Post-Training without Ground Truth

## Problem Definition
Training and aligning multi-step reasoning capabilities on vast corpora of unlabeled mathematical, logical, and code problems where human annotations, gold solutions, or deterministic verifiers are absent or expensive to scale.

## SOTA Recommendation (as of 2026-08-28)
- **Primary Method**: **u-OPSD** (`method:u-opsd`, `paper:u-opsd` `arXiv:2608.06296`) for unsupervised on-policy self-distillation.
- **When Labels/Verifiers Exist**: Prefer `method:opdvr` (for distillation with verifiers) or `method:cispo` (for train-time RL with labels).
