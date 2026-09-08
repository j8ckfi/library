---
id: method:flowbalance
type: method
title: "FlowBalance"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code RLVR default"
    reason: "FlowBalance is verifier-grounded trajectory-balance self-improvement; CISPO remains the Pass@1 labeled default"
    use_instead: "method:cispo"
  - when: "no verifier, no reward, no privileged hindsight"
    reason: "OPSA is teacher-/reward-/hint-free entropy-adaptive self-adaptation; FlowBalance needs a verifier and training-only context"
    use_instead: "method:opsa"
  - when: "a strong external teacher is available and the goal is intentional distillation"
    reason: "OPD remains the single-teacher distill default; FlowBalance is same-model self-guidance, not teacher matching"
    use_instead: "method:opd"
  - when: "a same-size teacher is privileged with a gold reference and the update is student-to-teacher adaptation"
    reason: "That shelf is VISTA / privileged OPSD, not trajectory-balance self-improvement"
    use_instead: "method:vista"
  - when: "unlabeled existing math problems with majority-vote pseudo-solutions"
    reason: "u-OPSD distills a consensus teacher along disagreeing paths"
    use_instead: "method:u-opsd"
  - when: "RLVR is already running and the goal is a synthetic OPD teacher from the training trajectory"
    reason: "RISE extrapolates RLVR displacement into token-level OPD targets"
    use_instead: "method:rise"
  - when: "long-horizon outcome-only agent RL with a programmatic checker"
    reason: "Coverage / anti-drift is CANOPY, not a math inner-loop trajectory energy"
    use_instead: "method:canopy"
assumptions:
  - "Host loop already samples a verifier-scored on-policy group. Paper: Qwen3-4B/8B, DAPO-Math-style prompts, group N=8, prompt 2048 / response 8192, step-180 main table, 5 seeds."
  - "Privileged training-only context c (reference solution or task feedback) is available to a frozen current-policy snapshot for scoring sampled tokens only. Inference sees neither c nor the hindsight view."
  - "Default η_A=15, β_G=1, clip B=4. Code maps β_G to FLOWSD_BETA_Q and η_A to FLOWSD_ETA_R."
last_reviewed: "2026-09-08"
papers:
  - paper:flowbalance
recipes:
  - recipe:flowbalance
claims:
  - benchmark: "Qwen3-4B AIME24@16 / HMMT25 / Minerva / MATH500 / Olympiad five-bench avg"
    metric: "average accuracy (5 seeds, step 180)"
    value: 64.26
    baseline: "FlowRL 63.22 / GRPO 62.31 / RLSD 59.55 / OPSD 54.12"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.03241"
    notes: "Table 1. AIME24 Pass@16; others Pass@1. Core four-bench (AIME24/HMMT25/MATH500/Olympiad) 67.69 vs GRPO 65.10 vs FlowRL +1.67."
  - benchmark: "Qwen3-8B AIME24@16 / HMMT25 / Minerva / MATH500 / Olympiad five-bench avg"
    metric: "average accuracy (5 seeds, step 180)"
    value: 67.61
    baseline: "FlowRL 65.85 / GRPO 65.49 / RLSD 64.12 / OPSD 41.16"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.03241"
    notes: "Table 1. Best mean on every reported bench. AIME24 Pass@16 89.33 vs FlowRL 86.67 vs GRPO 85.33. Core four-bench 71.09 vs GRPO 68.65 vs FlowRL +1.98."
  - benchmark: "Qwen3-8B AIME24 validation time-to-0.5"
    metric: "training steps to 0.5 accuracy"
    value: "~100 vs GRPO ~143 (1.43× fewer updates)"
    baseline: "GRPO ~143 steps; GRPO degrades after ~step 180 over a 400-step run"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.03241"
    notes: "Figure 2. FlowBalance stays near peak over 400 steps. Direct OPSD collapses response length."
  - benchmark: "AIME24 correct-only Simpson strategy diversity (Qwen3-8B diagnostic)"
    metric: "Simpson diversity"
    value: 0.2194
    baseline: "GRPO 0.1017 / RLSD 0.1456"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.03241"
    notes: "One-seed LLM-judged diagnostic, not a population-level diversity guarantee."
tags:
  - post-training
  - rlvr
  - self-improvement
  - trajectory-balance
  - flowbalance
  - active
---

# FlowBalance

## Method Overview
FlowBalance is a verifier-grounded self-improvement operator over complete responses. Sample a group $\mathcal{G}=\{y^{(i)}\}$ from the frozen current policy. A verifier supplies stopped group-relative advantages $A_i$. A frozen privileged-hindsight view of the same snapshot scores already sampled tokens with training-only context $c$ (reference solution). Clipped token logp-gains relative to a fixed reference policy average to a trajectory self-guidance score $G_{\mathrm{H}}$. The energy is

\[
E=\eta_A A+\beta_G G_{\mathrm{H}}\operatorname{sgn}(A).
\]

Keep $G_{\mathrm{H}}$ on $A>0$, reverse it on $A<0$, disable it when $A=0$. The reference-supported target is $\pi_{\mathrm{ref}}(y)\exp(E/\tau)$, fitted by profiled trajectory balance with one $\log Z$ per group. Gradients flow only through $\log\pi_\theta(y)$. There is no separate token-level imitation loss.

Default $\eta_A=15$, $\beta_G=1$. Raising $\beta_G$ is not strictly better.

## When to Use
- Already running verifier-scored math RLVR and want dense same-model trajectory structure without a larger teacher and without OPSD length collapse.
- When FlowRL-style trajectory balance is the host family and you can add privileged hindsight scoring.

## When NOT to Use
- Pass@1 labeled RLVR default → `method:cispo`.
- No verifier / no privileged context → `method:opsa`.
- External teacher distill → `method:opd`. Privileged teacher adaptation → `method:vista`. Unlabeled consensus → `method:u-opsd`. RLVR-extrapolated teacher → `method:rise`. Long-horizon agents → `method:canopy`.

## Relation to Existing SOTA
- Active on `task:math-code-rl-dense`. Does **not** supersede `method:cispo`, `method:opsa`, `method:opd`, `method:vista`, `method:u-opsd`, `method:rise`, or `method:canopy`.
- Distinct from VISTA: hindsight is a stopped energy feature, not a teacher update. Distinct from RISE: no extrapolated OPD teacher. Distinct from OPSA: needs a verifier and privileged $c$.

## Gotchas & Failure Modes
- Math-only large-scale evidence (Qwen3-4B/8B). Agentic / multimodal transfer is untested.
- Diversity claim is a one-seed LLM-judged AIME24 diagnostic.
- $\beta_G=3$ hurts AIME24/HMMT25 vs the default $\beta_G=1$. Do not treat denser guidance as strictly better.
- Direct OPSD in this paper's protocol collapses length; that is a comparator failure, not a reason to drop CISPO or OPD as library defaults.
- GRPO inside the paper is a baseline, not a revival of GRPO as the Pass@1 default.
