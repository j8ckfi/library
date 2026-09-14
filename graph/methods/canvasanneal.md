---
id: method:canvasanneal
type: method
title: "CanvasAnneal"
category: "diffusion-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "text-to-image / flow reward alignment"
    reason: "CanvasAnneal is discrete DLM RL with a teacher canvas; DiffusionOPSD / Self-OPD remain image/flow defaults"
    use_instead: "method:diffusion-opsd"
  - when: "lossless multi-token AR serving"
    reason: "Uno keeps AR/NTP weights; CanvasAnneal trains a masked diffusion LM"
    use_instead: "method:uno"
  - when: "dense Pass@1 math/code RLVR on an AR policy"
    reason: "CISPO remains AR Pass@1; this is DLM diffu-GRPO with a curriculum"
    use_instead: "method:cispo"
assumptions:
  - "Discrete masked DLM (paper: LLaDA-7B-A1B-Instruct). Host is diffu-GRPO. Teacher traces from a stronger model (paper: Gemini 3.1 Pro) injected into the initial canvas and annealed."
  - "No official GitHub as of 2026-09-14."
last_reviewed: "2026-09-14"
papers:
  - paper:canvasanneal
recipes:
  - recipe:canvasanneal
claims:
  - benchmark: "MATH500 vs diffu-GRPO, LLaDA-7B-A1B-Instruct"
    metric: "accuracy lift at gen lengths 128 / 256 / 512"
    value: "+6.0 / +2.0 / +0.4"
    baseline: "diffu-GRPO (unconditioned noise canvas)"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13060"
    notes: "Countdown +2.73 / +3.91 / +1.96 at the same lengths. GSM8K: diffu-GRPO remains stronger. Task-dependent."
  - benchmark: "Tau2 average (Retail / Airline / Telecom)"
    metric: "success rate"
    value: 13.03
    baseline: "diffu-GRPO 10.15"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13060"
    notes: "Retail 7.90 vs 6.14, Airline 18.00 vs 12.00, Telecom 13.20 vs 12.30."
tags:
  - diffusion
  - dlm
  - post-training
  - canvasanneal
  - active
---

# CanvasAnneal

## Method Overview
DLM RL explores from a fully masked canvas and stalls on hard reasoning. CanvasAnneal writes a teacher trace onto that canvas at the start of training and anneals the teacher tokens away so the student must fill more of the trajectory. The RL host stays diffu-GRPO.

## When to Use
- Discrete diffusion LMs (LLaDA-class) where vanilla diffu-GRPO is exploration-starved on MATH500 / Countdown / Tau2.

## When NOT to Use
- Image/flow rewards → `method:diffusion-opsd` / `method:self-opd`. AR serving → `method:uno`. AR Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- Active niche on `task:posttrain-diffusion`. Does **not** replace DiffusionOPSD, Self-OPD, or Uno.

## Gotchas & Failure Modes
- GSM8K got worse than unconditioned diffu-GRPO in the paper. Do not anneal blindly across tasks.
- Teacher-trace injection is training-time only.
