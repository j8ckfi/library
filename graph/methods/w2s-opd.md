---
id: method:w2s-opd
type: method
title: "W2S-OPD (Weak-to-Strong On-Policy Distillation)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "amplifying a verifier gradient along a teacher policy-shift (reverse distillation)"
    reason: "OPRD rescales RLVR updates; W2S-OPD matches the weak teacher on student prefixes"
    use_instead: "method:oprd"
  - when: "choosing the single-teacher distill default against a strong teacher"
    reason: "OPD remains the matching default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "CISPO remains the Pass@1 kernel"
    use_instead: "method:cispo"
assumptions:
  - "Weaker teacher, stronger student, on-policy matching. Distinct from OPRD (2609.08798), which does not treat the weak policy as a target."
last_reviewed: "2026-09-09"
papers:
  - paper:w2s-opd
recipes:
  - recipe:w2s-opd
claims:
  - benchmark: "Weak-to-Strong Generalization"
    metric: "student performance boost"
    value: "Elicits latent student capabilities beyond weak teacher limits"
    baseline: "Standard Distillation"
    date: "2026-08-26"
    verified: true
    notes: "Iterative bootstrapping of strong students using weak supervision. OPRD Table 3 reports a different reverse-distill mix; that is not a graph supersession."
tags:
  - post-training
  - distillation
  - weak-to-strong
  - w2s-opd
---

# W2S-OPD (Weak-to-Strong On-Policy Distillation)

## Method Overview
W2S-OPD matches a weaker teacher on stronger-student prefixes (on-policy verification and self-correction). `method:oprd` is the reverse-distill cousin: it rescales the student's verifier gradient along the teacher policy-shift and does **not** use the weak policy as a matching target. Keep both; neither replaces OPD or CISPO.

## When to Use
- Bootstrapping large capable base models with smaller, fast supervisor teachers via matching.

## When NOT to Use
- Reverse distillation / verifier-aligned teacher shift → `method:oprd`.
- Strong-teacher matching default → `method:opd`. Pass@1 RLVR → `method:cispo`.

## Relation to Existing SOTA
- Active on `task:student-distillation`. Does **not** supersede `method:opd`. Is **not** superseded by `method:oprd`.
