---
id: method:ek-fac
type: method
title: "EK-FAC (Eigenvalue-corrected Kronecker-Factored Approximate Curvature)"
category: "data-attribution"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "you control the trainer and need peak LDS"
    reason: "MAGIC is the LDS SOTA; EK-FAC is the influence-function baseline"
    use_instead: "method:magic"
  - when: "mix-ratio search or replacing an open pretrain mix"
    reason: "Influence scores are not mix-weight search"
    use_instead: "method:olmo-3"
assumptions:
  - "Final checkpoint is enough. Hessian damping must be tuned; untuned inversion can drive LDS ~0."
  - "Bergson EK-FAC verified to 7B on one 8×A100; Kronfluence still the larger EK-FAC model (14B) on that protocol."
last_reviewed: "2026-09-01"
papers:
  - paper:ek-fac
  - paper:bergson
claims:
  - benchmark: "GPT-2 WikiText FT LDS (50 queries, N=400, Adam)"
    metric: "Spearman rho (LDS)"
    value: "0.257 ± 0.015"
    baseline: "MAGIC 0.983 ± 0.005 / SOURCE 0.387 ± 0.039 / TrackStar 0.184 ± 0.015"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Bergson Table 1. Pearson 0.295 ± 0.016."
  - benchmark: "GPT-2 WikiText FT LDS, Muon-trained (README)"
    metric: "Spearman rho (LDS)"
    value: "0.474 ± 0.036"
    baseline: "Shampoo 0.522 ± 0.037 (Muon); Adam EK-FAC 0.257 ± 0.015"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://github.com/EleutherAI/bergson"
    notes: "README influence table. Optimizer of the attributed run matters."
tags:
  - interpretability
  - data-attribution
  - ek-fac
  - influence
---

# EK-FAC (Eigenvalue-corrected Kronecker-Factored Approximate Curvature)

## Method Overview
EK-FAC approximates the Hessian with eigenvalue-corrected Kronecker factors so influence functions \(\nabla L(z_q)^\top H^{-1} \nabla L(z_m)\) can run on transformers. Grosse et al. used it up to 52B. Bergson implements it as `bergson ekfac`; Kronfluence is the other production EK-FAC stack and still verifies a larger EK-FAC model (14B vs Bergson 7B) on the Appendix C one-node protocol.

Status `active`. Influence baseline, not LDS SOTA. Does not supersede MAGIC, TrackStar, SOURCE, or Bergson.

## When to Use
- Classical influence-function path on a dense checkpoint.
- Baseline against MAGIC / TrackStar on the same query set.

## When NOT to Use
- Peak LDS with a recorded trajectory -> `method:magic`.
- Small-lab LESS-style filter with projection -> `method:trackstar`.
- Mix-ratio search -> `method:olmo-3`.

## Gotchas & Failure Modes
- Untuned Hessian damping can drive LDS ~0.
- Do not write intro-scale 405B as a verified EK-FAC run. Verified Bergson single-node: EK-FAC 7B, grad-dot 72B.
- Fused MoE experts unsupported in Bergson.
- No LoGra / LiSSA in Bergson; those live in dattri.
