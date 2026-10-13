---
id: method:d2r
type: method
title: D2R (Dream to Remember)
category: servo-control
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: sample-efficient model-based RL / latent world-model planning from scratch
  reason: EfficientTDMPC remains the world-model control default; D2R steers a frozen
    policy
  use_instead: method:efficienttdmpc
- when: structure-aware numerical stabilization for half-precision PPO (control, not
    LLM)
  reason: PPO-FP16 is residual-protected FP16 PPO, not imagination rehearsal
  use_instead: method:ppo-fp16
assumptions:
- 'Frozen generalist robot policy plus a world model. Paper: CALVIN 8 tasks.'
- No public code as of 2026-10-13.
last_reviewed: '2026-10-13'
papers:
- paper:d2r
recipes:
- recipe:d2r
claims:
- benchmark: CALVIN 8 tasks, frozen-policy continual steering
  metric: success rate
  value: 63.7%→74.8% vs LoRA FT 11.7%
  baseline: frozen policy; LoRA fine-tune
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13816
  notes: Imagination rehearsal, not replay. Does not retarget EfficientTDMPC.
tags:
- control
- world-models
- d2r
- active
---

# D2R (Dream to Remember)

## Method Overview
Keep the robot policy frozen. Train a small steering adapter with continual RL. Rehearse prior tasks in a learned world model instead of a replay buffer.

## When to Use
- A deployed generalist policy must pick up new skills without LoRA overwrite, and a world model is available for imagination.

## When NOT to Use
World-model planning from scratch → `method:efficienttdmpc`. Half-precision control PPO → `method:ppo-fp16`.

## Relation to Existing SOTA
Active plug-in on `task:continuous-control-world-model` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace EfficientTDMPC.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-13.
- LoRA FT 11.7% is this paper's overwrite baseline, not a library LoRA default.
- Imagination quality bounds what can be retained; garbage world model, garbage rehearsal.
