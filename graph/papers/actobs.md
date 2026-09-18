---
id: paper:actobs
type: paper
title: "Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL"
authors:
  - "Juzheng Zhang"
  - "Disha Makhija"
  - "Manoj Ghuhan Arivazhagan"
  - "Vinayshekhar Bannihatti Kumar"
  - "Rashmi Gangadharaiah"
year: 2026
month: 9
arxiv_id: "2609.20715"
url: "https://arxiv.org/abs/2609.20715"
methods:
  - method:actobs
cites:
  - paper:grpo
  - paper:sao
  - paper:mini-swe-agent
tags:
  - post-training
  - agentic
  - sft
  - observation
  - actobs
---

# Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL

## Abstract Summary
Agent traces record actions and what the environment returns. Standard SFT puts loss only on agent-authored action tokens and treats observations as context. ActObs also supervises the observation tokens already in each trajectory. Deployed agents never emit observations; predicting them is a consequence model that adds no data, parameters, sequence tokens, or extra forward passes. SFT numbers look similar; GRPO then diverges. On Qwen3-4B, GRPO from ActObs raises pass@k at every evaluated budget on Terminal-Bench 2.0 vs action-only SFT. On Qwen3-8B it trades some pass@1 for higher pass@k (+3.4 pp at pass@16) and more distinct tasks. The gap transfers to aider-polyglot (+4.2 pp pass@1 at 4B), unseen in SFT and RL. ActObs keeps more entropy during RL with less policy movement, staying closer to the SFT init. Action and observation gradients rapidly become orthogonal; action-only SFT leaves a large residual observation gradient and degrades environment prediction below the base model.

## Key Contributions
1. **Observation-token SFT** on traces that already contain environment text; no extra data or parameters.
2. **SFT looks similar, GRPO does not**: exploration after RL is the measured difference.
3. **Gradient geometry**: action vs observation grads go orthogonal; action-only training unlearns consequence prediction.

## Empirical Highlights
- Qwen3-4B Terminal-Bench 2.0: GRPO from ActObs beats action-only at every evaluated pass@k.
- Qwen3-8B Terminal-Bench 2.0: +3.4 pp at pass@16; more distinct tasks; some pass@1 given up.
- aider-polyglot (unseen): +4.2 pp pass@1 at 4B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.20715`
- No official GitHub as of 2026-09-18 (`recipe:actobs` `code_status: none`).
