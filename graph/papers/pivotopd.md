---
id: paper:pivotopd
type: paper
title: "PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents"
authors:
  - "Yinghui He"
  - "Yapei Chang"
  - "Khushi Bhardwaj"
  - "Daniele Molinari"
  - "Tugrul Konuk"
  - "Jan Kautz"
  - "Ali Hatamizadeh"
year: 2026
month: 9
arxiv_id: "2609.40285"
url: "https://arxiv.org/abs/2609.40285"
methods:
  - method:pivotopd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - agentic
  - on-policy
  - pivotopd
---

# PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents

## Abstract Summary
In multi-turn agents, a single early action can change later states so errors compound. Across Qwen3 8B–235B, more than half of failed ALFWorld rollouts contain a pivotal mistake, typically early and often recoverable: correcting that turn or guiding the next few turns restores success. Standard OPD mostly removes incomplete-trajectory failures while pivotal-turn failures persist. PivotOPD detects pivotal turns with a teacher, then trains a privileged self-teacher: reverse-KL preventive distillation on the gold action, forward-KL recovery distillation on the next few recovery actions, combined with group RL. Strongest average on ALFWorld / WebShop / Search-QA for Qwen3-1.7B and 8B; +5.5 ALFWorld vs the strongest baseline at 1.7B; +3.2 SWE-Bench Verified on a Nemotron-3.5 student vs +0.2 for standard OPD. Princeton / NVIDIA. Project: `https://research.nvidia.com/labs/lpr/pivotopd/`.

## Key Contributions
1. **Pivotal-mistake diagnosis**: early recoverable mistakes dominate failures; vanilla OPD does not repair them.
2. **Prevent + recover**: reverse KL at the gold action, forward KL on recovery actions the student rarely samples.
3. **No oracle required at train time**: teacher-named gold / recovery actions; ALFWorld oracle is analysis-only.

## Empirical Highlights
- Qwen3-1.7B / 8B: strongest average vs 13 baselines on ALFWorld, WebShop, Search-based QA. ALFWorld +5.5 at 1.7B vs strongest baseline.
- Nemotron-3.5 SWE-Bench Verified resolve +3.2 vs +0.2 standard OPD. 8B recovers from pivotal mistakes more than 3× as often as OPD.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.40285`
- Project: `https://research.nvidia.com/labs/lpr/pivotopd/` (`code_status: announced`).
