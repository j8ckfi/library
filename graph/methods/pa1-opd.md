---
id: method:pa1-opd
type: method
title: PA1-OPD
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: same-tokenizer single-teacher matching distillation of a chat student
  reason: OPD remains post-train student matching; PA1-OPD is one-step prefix-augmented pretrain KD
  use_instead: method:opd
- when: choosing the ~7B dense NTP optimizer / mix
  reason: Muon2 / OLMo-3 remain the 7B pretrain defaults
  use_instead: method:muon2
assumptions:
- Shared tokenizer. Frozen teacher. One student-sampled token per selected corpus prefix, then teacher KL at the successor.
- Paper: two OLMo2 continued-pretraining settings; C4 / PG-19 / Pile CE.
- No public code as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:pa1-opd
recipes:
- recipe:pa1-opd
claims:
- benchmark: OLMo2 continued pretrain Stage2; C4 / PG-19 / Pile held-out CE
  metric: share of KD Macro CE gain over NTP recovered by Top10 surprisal roots
  value: Top10 surprisal adds 48.85% to KD Macro CE gain vs NTP (C4 61.60 / PG-19 22.24 / Pile 57.12); full coverage beats KD at every checkpoint
  baseline: corpus-path KD and NTP (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19601
  notes: Does not retarget OPD or Muon2.
tags:
- distillation
- pretraining
- opd
- active
---

# PA1-OPD

## Method Overview
Corpus-path KD plus one student-sampled transition per selected prefix. The teacher then supervises the successor state. Data-anchored roots keep sampling parallel. Differentiable tree attention shares prefixes. Student-surprisal selection can restrict which roots get a branch.

## When to Use
- Continued pretrain where corpus-path KD never sees student-induced contexts.

## When NOT to Use
Chat student matching → `method:opd`. 7B NTP default → `method:muon2`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`) with a mention on `task:pretrain-dense-7b`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-15.
- Stage1 favored full coverage over Top10; extra depth/breadth helped Macro CE with mixed per-corpus effects.
