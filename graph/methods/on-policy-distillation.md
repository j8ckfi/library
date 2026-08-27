---
id: method:on-policy-distillation
type: method
title: "On-Policy Distillation (GKD / Thinking Machines Recipe)"
category: "distillation"
status: superseded
superseded_by: method:opd
sota_for: []
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
Samples rollouts directly from the active *student* policy, then scores each token using the *teacher's* output logits.

## Supersession
- Superseded by `method:opd` (2604.13016) as the primary distillation citation.
