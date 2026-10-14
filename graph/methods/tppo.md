---
id: method:tppo
type: method
title: TPPO (Tracking-Value PPO)
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: token-level advantages from 1 sample/prompt with DPPO / bounded value / GAE
  reason: BPCO remains the single-sample critic first hop
  use_instead: method:bpco
- when: Actor-then-Critic IS-aligned critic after axiomatic token credit
  reason: PACT remains the Actor-then-Critic hop
  use_instead: method:pact
assumptions:
- PPO-style actor-critic on dense math. Paper: Qwen3-4B/8B-Base.
- Official repo LINs-lab/TPPO as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:tppo
recipes:
- recipe:tppo
claims:
- benchmark: Qwen3-4B/8B-Base math vs PPO
  metric: math score delta vs PPO
  value: 41.6 vs 34.6 (+7.0) at 4B; 45.9 vs 37.5 (+8.4) at 8B
  baseline: PPO (single-paper; not BPCO / CISPO)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.16794
  notes: HF Daily 2026-10-14. Does not retarget BPCO, PACT, or CISPO.
tags:
- post-training
- actor-critic
- ppo
- active
---

# TPPO (Tracking-Value PPO)

## Method Overview
Replace the scalar value head with a cumulative log-odds tracker so advantages stay on the same scale as token odds. Drop-in on a PPO host.

## When to Use
- Single-sample PPO critic is drifting on long CoT and you want a log-odds parameterization.

## When NOT to Use
BPCO recipe → `method:bpco`. Actor-then-Critic IS → `method:pact`. Dense Pass@1 group-relative → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:token-level-critic-rl` (`sota_for: []`). Does **not** replace BPCO or PACT.

## Gotchas & Failure Modes
- Baseline is PPO, not BPCO.
- Do not confuse with `method:pact` (Actor-then-Critic). Slug `tppo` is Tracking-Value PPO.
