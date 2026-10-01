---
id: paper:hdl
type: paper
title: "Where the Model Changes Its Mind: Hindsight-Divergence Localization for Efficient Reinforcement Learning with Verifiable Rewards"
authors:
  - "Fanchao Chen"
  - "Hengyu Fu"
  - "Shivaram Venkataraman"
  - "Jiantao Jiao"
year: 2026
month: 9
arxiv_id: "2609.36864"
url: "https://arxiv.org/abs/2609.36864"
methods:
  - method:hdl
cites:
  - paper:grpo
tags:
  - post-training
  - rlvr
  - hdl
---

# Where the Model Changes Its Mind: Hindsight-Divergence Localization for Efficient Reinforcement Learning with Verifiable Rewards

## Abstract Summary
Group-relative RLVR learns from outcome differences across independently sampled full trajectories. HDL (Hindsight-Divergence Localization) samples a few complete roots, scores each token by the absolute log-likelihood change under a hindsight context (verifier feedback + a reflection), and fills the rest of the group with fresh suffixes from those branch points under the original task context. Prefixes are reused; policy updates apply only to newly generated suffixes. Vs GRPO at matched group size and steps: up to 2.5× fewer generated tokens and 1.8× faster rollout wall-clock, with gains on math, code, and agents (up to +12.5 on agent tasks, including ScienceWorld). UW–Madison / Berkeley / ETH / NVIDIA. Hosted on slime; no dedicated public repo as of 2026-10-01.

## Key Contributions
1. **Hindsight-divergence branch points**: \(s_i=|\log p_i^H(y_i)-\log p_i^0(y_i)|\), not entropy or a trained reflection policy.
2. **Localized groups**: \(M<G\) roots, \(G-M\) continuations reuse prefixes; hindsight is selection-only, not a train context.
3. **Efficiency without shrinking the group**: same GRPO-family objective, cheaper generation.

## Empirical Highlights
- Up to 2.5× fewer tokens / 1.8× faster rollouts vs GRPO; token usage cut up to 61%, wall-clock up to 45% in the matched-budget tables.
- Task gains across math, code, and agents; largest reported agent lift +12.5. Distinct from GRAFT (peer all-fail salvage).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36864`
- Code: no dedicated public repo as of 2026-10-01; slime-based (`code_status: none`). Host: `https://github.com/THUDM/slime`.
