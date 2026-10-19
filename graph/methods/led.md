---
id: method:led
type: method
title: 'LED'
category: diffusion
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'recycle an AR post-training weight delta onto a converted dLLM'
  reason: 'A2D remains AR-delta recycle; LED is MDM lookahead-edit SFT'
  use_instead: method:a2d
- when: 'AR→discrete-dLLM on-policy distillation'
  reason: 'JustOPD is AR-to-dLLM OPD; LED keeps the MDM mask schedule'
  use_instead: method:justopd
- when: 'curriculum RL for a discrete diffusion LM (canvas anneal)'
  reason: 'CanvasAnneal is discrete-DLM RL; LED is SFT lookahead editing'
  use_instead: method:canvasanneal
assumptions:
- 'Masked diffusion LMs. Fine-tunes Qwen2.5-7B and Qwen3-8B into LED-7B / LED-8B.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:led
recipes:
- recipe:led
claims:
- benchmark: 'Eight benches, LED SFT vs standard MDM SFT; LED-8B vs LLaDA2.1-16B Q-mode'
  metric: 'average points vs MDM SFT'
  value: '+11.4 (7B) / +7.7 (8B) vs MDM SFT; LED-8B SFT-only beats LLaDA2.1-16B Q-mode (CPT+SFT+RL)'
  baseline: 'standard MDM SFT / LLaDA2.1-16B Q-mode (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23122'
  notes: 'Does not retarget A2D, JustOPD, or CanvasAnneal.'
tags:
- dllm
- mdm
- sft
- active
---

# LED

## Method Overview
Lookahead Editing keeps MDM's mask-based transition schedule and adds a rewritable proposal state: each decode step runs several lookahead updates before committing tokens to the masked sequence.

## When to Use
- Masked dLLM SFT when you want extra decode compute for expressivity without switching to uniform diffusion or AR-delta recycle.

## When NOT to Use
AR-delta recycle → `method:a2d`. AR→dLLM OPD → `method:justopd`.

## Relation to Existing SOTA
Active plug-in on `task:diffusion-lm-ar-delta-recycle` (`sota_for: []`). Does **not** replace A2D.

## Gotchas & Failure Modes
- SFT recipe, not A2D weight-delta recycle.
- LLaDA comparison is Q-mode, not a library A2D bake-off.
