---
id: method:pact
type: method
title: "PACT (Policy Aligned Critic Training)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "multi-sample dense Pass@1 RLVR default"
    reason: "CISPO remains Pass@1; PACT is an actor-critic / credit-alignment recipe"
    use_instead: "method:cispo"
  - when: "single-sample critic baseline without Actor-then-Critic emphasis"
    reason: "BPCO remains token-level-critic-rl first hop"
    use_instead: "method:bpco"
  - when: "async tool stragglers / importance-corrected replay"
    reason: "SAO remains async first hop; PACT's SWE lift does not retarget SAO"
    use_instead: "method:sao"
  - when: "structural credit split for tool-call vs natural-language-summary tokens"
    reason: "PACT is Actor-then-Critic token credit; SLCA-GRPO routes GRPO segment advantages"
    use_instead: "task:tool-agent-segment-credit"
assumptions:
  - "Actor-then-Critic update order with importance-sampling correction on critic training. BCE critic loss instead of MSE."
  - "Paper: agentic math Avg@16 on Qwen3.5-4B; SWE-bench Verified on Qwen3.6-35B-A3B."
  - "GitHub AllSpark-Research/PACT empty stub as of 2026-09-24."
last_reviewed: "2026-09-24"
papers:
  - paper:pact
recipes:
  - recipe:pact
claims:
  - benchmark: "Agentic math Avg@16 (AIME 2025 / AIME 2026 / BeyondAIME / HMMT Nov. 2025)"
    metric: "average accuracy"
    value: "72.87%"
    baseline: "GRPO +8.80; PPO +13.16"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.26355"
    notes: "Abstract / Figure 1. Qwen3.5-4B with OpenCode. Not a CISPO Pass@1 retarget."
  - benchmark: "SWE-bench Verified, Qwen3.6-35B-A3B"
    metric: "pass@1"
    value: "67.4%"
    baseline: "GRPO +2.0; PPO +2.4; SAO +3.8"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.26355"
    notes: "Mention on the async shelf only. SAO remains the straggler first hop."
tags:
  - post-training
  - rl-alignment
  - actor-critic
  - credit-assignment
  - pact
  - active
---

# PACT (Policy Aligned Critic Training)

## Method Overview
Completeness, Prefix Consistency, and Neutrality uniquely determine token-level credit as the martingale difference \(C_i=V_i-V_{i-1}\). That representation explains why an ideal OPD teacher is an implicit critic and why RLOO's coarser signal still matches expected token-credit gradients. Approximate sparsity under bounded outcome rewards makes GAE critic lag dangerous: intermediate value error can rival the credit itself.

PACT therefore updates the actor first, then trains the critic with importance-sampling correction against the updated policy, using BCE instead of MSE. BPCO remains the single-sample critic first hop. CISPO remains Pass@1. SAO remains async stragglers.

## When to Use
- Single/few-sample actor-critic where critic lag after actor updates is the failure mode, and you want the axiomatic credit view plus Actor-then-Critic IS correction.

## When NOT to Use
- Dense Pass@1 default → `method:cispo`. Single-sample critic baseline without Actor-then-Critic emphasis → `method:bpco`. Async tool stragglers → `method:sao`.

## Relation to Existing SOTA
- Active on `task:token-level-critic-rl` beside BPCO. Mentions on `task:agentic-async-rl`, `task:math-code-rl-dense`, and `task:software-engineering-agent-harness`. Does **not** enter those tasks' `current_sota`. Does **not** supersede `method:bpco`, `method:cispo`, or `method:sao`.

## Gotchas & Failure Modes
- AllSpark-Research/PACT is an empty stub as of 2026-09-24. Reimplement Actor-then-Critic + critic IS; do not claim a trainer.
- SWE-Verified +3.8 vs SAO is evidence on the critic path, not an async-straggler retarget.
- Credit uniqueness needs all three axioms. Dropping Neutrality or Prefix Consistency admits other assignments.
