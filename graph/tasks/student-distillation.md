---
id: task:student-distillation
type: task
title: "Small Local Student Distillation from Strong Teacher"
domain: "post-training"
summary: "Distilling reasoning and conversational capabilities from multi-hundred-billion parameter frontier teachers into small local student models."
current_sota:
  - method: method:opd
    as_of: "2026-08-26"
    benchmark: "GSM8k / HumanEval / MT-Bench Student Evaluation"
    metric: "task accuracy vs teacher parity"
    value: "Default SOTA for student distillation"
    notes: "OPD 2604.13016 + MOPD (Cascade-2 / Kimi-K3 / GLM-5)."
methods:
  - method:opd
  - method:tropd
  - method:stable-opd
  - method:opd2
  - method:w2s-opd
  - method:nemotron-cascade-2
  - method:on-policy-distillation
tags:
  - post-training
  - distillation
  - on-policy
  - opd
---

# Small Local Student Distillation from Strong Teacher

## Problem Definition
Training small local students (1B–8B) from large teacher models (70B–405B) with generalized on-policy divergence matching.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **OPD** (`method:opd`, 2604.13016) + **MOPD** (Cascade-2 / Kimi-K3 / GLM-5).
