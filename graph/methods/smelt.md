---
id: method:smelt
type: method
title: "SMELT (Sparse MoE Transformer, Middle Layers Loop Twice)"
category: "architecture"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the frontier MoE architecture template"
    reason: "SMELT is a compute-matched looping recipe on an internal MoE baseline, not DeepSeek-V4 or Kimi-K3"
    use_instead: "method:deepseek-v4"
  - when: "expert-parallel all-to-all layout / concentrating experts in fewer routed layers"
    reason: "That layout niche is CE-MoE, not looping"
    use_instead: "method:ce-moe"
  - when: "NVL72 fused dispatch+SwiGLU+combine megakernel"
    reason: "Looping does not replace Mixture-of-Kittens"
    use_instead: "method:mixture-of-kittens"
  - when: "recurrent CED all-token recurrence"
    reason: "SMELT is decoder-only MoE layer looping under budget matching; RLT is a different architecture"
    use_instead: "method:recurrent-looped-transformer"
assumptions:
  - "Match per-token FLOPs, total non-embedding parameters, and KV cache against an unlooped MoE Baseline. Typical residual mismatch: FLOPs <4%, params <1%, KV <4%."
  - "Locked recipe: loop middle 50% of layers twice; physical depth matches the Baseline; scale looped residuals by 1/r with r=2; narrow H and raise expert count; GQA/head-size for KV."
  - "Paper ladder: 100M/200M/600M/1.6B active, up to 54B non-embedding, S≈85/95/97%. Internal corpus, AdamW WSD. No public code as of 2026-09-12."
last_reviewed: "2026-09-12"
papers:
  - paper:smelt
recipes:
  - recipe:smelt
claims:
  - benchmark: "Compute-optimal frontier vs unlooped MoE Baseline (sparse-grid fit)"
    metric: "training FLOPs saved at matched validation loss (CE Gain)"
    value: "6.8–18.0%"
    baseline: "Unlooped MoE Baseline, matched FLOPs / non-embedding params / KV; S≈85/95/97%"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.01343"
    notes: "Table of CE Gain: 6.8–10.0% at 10^20 FLOPs; 14.7–18.0% at 10^21. 10^22 column is extrapolated. Cell-bootstrap 95% intervals in the paper. Separate Chinchilla-style surfaces; not a DeepSeek-V4 bake-off."
  - benchmark: "SMELT scale-up ladder"
    metric: "largest non-embedding parameter count"
    value: "54B"
    baseline: "1.6B-active cell, S≈97%, matched Baseline"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.01343"
    notes: "Four active scales 100M / 200M / 600M / 1.6B. SMELT lower loss than Baseline in every sparse-grid cell of the paper."
  - benchmark: "DCLM Completion / DCLM Core / MMLU vs matched Baseline"
    metric: "pairwise wins"
    value: "96/96 Completion; 83/96 Core; 29/30 MMLU (Baseline ≥10 pp above chance)"
    baseline: "Unlooped MoE Baseline at the same scale and sparsity"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.01343"
    notes: "Downstream lift exceeds a Baseline-calibrated loss-to-score map. Largest training-domain gain on Code. Second visit reduces attention sink."
tags:
  - architecture
  - moe
  - looped-transformer
  - smelt
  - scaling-laws
---

# SMELT (Sparse MoE Transformer, Middle Layers Loop Twice)

## Method Overview
Loop a contiguous middle span of a decoder-only MoE Transformer rather than stacking new layers. Extra visits cost FLOPs, so SMELT narrows hidden size \(H\), recovers stored parameters by raising per-layer expert count, and restores KV with head size / GQA. Looped residual updates are scaled by \(1/r\) (\(r=2\) ⇒ \(1/2\)) so tied visits do not inflate the stream.

Ablations lock three rules: (1) loop the middle 50% of layers, not the full stack; (2) keep physical depth at the Baseline optimum so effective depth-to-width is larger; (3) loop twice — a third or fourth visit thins the model under the FLOPs cap and regresses.

Sibling of `method:ce-moe` on the MoE shelf: CE-MoE retile *which layers are routed*; SMELT *reuses* middle routed layers under three-budget matching. Neither is the V4 / K3 template.

## When to Use
- You can retile an MoE pretrain run to loop the middle half twice and will match FLOPs, non-embedding params, and KV against the unlooped recipe.

## When NOT to Use
- Frontier architecture default → `method:deepseek-v4` / `method:kimi-k3`. Communication layout → `method:ce-moe`. NVL72 megakernel → `method:mixture-of-kittens`. All-token CED recurrence → `method:recurrent-looped-transformer`.

## Relation to Existing SOTA
- Active first hop on `task:compute-matched-moe-looped-pretrain` only. Mentioned beside CE-MoE on `task:pretrain-moe-frontier`. Does **not** replace DeepSeek-V4, Kimi-K3, or CE-MoE.

## Gotchas & Failure Modes
- No official code. Do not clone unrelated "SMELT" GitHub repos.
- Matching is the claim. Iso-parameter looping that grows FLOPs/KV is the comparison SMELT argues against.
- DCLM Core and validation loss can disagree on loop span; the paper selects span on validation loss.
- Internal data and AdamW WSD; do not assume the CE Gain transfers onto a DeepSeek-V4 stack without a rematch.
