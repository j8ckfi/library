---
id: paper:d2r
type: paper
title: 'Dream to Remember: Continual Steering of Generalist Robot Policies with World
  Models'
authors:
- Bahey Tharwat
- Iman Nematollahi
- Marvin Alles
- Xingyuan Zhang
- Akshay L Chandra
- Abhinav Valada
year: 2026
month: 10
arxiv_id: '2610.13816'
url: https://arxiv.org/abs/2610.13816
methods:
- method:d2r
cites:
- paper:efficienttdmpc
tags:
- control
- world-models
- continual-rl
- d2r
---

# Dream to Remember: Continual Steering of Generalist Robot Policies with World Models

## Abstract Summary
D2R steers a frozen robot policy with continual RL. A world model rehearses in imagination instead of storing replay. On CALVIN 8 tasks, success 63.7%→74.8% vs LoRA FT 11.7%. Plug-in on `task:continuous-control-world-model`. No public code.

## Key Contributions
1. Continual RL steering of a frozen generalist robot policy.
2. World-model imagination rehearsal instead of replay buffers.
3. CALVIN 8-task lift vs LoRA fine-tune collapse.

## Empirical Highlights
- CALVIN 8 tasks 63.7%→74.8%.
- LoRA FT 11.7% on the same protocol.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13816`
- Code: `none found` (`code_status: none`).
