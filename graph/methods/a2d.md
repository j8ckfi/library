---
id: method:a2d
type: method
title: "A2D"
category: "diffusion-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "text-to-image / flow reward alignment"
    reason: "A2D recycles an AR weight delta onto a dLLM; DiffusionOPSD / Self-OPD remain image/flow defaults"
    use_instead: "method:diffusion-opsd"
  - when: "discrete DLM curriculum RL with a teacher canvas"
    reason: "CanvasAnneal trains a masked DLM; A2D adds an AR post-training delta"
    use_instead: "method:canvasanneal"
  - when: "lossless multi-token AR serving"
    reason: "Uno keeps AR/NTP weights; A2D is a converted dLLM"
    use_instead: "method:uno"
assumptions:
  - "Converted discrete diffusion LM from an AR checkpoint, plus an AR post-training delta. No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:a2d
recipes:
  - recipe:a2d
claims:
  - benchmark: "AR post-training delta added to a converted dLLM vs direct diffusion post-training"
    metric: "approach to direct diffusion PT; composition with it"
    value: "AR delta on converted dLLM approaches direct diffusion PT and composes with it"
    baseline: "direct diffusion post-training; AR/diffusion deltas nearly orthogonal"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.08108"
    notes: "Does not replace DiffusionOPSD / Self-OPD / CanvasAnneal."
tags:
  - diffusion
  - dllm
  - a2d
  - active
---

# A2D

## Method Overview
Add an autoregressive post-training weight delta to a converted discrete diffusion LM. The recycle approaches direct diffusion post-training and composes with it because the AR and diffusion deltas are nearly orthogonal.

## When to Use
- A converted dLLM exists and an AR post-trained sibling already has a delta you do not want to re-train.

## When NOT to Use
- Image/flow rewards → `method:diffusion-opsd`. Canvas DLM RL → `method:canvasanneal`. AR serving → `method:uno`.

## Relation to Existing SOTA
- Active first hop on `task:diffusion-lm-ar-delta-recycle` (`sota_for: []`). Does **not** replace DiffusionOPSD / Self-OPD / CanvasAnneal.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-07.
- Recycle is not a substitute for CanvasAnneal's curriculum.
