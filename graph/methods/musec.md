---
id: method:musec
type: method
title: "Musec (MomentUm SpEctral Clipping)"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Musec is a Muon update-rule stability plug-in; Muon2 remains the 7B default"
    use_instead: "method:muon2"
  - when: "trillion-scale MoE / Kimi-K2 recipe"
    reason: "MuonClip is QK/attn-logit and MoE-scale clipping, a different mechanism"
    use_instead: "method:muonclip-kimi-k2"
  - when: "budget ~1.5-2B consumer-GPU pretrain recipe"
    reason: "Puro-2B remains that first hop"
    use_instead: "method:puro-2b"
assumptions:
  - "Muon-type matrix momentum on 2D weights. Embeddings / lm_head stay AdamW, same as Muon2."
  - "Paper experiments: modded-nanogpt host, NanoGPT-style GPT-2 descendants, LR sweep {0.05,…,1.0}. No dedicated repo."
last_reviewed: "2026-09-11"
papers:
  - paper:musec
recipes:
  - recipe:musec
claims:
  - benchmark: "modded-nanogpt NanoGPT-style models, wide LR / scale sweep"
    metric: "train stability vs Muon variants"
    value: "Soft Musec remains stable where Muon variants diverge; matches them when already well-tuned"
    baseline: "Muon spectral flattening; architecture-specific weight / attn-logit clipping"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.11655"
    notes: "Optimizer-level clip of momentum singular values above a threshold. First nonconvex-nonsmooth convergence claim for Muon-type methods. Not a 7B FineWeb bake-off vs Muon2."
tags:
  - pretraining
  - optimizer
  - muon
  - musec
  - stability
  - active
---

# Musec (MomentUm SpEctral Clipping)

## Method Overview
Muon flattens the momentum spectrum (singular values ≈ 1). Weak directions get oversized updates → loss spikes and unbounded weights. Musec **clips** singular values of the momentum matrix above a threshold and leaves the rest of the spectrum alone.

Soft Musec replaces the hard clip with a smooth saturation and approximates it by coupled Newton–Schulz iterations (same family as Muon's orthogonalization, no per-step SVD). Architecture-agnostic: it sits in the optimizer, not in QK-Norm or attn-logit caps.

Muon2 stays the ~7B optimizer. MuonClip stays the trillion-scale MoE / Kimi-K2 recipe (different clip target).

## When to Use
- Muon / Muon2 runs spike or weights blow up and you want an optimizer-level fix rather than QK-Norm or logit caps.
- You can retune the clip threshold; paper ablates sensitivity.

## When NOT to Use
- Picking the 7B default → `method:muon2`. Trillion-scale MoE recipe → `method:muonclip-kimi-k2`. Consumer ~2B → `method:puro-2b`.

## Relation to Existing SOTA
- Active stability plug-in / alternate Muon update on `task:llm-pretraining-optimization` and a mention on `task:pretrain-dense-7b`. Does **not** enter `current_sota`. Does **not** supersede Muon2 or MuonClip.

## Gotchas & Failure Modes
- No dedicated GitHub; port Soft Musec onto your Muon2 / modded-nanogpt host.
- Well-tuned Muon already stable: expect match, not a free loss win.
- Keep embeddings / `lm_head` on AdamW.
