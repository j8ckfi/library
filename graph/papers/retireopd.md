---
id: paper:retireopd
type: paper
title: "RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning"
authors:
  - "Yan Yu"
  - "Zhengxi Lu"
  - "Yizhou Liu"
  - "Yichen Pan"
  - "Aozhe Wang"
  - "Qipeng Chen"
  - "Hua Yang"
  - "Wenqi Zhang"
  - "Weiming Lu"
  - "Qianglong Chen"
  - "Yongliang Shen"
year: 2026
month: 9
arxiv_id: "2609.20784"
url: "https://arxiv.org/abs/2609.20784"
methods:
  - method:retireopd
cites:
  - paper:opd
  - paper:vista
  - paper:canopy
  - paper:sao
tags:
  - post-training
  - agentic
  - distillation
  - opsd
  - retireopd
---

# RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning

## Abstract Summary
Multi-turn agents trained with RL get one scalar reward per trajectory. Self on-policy distillation (OPD) from a privileged skill-conditioned teacher can densify that signal, but two agentic facts break a fixed schedule: privilege does not always make the teacher reliable, and teacher supervision is stage-dependent. RetireOPD first trains a decoupled skill-conditioned teacher on environment rewards, then trains a skill-free student with RL plus OPD. Adaptive Retirement drops the teacher once student–teacher discrepancy stops shrinking and the student reaches a target fraction of the teacher's success rate; training then continues with RL alone. Across Qwen2.5 1.5B–7B, ALFWorld success rises 14.1–18.8% over RL and WebShop accuracy 11.8–19.0%; the student also surpasses its own skill-conditioned teacher in every reported setting.

## Key Contributions
1. **Decoupled privileged teacher**: skill-conditioned teacher optimized on environment rewards, then a skill-free student under joint RL+OPD.
2. **Adaptive Retirement**: drop OPD when discrepancy stops shrinking and the student hits a fraction of teacher success; then pure RL.
3. **Agentic evidence** that privilege alone is not reliability and that teacher value is stage-dependent.

## Empirical Highlights
- ALFWorld, Qwen2.5 1.5B–7B: +14.1% to +18.8% success vs RL.
- WebShop: +11.8% to +19.0% accuracy vs RL.
- Student beats its own skill-conditioned teacher in every reported setting.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.20784`
- No official GitHub as of 2026-09-18 (`recipe:retireopd` `code_status: none`).
