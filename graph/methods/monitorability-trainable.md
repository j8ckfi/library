---
id: method:monitorability-trainable
type: method
title: 'Monitorability Post-Training'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:math-code-rl-dense'
  reason: 'Monitorability Post-Training is an active plug-in; method:cispo remains the first hop'
  use_instead: method:cispo
assumptions:
- 'CoT tokens are still produced. Mutual information vs the output, no extra labels. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:monitorability-trainable
recipes:
- recipe:monitorability-trainable
claims:
- benchmark: 'Three degraded-CoT organisms; undegraded policies vs CoT monitors and probes'
  metric: 'recovered monitorability; unsafe-behavior prediction'
  value: 'recovers most or all lost monitorability on three organisms; on undegraded policies improves judged monitorability and monitor/probe prediction of unsafe behavior'
  baseline: 'CoT-compressed / monitor-optimized / synthetic-document-degraded policies without the MI stage'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29734'
  notes: 'Does not retarget method:cispo.'
tags:
- rlvr
- monitorability
- active
---

# Monitorability Post-Training

## Method Overview
An unsupervised post-training stage maximizes mutual information between chain-of-thought and the final output so monitors stay coupled to what the model does.

## When to Use
- After RLVR or other post-train that compressed, hid, or decoupled CoT from actions.

## When NOT to Use
Default Pass@1 → `method:cispo`. Misspecification-vs-monitorability gotcha → `paper:reward-misspecification-cot`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:cispo`.

## Gotchas & Failure Modes
- No public code.
- This protects CoT as a monitor surface; it is not a Pass@1 optimizer.
