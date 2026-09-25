---
id: task:tool-agent-segment-credit
type: task
title: "Tool-Agent Segment Credit Assignment"
domain: "post-training"
summary: "Structural credit split for heterogeneous tool-call vs natural-language-summary trajectories under on-policy RL, so summary-gradient does not leak into tool-decision tokens."
scope: "On-policy RL credit routing along the structural axis (execution vs articulation) inside one tool-calling trajectory. Not context folding, not async stragglers, not Actor-then-Critic token credit, not which-turn trainability diagnostics, not single-turn math Pass@1."
out_of_scope:
  - "Context folding of a long tool trajectory (FoldGRPO)"
  - "Async straggler replay (SAO)"
  - "Actor-then-Critic IS token credit (PACT)"
  - "Which multi-turn call is trainable (Critical-State RL)"
  - "Single-turn math/code Pass@1 RLVR (CISPO)"
redirects:
  - when: "context folding of a long tool trajectory"
    to: "task:long-horizon-tool-agent"
  - when: "variable environment latency / async stragglers"
    to: "task:agentic-async-rl"
  - when: "Actor-then-Critic IS-aligned critic after axiomatic token credit"
    to: "method:pact"
  - when: "diagnose which multi-turn tool calls are trainable (nested sampling / contextual bandit)"
    to: "method:critical-state-rl"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
current_sota:
  - method: method:slca-grpo
    as_of: "2026-09-25"
    benchmark: "Toucan-Test Success@0.9 / BFCL V3 / tau2-Bench, Qwen2.5-7B-Instruct"
    metric: "mean vs matched GRPO"
    value: "+2.53 pp / +1.36 pp / +9.15 pp"
    notes: "SLCA-GRPO (2609.29050). Method status active. Does not replace FoldGRPO, SAO, PACT, Critical-State RL, or CISPO."
methods:
  - method:slca-grpo
  - method:foldgrpo
  - method:sao
  - method:pact
  - method:critical-state-rl
  - method:cispo
last_reviewed: "2026-09-25"
tags:
  - post-training
  - agentic
  - credit-assignment
  - tool-use
  - slca-grpo
---

# Tool-Agent Segment Credit Assignment

## Problem Definition
Tool-calling rollouts mix structured tool invocations with a user-facing natural-language summary. Standard GRPO broadcasts one trajectory advantage to every token, so summary-reward variation leaks into tool-decision tokens (cross-segment credit misattribution). This task owns the **structural** split (execution vs articulation) under on-policy RL, not temporal credit, not folding, not async stragglers.

## Evaluation Protocol
- **Primary Benchmarks**: in-domain Toucan-Test Success@0.9, BFCL (schema generalization), \(\tau^2\)-Bench (long-horizon collaboration).
- **Evaluation Pitfalls**: Do not treat a FoldGRPO folding lift, a SAO straggler lift, or a CISPO Pass@1 number as this task. Matched comparisons must share simulator, HierR (or equivalent segment rewards), and group size.

## SOTA Recommendation (as of 2026-09-25)
- **Primary Method (this task only)**: **SLCA-GRPO** (`method:slca-grpo`, `paper:slca-grpo` `arXiv:2609.29050`). Status `active`. Listed here as first hop; method `sota_for` stays empty.
- **Not This Task**: `method:foldgrpo` remains folding; `method:sao` remains async stragglers; `method:pact` remains Actor-then-Critic token credit; `method:critical-state-rl` remains which-turn trainability; `method:cispo` remains Pass@1.
