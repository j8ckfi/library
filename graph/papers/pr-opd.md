---
id: paper:pr-opd
type: paper
title: 'PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic Reinforcement Learning'
authors:
- Muyang Li
- Jie Yang
- Zhengyu Fang
- Junchao Zhu
- Zhengkun Xiao
- Ruining Deng
- Zhe Jiang
- Shigang Chen
year: 2026
month: 9
arxiv_id: '2609.36642'
url: https://arxiv.org/abs/2609.36642
methods:
- method:pr-opd
cites:
- paper:vista
- paper:nsd
- paper:canopy
tags:
- distillation
- privileged-opsd
- agentic
- hidden-states
---

# PR-OPD

## Abstract Summary
After a GRPO warm start, align hidden states to a hindsight-skill-conditioned self-teacher. Invisible advantage: skill changes <25% of token probs but >80% of hidden states. Related work only: PreSO 2610.14001 (hint-induced representation isolation) is SKIP'd this sweep.

## Key Contributions
1. Privileged representation OPSD (hidden-state match, not token reverse-KL only).
2. Invisible-advantage measurement on WebShop.
3. Released github.com/balibata/PR-OPD.

## Empirical Highlights
- Invisible advantage WebShop 42.2→56.2 skill; <25% tokens, >80% hidden states.
- After GRPO on Qwen2.5-3B-Instruct: +4.7 ALFWorld, +11.7 WebShop (single-paper).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36642`
- Code: `https://github.com/balibata/PR-OPD` (`code_status: released`).
- Related (not ingested): PreSO `arXiv:2610.14001`.
