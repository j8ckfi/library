---
id: method:mad-rsi
type: method
title: 'MaD-RSI'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'production kernel (rewind, sandbox, remote, TUI)'
  reason: 'omp2 remains the kernel; MaD-RSI trains a shared harness across heterogeneous LLMs'
  use_instead: method:omp2-harness
- when: 'recursive self-rewrite of a research-agent harness (accepted rewrite is the next incumbent)'
  reason: 'AIDE2 rewrites one incumbent; MaD-RSI treats models as training data for a shared harness'
  use_instead: method:aide2
assumptions:
- 'Multiple heterogeneous LLMs contribute failure trajectories to one harness optimization.'
- 'Code cuiyu-ai/MaD-RSI as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:mad-rsi
recipes:
- recipe:mad-rsi
claims:
- benchmark: 'Multiple datasets and LLMs; two complementary cross-model harness metrics'
  metric: 'cross-model generalization and training cost vs single-model RSI'
  value: 'improves generalization over existing RSI while reducing training cost by treating model differences as training evidence'
  baseline: 'single-model harness RSI with post-hoc cross-model eval'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28201'
  notes: 'Does not retarget omp2 or AIDE2.'
tags:
- agent-harness
- rsi
- multi-model
- active
---

# MaD-RSI

## Method Overview
MaD-RSI (Model-as-Data RSI) optimizes one shared harness on failure trajectories from several LLMs, instead of fitting a harness to one model and testing transfer later.

## When to Use
- Harness RSI that must transfer across models without a per-model search.

## When NOT to Use
Production kernel → `method:omp2-harness`. Single-incumbent rewrite → `method:aide2`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:omp2-harness`.

## Gotchas & Failure Modes
- Shared harness can still overfit the training model mix.
- Not a production kernel.
