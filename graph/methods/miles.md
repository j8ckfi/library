---
id: method:miles
type: method
title: "Miles v0.1"
category: "training-systems"
status: sota
sota_for:
  - task:frontier-rl-posttrain-stack
supersedes: []
do_not_use_for:
  - when: "factory process / experiments-as-code / lineage is the job"
    reason: "Miles is the RL post-train engine, not the industrial factory control plane"
    use_instead: "method:poolside-model-factory"
  - when: "async stragglers / tool-latency replay is the bottleneck"
    reason: "Miles ships fully async scheduling; SAO remains the async-algorithm default"
    use_instead: "method:sao"
  - when: "choosing the dense math/code Pass@1 loss"
    reason: "Miles is a stack; CISPO remains the Pass@1 kernel"
    use_instead: "method:cispo"
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Miles does not retarget Muon2"
    use_instead: "method:muon2"
  - when: "build a SWE / issue-to-patch harness rather than run post-training"
    reason: "mini-SWE-agent is the harness first hop"
    use_instead: "method:mini-swe-agent"
  - when: "outcome-only long-horizon agent RL (AppWorld coverage / anti-drift)"
    reason: "Coverage / anti-drift is CANOPY, not a production engine"
    use_instead: "method:canopy"
assumptions:
  - "Frontier MoE post-train with a split rollout/train fleet. Paper case study: GLM-5.2 744B-A40B on 64 GB300 (32/32), Megatron trainer, optimizer-state streaming to disk."
  - "SGLang rollouts; Megatron or FSDP trainer. LoRA RL is Megatron-only in v0.1."
  - "Does not replace the train-kernel defaults run inside the stack (CISPO, OPD, Muon2)."
last_reviewed: "2026-09-09"
papers:
  - paper:miles
recipes:
  - recipe:miles
claims:
  - benchmark: "GLM-5.2 744B-A40B Terminal-bench-2, 64x NVIDIA GB300"
    metric: "median training step time (first 30 measured steps)"
    value: "263 s"
    baseline: "step-0 warm-up 1042 s (clipped from the median)"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08368"
    notes: "Table 9 / Figure 5. 32 rollout + 32 train GPUs; TP2/PP4/CP4/EP8; BF16 train / FP8 serve; prefix-cache hit 96%."
  - benchmark: "Same GLM-5.2 100-step run"
    metric: "train–inference KL on sampled tokens"
    value: 0.0369
    baseline: "ends near its starting value over 100 steps"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08368"
    notes: "Figure 5(b). Truncated IS corrects remaining mismatch. Single run."
  - benchmark: "Same GLM-5.2 100-step run"
    metric: "raw task reward 9-step moving average"
    value: "0.438 → 0.556"
    baseline: "single-run observation; paper does not claim a measured improvement"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08368"
    notes: "Figure 5(c). Do not treat as a bake-off against SAO or CISPO."
tags:
  - systems
  - training-systems
  - post-training
  - agentic
  - miles
  - sota
---

# Miles v0.1

## Method Overview
Miles is a slime-descended **production post-training stack**, not a new RL kernel. SGLang generates multi-turn agentic trajectories (OpenEnv / Daytona sandboxes in the GLM-5.2 case study). A bounded buffer decouples generation from the trainer and drops groups that timed out, carry no advantage, or exceed a staleness limit. Sample-granularity async refill keeps engines near the in-flight cap. The trainer is Megatron or FSDP; objectives include GRPO-family RL, LoRA RL (adapter is the unit of work), OPD, SFT, and true-on-policy alignment. Optional R3 replays rollout expert assignments on MoE. Truncated IS corrects remaining train–rollout logp mismatch.

This does not replace CISPO, Muon2, Poolside factory, SAO, CANOPY, or mini-SWE-agent.

## When to Use
- Operating a frontier MoE post-train loop (rollout + train + weight sync) with public code.
- LoRA RL, OPD, SFT, or fully async agentic RL on the same engine.

## When NOT to Use
- Factory process → `method:poolside-model-factory`.
- Async-straggler algorithm → `method:sao`.
- Pass@1 loss → `method:cispo`. 7B optimizer → `method:muon2`.
- SWE harness → `method:mini-swe-agent`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
- First hop for `task:frontier-rl-posttrain-stack` only. Does **not** supersede `method:poolside-model-factory`, `method:sao`, `method:cispo`, `method:muon2`, `method:canopy`, or `method:mini-swe-agent`.
- Async scheduling here is an engine feature, not SAO's importance-corrected replay.

## Gotchas & Failure Modes
- GLM-5.2 reference run leaves R3 off; routing replay is a per-recipe choice and is expensive on long agentic sequences (~60MB routing tensor example in the paper).
- LoRA RL is Megatron-only in v0.1. P2P and disk-delta transports do not carry adapters.
- Single-run Terminal-bench-2 reward is not a competitive bake-off.
- Incomplete vision-language session support and partial weight-transfer coverage are stated limits.
