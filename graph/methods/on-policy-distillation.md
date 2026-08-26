---
id: method:on-policy-distillation
type: method
title: "On-Policy Distillation (GKD / Thinking Machines Recipe)"
category: "distillation"
status: sota
sota_for:
  - task:student-distillation
supersedes: []
papers:
  - paper:gkd
recipes:
  - recipe:on-policy-distillation
claims:
  - benchmark: "GSM8k / HumanEval / MT-Bench Student Benchmarks"
    metric: "student performance retention"
    value: "Strictly superior to offline teacher-trace SFT"
    baseline: "Offline SFT on Teacher Traces"
    date: "2025-01"
    verified: true
    notes: "Rolls out token sequences from the student policy, scoring student-generated tokens with teacher forward log-probs."
tags:
  - distillation
  - on-policy
  - gkd
---

# On-Policy Distillation (GKD / Thinking Machines Recipe)

## Method Overview
Unlike static offline distillation where students learn via teacher-generated tokens, **On-Policy Distillation** (Generalized Knowledge Distillation / Thinking Machines 2025 recipe) samples rollouts directly from the active *student* policy, then scores each token using the *teacher's* output logits via reverse or mixed KL divergence:
\[
\mathcal{L}_{\text{GKD}} = \mathbb{E}_{x \sim \mathcal{D}, y \sim \pi_{\text{student}}(\cdot|x)} \left[ D_{\text{KL}}(\pi_{\text{student}}(\cdot|x, y_{<t}) \,\|\, \pi_{\text{teacher}}(\cdot|x, y_{<t})) \right]
\]
This prevents distribution shift and exposure bias during inference.

## Supersession
- Supersedes offline teacher-CoT SFT for student distillation.
