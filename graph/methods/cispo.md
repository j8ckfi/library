---
id: method:cispo
type: method
title: "CISPO (Clipped IS-weight Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:math-code-rl-dense
  - task:reasoning-rl-alignment
supersedes:
  - method:dapo
do_not_use_for:
  - when: "exploration-preserving advantage shaping (surprisal + pass rate) for RLVR"
    reason: "CISPO remains Pass@1; ExPPO reshapes the existing group advantage"
    use_instead: "method:exppo"
  - when: "low-rank gradient sketches + predicted-KL step control for RL memory"
    reason: "CISPO remains Pass@1; LoGRA is an RL memory sketch"
    use_instead: "method:logra"
  - when: "critic-free PMD / Bellman telescoping RLVR (not CISPO default)"
    reason: "CISPO remains Pass@1; BPO is a matched-settings candidate that replaces the IS ratio with a complementary-token weight"
    use_instead: "method:bpo"
  - when: "Actor-then-Critic IS-aligned critic after axiomatic token credit (not CISPO default)"
    reason: "CISPO remains Pass@1; PACT is an actor-critic / credit-alignment recipe"
    use_instead: "method:pact"
  - when: "multi-stage agent capability stacking / continual learning"
    reason: "CISPO is a Pass@1 loss; ACLArena stacks heterogeneous post-train stages"
    use_instead: "task:agent-continual-learning"
  - when: "structural credit split for tool-call vs natural-language-summary tokens (not Pass@1)"
    reason: "CISPO remains Pass@1; SLCA-GRPO routes GRPO advantages on tool-calling agents"
    use_instead: "task:tool-agent-segment-credit"
  - when: "asymmetric entropy×sign exploration credit (not Pass@1 default)"
    reason: "CISPO remains Pass@1; EAPO redistributes an existing group advantage"
    use_instead: "method:eapo"
  - when: "MoE/VL RLVR train–infer engine mismatch (calibrated IS on log-odds displacement)"
    reason: "CISPO is the dense Pass@1 loss; CIS-RL caps the train–infer mismatch ratio"
    use_instead: "method:cis-rl"
  - when: "multi-model / all-fail group salvage by peer trajectory exchange"
    reason: "CISPO remains Pass@1; GRAFT replaces all-fail groups with peer traces"
    use_instead: "method:graft"
  - when: "length-scaling tax under RLVR; route solved prompts to EMA OPD"
    reason: "CISPO remains Pass@1; LSD distills solved groups against an EMA of the online policy"
    use_instead: "method:lsd"
  - when: "branchy RLVR token cost; hindsight-divergence prefix reuse"
    reason: "CISPO remains Pass@1; HDL reuses prefixes inside a GRPO-family group"
    use_instead: "method:hdl"
  - when: "multi-reward GRPO aggregation (Pearson covariance or density-aware)"
    reason: "CISPO remains Pass@1; CorrGRPO/DARA own multi-reward aggregation"
    use_instead: "task:multi-reward-rlvr"
  - when: "cancellation-aware off-policy response mask (absolute token log-ratios)"
    reason: "CISPO remains Pass@1; CARM is a sequence-level off-policy mask"
    use_instead: "method:carm"
  - when: "catastrophic strategy collapse in RLVR (coach prompting + strategy-balancing heads)"
    reason: "CISPO remains Pass@1; Mesh Learning keeps concurrent strategy heads from collapsing"
    use_instead: "method:mesh-learning"
  - when: "on-policy parameter update direction SFT (OPSFT), not Pass@1 RLVR"
    reason: "CISPO remains Pass@1; OPSFT is cheaper SFT aligned with the on-policy gradient"
    use_instead: "method:opsft"
last_reviewed: "2026-10-06"
papers:
  - paper:exppo
  - paper:logra
  - paper:minimax-m1
  - paper:scalerl
  - paper:spurious-advantage-grpo
  - paper:rlvr-group-correlation
  - paper:sharpening-tax
recipes:
  - recipe:cispo
claims:
  - benchmark: "MATH-500 / AIME 2024 / LiveCodeBench"
    metric: "pass@1 accuracy & sample efficiency"
    value: "Default SOTA for dense long-CoT reasoning RL"
    baseline: "DAPO / GRPO / PPO"
    date: "2026-08-26"
    verified: true
    notes: "MiniMax-M1 and ScaleRL recipe with clipped importance sampling."
tags:
  - post-training
  - rl-alignment
  - dense-rl
  - cispo
  - sota
---

# CISPO (Clipped IS-weight Policy Optimization)

## Method Overview
CISPO (Clipped IS-weight Policy Optimization) establishes the state-of-the-art reinforcement learning standard for dense reasoning models:
1. **Clipped IS-Weight Formulation**: Clips \(\text{sg}(\text{clip}(\rho))\) directly on the importance sampling weight (with stop-gradient) rather than standard PPO-surrogate objective clipping, ensuring every token (including rare forks) receives a non-zero gradient.
2. **Dense Reasoning Alignment**: Maximizes verifiable pass@1 accuracy across competitive math and programming benchmarks.

## Implementation & Frameworks
- Repository: `https://github.com/MiniMax-AI/MiniMax-M1`
- Supported in NeMo-RL and ms-swift via `loss_type=cispo`.

## When to Use
- Default SOTA optimizer for dense model math and code reasoning RL.

## Relation to Existing SOTA
- Remains the dense math/code RLVR default for Pass@1 when labels exist. GRPO inside `method:j-zero` is that method's inner self-play optimizer, not a change to this default.
- Optional critic-free PMD candidate (`method:bpo`): Bellman telescoping; complementary-token mismatch weight. Matched AIME24–26 Avg@32 50.5% vs this method 47.4% on Qwen3-30B-A3B-Base. Does not replace CISPO. No public code.
- Optional Actor-then-Critic IS (`method:pact`): axiomatic token credit then critic IS. Does not replace CISPO. Empty GitHub stub.
- For Pass@K / reasoning coverage or a no-backward memory budget, use `method:es-reasoning` on `task:passk-reasoning-coverage`. That is not a GRPO revival and does not replace CISPO.
- Optional token-filter plug-in: `method:gmts`. Example-reweight plug-in: `method:diem`. First-mistake process credit: `method:cliff` (not a PRM; does not replace VeriGate). Sample-level GRPO/OPSD router: `method:self-routing`. Adaptive IS clip: `method:gapo` (does not replace CISPO). RLVR+self-OPD loop: `method:rise` (does not replace CISPO, OPD, or OPSA). Tool-using pre-RL OPKD: `method:pta` (does not replace CISPO). Teacher-free unlabeled train-time self-adaptation: `method:opsa`. Olympiad NL proof TTC: `method:nemotron-imo-gold` (does not replace CISPO). None of these replace CISPO when labels exist.

## Supersession
- Supersedes `method:dapo` as the dense RL default (DAPO remains as a systems reference).

## Gotchas & Failure Modes
- Group-relative magnitude $|\hat{A}|=\sqrt{n^-/n^+}$ can reward lucky guesses on bounded-answer items, bounded sub-cases inside open math (~56% of MATH-7.5K by answer shape), and search-agent trajectories that cash out via outcome-only exact match (`paper:spurious-advantage-grpo`). CISPO still clips IS weights, not this composition-dependent scale. Do not revive GRPO or promote SignBalance over CISPO.
- Within-group verifier errors are correlated (`method:rlvr-group-correlation`, ρ≈0.53, Kish n_eff≈1.70 at k=8). Hygiene, not a CISPO replacement.
