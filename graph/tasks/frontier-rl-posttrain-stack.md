---
id: task:frontier-rl-posttrain-stack
type: task
title: "Frontier RL Post-Training Stack"
domain: "systems"
summary: "Production full-stack engine for frontier post-training: SGLang rollouts, Megatron/FSDP trainer, LoRA RL, OPD, SFT, true-on-policy sync, and async agentic RL. Process/system shelf, not a train-kernel default."
scope: "Choosing and operating a production post-training stack (rollout engine, trainer backend, weight sync, LoRA RL / OPD / SFT / async agentic RL) at frontier MoE scale."
out_of_scope:
  - "Industrial factory process / experiments-as-code / lineage (Poolside)"
  - "Async straggler algorithm (SAO)"
  - "Dense math/code Pass@1 loss (CISPO)"
  - "~7B dense pretrain optimizer (Muon2)"
  - "SWE issue-to-patch harness (mini-SWE-agent)"
  - "AppWorld outcome-only coverage (CANOPY)"
redirects:
  - when: "factory process / experiments-as-code / lineage rather than the RL engine"
    to: "task:industrial-model-building"
  - when: "variable environment latency / async stragglers, not the production stack"
    to: "task:agentic-async-rl"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "build a SWE / issue-to-patch harness rather than run a post-train stack"
    to: "task:software-engineering-agent-harness"
  - when: "outcome-only long-horizon agent RL (coverage / anti-drift or rubric credit)"
    to: "task:outcome-only-long-horizon-agent-rl"
current_sota:
  - method: method:miles
    as_of: "2026-09-09"
    benchmark: "GLM-5.2 744B-A40B async agentic RL on Terminal-bench-2, 64x GB300"
    metric: "median step time / train-inference KL / raw reward moving average"
    value: "263s median (first 30 steps); KL mean 0.0369; reward 0.438→0.556 (single run)"
    notes: "Miles v0.1 (2609.08368). Process/system SOTA for the frontier post-train engine. Does not replace Poolside factory, SAO, CISPO, Muon2, or mini-SWE-agent. Reward rise is a single-run observation."
methods:
  - method:miles
  - method:poolside-model-factory
  - method:sao
  - method:cispo
  - method:mini-swe-agent
  - method:online-draft-cotrain
last_reviewed: "2026-09-09"
tags:
  - systems
  - training-systems
  - post-training
  - agentic
  - miles
---

# Frontier RL Post-Training Stack

## Problem Definition
Frontier post-training is a systems problem: multi-turn tool rollouts on trillion-scale MoE, trainer/rollout numerical mismatch, weight sync across colocated and disaggregated topologies, and several objectives (full-param RL, LoRA RL, OPD, SFT, true-on-policy) on one stack. This is not the factory process, not the async-straggler algorithm, and not the Pass@1 loss.

## Evaluation Protocol
- **Primary Benchmarks**: end-to-end step time, train–inference KL on sampled tokens, prefix-cache hit rate, and a documented agentic case study (Miles: GLM-5.2 744B-A40B, Terminal-bench-2, 64× GB300).
- **Evaluation Pitfalls**: Do not treat a single-run reward curve as a bake-off against SAO or CISPO. Do not retarget Poolside factory current_sota.

## SOTA Recommendation (as of 2026-09-09)
- **Primary Method**: **Miles v0.1** (`method:miles`, `paper:miles` `arXiv:2609.08368`). slime-descended; SGLang rollouts; Megatron or FSDP trainer. Code: radixark/miles.
- **Not This Task**: `method:poolside-model-factory` remains the factory process; `method:sao` remains async stragglers; `method:cispo` remains Pass@1; `method:muon2` remains the 7B optimizer; `method:mini-swe-agent` remains the SWE harness.
- **Optional long-context speculative draft path**: `method:online-draft-cotrain` (`arXiv:2609.07108`, NeMo RL). Niche systems. Does not replace Miles or Uno.
