---
id: method:saki
type: method
title: "SAKI"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-teacher matching distillation from a strong frozen teacher (default OPD)"
    reason: "OPD remains student-rollout reverse-KL matching; SAKI routes TRB accept/correction events"
    use_instead: "method:opd"
  - when: "trust-region bounds on student–teacher divergence without coupling-routed supervision"
    reason: "TrOPD bounds OPD steps; SAKI realizes a KL-constrained *behavior* policy via maximal coupling"
    use_instead: "method:tropd"
  - when: "pairwise log-odds transport vs sampled reverse-KL"
    reason: "RouteOPD is a transport operator on sampled OPD, not accept/correction routing"
    use_instead: "method:routeopd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR without a teacher"
    reason: "Labeled dense RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "adapting the OPD teacher on student prefixes / off-policy teacher, not frozen-teacher OPD"
    reason: "SAKI gates student-side accept/correction for a frozen teacher; SCOUT trains the teacher with RL on student prefixes"
    use_instead: "method:scout"
assumptions:
  - "White-box teacher and student share a tokenizer. TRB constructs q_t with D_KL(q_t‖p_t)≤ε. Paper: 0.6B and 1.7B students, seven math benches, Mean@8/Pass@8."
  - "Maximal coupling: accept keeps sampled reverse-KL; correction is NLL on teacher top-1. Residual token continues the rollout."
  - "No public GitHub as of 2026-09-30."
last_reviewed: "2026-10-01"
papers:
  - paper:saki
recipes:
  - recipe:saki
claims:
  - benchmark: "Seven math benches, 1.7B student, Mean@8 / Pass@8"
    metric: "Mean@8 / Pass@8"
    value: "29.0 / 47.5"
    baseline: "Matched TRB teacher-guided OPD 27.9 / 44.6"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36601"
    notes: "0.6B 18.4 / 35.6 vs TRB 17.2 / 33.6. Not an OPD retarget."
  - benchmark: "Engine-resident speculative verifier vs external-loop teacher calls"
    metric: "matched-workload rollout throughput"
    value: "4.22×"
    baseline: "external-loop exact-q"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36601"
    notes: "Preserves exact-q trajectories and coupling semantics. Correction routing beats random and TV-weighted placement."
tags:
  - post-training
  - distillation
  - on-policy
  - saki
  - active
---

# SAKI

## Method Overview
TRB builds a teacher-guided behavior \(q_t\) inside \(D_{\mathrm{KL}}(q_t\|p_t)\le\epsilon\). SAKI samples \(q_t\) by maximal coupling with the frozen student \(p_t\). An accept keeps the student proposal and the usual detached reverse-KL advantage. A correction draws the residual needed to realize \(q_t\), continues the prefix with that residual token, and trains NLL on the teacher's top-1 at the same prefix. \(\Pr(C_t=1)=\mathrm{TV}(p_t,q_t)\le\sqrt{\epsilon/2}\). Speculative block verification amortizes teacher calls without changing the coupling. This is not OPD (pure student rollout), not TrOPD (trust-region on the *update*), and not RouteOPD (log-odds transport).

## When to Use
- Teacher-guided OPD where reverse-KL under-updates teacher modes at high-conflict prefixes, and you can realize TRB via coupling.

## When NOT to Use
- Default student-rollout matching → `method:opd`. Trust-region OPD steps → `method:tropd`. Probability transport → `method:routeopd`. Pass@1 RLVR → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:opd`, `method:tropd`, and `method:routeopd`. Does **not** enter `current_sota`. Does **not** replace OPD, TrOPD, RouteOPD, or CISPO.

## Gotchas & Failure Modes
- No public code as of 2026-09-30. Engine-resident verifier is load-bearing for the 4.22× claim.
- Residual token ≠ teacher top-1. Mixing them (train on the residual, or continue with top-1) is not SAKI.
- Equal-budget random and TV-weighted placement are weaker; do not ship those as SAKI.
- Weak students still need the TRB radius; \(\epsilon\to 0\) is student OPD, \(\epsilon\) too large is teacher cloning.
