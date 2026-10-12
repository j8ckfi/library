---
id: method:ppo-fp16
type: method
title: PPO-FP16
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: sample-efficient latent world-model continuous control
  reason: EfficientTDMPC remains that hop; PPO-FP16 is half-precision on-policy PPO
  use_instead: method:efficienttdmpc
- when: single-turn dense math/code Pass@1 RLVR
  reason: This paper is continuous-control PPO, not LLM RLVR
  use_instead: method:cispo
- when: full-pipeline FP8 RL entropy surge / calibrated clip bounds
  reason: Calibrated Clipping is LLM FP8 RL; PPO-FP16 is control-task FP16 PPO
  use_instead: method:fp8-calibrated-clipping
assumptions:
- 'On-policy PPO on commodity GPUs for continuous control. Paper: six tasks, five seeds. Not an LLM trainer.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:ppo-fp16
recipes:
- recipe:ppo-fp16
claims:
- benchmark: Six continuous-control tasks, five seeds, FP16 PPO vs FP32 Adam and naive FP16
  metric: mean return-AUC rank; PPO update speedup; optimizer-state / peak GPU memory vs FP32 Adam
  value: lowest mean return-AUC rank 1.90; first in 17/30 env-seed comparisons; 1.16–2.03× PPO update;
    optimizer state −71.7–74.9%; peak GPU mem up to −44.5%
  baseline: Full FP32 Adam; naive FP16 PPO
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13306
  notes: Control PPO, not LLM RL. Does not retarget EfficientTDMPC or CISPO.
tags:
- control
- ppo
- fp16
- ppo-fp16
- active
---

# PPO-FP16

## Method Overview
Keep PPO. Store and compare the tiny current-vs-behavior residual in higher precision. Protect batch-shared statistics and optimizer writeback. Do not dump the whole trainer into FP16.

## When to Use
- On-policy continuous-control PPO on commodity GPUs where optimizer state is the memory tax.

## When NOT to Use
World-model control default → `method:efficienttdmpc`. LLM Pass@1 → `method:cispo`. LLM FP8 clip → `method:fp8-calibrated-clipping`.

## Relation to Existing SOTA
Active plug-in on `task:continuous-control-world-model` (`sota_for: []`). Does **not** replace EfficientTDMPC. Not an LLM method.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Not LLM RL. Do not wire this to CISPO/Miles.
- Naive FP16 without residual protection is the failure mode the paper measures.
