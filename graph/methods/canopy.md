---
id: method:canopy
type: method
title: "CANOPY (Coverage-Anchored On-Policy RL)"
category: "rl-alignment"
status: sota
sota_for:
  - task:outcome-only-long-horizon-agent-rl
supersedes: []
do_not_use_for:
  - when: "variable tool latency / async stragglers is the bottleneck"
    reason: "CANOPY is coverage+anti-drift for sparse outcome groups, not an async replay engine"
    use_instead: "method:sao"
  - when: "the problem is folding a long tool trajectory into a small active context"
    reason: "FoldGRPO is the folding default; CANOPY does not fold history"
    use_instead: "method:foldgrpo"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "Dense labeled RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "build a SWE / issue-to-patch harness rather than train a policy"
    reason: "mini-SWE-agent is the harness; CANOPY used it as the SWE eval scaffold"
    use_instead: "method:mini-swe-agent"
  - when: "production harness kernel (rewind, sandbox, remote, TUI)"
    reason: "That shelf is omp2"
    use_instead: "method:omp2-harness"
  - when: "no programmatic checker exists and the reward must come from process criteria"
    reason: "DRACO is the outcome-blind rubric sibling"
    use_instead: "method:draco"
assumptions:
  - "A held-out unit-test / patch verifier exists. Sparse fully-correct reward, not pass-fraction."
  - "Paper: Qwen3-14B on AppWorld train split (90 tasks), veRL, n=32, 50 turns / 32k train, 100 turns / 61k test, KL β=1e-4, lr 3e-6, 90 steps, hardest tier kept."
  - "SWE transfer retunes n=16, KL 1e-2, 80 turns / 36k, and -0.2 for no-patch terminals. Not a literal hyperparameter copy."
last_reviewed: "2026-09-04"
papers:
  - paper:canopy
recipes:
  - recipe:canopy
claims:
  - benchmark: "AppWorld Test-Normal / Test-Challenge TGC, Qwen3-14B, Feb 2026 leaderboard"
    metric: "TGC mean@1"
    value: "86.9 / 67.6"
    baseline: "ESAT Qwen3-14B 75.2 / 58.5; LOOP Qwen2.5-32B 72.6 / 47.2; SAGE 72.0 / 50.1"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.01245"
    notes: "SGC 80.4 / 50.4. Training-free frontier systems (HCL-GP, ASSAY) are not trained-policy comparators."
  - benchmark: "SWE-bench Verified, Qwen3.5-9B, mini-swe-agent, matched 80-turn/36k budget"
    metric: "resolve rate mean@4"
    value: 47.9
    baseline: "Base 31.3; Δ +16.6. Enlarged budget 50.2 / best@4 60.8"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.01245"
    notes: "Table 4. Repository-level de-duplication vs Verified. Five missing Docker images scored 0."
tags:
  - post-training
  - agentic
  - outcome-only
  - canopy
  - sota
---

# CANOPY (Coverage-Anchored On-Policy RL)

## Method Overview
CANOPY is a protocol, not a new optimizer. It keeps GRPO's group-relative advantage and attacks two failures of outcome-only agent RL:

1. **Explore more (signal starvation).** Sparse reward yields gradient only when a same-task group mixes success and failure. Size $n$ from a pilot $\hat{p}_{\min}$ so $P_{\mathrm{sig}}\approx 1-(1-p)^n$ hits a target coverage; keep the hardest tasks; do not cap per-turn generation.
2. **Drift less.** One update per rollout batch (no stale mini-batches); sparse fully-correct reward (no pass-fraction proxy); pooled token-mean loss over action tokens only; KL to the frozen base; quarantine serving-layer faults so they do not look like agent failures.

Test-time budget transfer raises turns and context without search. Differentiated from `method:draco`: CANOPY assumes a programmatic checker; DRACO redistributes rubric scores when none exists.

## When to Use
- Long-horizon interactive agents with a unit-test / patch verifier, where prior work dropped hard tasks or added dense rewards because groups of n≤8 were silent.
- Transferring the same coverage+anti-drift principles to SWE repair (retune n, KL, horizon; do not copy AppWorld HPs).

## When NOT to Use
- Async tool-latency training -> `method:sao`.
- Context folding -> `method:foldgrpo`.
- Single-turn math/code -> `method:cispo`.
- Choosing a harness -> `method:mini-swe-agent`.
- No checker -> `method:draco`.

## Relation to Existing SOTA
- SOTA only for `task:outcome-only-long-horizon-agent-rl`. Does **not** supersede `method:sao`, `method:foldgrpo`, `method:cispo`, `method:mini-swe-agent`, `method:omp2-harness`, or `method:draco`.

## Gotchas & Failure Modes
- Dense pass-fraction rewards manufacture within-group variance but can reward wrong approaches. CANOPY's claim is that scaled exploration removes the need to densify.
- Importance clip is inert when there is one update per batch; do not read a CISPO-style clip as the method.
- SWE HPs are not AppWorld HPs. Copying n=32 / β=1e-4 onto expensive SWE episodes is a waste of GPU-weeks.
- Leaderboard TGC is mean@1 at 100 turns / 61k; do not compare to training-budget mean@4 without saying so.
