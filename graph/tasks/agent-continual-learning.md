---
id: task:agent-continual-learning
type: task
title: "Agent Continual Learning"
domain: "post-training"
summary: "Stack heterogeneous agent capabilities across sequential post-training stages without catastrophic overwrite, measuring forgetting and transfer at model and token level."
scope: "Multi-stage agent post-training (math, tool-use, instruction following) where later stages forget earlier ones. First hop is ACLArena / Mixture of Low-Rank Experts. Not Pass@1, not async stragglers, not AppWorld TGC, not the production engine, not the SWE loop."
out_of_scope:
  - "Single-turn math/code Pass@1 RLVR (CISPO)"
  - "Async tool-latency / straggler RL (SAO)"
  - "AppWorld outcome-only coverage / anti-drift (CANOPY)"
  - "Production post-train engine (Miles)"
  - "GitHub issue → patch SWE harness (mini-SWE-agent)"
  - "Single-teacher text distillation default (OPD) or multi-teacher distill default (Open-MOPD) without a continual-learning curriculum"
redirects:
  - when: "single-turn math Pass@1"
    to: "task:math-code-rl-dense"
  - when: "async stragglers"
    to: "task:agentic-async-rl"
  - when: "outcome-only AppWorld"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "production engine"
    to: "task:frontier-rl-posttrain-stack"
  - when: "SWE issue-to-patch loop"
    to: "task:software-engineering-agent-harness"
current_sota:
  - method: method:aclarena
    as_of: "2026-09-23"
    benchmark: "ACLArena in-domain (AIME26 / NQ / τ³-Retail / IF-Eval) after Math→Search→E-commerce→IF"
    metric: "stage metrics vs Seq-Final / per-task oracles"
    value: "MLE AIME26 21.04, NQ 49.7, Retail 32.9, IF-Eval 85.0 vs Seq-Final 10.21 / 33.5 / 29.6 / 84.8"
    notes: "ACLArena (2609.23989). Active first hop. Method status active (not sota). Does not replace CISPO / SAO / CANOPY / Miles / mini-SWE-agent."
methods:
  - method:aclarena
  - method:cispo
  - method:sao
  - method:canopy
  - method:miles
  - method:mini-swe-agent
  - method:opd
  - method:open-mopd
last_reviewed: "2026-09-23"
tags:
  - post-training
  - agentic
  - continual-learning
  - aclarena
---

# Agent Continual Learning

## Problem Definition
Industrial agents acquire CoT reasoning, tool use, and instruction following in separate post-training stages. Sequential training forgets earlier peaks. This task is stacking those stages without overwrite, with a testbed that reports in-domain and OOD forgetting.

This is **not** Pass@1 math, not async stragglers, not AppWorld TGC, not the frontier engine, and not the SWE start loop.

## Evaluation Protocol
- **Primary Benchmarks**: ACLArena sequential Math → Search → E-commerce → IF, in-domain (AIME26, NQ, \(\tau^3\)-Retail, IF-Eval) and OOD (GPQA, MMLU, search hops, \(\tau^3\)-Telecom/Mock, IF-Bench).
- **Evaluation Pitfalls**: Do not treat Seq-Final as the method. Do not retarget CISPO, CANOPY, SAO, Miles, or mini-SWE-agent. Do not treat MMOPD numbers as an Open-MOPD supersession.

## SOTA Recommendation (as of 2026-09-23)
- **Primary Method (this task only)**: **ACLArena** (`method:aclarena`, `paper:aclarena` `arXiv:2609.23989`). Status `active`. Listed here as first hop; method `sota_for` stays empty. Offline replay of high-quality trajectories plus routed LoRA experts specialized via RL.
- **Not This Task**: `method:cispo` remains Pass@1; `method:sao` remains async; `method:canopy` remains AppWorld coverage; `method:miles` remains the engine; `method:mini-swe-agent` remains issue-to-patch; `method:opd` / `method:open-mopd` remain text distill defaults.
