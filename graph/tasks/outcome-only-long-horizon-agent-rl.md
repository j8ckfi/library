---
id: task:outcome-only-long-horizon-agent-rl
type: task
title: "Outcome-Only Long-Horizon Agent RL"
domain: "post-training"
summary: "Train a long-horizon interactive agent from sparse end-of-task verification (or, when no checker exists, from rubric credit) without denser step rewards, SFT priors, or multi-agent scaffolding."
scope: "Policy training for multi-turn agents judged only at episode end, where the failure modes are signal starvation (all-success / all-fail groups) and policy drift on a small revisited task pool. Includes the outcome-blind rubric variant when no programmatic checker exists."
out_of_scope:
  - "Async straggler / tool-latency RL (SAO)"
  - "Folding a long tool/web/SWE trajectory into a small active context (FoldGRPO)"
  - "Single-turn dense math/code RLVR (CISPO)"
  - "Building or choosing a SWE harness rather than training a policy (mini-SWE-agent)"
  - "Production harness kernel (omp2)"
redirects:
  - when: "variable environment latency / async stragglers, not sparse-outcome coverage"
    to: "task:agentic-async-rl"
  - when: "the problem is context folding of a long tool trajectory, not the RL signal"
    to: "task:long-horizon-tool-agent"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "build an agent loop rather than train a policy"
    to: "task:software-engineering-agent-harness"
  - when: "production engine (rewind, sandbox, remote, TUI)"
    to: "task:agent-harness-runtime"
last_reviewed: "2026-09-04"
current_sota:
  - method: method:canopy
    as_of: "2026-09-04"
    benchmark: "AppWorld Test-Normal / Test-Challenge TGC, Qwen3-14B (Feb 2026 leaderboard)"
    metric: "TGC mean@1"
    value: "86.9 / 67.6"
    notes: "CANOPY (2609.01245). Sparse outcome reward, n=32, KL-anchored on-policy. Does not replace SAO, FoldGRPO, CISPO, mini-swe-agent, or omp2-harness. DRACO is the outcome-blind rubric sibling, not a supersession."
methods:
  - method:canopy
  - method:draco
  - method:sao
  - method:foldgrpo
  - method:cispo
  - method:mini-swe-agent
tags:
  - post-training
  - agentic
  - outcome-only
  - long-horizon
  - canopy
  - draco
---

# Outcome-Only Long-Horizon Agent RL

## Problem Definition
Train a multi-turn interactive policy (AppWorld-style application operation, SWE repair, similar) when the only trustworthy label is end-of-episode verification — or, when no checker exists, a rubric scored once per trajectory. The typical failure of nearby methods is compensating around the policy (dense step rewards, SFT priors, skill libraries, orchestration) instead of restoring coverage and stopping drift.

Two siblings share this task and are not substitutes:
- **CANOPY**: programmatic checker exists; scale same-task exploration and KL-anchor so sparse outcome RL suffices.
- **DRACO**: no programmatic checker; dynamic rubrics plus closed-form step credit redistribution.

## Evaluation Protocol
- **Primary Benchmarks**: AppWorld TGC/SGC (Test-Normal, Test-Challenge); SWE-bench Verified resolve rate when transferring the same design principles; τ-bench for outcome-blind transfer.
- **Evaluation Pitfalls**: Do not mix training-free frontier harness numbers (HCL-GP / ASSAY) with trained-policy TGC. Do not treat AppWorld leaderboard wins as a reason to drop SAO for async training or mini-SWE-agent for the harness.

## SOTA Recommendation (as of 2026-09-04)
- **Primary Method (checker exists)**: **CANOPY** (`method:canopy`, `paper:canopy` `arXiv:2609.01245`).
- **Outcome-blind / no checker**: **DRACO** (`method:draco`, `paper:draco` `arXiv:2609.04094`). Active, does not replace CANOPY when a verifier exists.
- **Not This Task**: `method:sao` remains async-straggler RL; `method:foldgrpo` remains trajectory folding; `method:cispo` remains dense Pass@1; `method:mini-swe-agent` remains the harness; `method:omp2-harness` remains the production engine.
