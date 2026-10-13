---
id: task:pixel-diffusion-pretrain
type: task
title: Pixel-Space Diffusion Transformer Pretraining
domain: diffusion
summary: Pretrain a pixel-space diffusion / flow-matching transformer for class-conditional
  or text-to-image generation, including representation bottlenecks that edit the
  flow target.
scope: Pixel-space DiT / flow-matching image pretrain (ImageNet FID, GenEval). First
  hop is Representation Guidance. Not image/flow reward alignment, not continuous
  text diffusion LMs, not discrete dLLM recycle.
out_of_scope:
- Text-to-image / flow reward alignment (DiffusionOPSD / Self-OPD)
- Continuous diffusion language model pretrain (SemiCat)
- Discrete dLLM AR-delta recycle (A2D)
- Video reward models / RGPO (RewardVerse)
redirects:
- when: aligning text-to-image diffusion or flow models with rewards
  to: task:posttrain-diffusion
- when: continuous diffusion language model pretrain (not pixel DiT)
  to: task:continuous-diffusion-lm-pretrain
- when: recycle an AR post-training weight delta onto a converted dLLM
  to: task:diffusion-lm-ar-delta-recycle
current_sota:
- method: method:representation-guidance
  as_of: '2026-10-13'
  benchmark: ImageNet-256 XL/16 FID; ImageNet-512 FID; GenEval
  metric: FID / GenEval
  value: IN-256 FID 1.55; IN-512 FID 1.74; GenEval 0.89
  notes: Representation Guidance (2610.12978). Method status active. Listed here as
    first hop; method sota_for stays empty. Does not replace DiffusionOPSD / Self-OPD.
methods:
- method:representation-guidance
- method:diffusion-opsd
- method:self-opd
- method:semicat
last_reviewed: '2026-10-13'
tags:
- diffusion
- pretraining
- pixel-dit
- representation-guidance
---

# Pixel-Space Diffusion Transformer Pretraining

## Problem Definition
Train a pixel-space diffusion or flow-matching transformer for images. This task owns representation bottlenecks that edit the flow target (RG). It is not reward alignment and not a text diffusion LM.

## Evaluation Protocol
- **Primary Benchmarks**: ImageNet-256 / 512 FID; GenEval; DPG-Bench.
- **Evaluation Pitfalls**: Do not cite DiffusionOPSD reward-alignment numbers as pixel-DiT pretrain. Pixel-space ≠ latent SD3/FLUX.

## SOTA Recommendation (as of 2026-10-13)
- **Primary (this task only)**: **Representation Guidance** (`method:representation-guidance`, `paper:representation-guidance` `arXiv:2610.12978`). Status `active`. Method `sota_for` stays empty. Code Pan-Zihao/Representation-Guidance.
- **Not This Task**: `method:diffusion-opsd` / `method:self-opd` remain image/flow post-train; `method:semicat` remains continuous text diffusion LM.
