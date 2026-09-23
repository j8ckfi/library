---
id: paper:aclarena
type: paper
title: "ACLArena: Agent Continual Learning in Multi-stage Post-training"
authors:
  - "Haixin Wang"
  - "Xiaoxuan Wang"
  - "Junkai Zhang"
  - "Han Zhang"
  - "Renliang Sun"
  - "Alexander K. Taylor"
  - "Yidan Shi"
  - "Haoran Deng"
  - "Chenguang Wang"
  - "Jason Cong"
  - "Yizhou Sun"
  - "Wei Wang"
year: 2026
month: 9
arxiv_id: "2609.23989"
url: "https://arxiv.org/abs/2609.23989"
methods:
  - method:aclarena
cites:
  - paper:opd
  - paper:open-mopd
  - paper:grpo
  - paper:sao
  - paper:canopy
  - paper:miles
tags:
  - post-training
  - agentic
  - continual-learning
  - aclarena
---

# ACLArena: Agent Continual Learning in Multi-stage Post-training

## Abstract Summary
Industrial agents stack capabilities across stages (math, search, multi-tool e-commerce, instruction following), but sequential post-training forgets earlier skills. ACLArena is a controlled testbed and analysis of Agent Continual Learning. Sequential training is the diagnostic baseline: forgetting and transfer are measured at model level (parameter-displacement directions) and token level (high-entropy positions move; low-entropy positions stay). The paper then compares multi-teacher mixed OPD, self-distilled fine-tuning, and model merging. The proposed recipe, Mixture of Low-Rank Experts (MLE), replays filtered high-quality specialist trajectories then routes multiple LoRA experts, each specialized by RL. Built on slime. Code: WillDreamer/ACLArena; HF collection willhx/aclarena.

## Key Contributions
1. **ACLArena**: sequential Math → Search → E-commerce → IF pipeline with in-domain and OOD splits.
2. **Mechanism**: tasks induce partially aligned updates; sequential training overwrites; prediction change concentrates on high-entropy tokens.
3. **MLE**: SDFT replay plus routed LoRA experts refined by RL, consolidating heterogeneous stages in one deployed model.

## Empirical Highlights
- Sequential E-commerce collapses AIME26 23.33→6.04 and NQ 45.2→14.6; Seq-Final only partially recovers (AIME26 10.21, NQ 33.5).
- MLE: AIME26 21.04, NQ 49.7, \(\tau^3\)-Retail 32.9, IF-Eval 85.0, GPQA 42.4, single-hop search 57.7, multi-hop 38.6 (Table 2), competitive with or above MMOPD / SDFT / merge on the joint profile.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.23989`
- Code: `https://github.com/WillDreamer/ACLArena` (`code_status: released`).
- Hugging Face: `willhx/aclarena`.
