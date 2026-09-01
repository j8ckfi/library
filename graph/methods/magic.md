---
id: method:magic
type: method
title: "MAGIC (Metagradient-based Attribution via Ground-truth Influence Computation)"
category: "data-attribution"
status: sota
sota_for:
  - task:training-data-attribution
supersedes: []
do_not_use_for:
  - when: "open-weight final checkpoint only, no training trajectory"
    reason: "MAGIC unrolls *your* training run; a third-party final ckpt has no trajectory to differentiate through"
    use_instead: "method:trackstar"
  - when: "7B pretrain attribution without a 3–5× train-run budget"
    reason: "MAGIC is ~3–5 train-run compute; TrackStar / EK-FAC are ~1–2"
    use_instead: "method:trackstar"
  - when: "mix-ratio search or replacing an open pretrain mix"
    reason: "MAGIC scores items for a query; it does not search source weights"
    use_instead: "method:olmo-3"
assumptions:
  - "You control the trainer (Bergson twice-differentiable trainer or an equivalent recorded trajectory)."
  - "Check metasmoothness (`bergson metasmoothness`) before trusting LDS; untuned runs can collapse to ~0."
  - "Paper/Bergson LDS is GPT-2 WikiText fine-tune, not a 7B from-scratch pretrain."
last_reviewed: "2026-09-01"
papers:
  - paper:magic
  - paper:bergson
recipes:
  - recipe:bergson-magic-gpt2-wikitext
claims:
  - benchmark: "GPT-2 WikiText FT LDS (50 queries, N=400 retrains, 95% CI, Adam)"
    metric: "Spearman rho (LDS)"
    value: "0.983 ± 0.005"
    baseline: "SOURCE 0.387 ± 0.039 / EK-FAC 0.257 ± 0.015 / TrackStar 0.184 ± 0.015"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Bergson Table 1. Pearson 0.979 ± 0.006. Narrow LDS SOTA only; does not retarget mix/kernel/factory/SAE."
  - benchmark: "WMDP bio, Deep Ignorance 7B LoRA r=32, 130M tokens, MAGIC per-token"
    metric: "eval accuracy change vs unweighted FT"
    value: "+4.61 pp (token reweight top 10% ×5)"
    baseline: "unweighted FT +3.11 pp; sequence-level reweight +3.81 pp (+0.7 pp extra)"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Bergson §6.1. Token reweight +1.5 pp extra vs unweighted FT."
tags:
  - interpretability
  - data-attribution
  - magic
  - unrolling
  - lds
  - sota
---

# MAGIC (Metagradient-based Attribution via Ground-truth Influence Computation)

## Method Overview
MAGIC estimates leave-one-out / leave-k-out effects by **unrolled differentiation** through the training trajectory. The score of a training token or sequence is the gradient of a query loss with respect to a per-example training weight, backpropagated through optimizer steps (metagradients). Implemented in Bergson as `bergson magic` / YAML `steps: - magic:`.

Status `sota` **only** for `task:training-data-attribution` (narrow LDS). Does not supersede TrackStar, EK-FAC, SOURCE, or Bergson (library vs algorithm). Bergson does not supersede MAGIC.

## When to Use
- You train (or can retrain) the model and need the highest LDS against retrains.
- Token-level scoring when the query behavior is a differentiable loss (WMDP-style capability probes).
- Interpretability that needs the precise ordering of influential examples.

## When NOT to Use
- Final open-weight checkpoint, no trajectory -> `method:trackstar`.
- No 3–5× train budget at 7B -> `method:trackstar`.
- Mix-ratio search -> `task:open-data-recipe`.
- SAE circuits -> `task:mechanistic-interpretability-dictionaries`.

## Gotchas & Failure Modes
- Untuned Hessian damping / low metasmoothness can drive LDS ~0. Run `bergson metasmoothness` before trusting scores.
- Fused MoE experts unsupported.
- Sorted-subset / filtering-shaped LDS is MAGIC 1.000; that is a different protocol from random-subset Table 1.
