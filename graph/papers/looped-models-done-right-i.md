---
id: paper:looped-models-done-right-i
type: paper
title: 'Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design'
authors:
- 'Benhao Huang'
- 'Chufan Shi'
- 'Junlin Chen'
- 'Shicheng Wen'
- 'Zhengzhong Liu'
- 'Eric Xing'
- 'Xuezhe Ma'
year: 2026
month: 10
arxiv_id: '2610.23036'
url: https://arxiv.org/abs/2610.23036
methods:
- method:looped-models-done-right
cites:
- paper:looped-models-done-right
- paper:recurrent-looped-transformer
- paper:smelt
tags:
- pretraining
- architecture
- looped-transformer
- looped-models-done-right
---

# Towards Looped Models Done Right, Part I

## Abstract Summary
Isolates recurrence placement, input injection, and recurrent-state organization for looped LMs at matched parameter scale, logical depth, and token budgets, then transfers the design to resident- and active-parameter-matched MoE. The prelude-recurrent block-coda sandwich (Huginn-style) is the consistent winner. Input injection helps knowledge/context; random init and separate H/L states are mixed or negative.

## Key Contributions
1. Controlled isolation of looped-LM topology / injection / state axes.
2. Huginn-style sandwich as the transferable design, including MoE.
3. Same code host as Part II: ifm-ai/xllm-loop.

## Empirical Highlights
- 730M / 336B tokens: complete Huginn outperforms Ouro on all ten benches.
- 8BA0.8B (32BA3B unrolled) / 500B tokens: Huginn beats Ouro on nearly all knowledge/reasoning/coding benches with more balanced expert routing.
- Matched train/infer FLOPs: Huginn-style uses 75% fewer resident parameters than a 112-layer feedforward MoE baseline; outperforms it on DROP and GSM8K, matches MATH500.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23036`
- Code: `https://github.com/ifm-ai/xllm-loop` (`code_status: released`).
