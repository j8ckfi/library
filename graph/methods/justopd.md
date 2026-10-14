---
id: method:justopd
type: method
title: JustOPD (AR→diffusion-LM OPD)
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: recycle an AR post-training weight delta onto a converted dLLM
  reason: A2D recycles a weight delta; JustOPD distills AR logits on-policy onto a dLLM
  use_instead: method:a2d
- when: same-tokenizer single-teacher matching distillation (AR student)
  reason: OPD remains AR-to-AR matching
  use_instead: method:opd
- when: continuous diffusion language model pretrain
  reason: SemiCat remains continuous dLM pretrain
  use_instead: method:semicat
assumptions:
- Discrete diffusion student (Dream-7B) plus AR teacher (Qwen3-14B) in the paper.
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:justopd
recipes:
- recipe:justopd
claims:
- benchmark: Dream-7B student / Qwen3-14B teacher GSM8K and MATH500
  metric: accuracy at generation length L
  value: L=256 GSM8K 77.03→81.80 MATH500 31.80→39.60; L=512 GSM8K 78.77→84.45; L=1024
    MATH500 36.80→48.00 (JSD)
  baseline: Dream-7B without JustOPD (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.17397
  notes: Does not retarget A2D, OPD, or SemiCat.
tags:
- distillation
- diffusion-lm
- opd
- active
---

# JustOPD (AR→diffusion-LM OPD)

## Method Overview
Run on-policy reverse-KL style matching from an AR teacher onto discrete diffusion-LM samples. The student stays a dLLM; the teacher stays AR.

## When to Use
- You already have a discrete dLLM and a stronger AR teacher, and you want OPD rather than a weight-delta recycle.

## When NOT to Use
AR-delta recycle → `method:a2d`. AR student distill → `method:opd`. Continuous pretrain → `method:semicat`.

## Relation to Existing SOTA
Active plug-in on `task:diffusion-lm-ar-delta-recycle` (`sota_for: []`). Mentions on `task:student-distillation` and `task:continuous-diffusion-lm-pretrain`. Does **not** replace A2D or OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Lives next to A2D on the recycle task because both move AR signal onto a dLLM; the mechanism is distillation, not delta add.
