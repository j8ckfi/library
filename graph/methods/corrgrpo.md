---
id: method:corrgrpo
type: method
title: "CorrGRPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-turn dense math/code Pass@1 RLVR (one verifier reward)"
    reason: "CISPO remains Pass@1; CorrGRPO is multi-reward GRPO covariance normalization"
    use_instead: "method:cispo"
  - when: "density-aware multi-reward aggregation (inverse-sqrt active-group density)"
    reason: "DARA corrects batch energy after reward-wise GDPO; CorrGRPO Pearson-normalizes a summed GRPO denominator"
    use_instead: "method:dara"
  - when: "MoE/VL RLVR loss rather than multi-reward aggregation"
    reason: "SAPO remains the MoE/VL optimizer"
    use_instead: "method:sapo"
  - when: "cancellation-aware off-policy response mask"
    reason: "CARM filters drifted rollouts; CorrGRPO rescales on-policy multi-reward advantages"
    use_instead: "method:carm"
  - when: "lexicographic priority multi-objective OPD from reward-specialist teachers (not scalarized multi-reward RL)"
    reason: "CorrGRPO Pearson-normalizes GRPO rewards; LMOPD is priority-ordered teacher OPD"
    use_instead: "method:lmopd"
assumptions:
  - "Several sequence-level reward components on a GRPO-family host. Paper: Qwen2.5-Coder 0.5B–7B coding; also tool calling and agent security. GDPO is a paper baseline, not a library method."
  - "Zero-variance reward rows/columns of the correlation matrix are zeroed, including the diagonal."
  - "Official code HKUST-KnowComp/CorrGRPO released as of 2026-10-01."
last_reviewed: "2026-10-05"
papers:
  - paper:corrgrpo
recipes:
  - recipe:corrgrpo
claims:
  - benchmark: "Qwen2.5-Coder-7B-Instruct coding Avg Pass@1 (LeetCodeDataset / HumanEval / MBPP / LCB v6)"
    metric: "Pass@1 average"
    value: "51.49"
    baseline: "GRPO 47.28 / GDPO 48.88 / base 47.64"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36820"
    notes: "Table 1. LeetCodeDataset Pass@1 24.12 vs GDPO 16.23 / GRPO 15.79. Dual-active with DARA. Not a CISPO retarget."
  - benchmark: "Qwen2.5-Coder-3B-Instruct coding Avg Pass@1"
    metric: "Pass@1 average"
    value: "45.56"
    baseline: "GRPO 43.29 / GDPO 43.41 / base 41.93"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36820"
    notes: "Table 1. Also tool-calling and agent-security domains in the paper."
tags:
  - post-training
  - rl-alignment
  - multi-reward
  - grpo
  - corrgrpo
  - active
---

# CorrGRPO

## Method Overview
Multi-reward GRPO sums components then divides by \(\sqrt{\widehat{\mathrm{Var}}(\sum_l R_l)}\). That variance is the sum of all pairwise covariances, so large-scale rewards dominate the denominator and suppress smaller signals. CorrGRPO keeps the centered total reward and replaces covariances with Pearson correlations:

\[
A^i_{\mathrm{CorrGRPO}}=\frac{\sum_l(R_l^i-\bar R_l)}{\sqrt{\sum_{l,m}\hat\rho_{lm}}+\varepsilon},\qquad\hat\rho_{lm}=\frac{\widehat{\mathrm{Cov}}(R_l,R_m)}{\sqrt{\widehat{\mathrm{Var}}(R_l)\widehat{\mathrm{Var}}(R_m)}}.
\]

Zero-variance components contribute a zero row/column. Advantage magnitudes still adapt to reward dependence; scale no longer weights the pairwise terms.

## When to Use
- Multi-objective GRPO (code + format + efficiency, tool accuracy + schema, utility vs security) where large correlated rewards drown smaller ones.

## When NOT to Use
- Single-reward Pass@1 → `method:cispo`. Sparse/slow rewards after reward-wise GDPO → `method:dara`. MoE/VL loss → `method:sapo`. Off-policy sequence mask → `method:carm`.

## Relation to Existing SOTA
- Dual-active first hop on `task:multi-reward-rlvr` beside `method:dara`. Plug-in mention on `task:math-code-rl-dense` / GRPO family. Does **not** enter CISPO `current_sota`. Does **not** replace CISPO, SAPO, or DARA. GDPO is prior art in the paper, not a library node.

## Gotchas & Failure Modes
- Needs more than one reward with nonzero within-group variance.
- Not a CISPO replacement. Single-reward groups reduce to ordinary GRPO-style std-norm (correlation matrix is 1).
- No bake-off vs DARA; pick correlation-scale vs density-energy from the failure mode, not from this table.
