---
id: method:bpo
type: method
title: "BPO (Bellman Policy Optimization)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "established dense Pass@1 default"
    reason: "CISPO remains the Pass@1 first hop; BPO is a critic-free PMD candidate under matched math RLVR"
    use_instead: "method:cispo"
  - when: "MoE / VL RLVR loss"
    reason: "SAPO remains the MoE/VL default; BPO's bake-off is Qwen3-30B-A3B-Base math, not SAPO's VL/MoE protocol"
    use_instead: "method:sapo"
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains async RL; BPO is a single-turn math loss"
    use_instead: "method:sao"
assumptions:
  - "Terminal-reward RLVR. Group-relative advantages as in GRPO. Practical loss replaces the token IS ratio with a complementary-token mismatch weight."
  - "Paper: Qwen3-30B-A3B-Base, English DAPO-Math-17k, 400 steps, 256 prompts × group 16, max response 16384, eight optimizer updates per rollout batch."
  - "No public GitHub as of 2026-09-23. Reimplement the loss; do not invent a CISPO replacement."
last_reviewed: "2026-09-23"
papers:
  - paper:bpo
recipes:
  - recipe:bpo
claims:
  - benchmark: "AIME 2024–2026 Avg@32, Qwen3-30B-A3B-Base, DAPO-Math-17k, matched settings"
    metric: "peak mean Avg@32"
    value: "50.5%"
    baseline: "CISPO 47.4% (+3.1); GRPO-ClipHigher 39.5% (+11.0); GSPO +7.0; DPPO +4.1"
    date: "2026-09-23"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.15987"
    notes: "Figure 1. 32 samples per question to estimate Pass@1. Not a CISPO retarget. No public code."
tags:
  - post-training
  - rl-alignment
  - math
  - bpo
  - active
---

# BPO (Bellman Policy Optimization)

## Method Overview
BPO is a critic-free RLVR loss derived from Policy Mirror Descent. For autoregressive generation with terminal rewards, Bellman identities express each token advantage as a difference of consecutive values. Those differences telescope, leaving the verifier reward and the prompt-level expected reward \(V^\mu(x)\). The resulting trajectory-level objective has the same unique optimum as advantage-based PMD on states reachable under the rollout policy.

The practical per-token loss keeps group-normalized advantages \(\hat{A}^i\) and a GRPO-style clip mask, but replaces the importance-sampling ratio with a mismatch-correction weight

\[
\omega_t^i=\frac{1+\varepsilon-\mu(y_t^i\mid x,y_{<t}^i)}{1+\varepsilon-\pi(y_t^i\mid x,y_{<t}^i)},
\]

truncated by \(\min\{\mathrm{sg}(\omega_t^i),C\}\). Additive smoothing \(\varepsilon\) and the cap \(C\) stabilize the complementary-token ratio. CISPO remains the dense Pass@1 default.

## When to Use
- Critic-free math RLVR where you want a PMD/Bellman derivation and a complementary-token weight instead of an IS ratio, under a matched GRPO-family trainer.

## When NOT to Use
- Established dense Pass@1 default → `method:cispo`. MoE/VL → `method:sapo`. Async tool stragglers → `method:sao`.

## Relation to Existing SOTA
- Active plug-in / candidate on `task:math-code-rl-dense`. Does **not** enter `current_sota`. Does **not** replace `method:cispo`, `method:sapo`, or `method:sao`.

## Gotchas & Failure Modes
- No public code as of 2026-09-23. The AIME lift is one matched Qwen3-30B-A3B-Base run family, not a library-wide Pass@1 retarget.
- \(\omega\) is not an IS ratio. Do not drop \(\varepsilon\) or \(C\); the paper uses them for numerical stability.
- Intermediate-state critics are exactly what this reformulation avoids. Do not reintroduce a value head "to be safe."
