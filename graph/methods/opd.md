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
last_reviewed: "2026-09-04"
papers:
  - paper:opd
  - paper:opd-one-example
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

## Relation to Existing SOTA
- Remains the single-teacher student-distillation default. For a privileged same-model teacher that sees the gold solution, use `method:vista` instead of vanilla OPSD; that does not replace OPD.
- Optional filter when a verifier is available: `method:ra-opd`. Sampled-token pass@k entropy plug-in: `method:ida-opd`. Teacher-free train-time self-adaptation is `method:opsa` and does not replace OPD when a strong teacher is the goal.
- Data-efficiency companion (`paper:opd-one-example`, `method:opd-one-example`): OPD is data-overfed but algorithm-starved. One query recovers most full-data gain; ~16 semantically diverse queries match full-data / MOPD. Prefer semantic diversity over volume. Does not change this method's status.

## Gotchas & Failure Modes
- Do not scale the prompt set when 16-shot already matches full-data OPD. The remaining gap is student absorption / step-efficiency (`method:opd-one-example`).
- Sampled-token OPD can raise pass@1 while flattening pass@k. That is `method:ida-opd`, not more data.

## Supersession
- Supersedes `method:on-policy-distillation` (GKD baseline) as the primary distillation reference.
