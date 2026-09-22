---
id: task:harness-distillation
type: task
title: "Harness Distillation"
domain: "agents"
summary: "Distill behaviors induced by an optimized agent harness into model weights so the gains survive under a single fixed target harness when source and target action spaces differ."
scope: "Training-time guidance from a domain- or instance-optimized harness, mapped into the target harness action space (agent-as-harness), then SFT so the specialized harness can be removed at deploy. First hop is Harness-Zero. Not a production kernel, not routing-harness RSI post-train, not plain OPD, not the SWE loop, not async RL."
out_of_scope:
  - "Production harness kernel (rewind, sandbox, remote, TUI / omp²)"
  - "Routing-harness RSI post-train of model weights (NeoHorse-1)"
  - "Single-teacher text distillation / sampled reverse-KL OPD"
  - "GitHub issue → patch SWE harness (mini-SWE-agent)"
  - "Async tool-latency / straggler RL (SAO)"
  - "AppWorld outcome-only coverage / anti-drift (CANOPY)"
redirects:
  - when: "production kernel (rewind, sandbox, remote, TUI)"
    to: "task:agent-harness-runtime"
  - when: "routing RSI post-train"
    to: "task:agentic-rsi-routing-posttrain"
  - when: "plain OPD"
    to: "task:student-distillation"
  - when: "issue-to-patch"
    to: "task:software-engineering-agent-harness"
  - when: "async RL"
    to: "task:agentic-async-rl"
current_sota:
  - method: method:harness-zero
    as_of: "2026-09-22"
    benchmark: "Qwen3.5-9B macro success (SpreadsheetBench / AppWorld / USPTO), specialized harness removed"
    metric: "macro-average task success"
    value: "23.3% → 44.3% (vs 41.7% with evolved harness still attached)"
    notes: "Harness-Zero (2609.24974). Active first hop. Method status active (not sota). Does not replace omp2 / NeoHorse-1 / OPD / Open-MOPD / SAO / CANOPY."
methods:
  - method:harness-zero
  - method:omp2-harness
  - method:neohorse-1
  - method:opd
  - method:open-mopd
  - method:mini-swe-agent
  - method:sao
  - method:canopy
  - method:rrsi
  - method:harness-onpolicy-correction
last_reviewed: "2026-09-22"
tags:
  - agents
  - agent-harness
  - distillation
  - harness-zero
---

# Harness Distillation

## Problem Definition
An optimized harness can raise agent success, but those gains stay tied to the harness at deployment. The best harness also varies by domain, instance, and model. This task is transferring the **behaviors the optimized harness induces** into weights so they survive under one fixed target harness. Source and target harnesses typically differ in action space and available information, so optimized-harness trajectories are not valid imitation targets.

This is **not** the production kernel, not routing-guided OPD, not plain text OPD, not the SWE start loop, and not async RL.

## Evaluation Protocol
- **Primary Benchmarks**: SpreadsheetBench Verified, AppWorld, USPTO Retrosynthesis after removing the specialized harness; frontier agent-as-harness vs code-as-harness without training.
- **Evaluation Pitfalls**: Do not treat AppWorld distillation numbers as CANOPY TGC. Do not retarget mini-SWE-agent from using it as the *target* harness \(h\). Do not treat this as OPD.

## SOTA Recommendation (as of 2026-09-22)
- **Primary Method (this task only)**: **Harness-Zero** (`method:harness-zero`, `paper:harness-zero` `arXiv:2609.24974`). Status `active`. Listed here as first hop; method `sota_for` stays empty. Agent-as-harness corrects student replies into the target action space, then SFT; drop the specialized harness at deploy.
- **Not This Task**: `method:omp2-harness` remains the production kernel; `method:neohorse-1` remains routing-harness RSI post-train; `method:opd` / `method:open-mopd` remain text distill; `method:mini-swe-agent` remains issue-to-patch; `method:sao` remains async; `method:canopy` remains AppWorld coverage. Regularized harness search with a frozen backbone is `method:rrsi` on `task:agent-harness-runtime`.
