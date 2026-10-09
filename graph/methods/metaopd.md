---
id: method:metaopd
type: method
title: "MetaOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "MetaOPD is a learned keep-weight on OPD tokens, not a new distill default"
    use_instead: "method:opd"
  - when: "sparse OPD token selection by gradient-estimation reliability (IER), not a learned weighting net"
    reason: "IER-OPD ranks SNR of the one-sample reverse-KL gradient; MetaOPD learns the map from post-update validation loss"
    use_instead: "method:ier-opd"
  - when: "probability-space token keep-mask that downweights low-low tokens (DIAL-OPD)"
    reason: "DIAL-OPD selects by log-mean probability; MetaOPD is bilevel weighting"
    use_instead: "method:dial-opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Host is sampled reverse-KL OPD with a frozen teacher and a held-out reference-solution validation split for the outer loop."
  - "No official GitHub as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:metaopd
recipes:
  - recipe:metaopd
claims:
  - benchmark: "Six math + three OOD, 0.6B / 1.7B students vs OPD"
    metric: "Avg@8 / Pass@8 lift vs uniform OPD"
    value: "+1.99 / +5.97 (0.6B); +2.25 / +6.41 (1.7B)"
    baseline: "uniform OPD; static proxy EOPD / TIP"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.11989"
    notes: "Seven baselines. Does not retarget OPD." 
tags:
  - post-training
  - distillation
  - opd
  - token-weighting
  - metaopd
  - active
---

# MetaOPD

## Method Overview
A 74-d detached token descriptor goes through a lightweight network. Scores are response-centered and unit-mean. The student updates on weighted sampled reverse-KL. The network updates from validation NLL after a virtual student step, so the signal-to-weight map tracks post-update gain instead of a frozen entropy or disagreement rule.

## When to Use
- OPD host where static token filters (entropy, IER, usefulness) stalled and you can afford a bilevel outer loop on reference solutions.

## When NOT to Use
- Default matching → `method:opd`. SNR keep-mask → `method:ier-opd`. Probability-space keep-mask → `method:dial-opd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD, IER-OPD, or DIAL-OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-09.
- Outer loop needs reference solutions. Virtual-update unrolling adds compute.
