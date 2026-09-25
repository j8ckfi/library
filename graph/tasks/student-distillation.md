---
id: task:student-distillation
type: task
title: "Small Local Student Distillation from Strong Teacher"
domain: "post-training"
summary: "Distilling reasoning and conversational capabilities from multi-hundred-billion parameter frontier teachers into small local student models."
redirects:
  - when: "privileged OPD TSD calibration (residual discrepancy during OPD, not teacher retirement)"
    to: "method:cal-opd"
  - when: "Adaptive Retirement of a privileged self-OPD teacher then pure agent RL"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "sparse OPD token selection by gradient-estimation reliability (IER), not usefulness keep-mask only"
    to: "method:ier-opd"
  - when: "distill optimized-harness behaviors into weights under a fixed target harness (action-space mismatch)"
    to: "task:harness-distillation"
  - when: "multi-stage agent capability stacking (MMOPD / SDFT / LoRA experts, not Open-MOPD default)"
    to: "task:agent-continual-learning"
  - when: "label-routed multi-teacher OPD of SWE category experts"
    to: "task:swe-agent-category-expert-rl"
  - when: "latent OPD collapse / last-layer crossfade into token OPD"
    to: "method:lastopd"
  - when: "Direct-OPD / weak-to-strong policy-shift token selection by teacher–ref JSD"
    to: "method:s2d-opd"
current_sota:
  - method: method:opd
    as_of: "2026-08-26"
    benchmark: "GSM8k / HumanEval / MT-Bench Student Evaluation"
    metric: "task accuracy vs teacher parity"
    value: "Default SOTA for single-teacher student distillation"
    notes: "OPD 2604.13016 generalized divergence matching on student rollouts."
  - method: method:open-mopd
    as_of: "2026-08-28"
    benchmark: "Multi-Teacher Capability Integration (SmolLM3-3B Benchmark)"
    metric: "oracle ensemble headroom recovery"
    value: "83.4% headroom recovery in a single deployable student"
    notes: "Open-MOPD (2608.19098) fixes multi-teacher imbalance with token-share balancing and gap-aware dynamic budgeting."
methods:
  - method:opd
  - method:open-mopd
  - method:opdvr
  - method:vista
  - method:tropd
  - method:stable-opd
  - method:opd2
  - method:w2s-opd
  - method:nemotron-cascade-2
  - method:on-policy-distillation
  - method:ra-opd
  - method:opd-one-example
  - method:opd-hard-cot-selection
  - method:ida-opd
  - method:opsa
  - method:rise
  - method:pta
  - method:tgopd
  - method:sparse-opd-supervision
  - method:opd-then-rlvr
  - method:routeopd
  - method:tv-opd
  - method:oprd
  - method:opd-eos
  - method:retireopd
  - method:cal-opd
  - method:ier-opd
  - method:aclarena
  - method:category-aware-swe-experts
  - method:lastopd
  - method:s2d-opd
last_reviewed: "2026-09-25"
tags:
  - post-training
  - distillation
  - on-policy
  - opd
---

# Small Local Student Distillation from Strong Teacher

## Problem Definition
Training small local students (1B–8B) from large teacher models (70B–405B) with generalized on-policy divergence matching.

