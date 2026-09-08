---
id: method:adana
type: method
title: "ADANA (Adaptive DANA)"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Muon2 + KL-SOAP remains the 7B optimizer default; ADANA is a scheduled-memory Adam-family variant studied on 51M–253M overtraining"
    use_instead: "method:muon2"
  - when: "you need the overtraining-axis HP study rather than the optimizer itself"
    reason: "Horizon-dependent LR / WD / memory rankings are documented on method:optimizer-memory-schedules"
    use_instead: "method:optimizer-memory-schedules"
assumptions:
  - "Adam-style adaptive optimizer with DANA log-time momentum. Primary paper: Ferbach et al. arXiv:2602.05298. OT-axis bake-off: Everett & Qiu arXiv:2609.04577."
  - "OT-study defaults: κ=0.85, δ=8, g_3=8. Not a drop-in for Muon2 hidden-matrix layers."
last_reviewed: "2026-09-08"
papers:
  - paper:adana
  - paper:optimizer-memory-schedules
recipes: []
claims:
  - benchmark: "Everett & Qiu 51M–253M overtraining bake-off vs AdamW (log-time WD + momentum cooldown)"
    metric: "fitted equivalent-OT exponent vs AdamW"
    value: "1.15–1.20 (close to 2−κ=1.15 at κ=0.85)"
    baseline: "AdamW with uniform or log-time weight decay"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04577"
    notes: "OT paper §7.1 / Figure 7. At 2× OT, ADANA token multiplier vs Muon is 0.59×–0.63×; it closes and can surpass Muon at the highest measured OT. Not a 7B result."
tags:
  - pretraining
  - optimizer
  - adana
  - momentum
  - active
---

# ADANA (Adaptive DANA)

## Method Overview
ADANA is DANA's growing momentum timescale inside an Adam-style adaptive optimizer (Ferbach et al., arXiv:2602.05298). Log-time weight decay grows the WD memory window through training. The 2026-09-08 OT paper (`method:optimizer-memory-schedules`) is the cross-optimizer study: ADANA vs AdamW / Muon / SOAP from 51M–253M and OT $1\times$–$256\times$. This method is a named optimizer with no `sota_for`. Muon2 stays the ~7B default.

## When to Use
- Research / small-model pretrain where training horizon is long (high OT) and you want scheduled memory rather than a fixed $\beta_2$.
- Read `method:optimizer-memory-schedules` before copying $\beta$ / WD from a $1\times$ Chinchilla recipe.

## When NOT to Use
- ~7B dense pretrain optimizer → `method:muon2`.
- Interpreting OT rankings without retuning LR / WD / memory per horizon → the OT method card, not a single ADANA HP.

## Relation to Existing SOTA
- Active, `sota_for: []`. Does **not** supersede `method:muon2`, `method:soap-muon-scale`, or AdamW embeddings/`lm_head`.
- Distinct from Muon/SOAP: those keep roughly constant token multipliers vs AdamW; ADANA's relative advantage grows with OT.

## Gotchas & Failure Modes
- Behind Muon/SOAP at short horizon (token multiplier $0.59\times$–$0.69\times$ at $2\times$ OT). Do not pick ADANA because it "outscales" without checking your actual token budget.
- $\kappa=0.85$ is the OT paper's data-spectrum default, not a 7B-verified constant.
- No official recipe node in this library as of 2026-09-08.
