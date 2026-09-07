---
id: method:opd-hard-cot-selection
type: method
title: "OPD Hard-CoT Selection"
category: "distillation"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "This is a data-selection finding on OPD, not a new distill objective; OPD remains the default"
    use_instead: "method:opd"
  - when: "the question is query diversity vs volume"
    reason: "OPD-II's ~16 semantically diverse queries is that result; this paper ranks hard/long-CoT vs easy"
    use_instead: "method:opd-one-example"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "This is still OPD; labeled RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "no teacher is available"
    reason: "Hard-CoT selection still needs teacher token distributions; teacher-free self-adaptation is OPSA"
    use_instead: "method:opsa"
assumptions:
  - "Running top-k reverse-KL OPD with a white-box teacher (paper: veRL, batch 64, 8 rollouts, top-16, 279 steps, 8x H100)."
  - "Rank a pool by A_i=(S_i+T_i)/2 from 16 student and 16 teacher rollouts. Hard is A_i<0.1. Prefer those over easy A_i>0.9."
  - "Does not change the OPD loss. Companion to paper:opd (2604.13016) and sibling to paper:opd-one-example (2609.04172)."
last_reviewed: "2026-09-07"
papers:
  - paper:opd-hard-cot-selection
recipes:
  - recipe:opd-hard-cot-selection
claims:
  - benchmark: "R1-Distill-Qwen-1.5B <- JustRL-1.5B math avg (AIME24/25 / AMC23 / MATH500 / Olympiad / Minerva)"
    metric: "average accuracy"
    value: 53.6
    baseline: "DAPO-Math-17K full-set OPD 53.7; 8 easy 51.2; 1-shot best hard π973 51.7"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05198"
    notes: "Table 2. 8 hard examples {π_874,...,π_997}. Random 1K subset also 53.6; the point is hard/long-CoT, not more prompts."
  - benchmark: "Skywork-OR1-Math-7B -> DeepSeek-R1-Distill-Qwen-7B math avg"
    metric: "average accuracy"
    value: 59.5
    baseline: "Full-set 17K 59.6; 1-shot 58.4; student 56.3"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05198"
    notes: "Table 3. 8 hard examples. Qwen3-4B -> Qwen3-1.7B-Base 8-shot 21.3 vs full-set 22.5."
tags:
  - post-training
  - distillation
  - on-policy
  - data-selection
  - opd
  - niche
---

# OPD Hard-CoT Selection

## Method Overview
OPD hard-CoT selection is not a new loss. It is a data-selection operating point of `method:opd`: keep the ordinary on-policy reverse-KL (paper: top-16) and train on the hardest queries. Score a pool with 16 student and 16 teacher rollouts, $A_i=(S_i+T_i)/2$, and take Hard $A_i<0.1$. Gains come from longer CoT paths — horizon alignment plus reflection tokens — not from high token entropy. Teacher-unsolvable hard items still work because the token-level teacher signal is not an outcome reward.

Sibling to `method:opd-one-example` (OPD-II, 2609.04172). OPD-II: one query recovers most full-data gain; ~16 *semantically diverse* queries match full-data / MOPD. This paper: *hard/long-CoT* examples drive the gain; 8 hard can match 17K. Cross-link both when choosing a small OPD set. Neither replaces OPD.

## When to Use
- Already running teacher OPD and you can score query difficulty with a few student/teacher rollouts: prefer hard/long-CoT over easy short traces.
- Diagnosing an OPD data stall: if 8 hard examples already match 17K, collecting more easy prompts will not help.

## When NOT to Use
- Distill algorithm -> `method:opd`.
- The open question is diversity vs volume (cluster representatives) -> `method:opd-one-example`.
- Labeled Pass@1 RLVR -> `method:cispo`.
- No teacher -> `method:opsa`.

## Relation to Existing SOTA
- Niche data-selection note on `task:student-distillation`. Does **not** supersede `method:opd` or `method:opd-one-example`.
- Distinct from `method:ida-opd` (sampled-token entropy plug-in) and `method:ra-opd` (trajectory filter).

## Gotchas & Failure Modes
- Do not confuse "8 hard" with OPD-II's "16 diverse". Different axes: difficulty/CoT length vs semantic coverage.
- Easy 8-shot (51.2) undershoots hard 8-shot (53.6) on the 1.5B pair. Ranking by $A_i$ is the method.
- Teacher-unsolvable hard examples are usable; do not drop them because the outcome would be zero under RLVR.
- Paper trains a fixed 279 steps (one 17K epoch). Few-shot is not fewer optimizer steps.
