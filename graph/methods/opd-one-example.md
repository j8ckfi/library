---
id: method:opd-one-example
type: method
title: "One-Shot OPD (OPD-II)"
category: "distillation"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "OPD-II is a data-efficiency finding on top of OPD, not a new distill objective; OPD remains the default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "This is still OPD; labeled RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "no teacher is available"
    reason: "One-shot OPD still needs teacher token distributions; teacher-free self-adaptation is OPSA"
    use_instead: "method:opsa"
  - when: "multi-teacher imbalance is the failure mode"
    reason: "16 diverse queries per domain can match full-data MOPD, but Open-MOPD remains the multi-teacher algorithm"
    use_instead: "method:open-mopd"
  - when: "filtering teacher-OPD trajectories by outcome alignment"
    reason: "That is RA-OPD, not a smaller query set"
    use_instead: "method:ra-opd"
assumptions:
  - "Running reverse-KL / sampled-token or top-k OPD with a white-box teacher (paper: veRL, batch of 64 rollouts, AdamW 1e-6)."
  - "Prefer semantically diverse queries over volume; 16 BGE-M3 cluster representatives matched full DAPO-Math-17K."
  - "Does not change the OPD loss. Companion to paper:opd (2604.13016)."
last_reviewed: "2026-09-04"
papers:
  - paper:opd-one-example
recipes:
  - recipe:opd-one-example
claims:
  - benchmark: "MATH-500 / AMC 2023 / AIME 2025 avg@16, R1-Distill-1.5B <- JustRL-1.5B"
    metric: "macro avg@16 accuracy"
    value: 68.5
    baseline: "Full-data OPD 69.8 at step 300; 87% of full-data gain / 69% of teacher-student gap"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04172"
    notes: "One query. Step 1000: 68.4 vs full-data 72.1 (72% of full-data gain)."
  - benchmark: "Full-data OPD state coverage (K=200 teacher-signature clusters)"
    metric: "cluster coverage"
    value: "71.5% one query / 98.9% 16 diverse queries"
    baseline: "Full-data held-out 100%"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04172"
    notes: "Most of the one-query coverage appears by step 100 (65.9%). 16 semantic clusters match full-data validation."
tags:
  - post-training
  - distillation
  - on-policy
  - data-efficiency
  - opd
  - niche
---

# One-Shot OPD (OPD-II)

## Method Overview
OPD-II is not a new loss. It is the data-minimal operating point of `method:opd`: train on one query (or a handful of semantically diverse queries) with the ordinary on-policy distillation objective. A query is consumed as the teacher-supervised prefixes its student rollouts visit. One query already covers 71.5% of the state clusters full-data OPD visits; 16 semantically distinct queries cover 98.9% and match full-data OPD and multi-teacher OPD. Alignment still takes hundreds of steps on a *fixed* set of states, so the run is limited by student absorption, not by prompt volume.

## When to Use
- Already running teacher OPD and the data-collection cost is high: start with ~16 semantically diverse queries per domain before scaling the prompt set.
- Diagnosing whether an OPD stall is data or algorithm: if one/16-shot already matches the full-data curve, collect more prompts will not help.

## When NOT to Use
- Do not replace `method:opd` as the distill default. Same loss, smaller set.
- Do not skip CISPO when labels exist, OPSA when there is no teacher, Open-MOPD when the failure is multi-teacher imbalance, or RA-OPD when the failure is misaligned teacher trajectories.

## Relation to Existing SOTA
- Niche data-efficiency note on `task:student-distillation`. Does **not** supersede `method:opd`, `method:cispo`, `method:opsa`, `method:open-mopd`, or `method:ra-opd`.
- Distinct from `method:opd2` (multi-teacher routing), which is a different node.

## Gotchas & Failure Modes
- Semantic diversity beats volume: 16 queries from 16 clusters beat 16 queries from one cluster. Order of a fixed set does not matter.
- A query the student never solves can still work; OPD's token-level teacher signal is not exhausted when the outcome reward would be.
- Content-light templates / off-domain WildChat can approach real-query baselines. Do not treat that as a reason to drop domain data when you already have it; it is a coverage result.
- Math runs in the paper used top-k advantage (k=16); other domains used sampled-token advantage. Do not mix those two curves.
