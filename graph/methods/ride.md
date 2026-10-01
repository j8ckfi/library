---
id: method:ride
type: method
title: "RIDE"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-teacher matching distillation from a strong frozen teacher (default OPD)"
    reason: "OPD remains reverse-KL matching; RIDE extrapolates RL-induced hidden-state residuals"
    use_instead: "method:opd"
  - when: "Direct-OPD / weak-to-strong policy-shift token selection by teacher–ref JSD"
    reason: "S2D-OPD is an output-space Direct-OPD keep-mask; RIDE is layerwise representation residual"
    use_instead: "method:s2d-opd"
  - when: "weak-to-strong reverse distillation that rescales a verifier gradient along the teacher shift"
    reason: "OPRD is reverse distill; RIDE is same-init representation extrapolation"
    use_instead: "method:oprd"
  - when: "latent OPD collapse / last-layer crossfade into token OPD"
    reason: "LastOPD is a last-layer latent schedule into token OPD, not residual extrapolation"
    use_instead: "method:lastopd"
assumptions:
  - "Student initialized at the teacher's pre-RL checkpoint so hidden states share a space. Frozen teacher + frozen pre-RL reference; one scalar λ (λ=1 recovers OPRD)."
  - "Paper: R1-Distill-1.5B, Qwen3-4B, Llama-3.2-3B, Phi-4-mini; Avg@16 on AIME24 / AIME25 / AIMO."
  - "Official code xixixixixxxx/RIDE released as of 2026-10-01."
last_reviewed: "2026-10-01"
papers:
  - paper:ride
recipes:
  - recipe:ride
claims:
  - benchmark: "Four base/RL-teacher pairs, AIME24/AIME25/AIMO Avg@16 mean"
    metric: "whether mean meets or exceeds the RL teacher"
    value: "only RIDE's mean does"
    baseline: "OPRD and output-space extrapolation; output-space is below the teacher on every pair"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36484"
    notes: "Same-init residual. Not an OPD or S2D-OPD retarget."
tags:
  - post-training
  - distillation
  - on-policy
  - ride
  - active
---

# RIDE

## Method Overview
On each student prefix, RIDE (RL-Induced Direction Extrapolation) reads frozen teacher and pre-RL hidden states \(h_T^{(l)}, h_{\mathrm{base}}^{(l)}\) and sets

\[
\tau^{(l)} = h_T^{(l)} + (\lambda-1)\,(h_T^{(l)}-h_{\mathrm{base}}^{(l)}).
\]

The student regresses \(h_\theta^{(l)}\) toward \(\tau^{(l)}\) at every layer. \(\lambda=1\) is OPRD. Conditioned on a rollout this is a linear directional reward with a quadratic penalty at the teacher. Output-space log-ratio extrapolation is the head-projected image of the same target and loses most of the residual in the head's weak singular directions.

## When to Use
- Distilling an RL run back into its own initialization along the RL-induced hidden-state direction rather than noisy logit ratios.

## When NOT to Use
- Frozen-teacher matching → `method:opd`. Direct-OPD JSD keep-mask → `method:s2d-opd`. Reverse distill → `method:oprd`. Last-layer latent schedule → `method:lastopd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:opd` and `method:s2d-opd`. Does **not** enter `current_sota`. Does **not** replace OPD, S2D-OPD, OPRD, or LastOPD.

## Gotchas & Failure Modes
- Needs the pre-RL checkpoint. Different-init teachers are not this method.
- \(\lambda\) too large overshoots; \(\lambda=1\) is matching, not extrapolation.
- Do not implement this as a sampled-token log-ratio scale. That is the output-space baseline that loses when the teacher is close to base.
