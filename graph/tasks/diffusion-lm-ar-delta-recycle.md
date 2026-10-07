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
redirects:
  - when: "aligning text-to-image diffusion or flow models with rewards"
    to: "task:posttrain-diffusion"
  - when: "curriculum RL for a discrete diffusion LM (canvas anneal), not AR-delta recycle"
    to: "method:canvasanneal"
  - when: "lossless multi-token / diffusion-augmented AR serving"
    to: "task:diffusion-augmented-ar"
  - when: "single-turn dense math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
current_sota:
  - method: method:a2d
    as_of: "2026-10-07"
    benchmark: "AR post-training delta added to a converted dLLM base"
    metric: "approach to direct diffusion post-training; composition with it"
    value: "AR delta on converted dLLM approaches direct diffusion PT and composes with it; AR/diffusion deltas nearly orthogonal"
    notes: "A2D (2610.08108). Method status active. Does not replace DiffusionOPSD / Self-OPD / CanvasAnneal."
methods:
  - method:a2d
  - method:canvasanneal
  - method:diffusion-opsd
  - method:self-opd
  - method:uno
last_reviewed: "2026-10-07"
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
