---
id: method:cis-rl
type: method
title: "CIS-RL"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "CIS truncates train–infer log-odds displacement; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "choosing the MoE/VL RLVR loss"
    reason: "SAPO remains the MoE/VL optimizer; CIS is a mismatch-ratio plug-in on the GRPO-family surrogate"
    use_instead: "method:sapo"
  - when: "choosing the frontier post-train engine"
    reason: "Miles is the stack; CIS is a token IS correction inside that stack"
    use_instead: "method:miles"
  - when: "adaptive IS clip width from group correctness scarcity"
    reason: "GAPO widens PPO/GSPO clip on scarce-correct rollouts; CIS caps the train–infer mismatch ratio"
    use_instead: "method:gapo"
assumptions:
  - "Rollouts from vLLM/SGLang, gradients from FSDP/Megatron. Paper: Qwen1.5-MoE, DeepSeek-V2-Lite, Qwen3-30B-A3B on five math benches."
  - "Default λ=2.3 (positive-displacement cap k≤1+λ(1-p)). Optional two-sided floor with κ=5e-3."
  - "Official code kzhao5/CIS-RL released as of 2026-09-30."
last_reviewed: "2026-09-30"
papers:
  - paper:cis-rl
recipes:
  - recipe:cis-rl
claims:
  - benchmark: "Qwen1.5-MoE five math benches, mismatch-correction bake-off"
    metric: "five-benchmark average"
    value: "34.78"
    baseline: "IcePop 34.18 / Exact 32.48 / TIS 31.40 / no-corr 30.99"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.32444"
    notes: "Best of the compared train–infer corrections. Not a CISPO or SAPO retarget."
  - benchmark: "Qwen3-30B-A3B five math benches"
    metric: "five-benchmark average"
    value: "69.88"
    baseline: "IcePop 68.99 / GSPO 69.23 / TIS 69.14 / base 67.84"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.32444"
    notes: "DeepSeek-V2-Lite CIS 37.16, also best of that model's compared corrections."
tags:
  - post-training
  - rlvr
  - moe
  - importance-sampling
  - cis-rl
  - active
---

# CIS-RL

## Method Overview
Train and infer engines load the same \(\theta\) but disagree on next-token probabilities. The mismatch ratio \(k=p_{\mathrm{train}}/q_{\mathrm{infer}}\) reweights the GRPO-family token loss. Writing logits \(z\) (train) and \(z+\delta\) (infer) gives

\[
k=p+(1-p)\exp(\varepsilon),\qquad \varepsilon=\log\frac{p}{1-p}-\log\frac{q}{1-q}.
\]

On MoE, \(\varepsilon\) is heavy-tailed (routing disagreement), and its distribution is nearly confidence-invariant, while \(k\) is not: the same \(\varepsilon\) explodes \(k\) on low-\(p\) tokens. CIS truncates large positive \(\varepsilon\) at one constant, which maps to a confidence-dependent cap

\[
k_{\mathrm{CIS}}=\min\bigl\{k,\; 1+\lambda(1-p)\bigr\}
\]

with paper \(\lambda=2.3\). Optional two-sided floor uses \(\kappa=5\times 10^{-3}\). This is not CISPO (Pass@1 clipped IS on the *update* ratio) and not SAPO (MoE/VL loss).

## When to Use
- MoE RLVR where vLLM/SGLang vs FSDP/Megatron mismatch is the instability, and TIS/IcePop/KPop dump bias onto low-confidence tokens.

## When NOT to Use
- Dense Pass@1 default → `method:cispo`. MoE/VL optimizer → `method:sapo`. Production engine → `method:miles`. Scarcity clip width → `method:gapo`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-moe` with a mention on `task:frontier-rl-posttrain-stack`. Does **not** enter `current_sota`. Does **not** replace CISPO, SAPO, Miles, or GAPO.

## Gotchas & Failure Modes
- Name collision: CIS-RL is *not* CISPO. Slug is `cis-rl`.
- Upward clipping of *small* importance weights hurt held-out accuracy in the paper; prefer one-sided positive-displacement truncation unless you are reproducing the two-sided ablation (6.01).
- Dense models in the paper look like bf16 rounding; do not expect MoE-sized tails.
- Exact IS is unbiased and high-variance; do not ship Exact as the default on MoE.
