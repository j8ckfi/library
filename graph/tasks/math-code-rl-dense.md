---
id: task:math-code-rl-dense
type: task
title: "Mathematical and Code RL Reasoning (Dense Policies)"
domain: "post-training"
summary: "Reinforcement learning on verifiable mathematical and coding tasks using dense transformer policies."
scope: "Single-turn (or short-CoT) dense math/code RLVR with a programmatic verifier. Pass@1 default is CISPO."
out_of_scope:
  - "Long-horizon interactive agents judged only at episode end (CANOPY / DRACO)"
  - "Async tool-latency RL (SAO)"
redirects:
  - when: "outcome-only long-horizon interactive agent RL"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "train asynchronous RL for a tool-use policy"
    to: "task:agentic-async-rl"
current_sota:
  - method: method:cispo
    as_of: "2026-08-26"
    benchmark: "MATH-500 / AIME 2024 / LiveCodeBench"
    metric: "pass@1 accuracy & training stability"
    value: "Default SOTA for Dense RL"
    notes: "CISPO via MiniMax-M1 (2506.13585) + ScaleRL (2510.13786)."
methods:
  - method:cispo
  - method:es-reasoning
  - method:bpco
  - method:dapo
  - method:sspo
  - method:minpro
  - method:dr-grpo
  - method:grpo
  - method:gmts
  - method:diem
  - method:cliff
  - method:self-routing
  - method:opsa
last_reviewed: "2026-09-04"
tags:
  - post-training
  - reasoning
  - math
  - code
  - cispo
---

# Mathematical and Code RL Reasoning (Dense Policies)

## Problem Definition
Training dense language models to generate long chains of thought (CoT) and verifiable solutions for competitive math and coding problems.

## SOTA Recommendation (as of 2026-09-04)
- **Primary Method (Pass@1 labeled RLVR)**: **CISPO** (`method:cispo`, MiniMax-M1 2506.13585 + ScaleRL 2510.13786). Unchanged.
- **Systems Reference**: DAPO stays as systems paper reference. GRPO stays retired.
- **Related alternative (Pass@K / coverage / no-backward)**: `method:es-reasoning` (`arXiv:2608.27351`). Do not swap CISPO for ES or revive GRPO when the goal is Pass@1.
- **Optional token-filter plug-in**: `method:gmts` (`arXiv:2608.30632`) when using GRPO/DAPO/CISPO-family token truncation. Does not replace CISPO.
- **Optional example-reweight plug-in**: `method:diem` (`arXiv:2608.29252`) gradient-alignment batch reweight. Does not replace CISPO.
- **Optional first-mistake process credit**: `method:cliff` (`arXiv:2609.02817`). Active plug-in, not a PRM, not a CISPO replacement. VeriGate remains the gated-PRM default.
- **Optional sample-level recipe router**: `method:self-routing` (`arXiv:2609.01422`) GRPO / OPSD / REG / skip from rollout correctness+confidence. Does not replace CISPO or OPSA.
- **No labels / no teacher**: `method:opsa` on `task:teacher-free-on-policy-self-adaptation`. Does not replace CISPO when labels exist.
- **Gotcha**: group-relative magnitude can reward lucky guesses on bounded-answer / search-agent settings (`paper:spurious-advantage-grpo`). Do not promote SignBalance over CISPO.
