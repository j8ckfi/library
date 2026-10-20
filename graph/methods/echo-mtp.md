---
id: method:echo-mtp
type: method
title: 'ECHO'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'diffusion-adapter lossless multi-token AR serving'
  reason: 'Uno remains first hop; ECHO is causal self-recursion MTP, not diffusion adapters'
  use_instead: method:uno
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains the optimizer'
  use_instead: method:muon2
assumptions:
- 'AR pretrain with multi-horizon loss on the shared final layer. Dynamic Depth Sampling.'
- 'No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:echo-mtp
recipes:
- recipe:echo-mtp
claims:
- benchmark: 'ECHO vs DeepSeek-style auxiliary MTP; speculative decode acceptance under open-ended generation'
  metric: 'downstream vs MTP overhead; ECHO-1.5(3) vs ECHO-3'
  value: 'ECHO-1.5(3) matches ECHO-3 gain at half MTP overhead; deeper supervision helps where DeepSeek MTP plateaus; drafting with pretrained weights avoids post-hoc drafter overfit'
  baseline: 'DeepSeek V3-style auxiliary MTP; post-hoc drafter finetune'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24766'
  notes: 'Does not replace Uno. Not a dLLM.'
tags:
- architecture
- mtp
- speculative-decoding
- active
---

# ECHO

## Method Overview
ECHO (Efficient Causal Self-Recursion) puts multi-horizon supervision on the backbone's own final layer instead of auxiliary MTP modules. Dynamic Depth Sampling draws training depth with decaying probability so longer-horizon supervision stays cheap. The same shared layer can draft beyond the trained depth.

## When to Use
- Pretraining an AR model that should later draft multi-token without a separate draft network or diffusion adapter.

## When NOT to Use
Diffusion-augmented AR serving default → `method:uno`.

## Relation to Existing SOTA
Active plug-in on `task:diffusion-augmented-ar` (`sota_for: []`). Does **not** replace Uno.

## Gotchas & Failure Modes
- This is MTP pretrain, not Diffusion Distillation.
- No public code.
