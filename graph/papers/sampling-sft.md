---
id: paper:sampling-sft
type: paper
title: "Finetuning with Sampling: SFT Learns Better Than You Think"
authors:
  - "Aayush Karan"
  - "Sitan Chen"
  - "Yilun Du"
year: 2026
month: 10
arxiv_id: "2610.02140"
url: "https://arxiv.org/abs/2610.02140"
methods:
  - method:sampling-sft
cites:
  - paper:grpo
  - paper:vista
tags:
  - post-training
  - sft
  - mcmc
  - sampling-sft
---

# Finetuning with Sampling: SFT Learns Better Than You Think

## Abstract Summary
Conventional post-training wisdom says RL generalizes and forgets less, while SFT is off-policy and collapses. This paper keeps ordinary SFT and instead **samples the data toward the base model**. MCMC / Metropolis–Hastings projection sampling rewrites off-policy expert traces to be more on-policy while remaining correct. Across chemistry, math, and medical, sampling-SFT rivals GRPO and OPSD on new-task accuracy and prior-task retention. Vanilla SFT still loses to GRPO; the claim is not “SFT beats GRPO.” Sampling SFT then GRPO is the strongest math run in Table 1. Harvard. Project: `https://aakaran.github.io/finetuning_with_sampling/`.

## Key Contributions
1. **Target policy**: keep expert information content, maximize proximity to the base model, then SFT.
2. **Projection sampling**: blockwise MH edits of expert traces (B=32, T=1856, N_MCMC=10) with a correctness filter.
3. **SFT vs GRPO vs OPSD bake-off**: Qwen2.5-3B math and Qwen2.5-7B-Instruct chemistry/medical. Vanilla SFT is the weak baseline, not the headline.

## Empirical Highlights
- Qwen2.5-3B MATH(3,4,5): Sampling SFT 0.495 vs GRPO 0.457 vs UFT 0.470 vs vanilla SFT 0.243 vs base 0.315. MATH500: 0.582 vs GRPO 0.313. Sampling SFT+RL: 0.545 / 0.652 (best).
- Chemistry (Qwen2.5-7B-Instruct): Sampling SFT 0.660 vs OPSD 0.618 vs SFT 0.618 vs base 0.343. Prior avg 0.586 vs OPSD 0.568 vs SFT 0.520.
- Medical: 0.458 vs OPSD 0.466 vs SFT 0.448 vs base 0.353. Prior avg 0.516 vs OPSD 0.501 vs SFT 0.353 (vanilla SFT forgets).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02140`
- Project: `https://aakaran.github.io/finetuning_with_sampling/`
- No official training GitHub as of 2026-10-03 (`recipe:sampling-sft` `code_status: none`). `aakaran/reasoning-with-sampling` is a different 2025 inference paper.
