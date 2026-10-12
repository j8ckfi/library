---
id: method:cbpo
type: method
title: CBPO
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-turn dense math/code Pass@1 RLVR
  reason: CISPO remains Pass@1; CBPO unifies SFT/RL sources under one regression target
  use_instead: method:cispo
- when: cancellation-aware off-policy response mask (absolute token log-ratios)
  reason: CARM is a sequence mask; CBPO is a shared regression target across behaviors
  use_instead: method:carm
assumptions:
- 'Math reasoning post-train with offline demos plus on/off-policy rollouts. Paper: two model scales,
  four math benches, avg@32 / pass@32.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:cbpo
recipes:
- recipe:cbpo
claims:
- benchmark: Four mathematical reasoning benchmarks, Qwen3-1.7B, avg@32 / pass@32
  metric: benchmark-averaged avg@32 and pass@32 vs SFT then DAPO
  value: CBPO-Unified +2.33 avg@32 / +4.44 pass@32; replay of historical rollouts +1.87 / +3.72 vs no-history
  baseline: SFT then DAPO; CBPO without historical replay
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12830
  notes: Does not retarget CISPO. DAPO is a paper baseline, not library SOTA.
tags:
- post-training
- rlvr
- cbpo
- active
---

# CBPO

## Method Overview
Label every response with a reward against a fixed reference. Regress. Mix offline gold, negatives, live rollouts, and replay in one buffer. Do not change the loss when a new source arrives.

## When to Use
- You have offline demos and on/off-policy rollouts and do not want a two-objective SFT→RL split.

## When NOT to Use
Pass@1 default → `method:cispo`. Off-policy sequence mask → `method:carm`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Headline vs SFT+DAPO, not CISPO.
- Fixed reference is load-bearing; a moving reference reintroduces the two-objective split.
