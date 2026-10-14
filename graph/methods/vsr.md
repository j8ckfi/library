---
id: method:vsr
type: method
title: VSR (Variance-driven State Resampling)
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-turn dense math/code Pass@1 RLVR
  reason: CISPO remains Pass@1; VSR resamples prefixes inside a GRPO/GiGPO host
  use_instead: method:cispo
- when: adaptive sampling until ≥1 correct on math/code prompts
  reason: NGU keeps drawing a prompt until a correct rollout exists
  use_instead: method:ngu
- when: RLVR cold-start silent-group prompt prior
  reason: ThinkPrior is a zero-rollout Beta difficulty prior
  use_instead: method:thinkprior
assumptions:
- Access to prefix occupancy d(s) and residual variance σ(s). Paper uses a prefix
  replay buffer on GRPO / GiGPO hosts.
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:vsr
recipes:
- recipe:vsr
claims:
- benchmark: Qwen2.5-7B / Llama-3.2-3B math; Qwen2.5-1.5B BabyAI / Sokoban
  metric: score vs GRPO; GiGPO+VSR vs GiGPO
  value: Qwen2.5-7B 37.6 vs GRPO 36.1; Llama-3.2-3B 19.1 vs 15.4; BabyAI 47.6 vs 30.4;
    Sokoban 18.8 vs 12.7
  baseline: GRPO / GiGPO (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.15888
  notes: Distinct from NGU / ThinkPrior. Does not retarget CISPO or CANOPY.
tags:
- post-training
- rlvr
- resampling
- active
---

# VSR (Variance-driven State Resampling)

## Method Overview
Replay prefixes with Neyman allocation μ(s)∝d(s)σ(s) so high-occupancy, high-variance states get more samples. Plug-in on GRPO and GiGPO-style groups.

## When to Use
- Group RLVR wastes budget on low-variance prefixes and you can store a prefix buffer.

## When NOT to Use
Pass@1 loss → `method:cispo`. Until-correct sampling → `method:ngu`. Silent-group prior → `method:thinkprior`. Outcome-only AppWorld coverage → `method:canopy`. Per-state advantage shrinkage → `method:adastep`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Mention on `task:outcome-only-long-horizon-agent-rl`. Does **not** replace CISPO, NGU, ThinkPrior, or CANOPY.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Baselines are GRPO / GiGPO, not CISPO.
