---
id: method:criticopd
type: method
title: CriticOPD
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: same-tokenizer single-teacher matching on already-correct rollouts
  reason: OPD remains matching; CriticOPD repairs teacher recoverability on incorrect prefixes
  use_instead: method:opd
- when: critique-conditioned privileged OPSD (teacher critiques then scores)
  reason: CC-OPSD is privileged scoring with a gold solution; CriticOPD rewrites student rollouts then scores
  use_instead: method:cc-opsd
- when: privileged same-size gold teacher OPSD
  reason: VISTA remains scoring-teacher OPSD
  use_instead: method:vista
assumptions:
- Teacher can recognize errors but follows them from incorrect prefixes. Paper: Qwen3-0.6B/1.7B; Olmo-3-7B-Instruct-SFT mention.
- Code: kzhao5/CriticOPD released as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:criticopd
recipes:
- recipe:criticopd
claims:
- benchmark: Qwen3-1.7B / 0.6B six math benches (AIME24/25, AMC 2023, MATH500, OlympiadBench, Minerva)
  metric: macro Avg vs OPD
  value: 1.7B 50.08→54.65 (+4.57); 0.6B 34.80→38.86 (+4.06); AIME24/25/AMC +6.01/+7.36/+6.94
  baseline: OPD, FastOPD, RelayOPD (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.20572
  notes: Distinct from CC-OPSD. Does not retarget OPD or VISTA.
tags:
- distillation
- opd
- critique
- active
---

# CriticOPD

## Method Overview
OPD assumes the teacher can recover a correct answer from any student prefix. That recoverability fails on incorrect rollouts: the teacher follows the error even when it can name it. CriticOPD has the teacher critique an incorrect rollout, lets the student rewrite, then scores the revision with the critique as privileged context while the student trains on the rewrite without it.

## When to Use
- Teacher OPD on math where incorrect prefixes poison teacher token targets.

## When NOT to Use
Plain matching → `method:opd`. Privileged gold scoring → `method:vista`. Critique-then-score privileged OPSD → `method:cc-opsd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD.

## Gotchas & Failure Modes
- Largest gains on competition math; Olmo-3-7B-Instruct-SFT 54.69→57.23 is a same-tokenizer family check, not a VISTA bake-off.
