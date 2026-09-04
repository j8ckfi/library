---
id: method:draco
type: method
title: "DRACO (Dynamic Rubric Credit Optimization)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "a programmatic checker exists and sparse outcome RL is enough"
    reason: "CANOPY is the outcome-only sufficiency protocol; DRACO is for when there is no checker"
    use_instead: "method:canopy"
  - when: "variable tool latency / async stragglers is the bottleneck"
    reason: "SAO is the async default; DRACO is rubric credit, not replay"
    use_instead: "method:sao"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "Dense labeled RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "the problem is folding a long tool trajectory"
    reason: "FoldGRPO folds context; DRACO redistributes rubric scores"
    use_instead: "method:foldgrpo"
assumptions:
  - "No ground-truth success signal at train time. A frozen judge can propose and score rubrics and cite responsible steps."
  - "Paper: Qwen3.6-27B and Qwen2.5-32B-Instruct LoRA GRPO, 8x H100, B=16, G=6, GPT-5.4 judge. AppWorld train 90 tasks. Ground-truth tests used only at eval."
last_reviewed: "2026-09-04"
papers:
  - paper:draco
recipes:
  - recipe:draco
claims:
  - benchmark: "AppWorld Test-Normal TGC p^1, Qwen3.6-27B"
    metric: "TGC pass^1"
    value: 85.3
    baseline: "Base 69.4 / outcome-reward GRPO 80.0 / static-rubric 81.1"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04094"
    notes: "Table 2. +15.9 vs base, +5.3 vs verifier-trained GRPO, without using verifiers at train time. SGC p^1 70.6."
  - benchmark: "τ-bench Banking SR p^1, Qwen3.6-27B zero-shot"
    metric: "success rate pass^1"
    value: 20.4
    baseline: "Base 15.8 / outcome-reward 17.6"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04094"
    notes: "Self-judge variant 21.1 SR, 81.1 AppWorld TN TGC."
tags:
  - post-training
  - agentic
  - outcome-blind
  - rubrics
  - draco
  - active
---

# DRACO (Dynamic Rubric Credit Optimization)

## Method Overview
DRACO is outcome-blind long-horizon agent RL. Differentiated from `method:canopy`: CANOPY shows sparse *programmatic* outcome RL can suffice if you explore more and drift less; DRACO is what to do when there is **no** checker.

1. A frozen judge proposes criteria from the instruction, extends them from each sampled trajectory, merges, and drops criteria nobody failed.
2. Reward $R_i=(p_i-f_i)/(p_i+f_i)$ from applicable pass/fail counts. GRPO standardizes to $A_i$.
3. Each criterion cites steps. Step quality $Q_j$ is the pass fraction of citing criteria. Winners put weight on high-$Q$ steps, losers on low-$Q$ steps. Per-step advantage $a_j=A_i N w_j/(n_j\sum_k w_k)$ conserves $\sum_j n_j a_j=A_i N$ and never flips sign.

No learned attribution module. Gap tokens (tool echoes) get no credit.

## When to Use
- Long-horizon tool agents (customer support, open-ended ops) with no unit-test oracle.
- When a trajectory-level rubric exists but uniform GRPO credit wastes successful traces that contain bad steps (and vice versa).

## When NOT to Use
- Checker exists -> `method:canopy` (or SAO if the issue is async latency).
- Dense math/code -> `method:cispo`.
- Context folding -> `method:foldgrpo`.

## Relation to Existing SOTA
- Active sibling on `task:outcome-only-long-horizon-agent-rl`. Does **not** supersede `method:canopy`, `method:sao`, `method:cispo`, or `method:foldgrpo`. CANOPY remains current_sota when a verifier exists.

## Gotchas & Failure Modes
- Judge cost is the practical tax (paper: GPT-5.4 at T=0.1 for generate+score). Self-judge is weaker on AppWorld, slightly stronger on τ-bench.
- Overlapping criteria double-count mistakes; the paper instructs mutually exclusive criteria.
- If the rubric cites no steps, fall back to uniform GRPO.
- Do not compare DRACO's 85.3 TN TGC on Qwen3.6-27B to CANOPY's 86.9 on Qwen3-14B as a bake-off: different backbone, protocol (p^1 over 3 evals vs leaderboard mean@1), and reward access (blind vs unit tests).
