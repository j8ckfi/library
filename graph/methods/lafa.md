---
id: method:lafa
type: method
title: 'Lafa'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'continuous diffusion language model pretrain (self-conditioning / SemiCat), not AR-delta recycle'
  reason: 'SemiCat remains the experimental continuous-DLM hop; Lafa is blockwise flow trained from an AR init'
  use_instead: method:semicat
- when: 'lossless multi-token / diffusion-augmented AR serving'
  reason: 'Uno remains AR+diffusion serving; Lafa is a flow LM with self-speculative AR verify'
  use_instead: method:uno
assumptions:
- 'Blockwise flow: causal prefix attention, bidirectional asynchronous flow inside each block. Adapted from pretrained AR.'
- 'Code lafa-gh/large-flow-lms as of 2026-10-21. Scales 0.5B/7B/8B with <30B tokens.'
last_reviewed: '2026-10-21'
papers:
- paper:lafa
recipes:
- recipe:lafa
claims:
- benchmark: '0.5B/7B/8B instruction/reasoning/coding; self-speculative throughput vs AR'
  metric: 'quality vs AR; throughput vs AR / MTP / discrete diffusion'
  value: 'matches or surpasses AR quality after <30B tokens; 2.54x AR throughput at comparable quality via self-speculative AR verify of flow drafts'
  baseline: 'AR init; multi-token prediction; discrete diffusion LMs'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28559'
  notes: 'Does not retarget SemiCat or Uno.'
tags:
- flow-lm
- continuous-diffusion
- speculative
- active
---

# Lafa

## Method Overview
Lafa is a blockwise continuous flow language model adapted from a pretrained AR checkpoint. Prefix caching plus blockwise parallel decoding, then optional distillation to one/few-step flow maps. Flow drafts can be AR-verified inside the same model.

## When to Use
- Continuous flow LM at billion scale from an AR init when discrete diffusion token budgets are too high.

## When NOT to Use
Continuous DLM experimental hop → `method:semicat`. AR+diffusion serving → `method:uno`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:semicat`.

## Gotchas & Failure Modes
- Experimental relative to SemiCat's library hop.
- Self-speculative verify is AR, not Uno diffusion adapters.
