---
id: paper:critical-state-rl
type: paper
title: "Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use"
authors:
  - "Zixiang Chen"
  - "Wenting Zhao"
  - "Zhepeng Cen"
  - "Akshara Prabhakar"
  - "Jielin Qiu"
  - "Jianguo Zhang"
  - "Zhiwei Liu"
  - "Tulika Manoj Awalgaonkar"
  - "Liangwei Yang"
  - "Shelby Heinecke"
  - "Silvio Savarese"
  - "Huan Wang"
year: 2026
month: 9
arxiv_id: "2609.24985"
url: "https://arxiv.org/abs/2609.24985"
methods:
  - method:critical-state-rl
cites:
  - paper:sao
  - paper:canopy
  - paper:minimax-m1
  - paper:foldgrpo
  - paper:grpo
  - paper:dapo
tags:
  - post-training
  - agentic
  - tool-use
  - critical-state-rl
---

# Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use

## Abstract Summary
A multi-turn tool failure can hinge on one model call, but reward variation does not say which call is trainable. When later interactions contribute to the reward, mixed success/fail groups can be continuation noise rather than action effects. Critical-State RL diagnoses candidate calls: the local reward must capture the action's effect on task success, there must be headroom versus a reference policy, and nested sampling at a fixed prefix must separate action-dependent label variance from continuation noise. The selected occurrence is then trained as a contextual bandit; surrounding turns supply context or reward without gradient. On BFCL v4, training diagnostic-selected states lifts missing-function accuracy about 14 pp; training the alternative turns is flat or worse. No public code as of 2026-09-22.

## Key Contributions
1. **Trainability diagnostic**: action-sufficiency, reference-policy headroom, nested-sampling action variance — mixed-group GRPO/DAPO is not enough.
2. **Occurrence-local RL**: contextual-bandit loss only on the selected call's tokens.
3. **Four-cell BFCL test**: diagnostic picks recovery for miss_func and decision for miss_param; always-decision / always-recovery each help one cell and hurt or stall the other.

## Empirical Highlights
- Gemma-4-26B-A4B no-think, BFCL v4 multi_turn, four seeds: miss_func recovery 0.14 → 0.283±0.015 (+14.3 pp); miss_func decision alternative −4.5 pp.
- miss_param decision 0.435 → 0.473±0.010 (+3.8 pp); miss_param recovery +1 pp.
- Nemotron missing-function: trains the decision before tool availability, +4.4 pt. Repeat-call logs: GPT-4.1 agreement 37% → ~75%. Memory sub-task: xLAM 34.54% → 50.54%; Gemma 38.1% → 52.7%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.24985`
- No public GitHub as of 2026-09-22 (`recipe:critical-state-rl` `code_status: none`). Same note pattern as Cal-OPD.
