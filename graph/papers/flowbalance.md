---
id: paper:flowbalance
type: paper
title: "FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience"
authors:
  - "Zixun Huang"
  - "Kishan Panaganti"
  - "Haitao Mi"
  - "Leowei Liang"
year: 2026
month: 9
arxiv_id: "2609.03241"
url: "https://arxiv.org/abs/2609.03241"
methods:
  - method:flowbalance
cites:
  - paper:grpo
  - paper:vista
  - paper:opd
tags:
  - post-training
  - rlvr
  - self-improvement
  - trajectory-balance
  - flowbalance
---

# FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience

## Abstract Summary
A reasoning model can improve from its own on-policy experience, but the inner loop is fragile: terminal verifiers are reliable yet sparse, while dense same-model guidance can reinforce false confidence or collapse onto one solution mode. FlowBalance learns a normalized distribution over complete responses. A frozen training-time view of the same policy uses privileged context to produce token-level log-probability gains, aggregated into a trajectory self-guidance score. That score is calibrated by the verifier group advantage: keep on +, reverse on −, disable when the group has no outcome preference. Profiled trajectory balance fits the reference-supported Gibbs target with one log-partition estimate per rollout group. No separate token-level imitation loss. On Qwen3-4B and Qwen3-8B math, FlowBalance beats FlowRL, GRPO, OPSD, and RLSD on the five-benchmark average, avoids direct OPSD length collapse, and shows higher correct-strategy diversity on an AIME24 diagnostic.

## Key Contributions
1. **Outcome-calibrated trajectory energy**: $E=\eta_A A+\beta_G G_{\mathrm{H}}\operatorname{sgn}(A)$. Privileged hindsight is a stopped feature, not an imitation loss.
2. **Profiled trajectory balance**: one $\log Z$ per group; all $N-1$ within-group contrasts remain.
3. **False-positive correction**: sign gating multiplies the success/fail target ratio by $\exp(2\beta_G G_{\mathrm{H}}(y_{-})/\tau)$ relative to ungated guidance.
4. **Fixed-task inner loop**: isolates experience-to-policy update; not an outer-loop curriculum generator.

## Empirical Highlights
- Qwen3-4B five-bench avg 64.26 vs FlowRL 63.22 vs GRPO 62.31 vs RLSD 59.55 vs OPSD 54.12 (Table 1, five seeds, step 180).
- Qwen3-8B five-bench avg 67.61 vs FlowRL 65.85 vs GRPO 65.49; AIME24 Pass@16 89.33 vs FlowRL 86.67 vs GRPO 85.33.
- Reaches 0.5 AIME24 val in ~100 steps vs ~143 for GRPO; stable over 400 steps.
- Default $\eta_A=15$, $\beta_G=1$. Raising $\beta_G$ to 3 drops Qwen3-8B AIME24 89.33→86.00 and HMMT25 34.67→30.00.

## Open Source Repository & Resources
- Code: `https://github.com/alexhuang13/FlowBalance` (vendored verl; recipe maps $\beta_G$→`FLOWSD_BETA_Q`, $\eta_A$→`FLOWSD_ETA_R`).
- Blog: `https://alexhuang13.github.io/FlowBalance-Blog/`.
