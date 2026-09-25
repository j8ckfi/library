---
id: task:token-level-critic-rl
type: task
title: "Token-Level Advantage Estimation with Single-Sample Critics"
domain: "post-training"
summary: "Stabilizing single-response actor-critic reinforcement learning for LLMs with token-level advantage estimation without group sampling."
current_sota:
  - method: method:bpco
    as_of: "2026-08-27"
    benchmark: "Mathematical Reasoning & Rubric Evaluation (1.5B to 30B-A3B)"
    metric: "sample efficiency & accuracy at 1 sample/prompt"
    value: "Matches or exceeds group-relative GRPO baseline with 1 response per prompt"
    notes: "BPCO (2608.23566) actor-critic recipe with DPPO, bounded value head, MC targets, and length-adaptive GAE."
methods:
  - method:bpco
  - method:pact
  - method:sao
  - method:grpo
  - method:dapo
  - method:dr-grpo
  - method:slca-grpo
redirects:
  - when: "Actor-then-Critic IS-aligned critic after axiomatic token credit"
    to: "method:pact"
  - when: "structural credit split for tool-call vs natural-language-summary tokens (not Actor-then-Critic)"
    to: "task:tool-agent-segment-credit"
last_reviewed: "2026-09-25"
tags:
  - post-training
  - rl-alignment
  - actor-critic
---

# Token-Level Advantage Estimation with Single-Sample Critics

## Problem Definition
Reinforcement learning alignment often relies on group-relative comparisons (such as GRPO) to circumvent training a value model, which requires generating 8 to 16 samples per prompt. Critic-based optimization enables single-response training with dense per-token advantages, but standard PPO implementations suffer from value unboundedness, normalization drift, and horizon mismatch.

## SOTA Recommendation (as of 2026-08-27)
- **Primary Method**: **BPCO** (`method:bpco`, `paper:bpco` `arXiv:2608.23566`) for robust single-sample actor-critic training with DPPO and bounded value heads.
- **Active Actor-then-Critic IS plug-in (not this first hop)**: `method:pact` (`arXiv:2609.26355`) axiomatic token credit then Actor-then-Critic with IS on the critic. Agentic-math avg 72.87%; SWE-Verified 67.4% (+3.8 SAO) is mention-only. Empty GitHub stub. Does not replace BPCO, CISPO, or SAO.
- **Not this task (structural tool/summary GRPO credit)**: `method:slca-grpo` on `task:tool-agent-segment-credit`. Does not replace BPCO or PACT.
