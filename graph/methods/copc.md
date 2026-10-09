---
id: method:copc
type: method
title: "COPC"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "async straggler algorithm / importance-corrected replay"
    reason: "SAO remains the async-algorithm default; COPC couples actor IS with advantage-side TD correction"
    use_instead: "method:sao"
  - when: "sampler-anchored KL least-squares without a critic"
    reason: "KLPO is critic-free one-rollout; COPC is actor-critic with TD residuals"
    use_instead: "method:klpo"
  - when: "dense math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Actor-critic async RL with TD residuals. Paper: tool-integrated math and search; staleness up to 64 steps."
  - "No official GitHub as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:copc
recipes:
  - recipe:copc
claims:
  - benchmark: "Async LLM RL, tool-integrated math and search, up to 64-step staleness"
    metric: "task success and step-time vs async PPO / sync PPO"
    value: "highest reported in-paper async baselines; stable at 64-step staleness; 1.7x step-time vs sync PPO"
    baseline: "policy-side IS correction alone / async PPO"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.09597"
    notes: "Does not retarget SAO. Policy-side and advantage-side HPs must be swept jointly." 
tags:
  - post-training
  - async-rl
  - off-policy
  - copc
  - active
---

# COPC

## Method Overview
Correct the actor with token-level ratio masking and simultaneously reweight TD residuals with a two-sided clipped importance ratio when estimating returns and advantages. Policy-side and advantage-side errors multiply; sweeping only one HP can reverse the other.

## When to Use
- Async actor-critic LLM RL where advantages stay wrong after actor IS correction, including long-staleness search.

## When NOT to Use
- Async straggler default -> `method:sao`. Critic-free sampler-anchored update -> `method:klpo`.

## Relation to Existing SOTA
- Active plug-in on `task:agentic-async-rl` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace SAO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-09.
- Sweep policy-mask and advantage-clip jointly; they are not separable.
