---
id: paper:rsd
type: paper
title: 'Self-Evolving Agents through Privileged Retrospective Distillation'
authors:
- 'Yuhang Zhou'
- 'Yifan Wu'
- 'Bo Peng'
- 'Mingyi Wang'
- 'Jiayi Liu'
- 'Xiangjun Fan'
- 'Lizhu Zhang'
- 'Zhuokai Zhao'
year: 2026
month: 10
arxiv_id: '2610.27495'
url: https://arxiv.org/abs/2610.27495
methods:
- method:rsd
cites:
- paper:vista
tags:
- opsd
- privileged
- agentic
- active
---

# Self-Evolving Agents through Privileged Retrospective Distillation

## Abstract Summary
RSD uses the same model as student and teacher: the teacher re-scores realized actions with hindsight, turn-level reflection, and cross-task lessons, then those distributions are distilled on-policy without gold solutions or verifier rewards.

## Key Contributions
1. Privileged retrospective self-distill plus optional frontier-guided context-policy edits.

## Empirical Highlights
- ALFWorld / ScienceWorld / SearchQA Qwen3-8B/14B up to +59.7% relative vs base; context-policy evolution adds up to +44.7%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27495`
- Code: `none found` (`code_status: none`).
