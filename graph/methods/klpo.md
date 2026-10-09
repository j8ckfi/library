---
id: method:klpo
type: method
title: "KLPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "async straggler algorithm / importance-corrected replay"
    reason: "SAO remains the async-algorithm default; KLPO is a sampler-anchored update"
    use_instead: "method:sao"
  - when: "critic-free PMD / Bellman telescoping RLVR on dense Pass@1"
    reason: "BPO is a dense RLVR candidate; KLPO targets stale-sampler async trajectories"
    use_instead: "method:bpo"
  - when: "dense math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Rollouts come from a stale sampler / inference engine. One trajectory per prompt is enough."
  - "Code: yifanzhang-pro/KLPO (`code_status: released`)." 
last_reviewed: "2026-10-09"
papers:
  - paper:klpo
recipes:
  - recipe:klpo
claims:
  - benchmark: "Asynchronous LLM RL with stale sampler trajectories"
    metric: "whether an IS-clip-free one-rollout update exists"
    value: "sampler-anchored KL least-squares; no importance weights; one rollout per prompt; critic-free even under stochastic tools"
    baseline: "clipped IS / GRPO groups"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.08963"
    notes: "Abstract has no numeric bake-off table. Does not retarget SAO or CISPO." 
tags:
  - post-training
  - async-rl
  - klpo
  - active
---

# KLPO

## Method Overview
Anchor the KL regularizer at the sampler policy that generated the trajectory. Fit the log-ratio optimality condition by least squares on those trajectories. The sampler probability enters through a log-ratio, so you do not clip or weight an importance ratio. One rollout per prompt.

## When to Use
- Async or off-engine RL where IS clipping biases the update and group rollouts are too expensive.

## When NOT to Use
- Async straggler replay default -> `method:sao`. Dense Pass@1 -> `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:agentic-async-rl` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace SAO.

## Gotchas & Failure Modes
- **code: released** yifanzhang-pro/KLPO as of 2026-10-09.
- Abstract has no numeric bake-off. Profile out the regression intercept; do not drop the sampler-to-trainer KL term.
