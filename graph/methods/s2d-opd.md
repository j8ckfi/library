---
id: method:s2d-opd
type: method
title: "S2D-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "standard strong-teacher OPD (matching a frozen teacher, not a Direct-OPD log-ratio shift)"
    reason: "OPD remains the single-teacher distill default; S2D-OPD is a keep-mask on Direct-OPD"
    use_instead: "method:opd"
  - when: "TSD residual calibration of teacher–student discrepancy"
    reason: "Cal-OPD calibrates OPD advantage; S2D-OPD ranks teacher–reference JSD on Direct-OPD"
    use_instead: "method:cal-opd"
  - when: "sparse OPD token selection by gradient-estimation reliability (IER)"
    reason: "IER-OPD ranks reverse-KL gradient SNR; S2D-OPD ranks teacher–ref JSD for Direct-OPD"
    use_instead: "method:ier-opd"
  - when: "latent OPD collapse / last-layer crossfade"
    reason: "LastOPD is a latent-then-token schedule; S2D-OPD is Direct-OPD state selection"
    use_instead: "method:lastopd"
  - when: "weak-to-strong reverse distillation that rescales a verifier gradient along the teacher shift"
    reason: "OPRD is reverse distill; S2D-OPD keeps Direct-OPD's log-ratio reward on a JSD subset"
    use_instead: "method:oprd"
assumptions:
  - "Host is Direct-OPD: post-RL teacher vs pre-RL reference log-ratio on the student's top-K candidates, plus student-anchor KL. Paper does not run RL; it uses public teacher pairs."
  - "Paper: R1-Distill-1.5B→JustRL-1.5B and Nemotron-1.5B→QuestA-1.5B into Qwen3-1.7B/4B/8B and R1-Distill-7B; Skywork-OR1-RL-Data; ρ=0.1; Avg@32."
  - "Review-anonymous code as of 2026-09-25: anonymous.4open.science/r/S2D-OPD-8868."
last_reviewed: "2026-09-25"
papers:
  - paper:s2d-opd
recipes:
  - recipe:s2d-opd
claims:
  - benchmark: "Held-out AIME26+HMMT Avg@32 mean over 8 teacher–student settings"
    metric: "mean accuracy over 93 held-out problems"
    value: "47.31%"
    baseline: "dense Direct-OPD 46.36% (+0.95; 95% CI 0.40–1.54; 7/8 wins, 1 tie)"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.29142"
    notes: "Table 1 / §5.2. No extra forward passes. Not an OPD retarget."
  - benchmark: "Qwen3-1.7B Test Avg. under JustRL / QuestA teacher pairs"
    metric: "held-out Test Avg. (AIME26+HMMT)"
    value: "37.6 / 38.1"
    baseline: "Direct-OPD 36.4 / 36.5; student 31.3"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.29142"
    notes: "Table 1. Lowest JSD bins trained alone collapse; top bin beats random 10%."
tags:
  - post-training
  - distillation
  - on-policy
  - weak-to-strong
  - s2d-opd
  - active
---

# S2D-OPD

## Method Overview
Direct-OPD rewards every student state with \(\Delta_t(v)=\log\pi_{\mathrm{T}}(v)/\pi_{\mathrm{ref}}(v)\). Rescaling teacher and reference mass on the student's top-K by a common \(\epsilon\) leaves every log-ratio (and the local Direct-OPD gradient) unchanged, while JSD and both KLs scale with \(\epsilon\). S²D-OPD therefore scores each state by teacher–reference JSD on the compressed top-K plus residual token \(v_{\mathrm{o}}\), keeps the top \(\rho\approx 10\%\) of valid positions per response, and applies the usual Direct-OPD reward and student-anchor KL only there. The score reuses probabilities Direct-OPD already computes.

OPD remains strong-teacher matching. Cal-OPD / IER-OPD / LastOPD are different axes. OPRD is reverse distillation, not this keep-mask.

## When to Use
- Already running Direct-OPD / weak-to-strong policy-shift transfer, and you want to drop low-JSD states that can still carry a large log-ratio.

## When NOT to Use
- Strong-teacher OPD → `method:opd`. TSD calibration → `method:cal-opd`. IER sparse reverse-KL → `method:ier-opd`. Latent collapse → `method:lastopd`. Verifier-aligned reverse distill → `method:oprd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` for Direct-OPD. Does **not** enter `current_sota`. Does **not** replace `method:opd`, `method:open-mopd`, `method:cal-opd`, `method:ier-opd`, `method:lastopd`, or `method:oprd`.

## Gotchas & Failure Modes
- Code is review-anonymous as of 2026-09-25. Do not treat it as a named public GitHub.
- Training only on the lowest JSD bins can drop the student below init and collapse. Dense Direct-OPD is not "more tokens are safer."
- JSD and log-ratio magnitude rank states differently. The largest sampled-token log-ratio in a response can be masked.
- \(\rho=1\) recovers Direct-OPD. 5–20% all beat dense Direct-OPD on the 1.7B JustRL ablation; 10% is the default, not a learned budget.
