---
id: method:tetpo
type: method
title: TETPO (Target-ESS Tempered Policy Optimization)
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: variable environment latency / async stragglers
  reason: SAO remains the async first hop; TETPO tempers IS weights
  use_instead: method:sao
- when: single-turn dense math/code Pass@1 RLVR
  reason: CISPO remains Pass@1; TETPO is an IS-temper plug-in
  use_instead: method:cispo
assumptions:
- Off-policy or stale IS weights on a GRPO-family host. Paper uses k=32 avg@16.
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:tetpo
recipes:
- recipe:tetpo
claims:
- benchmark: k=32 avg@16 Table 1 (Qwen3-Base-1.7B; Llama-3.2-3B-Instruct)
  metric: avg@16 vs M2PO / GSPO / GEPO
  value: Qwen3-Base-1.7B 44.4 vs M2PO 42.3 / GSPO 39.0; Llama-3.2-3B-Instruct 18.5
    vs GEPO 16.2
  baseline: M2PO / GSPO / GEPO (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.14440
  notes: Does not retarget SAO or CISPO.
tags:
- post-training
- importance-sampling
- ess
- active
---

# TETPO (Target-ESS Tempered Policy Optimization)

## Method Overview
Replace ρ with ρ^α. Solve α each batch so the Kish ESS matches a target κ. Softer than a hard IS clip when weights are heavy-tailed.

## When to Use
- GRPO-family / PPO-style IS weights are unstable and you would rather hit an ESS target than clip.

## When NOT to Use
Async stragglers → `method:sao`. Dense Pass@1 → `method:cispo`. Coupled staleness TD → `method:copc`. Sampler-anchored KL least-squares → `method:klpo`.

## Relation to Existing SOTA
Active plug-in on `task:agentic-async-rl` (`sota_for: []`). Mention on `task:math-code-rl-dense`. Does **not** replace SAO or CISPO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Baselines are M2PO / GSPO / GEPO, not CISPO or SAO.