## SOTA Recommendation (as of 2026-09-09)
- **Single-Teacher Distillation Default**: **OPD** (`method:opd`, `paper:opd` `arXiv:2604.13016`). Unchanged.
- **Multi-Teacher Student Distillation Default**: **Open-MOPD** (`method:open-mopd`, `paper:open-mopd` `arXiv:2608.19098`) for token-share balancing, gap-aware dynamic budget allocation, and student reward refresh across specialized teacher models.
- **Related alternative**: Use `method:vista` instead when the teacher is a privileged same-model copy that sees the gold solution (not a larger frozen teacher). OPD remains the student-distillation default.
- **Optional teacher-OPD filter**: `method:ra-opd` (`arXiv:2608.27960`) keeps trajectories with sign-agree teacher return vs outcome reward. Does not replace OPD.
- **Optional sampled-token entropy plug-in**: `method:ida-opd` (`arXiv:2608.29846`) keeps entropy-expanding $A_y$ and shrinks $\mathcal{I}_H<0$ by $|q-p|/(q+p)$. Does not replace OPD or CISPO.
- **Optional probability-transport plug-in**: `method:routeopd` (`arXiv:2609.08337`) pairwise log-odds transport vs sampled reverse-KL. Does not replace OPD.
- **Optional TV-shaped stability plug-in**: `method:tv-opd` (`arXiv:2609.08341`) sign of token advantages plus a shared TV scale. Relate to RA-OPD / TrOPD / Stable-OPD without supersession.
- **Optional reverse distillation (weak-to-strong)**: `method:oprd` (`arXiv:2609.08798`, code raymin0223/on_policy_reverse_distillation) amplifies verifier-supported student gradients along the teacher policy-shift. Distinct from `method:w2s-opd` (matching). Does not replace OPD or CISPO.
- **Data-efficiency note**: `method:opd-one-example` (`arXiv:2609.04172`) — one query recovers most full-data OPD; ~16 diverse queries ≈ full-data / MOPD. Does not replace OPD.
- **Data-selection sibling**: `method:opd-hard-cot-selection` (`arXiv:2609.05198`) — hard/long-CoT examples drive OPD gains (not high token entropy); 8 hard can match 17K. Does not replace OPD or OPD-II.
- **Related self-extrapolating teacher**: `method:rise` (`arXiv:2609.05295`) synthesizes an OPD teacher from the student's RLVR trajectory. No external teacher. Does not replace OPD, CISPO, or OPSA.
- **Tool-using OPKD**: `method:pta` (`arXiv:2609.04773`, EMNLP 2026 Main) — student-induced but teacher-committed rollouts; tool calls execute only after the teacher verifies the turn. Pre-RL distill for Search-R1 / DeepEyes. Does not replace OPD for text-only distillation.
- **Optional prompt-level teacher gate**: `method:tgopd` (`arXiv:2609.02998`) admits dense OPD only after verifier-scored teacher probes pass; else GRPO. Sibling of RA-OPD / IDA-OPD / VISTA. Does not replace OPD, CISPO, OPSA, or Open-MOPD.
- **Optional sparse token-budget plug-in**: `method:sparse-opd-supervision` (`arXiv:2609.04565`) supervises 1–2 tokens per trajectory (~0.05%) and can match/beat full-token OPD. Does not replace OPD or CISPO.
- **Optional stacking order when both OPD and RLVR will run**: `method:opd-then-rlvr` (`arXiv:2609.04108`) — OPD then RL, not joint one-step fusion. Does not replace OPD or CISPO.
- **No teacher / no labels**: `method:opsa` on `task:teacher-free-on-policy-self-adaptation`. Does not replace OPD when a strong teacher is the goal.
- **Gotcha (EOS mismatch)**: `method:opd-eos` / `paper:opd-eos` (`arXiv:2609.20511`). Teacher/student stop ids can disagree even when declared stop sets match; length inflates under OPD. Semantic-class EOS is the fix. Does not replace OPD.
- **Optional TSD calibration plug-in**: `method:cal-opd` (`arXiv:2609.21619`) estimates the teacher self-deviation region with positive+negative privileged probes and keeps residual discrepancy (~52–65%) as the OPD advantage. Signal calibration during OPD, not teacher retirement. Does not replace OPD, VISTA, or RetireOPD.
- **Optional sparse-OPD reliability plug-in**: `method:ier-opd` (`arXiv:2609.24432`) ranks tokens by information-efficiency ratio (gradient signal-to-noise under an optimal scalar baseline) and fuses with usefulness scores. 0.1%–1% budgets match/exceed full OPD. Does not replace OPD, CISPO, sparse-opd-supervision, IDA-OPD, or Cal-OPD.
- **Optional latent-collapse plug-in**: `method:lastopd` (`arXiv:2609.28845`) applies latent loss only at the last-layer pre-LM-head state and crossfades into reverse top-k OPD over ~10 steps. MATH-500 +5.55 / +4.02 vs token-only OPD on Qwen3-4B/8B → 1.7B. Same-lineage latent-only OPRD-Vanilla can already work; do not retarget OPD or Open-MOPD. Cal-OPD remains TSD calibration.
- **Optional Direct-OPD JSD keep-mask**: `method:s2d-opd` (`arXiv:2609.29142`) ranks student states by teacher–reference JSD and keeps the top ~10% per response. +0.95 mean held-out Acc over dense Direct-OPD (7/8 settings). Not standard strong-teacher OPD.
- **Not this task**: Adaptive Retirement of a privileged self-OPD teacher in agent RL is `method:retireopd` on `task:outcome-only-long-horizon-agent-rl`. Distilling optimized-harness behaviors into weights under a fixed target harness is `method:harness-zero` on `task:harness-distillation`. Multi-stage agent continual learning (MMOPD / SDFT / MLE) is `method:aclarena` on `task:agent-continual-learning` and does not retarget Open-MOPD. Label-routed MOPD of SWE category experts is `method:category-aware-swe-experts` on `task:swe-agent-category-expert-rl`.

