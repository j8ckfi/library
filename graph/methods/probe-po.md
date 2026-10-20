---
id: method:probe-po
type: method
title: 'ProbePO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'single-turn dense math/code Pass@1 RLVR default'
  reason: 'CISPO remains Pass@1; ProbePO is budgeted partial-solution probes on a GRPO host'
  use_instead: method:cispo
- when: '1-sample actor-critic with a learned value head'
  reason: 'BPCO remains the critic first hop'
  use_instead: method:bpco
assumptions:
- 'GRPO host. Paper: DeepSeekMath and Qwen 1.5B-7B, six benches; VinePPO dense-probe comparison.'
- 'NeurIPS 2026 workshop. No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:probe-po
recipes:
- recipe:probe-po
claims:
- benchmark: 'DeepSeekMath / Qwen 1.5B-7B, six benches; DeepSeekMath-7B vs VinePPO'
  metric: 'accuracy vs GRPO; wall-clock vs VinePPO'
  value: 'highest of four methods in 16/18 model-bench pairs; vs VinePPO higher on all six benches at 76% less e2e time'
  baseline: 'GRPO; VinePPO dense probes'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24515'
  notes: 'Reward-free uncertainty selector; GRPO-anchored shrinkage then segment redistribution. Does not replace CISPO or BPCO.'
tags:
- rl-alignment
- rlvr
- credit
- active
---

# ProbePO

## Method Overview
ProbePO spends a limited rollout budget on partial-solution prefixes selected by a reward-free uncertainty score, estimates their expected verifier reward, and redistributes GRPO advantage onto segments instead of broadcasting one group advantage to every token.

## When to Use
- Critic-free RLVR where full-trajectory GRPO credit is too coarse and dense VinePPO probes are too expensive.

## When NOT to Use
Pass@1 default → `method:cispo`. Learned critic → `method:bpco`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO or BPCO.

## Gotchas & Failure Modes
- Probe budget vs accuracy is the trade.
- Workshop paper.
