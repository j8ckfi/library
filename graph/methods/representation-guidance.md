---
id: method:representation-guidance
type: method
title: Representation Guidance (RG)
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "Schedule-Free / LR decay instead of constant-LR EMA for large diffusion"
    reason: "RG remains pixel DiT first hop; Schedule-Free is the optimizer/EMA schedule"
    use_instead: "method:schedule-free-diffusion"
  - when: aligning text-to-image diffusion or flow models with rewards
    reason: RG is pixel-DiT pretrain; DiffusionOPSD / Self-OPD remain reward alignment
    use_instead: method:diffusion-opsd
  - when: continuous diffusion language model pretrain
    reason: SemiCat is text diffusion LM; RG is pixel-space image DiT
    use_instead: method:semicat
assumptions:
- 'Pixel-space DiT / flow matching. Paper: ImageNet-256/512 class-conditional; GenEval
  / DPG-Bench.'
- 'Code: Pan-Zihao/Representation-Guidance (code_status: released).'
last_reviewed: '2026-10-19'
papers:
  - paper:representation-guidance
  - paper:schedule-free-diffusion
recipes:
  - recipe:representation-guidance
claims:
- benchmark: ImageNet-256 XL/16 FID; ImageNet-512 FID; GenEval
  metric: FID / GenEval
  value: IN-256 FID 1.55; IN-512 FID 1.74; GenEval 0.89
  baseline: pixel DiT / flow matching without representation offset (paper suite)
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12978
  notes: L/16 1.79 FID at 459M; DPG-Bench 87.1. Does not retarget DiffusionOPSD.
tags:
- diffusion
- pretraining
- representation-guidance
- active
---

# Representation Guidance (RG)

## Method Overview
A pixel-space DiT predicts a low-dimensional bottleneck. That bottleneck's offset edits the flow-matching velocity target so representation structure guides pixel generation.

## When to Use
- Pixel-space image DiT / flow-matching pretrain (ImageNet class-conditional or GenEval-style T2I).

## When NOT to Use
Image/flow reward alignment → `method:diffusion-opsd`. Continuous text diffusion LM → `method:semicat`.

## Relation to Existing SOTA
Active first hop on `task:pixel-diffusion-pretrain` (`sota_for: []`). Does **not** replace DiffusionOPSD / Self-OPD.

## Gotchas & Failure Modes
- **code: released** Pan-Zihao/Representation-Guidance as of 2026-10-13.
- Pixel-space, not latent-DiT (SD3/FLUX) by default.
- Reward alignment remains a different task.
