---
id: method:law
type: method
title: 'LAW'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:continuous-diffusion-lm-pretrain'
  reason: 'LAW is an active plug-in; method:semicat remains the first hop'
  use_instead: method:semicat
assumptions:
- 'Continuous DLM. Expected-embedding recurrence across steps. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:law
recipes:
- recipe:law
claims:
- benchmark: 'Sudoku; Maze 2-64 NFE; TinyGSM T=1 vs discrete and continuous DLMs'
  metric: 'accuracy vs Loopholing Discrete Diffusion / prior continuous DLMs'
  value: 'Sudoku beats prior discrete and continuous DLMs including Loopholing Discrete Diffusion; Maze most accurate from 2 to 64 NFE'
  baseline: 'Loopholing Discrete Diffusion; prior continuous DLMs'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.30068'
  notes: 'Does not retarget method:semicat.'
tags:
- diffusion-lm
- self-conditioning
- active
---

# LAW

## Method Overview
LAW (Loopholing All the Way) makes Self-Conditioning the whole generative process: it carries the expected embedding across denoise steps and decodes tokens only at the end.

## When to Use
- Continuous diffusion LMs where SC is currently an auxiliary heuristic and you want a pure self-conditioned sampler.

## When NOT to Use
Experimental continuous-DLM first hop → `method:semicat`. Blockwise flow from AR init → `method:lafa`. AR-delta recycle → `method:a2d`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:semicat`.

## Gotchas & Failure Modes
- No public code.
- Not a 7B NTP pretrain recipe.
