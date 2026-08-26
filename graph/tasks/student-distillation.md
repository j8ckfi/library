---
id: task:student-distillation
type: task
title: "Small Local Student Distillation from Strong Teacher"
domain: "post-training"
summary: "Distilling reasoning and conversational capabilities from multi-hundred-billion parameter frontier teachers into small local student models."
current_sota:
  - method: method:on-policy-distillation
    as_of: "2026-08-26"
    benchmark: "GSM8k / HumanEval / MT-Bench Student Evaluation"
    metric: "task accuracy vs teacher parity"
    value: "Strictly Pareto-superior to offline SFT"
    notes: "On-policy distillation (GKD / Thinking Machines 2025 recipe): sample from the student, score tokens with teacher log-probs (reverse or mixed KL)."
methods:
  - method:on-policy-distillation
tags:
  - post-training
  - distillation
  - on-policy
---

# Small Local Student Distillation from Strong Teacher

## Problem Definition
Training small local students (1B–8B) from large teacher models (70B–405B). Standard offline SFT on static teacher traces suffers from severe exposure bias / distribution shift when the student deviates at test time.

## SOTA Recommendation (as of 2026-08-26)
- **Method**: **On-Policy Distillation** (`method:on-policy-distillation`, GKD / Thinking Machines 2025 recipe).
- **Protocol**: Sample token sequences from the *student* policy, then score tokens with teacher log-probabilities using reverse or mixed KL divergence.
