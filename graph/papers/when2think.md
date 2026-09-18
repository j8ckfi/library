---
id: paper:when2think
type: paper
title: "When2Think: Learning Difficulty-Aware Length Control for Efficient Hybrid Reasoning Models"
authors:
  - "Jaejun Shim"
  - "HyunJin Kim"
  - "Young Jin Kim"
  - "JinYeong Bak"
year: 2026
month: 9
arxiv_id: "2609.19671"
url: "https://arxiv.org/abs/2609.19671"
methods:
  - method:when2think
cites:
  - paper:minimax-m1
  - paper:grpo
tags:
  - post-training
  - rlvr
  - hybrid-reasoning
  - length-control
  - when2think
---

# When2Think: Learning Difficulty-Aware Length Control for Efficient Hybrid Reasoning Models

## Abstract Summary
Large reasoning models overthink easy problems and underthink hard ones. Uniform length penalties and rigid routers pay an efficiency tax: they save tokens on easy items by losing accuracy on hard ones. When2Think treats computation as instance-adaptive allocation. Instance-level Difficulty-Aware Control (IDAC) shapes rewards from pre-computed reference statistics (accuracy and token usage) so the policy learns System 1 (NoThink) on easy instances and System 2 (Think) on hard ones. Combined with verifier rewards and batch-wise standardized advantages, IDAC is critic-free and does not need a learned reward model or online reference queries. On AIME24, Pass@3 rises 10.0% while tokens fall 27.9% vs the base model; on AIME25, When2Think reaches 40.0% Pass@3 over compression and routing-only baselines.

## Key Contributions
1. **Hybrid Think / NoThink as a learned policy**, not a fixed router or a uniform length penalty.
2. **IDAC**: reward shaping from offline reference accuracy and token-usage statistics.
3. **Critic-free GRPO-family update** with verifier rewards and batch-standardized advantages.

## Empirical Highlights
- AIME24: Pass@3 +10.0% with token usage −27.9% vs the base model.
- AIME25: 40.0% Pass@3, above compression and routing-only baselines.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.19671`
- Claimed code: `https://github.com/JJunShim/When2Think` (stub README as of 2026-09-18; `recipe:when2think` `code_status: partial`).
