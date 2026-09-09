---
id: method:tv-opd
type: method
title: "TV-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "TV-OPD reshapes sampled-token advantages; OPD remains the distill default"
    use_instead: "method:opd"
  - when: "filtering trajectories by (2R-1)G alignment"
    reason: "RA-OPD is a keep/drop mask, not a TV-shaped coefficient"
    use_instead: "method:ra-opd"
  - when: "trust-region teacher matching is the named method"
    reason: "TrOPD bounds student divergence; TV-OPD bounds the sampled coefficient"
    use_instead: "method:tropd"
  - when: "control-variate variance reduction on sampled OPD"
    reason: "Stable-OPD / vOPD subtract a baseline; TV-OPD does not"
    use_instead: "method:stable-opd"
  - when: "explicit source–destination probability transport"
    reason: "That is RouteOPD"
    use_instead: "method:routeopd"
assumptions:
  - "Running sampled-token OPD. Paper: JustRL-DeepSeek-1.5B → R1-Distill-Qwen-1.5B and a second 8B pair; DAPO-Math-17K; two seeds on the diagnostic."
  - "Default reported regulator uses a shared TV-responsive scale (α=0.5 in Table 2). Sign(0)=0."
last_reviewed: "2026-09-09"
papers:
  - paper:tv-opd
recipes:
  - recipe:tv-opd
claims:
  - benchmark: "JustRL-DeepSeek-1.5B AIME 2024/2025 two-seed diagnostic"
    metric: "per-seed best-over-training accuracy"
    value: "Sign 50.00±1.18 / 37.50; trajectory avg 36.29"
    baseline: "Raw 47.50 / 35.83 (trajectory avg 35.40); Group-Constant 34.67; Permuted 34.35"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08341"
    notes: "Figure 1 / Appendix D. Sign keeps direction and drops token magnitude."
  - benchmark: "JustRL late-stage AIME 2024 (steps 500–625)"
    metric: "stage-mean accuracy"
    value: 49.58
    baseline: "Sign-TV 47.92 / Raw OPD 46.11"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08341"
    notes: "Table 2. Late AIME 2025: TV-OPD 36.53 vs Sign-TV 35.56 vs Raw 35.63. Regulator is not uniformly best in early/middle windows."
  - benchmark: "Two-benchmark LateMean / PeakDrop (steps 500–625)"
    metric: "LateMean ± sd"
    value: "43.06 ± 0.10; PeakDrop 2.36 ± 0.49"
    baseline: "Raw LateMean 40.87 ± 0.83; PeakDrop 3.51 ± 1.13"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08341"
    notes: "Paired complete coverage only. Two seeds."
tags:
  - post-training
  - distillation
  - on-policy
  - tv-opd
  - active
---

# TV-OPD

## Method Overview
TV-OPD is an OPD **stability plug-in**. Sampled reverse-KL uses $\Delta_i=\log\pi_T-\log\pi_\theta$ as an unbounded token coefficient. The paper splits that signal into sign, relative magnitude, and global scale. Keeping only $z_i=\mathrm{sign}(\Delta_i)$ (Sign-TV) is a sampled estimator of conditional total variation. TV-OPD multiplies that sign by a shared TV-responsive scale $c_k$ so the update shrinks as teacher and student agree, without restoring per-token $|\Delta_i|$. Coefficients are bounded.

Relate to RA-OPD (trajectory mask), TrOPD (trust region), Stable-OPD (control variates), RouteOPD (transport pairs). None of these replace OPD.

## When to Use
- Sampled OPD late training is noisy or peaks then drops.
- You want a bounded coefficient without a new teacher or a keep/drop filter.

## When NOT to Use
- Distill default → `method:opd`. Trajectory filter → `method:ra-opd`. Trust region → `method:tropd`. Control variates → `method:stable-opd`. Transport destinations → `method:routeopd`.
- Pass@1 RLVR → `method:cispo`.

## Relation to Existing SOTA
- Active OPD plug-in on `task:student-distillation`. Does **not** supersede `method:opd`, `method:ra-opd`, `method:tropd`, `method:stable-opd`, or `method:routeopd`.
- Sign-TV is the unregulated ablation; TV-OPD adds the shared scale. Early-stage Sign-TV can beat TV-OPD (Table 2).

## Gotchas & Failure Modes
- No official GitHub as of 2026-09-09. Two seeds on the diagnostic pair.
- The regulator is for late-stage retention, not every window.
- Do not restore token-wise magnitude on top of the sign; that is the thing the paper finds unhelpful.
