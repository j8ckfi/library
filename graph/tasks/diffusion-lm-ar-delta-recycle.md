---
id: task:diffusion-lm-ar-delta-recycle
type: task
title: "Diffusion-LM Recycle of Autoregressive Post-Training Deltas"
domain: "diffusion"
summary: "Reuse an autoregressive post-training weight delta on a converted discrete diffusion LM instead of (or before) running diffusion post-training from scratch."
scope: "Adding an AR post-training delta onto a converted dLLM base, and composing that recycle with direct diffusion post-training. First hop is A2D. Not image/flow reward alignment, not discrete-DLM canvas RL, not AR multi-token serving."
out_of_scope:
  - "Text-to-image / flow reward alignment (DiffusionOPSD / Self-OPD)"
  - "Discrete DLM curriculum RL with a teacher canvas (CanvasAnneal)"
  - "Lossless multi-token / diffusion-augmented AR serving (Uno)"
  - "Dense AR Pass@1 RLVR (CISPO)"
  - "Continuous diffusion language model pretrain (SemiCat / DoubleCat)"
redirects:
  - when: "masked dLLM lookahead-edit SFT (LED; not AR-delta recycle)"
    to: "method:led"
  - when: "calibration-free dLLM quantization (not AR-delta recycle)"
    to: "method:soloq"
  - when: "aligning text-to-image diffusion or flow models with rewards"
    to: "task:posttrain-diffusion"
  - when: "curriculum RL for a discrete diffusion LM (canvas anneal), not AR-delta recycle"
    to: "method:canvasanneal"
  - when: "lossless multi-token / diffusion-augmented AR serving"
    to: "task:diffusion-augmented-ar"
  - when: "single-turn dense math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "continuous diffusion language model pretrain (self-conditioning / SemiCat), not AR-delta recycle"
    to: "task:continuous-diffusion-lm-pretrain"
  - when: "AR→discrete-dLLM on-policy distillation (JustOPD), not a weight-delta recycle"
    to: "method:justopd"
  - when: "16x DLM-vs-AR pretrain compute gap under ELBO vs exact likelihood"
    to: "paper:dlm-ar-compute-gap"
  - when: "dLLM RL that forks from high-entropy intermediate states (ForkGRPO)"
    to: "method:forkgrpo"
current_sota:
  - method: method:a2d
    as_of: "2026-10-07"
    benchmark: "AR post-training delta added to a converted dLLM base"
    metric: "approach to direct diffusion post-training; composition with it"
    value: "AR delta on converted dLLM approaches direct diffusion PT and composes with it; AR/diffusion deltas nearly orthogonal"
    notes: "A2D (2610.08108). Method status active. Does not replace DiffusionOPSD / Self-OPD / CanvasAnneal."
methods:
  - method:led
  - method:forkgrpo
  - method:justopd
  - method:semicat
  - method:soloq
  - method:a2d
  - method:canvasanneal
  - method:diffusion-opsd
  - method:self-opd
  - method:uno
last_reviewed: '2026-10-19'
tags:
  - diffusion
  - post-training
  - dllm
  - weight-delta
---

# Diffusion-LM Recycle of Autoregressive Post-Training Deltas

## Problem Definition
Discrete diffusion LMs converted from AR checkpoints often lag the AR post-trained sibling. Training the dLLM from scratch is expensive. This task owns **recycling the AR post-training weight delta** onto the converted dLLM, and whether that delta composes with a later diffusion post-train.

This is **not** image/flow reward alignment and not CanvasAnneal.

## Evaluation Protocol
- **Primary Benchmarks**: converted dLLM vs direct diffusion post-training vs AR-delta recycle vs recycle-then-diffusion; orthogonality of AR vs diffusion deltas.
- **Evaluation Pitfalls**: Do not treat this as Uno serving or as DiffusionOPSD image alignment.

## SOTA Recommendation (as of 2026-10-07)
- **Primary (this task only)**: **A2D** (`method:a2d`, `paper:a2d` `arXiv:2610.08108`). Status `active`. Listed here as first hop; method `sota_for` stays empty.
- **Not This Task**: `method:diffusion-opsd` / `method:self-opd` remain image/flow post-train; `method:canvasanneal` remains discrete-DLM canvas RL.
- **Related dLLM inference PTQ (not this recycle hop)**: `method:soloq` (`arXiv:2610.07121`) on `task:fp4-hardware-training`. Calibration-free 4-bit / NVFP4 for existing dLLMs. Does not replace A2D.
- **Not this task (continuous diffusion LM pretrain)**: `method:semicat` on `task:continuous-diffusion-lm-pretrain` (`arXiv:2610.13834`). Discrete-dLLM questions stay here.
- **Optional AR→dLLM on-policy distillation (not this recycle hop)**: `method:justopd` (`arXiv:2610.17397`). Dream-7B / Qwen3-14B; L=256 GSM8K 77.03→81.80. No public code. Does not replace A2D or OPD.
- **Gotcha (16× compute protocol)**: `paper:dlm-ar-compute-gap` (`arXiv:2610.17590`). ELBO MDM 17.8× vs DUEL 12.8×; E2D2 b=4 3.0×. Older 16× claims used ELBO/full-sequence. Does not retarget A2D or SemiCat.
- **Optional dLLM fork RL (not this recycle hop)**: `method:forkgrpo` (`arXiv:2610.19408`). GSM8K/MATH-500/HumanEval/MBPP 90.4/46.6/51.8/49.0 vs JustGRPO; ForkGRPO-fast 2.49×. No dedicated repo. Does not replace A2D, JustOPD, or CanvasAnneal.
- **Optional MDM lookahead-edit SFT**: `method:led` (`arXiv:2610.23122`). +11.4 / +7.7 vs MDM SFT on 7B/8B. Does not replace A2D or JustOPD.

