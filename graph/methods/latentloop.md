---
id: method:latentloop
type: method
title: LatentLoop
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: compute-matched MoE looping of middle layers (FLOPs/params/KV matched)
  reason: SMELT remains the compute-matched looped-MoE first hop
  use_instead: method:smelt
- when: elastic mixed-depth looped LM (gated state update / mixed loop counts)
  reason: ELR owns mixed loop counts on dense / MoE LMs
  use_instead: method:elr
- when: choosing the frontier MoE architecture template
  reason: DeepSeek-V4 / Kimi-K3 remain the sparse-from-scratch template
  use_instead: method:deepseek-v4
assumptions:
- Shared MoE weights across two visits; separate attention. Compress the first visit's sequence, full-res the second, reallocate FLOPs to width.
- Paper: 15 configs 1.3B-7B; largest budget >10^21 FLOPs. No public code as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:latentloop
recipes:
- recipe:latentloop
claims:
- benchmark: 15 looped-MoE configs 1.3B-7B, fitted NLL 1.988; nine 0-shot/5-shot benches
  metric: predicted compute vs MoE Base / MoE Loop; 5-shot delta vs Loop
  value: 19.0% vs MoE Base, 7.9% vs MoE Loop at NLL 1.988; downstream +0.73-1.18 5-shot vs Loop
  baseline: unlooped MoE Base and uniform MoE Loop (single-paper; not SMELT)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19975
  notes: Does not retarget SMELT.
tags:
- architecture
- moe
- looped-transformer
- active
---

# LatentLoop

## Method Overview
Looped MoE visits are not equal. Compress the first visit's sequence, keep full resolution on the second, and spend the saved compute on hidden size. Share MoE weights across visits; keep separate attention because the sequence lengths differ. A learned residual scale controls how strongly the first visit writes back.

## When to Use
- Compute-matched looped MoE where a second visit should stay full-res and the first visit is a cheap draft.

## When NOT to Use
Matched middle-layer looping default → `method:smelt`. Mixed-depth looping → `method:elr`. Frontier MoE template → `method:deepseek-v4`.

## Relation to Existing SOTA
Active plug-in on `task:compute-matched-moe-looped-pretrain` (`sota_for: []`). Does **not** replace SMELT.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-15.
- Not a SMELT bake-off; savings are vs the paper's own MoE Base / Loop.
