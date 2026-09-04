---
id: method:gmts
type: method
title: "GMTS (Gradient Magnitude-based Token Selection)"
category: "rl-alignment"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code RLVR optimizer"
    reason: "GMTS is a token-filter add-on, not an RL objective; CISPO remains the Pass@1 default"
    use_instead: "method:cispo"
  - when: "the goal is Pass@K / coverage / no-backward RLVR"
    reason: "That shelf is ES-reasoning, not token truncation"
    use_instead: "method:es-reasoning"
  - when: "reweighting whole examples by gradient alignment"
    reason: "That is DIEM; GMTS filters tokens"
    use_instead: "method:diem"
assumptions:
  - "Host RLVR already computes per-token entropy, importance ratio, advantage, and clip indicator (GRPO/DAPO/CISPO-family)."
  - "Paper evaluates plug-in to GRPO and DAPO on Qwen2.5-Math/Coder 1.5B/7B and Qwen3-8B; default keep ratio is top 20%."
last_reviewed: "2026-09-01"
papers:
  - paper:gmts
recipes:
  - recipe:gmts
claims:
  - benchmark: "Qwen2.5-Math-7B five-bench math avg@16"
    metric: "average accuracy"
    value: 50.14
    baseline: "DAPO 48.47 / DAPO+ETS 48.81; GRPO+GMTS 49.84 vs GRPO+ETS 46.43"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30632"
    notes: "Tables 1-2. About 1-3pp over entropy-only top-20% selection."
  - benchmark: "Qwen3-8B DAPO six-bench math avg@16"
    metric: "average accuracy"
    value: 56.08
    baseline: "DAPO 53.71 / DAPO+ETS 54.23"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30632"
    notes: "Table 3. AIME2024 39.79 vs ETS 34.58 vs DAPO 33.33."
tags:
  - post-training
  - rlvr
  - token-selection
  - gmts
  - niche
---

# GMTS (Gradient Magnitude-based Token Selection)

## Method Overview
GMTS is a plug-in token filter for RLVR. Entropy-only top-20% selection (ETS) tracks gradient magnitude *within* one answer but not *across* answers whose advantages and clip flags differ. Score

\[
\delta_{i,t}=\lvert E_{i,t}\cdot\omega_{i,t}(\theta)\rvert
\]

where $E_{i,t}$ is token entropy and $\omega_{i,t}$ is the PPO-style coefficient (importance ratio $\times$ advantage $\times$ clip indicator, plus KL terms if present). Keep the top-$\rho$ tokens in the batch by $\delta$ (default $\rho=0.2$) and average the RL loss only over those tokens.

## When to Use
- Optional add-on when already running GRPO, DAPO, or a CISPO-family trainer with token truncation / high-entropy masks.
- When ETS helps on some groups and hurts on others because advantages differ.

## When NOT to Use
- Do not pick GMTS instead of `method:cispo` as the dense RLVR algorithm.
- Do not revive GRPO as the library default just because the paper plugs into GRPO/DAPO.

## Relation to Existing SOTA
- Niche token-filter on `task:math-code-rl-dense`. Does **not** supersede `method:cispo`. DAPO stays a systems reference.

## Gotchas & Failure Modes
- Bottom-k GMTS is worse than bottom-k ETS; the high-$\delta$ tail is the useful set.
- Default $\rho=0.2$; the paper is not extremely ratio-sensitive in $\{0.1,0.2,0.5,0.7,0.9\}$ but 20% is the reported default.
- Requires the clip/advantage coefficient already in the trainer; do not backprop through $\delta$ as a learned gate.
