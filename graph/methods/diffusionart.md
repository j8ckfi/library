---
id: method:diffusionart
type: method
title: DiffusionART
category: diffusion-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: on-policy self-distillation with bounded intermediate clean-output targets (images)
  reason: DiffusionOPSD remains that hop; DiffusionART is aggregation-first reverse-process RL
  use_instead: method:diffusion-opsd
- when: teacher-free flow matching multi-objective alignment
  reason: Self-OPD remains teacher-free flow alignment
  use_instead: method:self-opd
- when: flow-model RL via proximal velocity matching (~100 updates vs Flow-GRPO ~4k)
  reason: MEND is velocity matching; DiffusionART is reward-tilting reverse-process RL
  use_instead: method:mend
assumptions:
- 'Image/video diffusion or flow with a black-box reward. Paper: HunyuanVideo-13B visual+motion rewards.'
- 'Code: vanzll/DiffusionART (code_status: released).'
last_reviewed: '2026-10-12'
papers:
- paper:diffusionart
recipes:
- recipe:diffusionart
claims:
- benchmark: HunyuanVideo-13B, equally weighted visual and motion quality rewards
  metric: GPU-hours to late-stage mean reward of DiffusionNFT / Flow-GRPO-Fast
  value: 12.02× / 11.72× fewer GPU-hrs; 28.8% / 53.0% higher mean training rewards
  baseline: DiffusionNFT; Flow-GRPO-Fast
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12572
  notes: Does not retarget DiffusionOPSD or Self-OPD. No CISPO/OPD bake-off.
tags:
- diffusion
- post-training
- diffusionart
- active
---

# DiffusionART

## Method Overview
Aggregate a prompt group's rewards into one reward-improving direction applied to reverse-process states. Mask a second restoration update with a trust region instead of an EMA teacher. Keep the original denoiser; no reward-model Jacobian.

## When to Use
- Black-box image/video diffusion RL where Flow-GRPO-Fast or DiffusionNFT GPU-hrs dominate, and you can group samples per prompt.

## When NOT to Use
Image OPSD targets → `method:diffusion-opsd`. Teacher-free flow multi-objective → `method:self-opd`. Proximal velocity matching → `method:mend`.

## Relation to Existing SOTA
Active plug-in on `task:posttrain-diffusion` beside `method:mend` / Flow-GRPO / DiffusionNFT (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace DiffusionOPSD or Self-OPD.

## Gotchas & Failure Modes
- **code: released** vanzll/DiffusionART as of 2026-10-12.
- Paper numbers are vs DiffusionNFT / Flow-GRPO-Fast, not vs DiffusionOPSD.
- Fewer samples per prompt is a claimed feature; do not drop grouping entirely.
