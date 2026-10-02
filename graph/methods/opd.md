---
id: method:opd
type: method
title: "OPD (On-Policy Distillation)"
category: "distillation"
status: sota
sota_for:
  - task:student-distillation
supersedes:
  - method:on-policy-distillation
do_not_use_for:
  - when: "latent OPD collapse / last-layer crossfade into token OPD"
    reason: "OPD remains the matching default; LastOPD is a latent-collapse schedule on reverse top-k OPD"
    use_instead: "method:lastopd"
  - when: "Direct-OPD / weak-to-strong policy-shift token selection by teacher–ref JSD"
    reason: "OPD is strong-teacher matching; S2D-OPD is a Direct-OPD keep-mask"
    use_instead: "method:s2d-opd"
  - when: "sample-efficient / off-policy OPD (Huber quadratic matching + replay)"
    reason: "OPD remains the matching default; LSPD is least-square + entropy with optional replay"
    use_instead: "method:lspd"
  - when: "maximal-coupling-routed teacher supervision / TRB accept-correction routing"
    reason: "OPD is student-rollout reverse-KL; SAKI routes TRB coupling events"
    use_instead: "method:saki"
  - when: "adapting the OPD teacher on student prefixes / off-policy teacher, not frozen-teacher OPD"
    reason: "OPD keeps a frozen teacher; SCOUT RL-adapts the teacher on student prefixes"
    use_instead: "method:scout"
  - when: "distilling RL gains via representation residuals rather than logits"
    reason: "OPD is reverse-KL matching; RIDE extrapolates RL-induced hidden-state residuals"
    use_instead: "method:ride"
  - when: "multi-task OPD and teacher can be wrong on some tasks"
    reason: "OPD ignores joint outcomes; DuoOPD gates direction and teacher support from who was correct"
    use_instead: "method:duoopd"
  - when: "multi-turn agent OPD at pivotal early mistakes (prevent reverse-KL + recover forward-KL)"
    reason: "OPD is matching; PivotOPD is prevent+recover at pivotal turns"
    use_instead: "method:pivotopd"
  - when: "act-first / reason-later multi-turn OPD (inverse dynamics + async full-response distill)"
    reason: "OPD waits for think-then-act; ActFirst-OPD acts via inverse dynamics then distills asynchronously"
    use_instead: "method:actfirst-opd"
last_reviewed: "2026-10-01"
papers:
  - paper:opd
  - paper:opd-one-example
  - paper:opd-hard-cot-selection
  - paper:opd-eos
  - paper:opd-same-family-scaling
recipes:
  - recipe:opd
claims:
  - benchmark: "GSM8k / HumanEval / MT-Bench Student Distillation"
    metric: "distillation task accuracy"
    value: "Default SOTA for student distillation"
    baseline: "GKD / Offline SFT"
    date: "2026-08-26"
    verified: true
    notes: "Generalized divergence matching on student-generated rollouts."
tags:
  - post-training
  - distillation
  - on-policy
  - opd
  - sota
---

# OPD (On-Policy Distillation)

## Method Overview
OPD (On-Policy Distillation) is the state-of-the-art framework for distilling large frontier teachers into compact local student models:
1. **Student Rollout Generation**: Samples token sequences from the *student* policy rather than teacher traces.
2. **Generalized Divergence Scoring**: Evaluates student tokens using teacher forward log-probabilities with reverse or mixed KL divergence.

## When to Use
- Default SOTA method for distilling reasoning and conversational capabilities into small student models.

## Relation to Existing SOTA
- Remains the single-teacher student-distillation default. For a privileged same-model teacher that sees the gold solution, use `method:vista` instead of vanilla OPSD; that does not replace OPD.
- Optional filter when a verifier is available: `method:ra-opd`. Sampled-token pass@k entropy plug-in: `method:ida-opd`. Teacher-free train-time self-adaptation is `method:opsa` and does not replace OPD when a strong teacher is the goal.
- Data-efficiency companion (`paper:opd-one-example`, `method:opd-one-example`): OPD is data-overfed but algorithm-starved. One query recovers most full-data gain; ~16 semantically diverse queries match full-data / MOPD. Prefer semantic diversity over volume. Does not change this method's status.
- Hard-CoT selection sibling (`paper:opd-hard-cot-selection`, `method:opd-hard-cot-selection`): hard/long-CoT examples drive gains, not high token entropy; 8 hard can match 17K. Does not replace this method or OPD-II.
- Self-extrapolating teacher (`method:rise`): no external teacher; needs RLVR grounding. Does not replace OPD when a white-box teacher is the goal.
- Tool-using OPKD (`method:pta`): student-induced but teacher-committed rollouts; tool calls execute only after the teacher verifies the turn. Does not replace OPD for plain text distillation.
- Prompt-level teacher gate (`method:tgopd`): verifier-scored teacher probes then exclusive OPD vs GRPO. Does not replace this method.
- Sparse token-budget plug-in (`method:sparse-opd-supervision`): 1–2 tokens per trajectory (~0.05%) can match/beat full-token OPD. Does not replace this method.
- Sparse-OPD reliability plug-in (`method:ier-opd`): information-efficiency ratio (gradient SNR under an optimal scalar baseline) fused with usefulness. 0.1%–1% budgets match/exceed full OPD. Does not replace this method.
- Sequential stack (`method:opd-then-rlvr`): OPD then RLVR beats joint one-step fusion when both are used. Does not replace this method or CISPO.
- Optional TSD calibration (`method:cal-opd`): residual discrepancy beyond a probed teacher-self-deviation region. Signal calibration during OPD. Does not replace this method, VISTA, or RetireOPD.
- Latent-collapse schedule (`method:lastopd`): last-layer pre-head latent term, then a ~10-step crossfade into token OPD. Does not replace this method. Same-lineage latent-only can stay on OPRD-Vanilla.
- Direct-OPD JSD keep-mask (`method:s2d-opd`): keep top ~10% student states by teacher–reference JSD. Does not replace this method.
- Multi-stage agent continual learning (`method:aclarena`) compares MMOPD / SDFT / merge then proposes MLE. Does not replace this method or Open-MOPD. Label-routed MOPD of SWE category experts is `method:category-aware-swe-experts`.

## Gotchas & Failure Modes
- Do not scale the prompt set when 16-shot already matches full-data OPD. The remaining gap is student absorption / step-efficiency (`method:opd-one-example`).
- Prefer hard/long-CoT over easy short traces when ranking a small set (`method:opd-hard-cot-selection`). Do not treat that as OPD-II's diversity finding.
- Sampled-token OPD can raise pass@1 while flattening pass@k. That is `method:ida-opd`, not more data.
- Teacher/student EOS ids can disagree even when declared stop sets match (`paper:opd-eos`, `arXiv:2609.20511`). The teacher puts stop mass on a token the student never samples; length inflates into the budget. Aligning decode stops is not enough. Score equivalent EOS tokens as one semantic stop (`method:opd-eos`, `EOS_MODE=semantic_class`). A later K2-Horizon inflation mode can remain after alignment. Does not replace this method.
- Same-family OPD scaling (`paper:opd-same-family-scaling`, `arXiv:2609.32722`): early useful-transfer is linear in \(\sqrt{\mathrm{KL}}\) from the student init; peak gold score improves with teacher scale only up to roughly the student's scale; at a matched score, smaller teachers transfer better. Claim note, not a new method.

## Supersession
- Supersedes `method:on-policy-distillation` (GKD baseline) as the primary distillation reference.
