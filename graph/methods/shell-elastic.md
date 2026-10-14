---
id: method:shell-elastic
type: method
title: ShellElastic (+ μE)
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: choosing the ~7B dense pretrain optimizer
  reason: ShellElastic is a nested-width supernet, not the 7B optimizer
  use_instead: method:muon2
- when: elastic mixed-depth looped LM rather than nested width
  reason: ELR varies loop count; this card varies width
  use_instead: method:elr
- when: budget ~1.5-2B dense pretrain on consumer GPUs
  reason: Puro-2B remains the consumer-GPU 2B hop
  use_instead: method:puro-2b
assumptions:
- Nested-width supernet. Paper reports 119M–1.69B bands. μP-style transfer (μE).
- Official repo jincan333/ShellElastic as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:shell-elastic
recipes:
- recipe:shell-elastic
claims:
- benchmark: nested-width supernet 119M–1.69B vs best baseline
  metric: mean val-loss nats below best baseline; 5-shot win rate
  value: 0.028 / 0.005 / 0.018 nats at 119M–285M / 375M–906M / 675M–1.69B; best or
    tied 12/15 val-loss and 14/15 5-shot tiers
  baseline: independent-width / sequential elastic baselines in Table 2 (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.15124
  notes: HF Daily 2026-10-14. Does not retarget Muon2, ELR, or Puro-2B.
tags:
- pretraining
- elastic
- width
- active
---

# ShellElastic (+ μE)

## Method Overview
Train a nested-width supernet whose inner subnets sit in a block-lower-triangular layout, so one outer pass updates all widths. μE transfers μP-style HPs from a small nested run.

## When to Use
- Need many widths from one pretrain at about the cost of the widest model, with HPs that transfer.

## When NOT to Use
~7B optimizer → `method:muon2`. Mixed-depth looping → `method:elr`. Consumer 2B from scratch → `method:puro-2b`.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Mention on `task:elastic-depth-looped-lm`. Does **not** replace Muon2, ELR, or Puro-2B.

## Gotchas & Failure Modes
- Width elasticity, not depth/loop elasticity.
- Table 2 is vs elastic-width baselines, not a Muon2 7B bake-off.
