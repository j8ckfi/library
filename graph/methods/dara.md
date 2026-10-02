---
id: method:dara
type: method
title: "DARA"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-turn dense math/code Pass@1 RLVR (one verifier reward)"
    reason: "CISPO remains Pass@1; DARA reweights multi-reward GDPO-style advantages by active-group density"
    use_instead: "method:cispo"
  - when: "Pearson-normalize multi-reward GRPO covariances (large correlated rewards suppress smaller ones)"
    reason: "CorrGRPO rescales the summed-GRPO denominator; DARA is density-aware aggregation after reward-wise norm"
    use_instead: "method:corrgrpo"
  - when: "MoE/VL RLVR loss rather than multi-reward aggregation"
    reason: "SAPO remains the MoE/VL optimizer"
    use_instead: "method:sapo"
  - when: "cancellation-aware off-policy response mask"
    reason: "CARM filters drifted rollouts; DARA reweights on-policy multi-reward energy"
    use_instead: "method:carm"
assumptions:
  - "Several sequence-level rewards on a GDPO-style host (reward-wise group norm, then aggregate). Paper: Qwen2.5-1.5B/3B tool calling (ToolRL) and math length+correctness."
  - "Default is DARA-Asym (amplify positive advantages of low-density rewards; keep negatives at GDPO scale). Cap w_max on inverse-sqrt density."
  - "Official code zhaihaotian/DARA. GDPO is prior art, not a library method."
last_reviewed: "2026-10-02"
papers:
  - paper:dara
recipes:
  - recipe:dara
claims:
  - benchmark: "Tool calling format compliance vs GDPO (Qwen2.5-1.5B/3B-Instruct, ToolRL)"
    metric: "training steps to high format compliance"
    value: "up to 26% fewer steps"
    baseline: "GDPO (reward-wise group norm, then aggregate)"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.00574"
    notes: "Abstract. Competitive final BFCL-v4 accuracy/format. Dual-active with CorrGRPO. Not a CISPO retarget."
  - benchmark: "Mathematical reasoning length compliance vs GDPO"
    metric: "training steps to near-saturated length compliance"
    value: "up to 65% fewer steps"
    baseline: "GDPO"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.00574"
    notes: "Abstract. Learning-speed claim; final performance remains competitive with GDPO."
tags:
  - post-training
  - rl-alignment
  - multi-reward
  - dara
  - density
  - active
---

# DARA

## Method Overview
Reward-wise GDPO normalization equalizes each *active group*, but batch advantage energy \(E_k=\sum_{i,j}(A_k^{(i,j)})^2\) still scales with active-group density \(\pi_k\) (fraction of groups where reward \(k\) has nonzero relative advantages). DARA matches energy to the densest reward with \(w_k=\min(w_{\max},\sqrt{\pi_{\mathrm{ref}}/\pi_k})\) for \(\pi_k>0\). DARA-Asym (default) applies the extra weight only to positive advantages so conflicting negatives are not amplified. Then sum and batch-normalize as in GDPO. The policy surrogate is unchanged.

## When to Use
- Multi-reward RL where some objectives (format, length) are sparse or saturate while others stay active every group.

## When NOT to Use
- Single-reward Pass@1 → `method:cispo`. Correlated large-scale rewards on *summed* GRPO → `method:corrgrpo`. MoE/VL loss → `method:sapo`. Off-policy sequence mask → `method:carm`.

## Relation to Existing SOTA
- Dual-active first hop on `task:multi-reward-rlvr` beside `method:corrgrpo`. Plug-in mention on `task:math-code-rl-dense`. Does **not** enter CISPO `current_sota`. GDPO is prior art only (not a library node). Does **not** replace CISPO or CorrGRPO.

## Gotchas & Failure Modes
- Needs reward-wise group statistics (GDPO-style), not only a summed scalar.
- Uncapped inverse-sqrt can explode when a reward is active in one group; keep \(w_{\max}\).
- DARA-Sym amplifies both signs and can worsen reward conflict; the paper default is Asym.
- No bake-off vs CorrGRPO.
