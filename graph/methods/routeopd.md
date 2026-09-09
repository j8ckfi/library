---
id: method:routeopd
type: method
title: "RouteOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "RouteOPD is a transport operator on sampled OPD, not a new distill default"
    use_instead: "method:opd"
  - when: "filtering teacher-OPD trajectories by outcome-alignment of G vs R"
    reason: "That is RA-OPD's (2R-1)G mask"
    use_instead: "method:ra-opd"
  - when: "sampled-token entropy shrink on already-admitted OPD"
    reason: "IDA-OPD reweights tokens after the teacher is already in the loss"
    use_instead: "method:ida-opd"
  - when: "prompt-level teacher reliability gate then exclusive OPD vs GRPO"
    reason: "That is TGOPD"
    use_instead: "method:tgopd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR without a teacher"
    reason: "Labeled dense RLVR stays CISPO"
    use_instead: "method:cispo"
assumptions:
  - "White-box teacher and student share tokenizer IDs. Paper checks ordered vocab maps before token-level routing."
  - "Defaults: k=32, m=2, Bmin=log 1.2, Bmax=log 1.5, Huber κ=1. DAPO-Math-17K, Avg@16."
  - "Routing statistics are detached per update; only current-student terms in Δt are differentiable."
last_reviewed: "2026-09-09"
papers:
  - paper:routeopd
recipes:
  - recipe:routeopd
claims:
  - benchmark: "Four teacher–student settings, MATH500/AMC23/AIME24/AIME25 Avg@16"
    metric: "macro Avg@16 vs sampled reverse-KL OPD"
    value: "+2.70 [2.28, 3.13]"
    baseline: "sampled-RKL; also +1.24 vs full-vocab RKL and +1.20 vs fixed-mid routing"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08337"
    notes: "Table 1/3. Per-setting vs sampled-RKL: +2.35 / +2.19 / +3.61 / +2.65."
  - benchmark: "JustRL-DeepSeek-1.5B four-bench Avg@16"
    metric: "Avg@16"
    value: 65.53
    baseline: "sampled-RKL 63.34 / full-vocab RKL 64.40 / fixed-mid 64.43"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08337"
    notes: "Table 1. AIME24 52.50 vs sampled-RKL 48.13."
  - benchmark: "Default k=32, m=2 vs sampled-RKL, identical hardware"
    metric: "relative end-to-end step time / extra peak memory"
    value: "1.025× / +2.0 GB"
    baseline: "sampled-RKL 184.6 s/step, 64.2 GB; full-vocab routing 1.125× / +9.4 GB"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08337"
    notes: "Table 10. Same teacher-call count."
tags:
  - post-training
  - distillation
  - on-policy
  - routeopd
  - active
---

# RouteOPD

## Method Overview
RouteOPD is an OPD **transport plug-in**. Sampled reverse-KL gives a scalar on the realized token. RouteOPD instead decomposes teacher–student disagreement on a detached top-k union into excess sources $q^-$ and deficit destinations $q^+$, samples $m$ pairs from $q^-\times q^+$, and regresses pairwise log-odds $\Delta_t(a,b)$ toward a cycle-consistent target $\hat D_t(a,b)=\phi_{B_t}(g_t(b))-\phi_{B_t}(g_t(a))$ from one bounded teacher potential. Budget $B_t$ interpolates $[B_{\min},B_{\max}]$ with teacher-demand concentration $c_t$ (normalized Herfindahl). Direct logit gradient of a pair is $e_b-e_a$ (no direct gradient on unrelated logits).

Sits beside RA-OPD, IDA-OPD, TGOPD, TV-OPD. Does not replace OPD.

## When to Use
- Already running sampled-token OPD and redistribution leaks into the student background.
- Teacher and student share tokenizer IDs.

## When NOT to Use
- Distill default → `method:opd`. Trajectory filter → `method:ra-opd`. Entropy shrink → `method:ida-opd`. Teacher gate → `method:tgopd`. Sign/TV stability → `method:tv-opd`.
- Pass@1 RLVR → `method:cispo`.

## Relation to Existing SOTA
- Active OPD plug-in on `task:student-distillation`. Does **not** supersede `method:opd`, `method:ra-opd`, `method:ida-opd`, `method:tgopd`, or `method:cispo`.
- Orthogonal to *which* tokens/spans to distill (sparse OPD, TIP, TRACE): this answers *which vocabulary destination* receives mass.

## Gotchas & Failure Modes
- No official GitHub as of 2026-09-09.
- Independent edge clipping is an ablation; it creates 27.6% four-cycle violations. Use the shared potential.
- Tokenizer mismatch forbids token-level routing. Paper refuses those pairs.
- Accuracy saturates at k=32; full-vocab routing is +0.08 Avg@16 for +12.5% time.
