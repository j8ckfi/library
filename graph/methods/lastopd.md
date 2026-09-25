---
id: method:lastopd
type: method
title: "LastOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "OPD remains the distill default; LastOPD is a latent-collapse fix on reverse top-k OPD"
    use_instead: "method:opd"
  - when: "multi-teacher token-share balancing"
    reason: "Open-MOPD remains the multi-teacher default"
    use_instead: "method:open-mopd"
  - when: "same-lineage pairs where latent-only OPRD-Vanilla already works"
    reason: "Diagonal CKA pairs do not show the collapse; keep latent-only OPRD rather than the 10-step fade"
    use_instead: "method:oprd"
  - when: "TSD residual calibration of teacher–student discrepancy during OPD"
    reason: "Cal-OPD calibrates residual advantage; LastOPD is a latent-depth collapse schedule"
    use_instead: "method:cal-opd"
  - when: "weak-to-strong reverse distillation along a teacher policy-shift"
    reason: "OPRD rescales verifier gradients; LastOPD is latent-then-token OPD"
    use_instead: "method:oprd"
assumptions:
  - "Student and teacher share a tokenizer. Reverse top-k token OPD (k=16) plus last-layer MSE on L2-normalized states with a trainable width MLP."
  - "Paper: DAPO-Math-17k, 62 optimizer steps, Qwen3 non-thinking. Crossfade window Tw=10. Teachers Qwen3-4B/8B into Qwen3-1.7B-Base; same-lineage control JustRL-1.5B → R1-Distill-1.5B."
  - "GitHub Muyiiiii/LastOPD 404 as of 2026-09-25. Announced, not yet public."
last_reviewed: "2026-09-25"
papers:
  - paper:lastopd
recipes:
  - recipe:lastopd
claims:
  - benchmark: "MATH-500 avg@8, Qwen3-4B → Qwen3-1.7B-Base"
    metric: "avg@8"
    value: 58.95
    baseline: "token-only OPD 53.40; OPRD-Bridge latent-only 12.12; LastOPD-always 53.77"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.28845"
    notes: "Table 1. +5.55 vs token-only OPD. Eight-dataset mean 31.88 vs 27.95."
  - benchmark: "MATH-500 avg@8, Qwen3-8B → Qwen3-1.7B-Base"
    metric: "avg@8"
    value: 53.45
    baseline: "token-only OPD 49.43; OPRD-Bridge latent-only 12.32"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.28845"
    notes: "Table 1. +4.02 vs token-only OPD. Eight-dataset mean +2.10. Reaches token-OPD final score in about half the steps."
tags:
  - post-training
  - distillation
  - on-policy
  - lastopd
  - active
---

# LastOPD

## Method Overview
Depth-paired latent OPD (OPRD-Bridge) on cross-size pairs lifts early then collapses, while the alignment metric keeps improving. LastOPD keeps the useful part of the latent signal: apply Eq. 2 only at the last-layer pre-LM-head states (common interface both heads read), bridge width with a trainable MLP, and on the same student rollouts mix that term with reverse top-k token OPD. Over a window \(T_w=10\),

\[
\mathcal{L}_t=\alpha(t)\,\mathcal{L}_{\mathrm{OPD}}+\lambda_{\mathrm{rep}}\,\beta(t)\,\mathcal{L}_{\mathrm{rep}},\quad \alpha(t)=\min(1,t/T_w),\quad \beta(t)=\max(0,1-t/T_w).
\]

Step 0 is latent-only; from step \(T_w\) the run is exactly token-only OPD. The projector is discarded at inference.

OPD remains the single-teacher default. Open-MOPD remains multi-teacher. Cal-OPD is TSD residual calibration, not this collapse schedule.

## When to Use
- Cross-size latent OPD that gains then collapses under continued depth-paired alignment.

## When NOT to Use
- Distill default → `method:opd`. Multi-teacher → `method:open-mopd`. Same-lineage latent-only already working → `method:oprd`. TSD calibration → `method:cal-opd`.

## Relation to Existing SOTA
- Active on `task:student-distillation` beside OPD / Cal-OPD / OPRD. Does **not** enter `current_sota`. Does **not** replace `method:opd`, `method:open-mopd`, `method:cal-opd`, or `method:oprd`.

## Gotchas & Failure Modes
- Claimed GitHub `Muyiiiii/LastOPD` is 404 as of 2026-09-25. Reimplement last-layer + crossfade; do not claim a trainer.
- Hard switch at step 10 without overlap drops below token-only OPD (50.45 vs 53.40). The two terms must overlap while the latent weight fades.
- Same-lineage JustRL → R1-Distill: OPRD-Vanilla wins; the 10-step fade is the wrong default there.
- Masking massive activations hurts always-on latent recipes and barely moves LastOPD. Do not treat CKA ridge remapping as a fix.
