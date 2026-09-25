---
id: paper:slca-grpo
type: paper
title: "SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL"
authors:
  - "Yan Zhan"
  - "Shaobo Liu"
  - "Qiunan Liu"
  - "Yuanjun Shi"
  - "Siqi Xu"
  - "WeiYi Hou"
  - "Xiang Xu"
  - "Zekang Li"
  - "Weizhou Pan"
  - "Jiahong Yan"
year: 2026
month: 9
arxiv_id: "2609.29050"
url: "https://arxiv.org/abs/2609.29050"
methods:
  - method:slca-grpo
cites:
  - paper:grpo
  - paper:foldgrpo
  - paper:sao
  - paper:pact
  - paper:critical-state-rl
tags:
  - post-training
  - rl-alignment
  - credit-assignment
  - tool-use
  - slca-grpo
---

# SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL

## Abstract Summary
Tool-calling agents interleave structured tool invocations with user-facing summaries. GRPO broadcasts one trajectory-level advantage to all tokens, so summary-gradient leaks into tool-decision tokens (cross-segment credit misattribution). SLCA-GRPO routes independently normalized tool-side advantages only to tool tokens and summary-side advantages only to summary tokens, at zero extra rollout cost, inside one unified policy. Hierarchical Rewards (HierR) supply the two segment returns. A Schema-Guided LLM Simulator (SGLS) supplies schema-consistent observations without live APIs. The structural axis is orthogonal to temporal credit (VinePPO / SPO / GiGPO). Peking University / Shenzhen University / Tencent PCG QQ. On a 7B backbone: +2.53 pp in-domain, +1.36 pp BFCL, +9.15 pp \(\tau^2\)-Bench vs matched GRPO.

## Key Contributions
1. **Failure mode**: global advantage conflation on heterogeneous tool/summary trajectories; sign-conflict can reward bad tools or penalize good ones.
2. **SLCA**: per-group segment normalization and mask routing; \(\partial g_{\mathrm{tool}}/\partial R^{\mathrm{sum}}=\mathbf{0}\) per update.
3. **SGLS + HierR**: schema-guided simulator and split process/summary rewards that make the routing meaningful.

## Empirical Highlights
- Qwen2.5-7B-Instruct, matched GRPO (same SFT, SGLS, HierR, G=16): Toucan-Test Success@0.9 79.13% (+2.53 pp); BFCL +1.36 pp; \(\tau^2\)-Bench +9.15 pp.
- Toucan gaps also +2.35 pp (3B) and +2.05 pp (8B).
- Ablations: w/o SLCA / SGLS / HierR. ToolPO and RLTR keep method-specific protocols.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.29050`
- Claimed code: `https://github.com/SLCA-GRPO/SLCA-GRPO` (404 as of 2026-09-25; `recipe:slca-grpo` `code_status: announced`).
- Dataset: `https://huggingface.co/datasets/YanZhanPKU/SLCA-GRPO-Datasets`.
