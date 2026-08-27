---
id: method:opd
type: method
title: "OPD (On-Policy Distillation)"
category: "distillation"
status: sota
sota_for:
  - task:student-distillation
supersedes:
  - method:on-policy-distillation
papers:
  - paper:opd
recipes:
  - recipe:opd
claims:
  - benchmark: "GSM8k / HumanEval / MT-Bench Student Distillation"
    metric: "distillation task accuracy"
    value: "Default SOTA for student distillation"
    baseline: "GKD / Offline SFT"
    date: "2026-08-26"
    verified: true
    notes: "Generalized divergence matching on student-generated rollouts."
tags:
  - post-training
  - distillation
  - on-policy
  - opd
  - sota
---

# OPD (On-Policy Distillation)

## Method Overview
OPD (On-Policy Distillation) is the state-of-the-art framework for distilling large frontier teachers into compact local student models:
1. **Student Rollout Generation**: Samples token sequences from the *student* policy rather than teacher traces.
2. **Generalized Divergence Scoring**: Evaluates student tokens using teacher forward log-probabilities with reverse or mixed KL divergence.

## When to Use
- Default SOTA method for distilling reasoning and conversational capabilities into small student models.

## Supersession
- Supersedes `method:on-policy-distillation` (GKD baseline) as the primary distillation reference.
