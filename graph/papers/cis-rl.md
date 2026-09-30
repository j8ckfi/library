---
id: paper:cis-rl
type: paper
title: "Rethinking Training–Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It"
authors:
  - "Tianrun Yu"
  - "Kaixiang Zhao"
  - "Shangzhe Li"
  - "Yuxiao Yang"
  - "Porter Jenkins"
  - "Weitong Zhang"
  - "Taylor W. Killian"
year: 2026
month: 9
arxiv_id: "2609.32444"
url: "https://arxiv.org/abs/2609.32444"
methods:
  - method:cis-rl
cites:
  - paper:gspo
tags:
  - post-training
  - rlvr
  - moe
  - importance-sampling
  - cis-rl
---

# Rethinking Training–Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It

## Abstract Summary
RLVR rollouts come from an inference engine while gradients come from a training engine; the two assign different probabilities to the same tokens. On MoE models the mismatch is a heavy-tailed log-odds displacement \(\varepsilon_t\) from per-logit perturbation (routing disagreement amplifies the tail); the same displacement moves the IS ratio far from one on low-confidence tokens and barely on high-confidence ones. Fixed-ratio caps (TIS) and interval masks (IcePop / KPop) therefore dump truncation bias onto low-confidence tokens. Calibrated Importance Sampling (CIS) truncates the displacement, not the raw ratio, which maps to a confidence-dependent cap \(k\le 1+\lambda(1-p)\) that tightens as token confidence \(p\) grows. Best five-benchmark average on three MoE models vs TIS / IcePop / KPop / Exact. BYU / UNC. Code: `https://github.com/kzhao5/CIS-RL`.

## Key Contributions
1. **Log-odds identity**: \(k=p+(1-p)\exp(\varepsilon)\); \(\varepsilon\) is approximately confidence-invariant, while \(k\) is not.
2. **CIS**: truncate large positive \(\varepsilon\) at one constant; the implied ratio cap is tighter for confident tokens. Bounds the unbounded second moment of exact IS at a controlled truncated-excess bias.
3. **MoE diagnosis**: dense controls stay near rounding error; MoE routing disagreement is a major tail amplifier.

## Empirical Highlights
- Qwen1.5-MoE five-bench avg 34.78 vs IcePop 34.18 / Exact 32.48 / TIS 31.40 / no-corr 30.99.
- DeepSeek-V2-Lite 37.16 (best of the compared mismatch corrections).
- Qwen3-30B-A3B 69.88 vs IcePop 68.99 / GSPO 69.23 / TIS 69.14 / base 67.84.
- Defaults \(\lambda=2.3\); two-sided floor uses \(\kappa=5\times 10^{-3}\). Two-sided ablation 6.01 on the reported diagnostic.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.32444`
- Code: `https://github.com/kzhao5/CIS-RL` (`code_status: released`).
