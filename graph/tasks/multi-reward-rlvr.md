---
id: task:multi-reward-rlvr
type: task
title: "Multi-Reward RLVR Aggregation"
domain: "post-training"
summary: "Group-relative RLVR when several reward components are optimized jointly: correlated large-scale rewards must not suppress smaller ones, and sparse/slow rewards must not starve under batch density imbalance."
scope: "Multi-objective GRPO-family advantage aggregation (sum-then-normalize vs reward-wise then density-correct). First hop is CorrGRPO (correlation scale) + DARA (active-group density). Not single-reward Pass@1, not a CISPO replacement."
out_of_scope:
  - "Single-turn dense math/code Pass@1 with one verifier reward (CISPO)"
  - "MoE/VL RLVR loss rather than multi-reward aggregation (SAPO)"
  - "MoE train–infer engine mismatch IS (CIS-RL)"
  - "Cancellation-aware off-policy sequence masking (CARM)"
  - "Outcome-only long-horizon agent RL (CANOPY)"
redirects:
  - when: "single-turn dense math/code Pass@1 RLVR (one verifier reward, not multi-reward aggregation)"
    to: "task:math-code-rl-dense"
  - when: "MoE/VL RLVR loss rather than multi-reward aggregation"
    to: "task:math-code-rl-moe"
  - when: "MoE/VL RLVR train–infer engine mismatch (calibrated IS on log-odds displacement)"
    to: "method:cis-rl"
  - when: "cancellation-aware off-policy response mask (absolute token log-ratios)"
    to: "method:carm"
  - when: "outcome-only long-horizon interactive agent RL"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "lexicographic priority multi-objective OPD from reward-specialist teachers (not scalarized multi-reward RL)"
    to: "method:lmopd"
current_sota:
  - method: method:corrgrpo
    as_of: "2026-10-02"
    benchmark: "Qwen2.5-Coder-7B-Instruct coding Avg Pass@1 (LeetCodeDataset / HumanEval / MBPP / LCB v6)"
    metric: "Pass@1 average vs GRPO / GDPO"
    value: "51.49 vs GRPO 47.28 / GDPO 48.88 / base 47.64"
    notes: "CorrGRPO (2609.36820). Pearson-normalizes multi-reward covariances. Dual-active with DARA (no head-to-head). Method status active. Does not replace CISPO."
  - method: method:dara
    as_of: "2026-10-02"
    benchmark: "Tool calling format compliance / math length compliance vs GDPO"
    metric: "steps to high / near-saturated compliance"
    value: "up to 26% fewer steps (tool format) / 65% fewer steps (math length); competitive final score"
    notes: "DARA (2610.00574). Inverse-sqrt density on advantage energy. Dual-active with CorrGRPO. GDPO is prior art, not a library node. Does not replace CISPO."
methods:
  - method:corrgrpo
  - method:dara
  - method:cispo
  - method:grpo
  - method:dr-grpo
  - method:carm
  - method:lmopd
last_reviewed: "2026-10-05"
tags:
  - post-training
  - rl-alignment
  - multi-reward
  - grpo
  - corrgrpo
  - dara
---

# Multi-Reward RLVR Aggregation

## Problem Definition
GRPO-family trainers often sum several reward components (format, correctness, efficiency, safety, tool schema) then std-normalize the total. Pairwise covariances make that denominator; large-scale correlated rewards dominate and shrink advantages on smaller signals. Reward-wise GDPO-style normalization removes some collapse but still leaves batch-level imbalance: sparse or nearly saturated rewards are active in fewer groups, so their advantage energy is starved. This task owns **how multi-reward advantages are aggregated**, not the Pass@1 loss and not train–infer IS.

This is **not** single-reward CISPO, not SAPO, and not CARM's off-policy sequence mask.

## Evaluation Protocol
- **Primary Benchmarks**: coding with multi-component rewards (Pass@1 + efficiency), tool calling (accuracy + format), agent utility vs security; learning-speed (steps to compliance) when density is the complaint.
- **Evaluation Pitfalls**: Do not treat a CISPO Pass@1 number as this task. GDPO is prior art in both papers and is **not** a library method. CorrGRPO and DARA have **no head-to-head**; they fix different residuals (Pearson scale vs active-group density).

## SOTA Recommendation (as of 2026-10-02)
- **Primary (correlation / scale, this task only)**: **CorrGRPO** (`method:corrgrpo`, `paper:corrgrpo` `arXiv:2609.36820`). Keep the centered total reward; replace covariance-sum std with Pearson-correlation-sum. Status `active`. Dual-active with DARA.
- **Primary (density / sparse rewards, this task only)**: **DARA** (`method:dara`, `paper:dara` `arXiv:2610.00574`). Inverse-sqrt active-group density on GDPO-style reward-wise advantages. Status `active`. Dual-active with CorrGRPO.
- **Not This Task**: `method:cispo` remains dense Pass@1; `method:sapo` remains MoE/VL; `method:cis-rl` remains train–infer IS; `method:carm` remains off-policy sequence masking.
- **Optional priority-ordered multi-teacher OPD (not this scalarized RL task)**: `method:lmopd` (`arXiv:2610.02359`) on `task:student-distillation`. Lexicographic specialist OPD, not Pearson/density GRPO aggregation. Does not replace CorrGRPO or DARA.
