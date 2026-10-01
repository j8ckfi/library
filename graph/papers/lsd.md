---
id: paper:lsd
type: paper
title: "Mitigating Length-Scaling Tax with Online Distillation"
authors:
  - "Xu Wan"
  - "Wenyue Xu"
  - "Shengjie Zhao"
  - "Mingyang Sun"
year: 2026
month: 9
arxiv_id: "2609.38854"
url: "https://arxiv.org/abs/2609.38854"
methods:
  - method:lsd
cites:
  - paper:opd
  - paper:minimax-m1
tags:
  - post-training
  - rlvr
  - distillation
  - lsd
---

# Mitigating Length-Scaling Tax with Online Distillation

## Abstract Summary
RLVR length growth on already-solved prompts is a length-scaling tax (LST): extra tokens without a commensurate accuracy gain, because all-correct groups have collapsed relative advantages while hard groups keep reshaping the shared policy. Length Self-Distillation (LSD) routes solved prompt groups to on-policy distillation against an EMA of the online policy and keeps the original RL objective on unsolved groups. No external teacher. SG-FKL matches or beats RL Pass@1 while cutting LST from 19.0% to −3.7% on single-turn reasoning and from 31.4% to 13.7% on multi-turn agentic tasks. ByteDance Seed / Tongji / Peking. No public GitHub as of 2026-10-01.

## Key Contributions
1. **LST metric**: frozen easy-query set from an RL anchor; excess length vs the shortest accuracy-qualified checkpoint.
2. **Accuracy-routed mix**: solved groups → EMA OPD; unsolved groups → RLVR.
3. **Three OPD estimators**: supervised-gradient forward / reverse KL vs sampled reverse-KL; SG-FKL is the reported default.

## Empirical Highlights
- Single-turn: LST 19.0% → −3.7% with comparable or better Pass@1 vs RL (Qwen3-4B-Base, DAPO-Math-17K, AMC 2023 / AIME 2025 / AIME 2026).
- Multi-turn agentic: LST 31.4% → 13.7%. Teacher half-life and routing threshold trade preservation vs exploration.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.38854`
- Code: none found as of 2026-10-01 (`code_status: none`).
