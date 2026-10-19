---
id: method:mlexpert
type: method
title: 'MLExpert'
category: rl
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'asynchronous environment and tool-use RL (SAO)'
  reason: 'SAO remains async stragglers; MLExpert is WIRL on MLE trajectories'
  use_instead: method:sao
- when: 'outcome-only long-horizon agent RL (coverage / anti-drift)'
  reason: 'CANOPY remains AppWorld coverage; MLExpert is Kaggle-MLE'
  use_instead: method:canopy
assumptions:
- '35B MoE agentic model. Hierarchical agentic SFT then Windowed Interaction RL (WIRL) with async collection and policy correction. Code: InternScience/MLExpert.'
last_reviewed: '2026-10-19'
papers:
- paper:mlexpert
recipes:
- recipe:mlexpert
claims:
- benchmark: 'MLE-Bench Lite average medal rate vs base; NatureBench Lite / scaffold / algorithm opt'
  metric: 'average medal rate'
  value: '37.9%→72.7% on MLE-Bench Lite; comparable to larger Kimi-K3 / GLM-5.3 in the paper'
  baseline: 'base 35B MoE (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22344'
  notes: 'Does not retarget SAO. WIRL windows are successive experiment results, not SAO tool-latency.'
tags:
- mle
- agentic-rl
- wirl
- active
---

# MLExpert

## Method Overview
MLExpert post-trains a 35B MoE MLE agent with hierarchical agentic SFT, then Windowed Interaction RL that shares an outcome reward across the multi-turn decisions between successive experiment results, with asynchronous collection and policy correction.

## When to Use
- Autonomous MLE / Kaggle-style long-horizon experiment agents where each experiment's feedback covers several prior decisions.

## When NOT to Use
Async tool-latency default → `method:sao`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:agentic-async-rl` (`sota_for: []`). Does **not** replace SAO.

## Gotchas & Failure Modes
- MLE-Bench Lite medal rate is not SWE-bench or AppWorld TGC.
- WIRL is windowed outcome credit, not SAO straggler replay.
