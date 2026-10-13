---
id: task:continuous-diffusion-lm-pretrain
type: task
title: Continuous Diffusion Language Model Pretraining
domain: diffusion
summary: Pretrain a continuous (Gaussian/interpolant) diffusion language model rather
  than a discrete masked/absorbing dLLM, including train/inference self-conditioning
  fixes.
scope: Continuous diffusion LM design space and pretrain (self-conditioning, DoubleCat
  interpolant, SemiCat discrete reveals). First hop is SemiCat. Not discrete-dLLM
  AR-delta recycle, not discrete canvas RL, not image/flow reward alignment.
out_of_scope:
- AR post-training delta recycle onto a converted discrete dLLM (A2D)
- Discrete DLM curriculum RL (CanvasAnneal)
- Text-to-image / flow reward alignment (DiffusionOPSD / Self-OPD)
- Lossless multi-token / diffusion-augmented AR serving (Uno)
redirects:
- when: discrete-dLLM AR-delta recycle / converted absorbing or masked dLLM, not continuous
    pretrain
  to: task:diffusion-lm-ar-delta-recycle
- when: curriculum RL for a discrete diffusion LM (canvas anneal)
  to: method:canvasanneal
- when: aligning text-to-image diffusion or flow models with rewards
  to: task:posttrain-diffusion
- when: lossless multi-token / diffusion-augmented AR serving
  to: task:diffusion-augmented-ar
current_sota:
- method: method:semicat
  as_of: '2026-10-13'
  benchmark: TinyGSM; 1.7B likelihood evals vs discrete diffusion
  metric: TinyGSM accuracy; win count on 6 likelihood evals
  value: SemiCat 49.94% TinyGSM (tuned sampler); 1.7B beats discrete diffusion on
    4/6 likelihood evals
  notes: SemiCat/DoubleCat (2610.13834). Method status active. Experimental evidence
    (design-space, not a 7B bake-off). Method sota_for stays empty. Does not replace
    A2D or CanvasAnneal.
methods:
- method:semicat
- method:a2d
- method:canvasanneal
- method:diffusion-opsd
- method:self-opd
- method:uno
last_reviewed: '2026-10-13'
tags:
- diffusion
- pretraining
- dllm
- semicat
---

# Continuous Diffusion Language Model Pretraining

## Problem Definition
A continuous diffusion LM denoises Gaussian/interpolant latents over tokens. Train and inference diverge unless the network is self-conditioned. This task owns that design space (DoubleCat interpolant, SemiCat discrete reveals).

This is **not** discrete dLLM recycle (A2D) and not image/flow alignment.

## Evaluation Protocol
- **Primary Benchmarks**: TinyGSM; 1.7B likelihood evals vs a discrete diffusion LM (paper: 4/6 wins).
- **Evaluation Pitfalls**: 49.94% TinyGSM is the tuned-sampler SemiCat number. Discrete-dLLM questions belong on `task:diffusion-lm-ar-delta-recycle`.

## SOTA Recommendation (as of 2026-10-13)
- **Experimental first hop (this task only)**: **SemiCat / DoubleCat** (`method:semicat`, `paper:semicat` `arXiv:2610.13834`). Status `active`. Method `sota_for` stays empty. No public code.
- **Not This Task**: `method:a2d` remains discrete-dLLM AR-delta recycle; `method:canvasanneal` remains discrete canvas RL; `method:diffusion-opsd` / `method:self-opd` remain image/flow post-train.
