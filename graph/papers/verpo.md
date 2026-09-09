---
id: paper:verpo
type: paper
title: "VERPO: Verified Evidence Regularized Policy Optimization"
authors:
  - "Haijiang Li"
  - "Chengyu Lv"
  - "Yi Zhang"
  - "Zhibing Zhang"
  - "Rui Qian"
  - "Yuchen Zhang"
  - "Xiaofan Zhang"
  - "Mingshan Wang"
  - "Xiaofei Jing"
  - "Yu Tong"
  - "Cangqi Zhou"
year: 2026
month: 9
arxiv_id: "2609.06100"
url: "https://arxiv.org/abs/2609.06100"
methods:
  - method:verpo
cites:
  - paper:grpo
  - paper:vista
tags:
  - post-training
  - opsd
  - privileged-teacher
  - verpo
---

# VERPO: Verified Evidence Regularized Policy Optimization

## Abstract Summary
Sequence-level verifiable rewards do not say which tokens to keep. Evidence-conditioned teachers replay sampled trajectories with privileged feedback, but naive imitation copies formatting and style that do not support success. VERPO treats evidence as a *proposal* for policy correction while keeping the outcome objective. It splits evidence-free reference restoration from signed token-level evidence corrections, attenuates corrections along a Fisher evidence-presence direction, and uses a stopped token-wise ZPD controller so acceptance tracks local reward alignment and Fisher movement cost. The reference channel does not depend on acceptance.

## Key Contributions
1. **Proposal, not target**: privileged evidence proposes token corrections; the outcome objective stays.
2. **Two channels**: evidence-free restoration vs signed evidence corrections.
3. **Fisher Evidence Contrast + ZPD**: attenuate and gate which corrections are accepted.

## Empirical Highlights
- Five scientific-reasoning and tool-use tasks. Best variant vs strongest compared baseline, average score: Qwen3-4B 0.6826→0.6857; Qwen3-8B 0.6895→0.7058; Llama-3.2-1B 0.4751→0.5657.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
