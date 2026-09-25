---
id: paper:rufus-air
type: paper
title: "Rufus-Air: An Open LLM Post-Training Recipe"
authors:
  - "Chia-Yuan Chang"
  - "Renyuan Cheng"
  - "Rui Feng"
  - "Xiaotian Han"
  - "Yuan He"
  - "Hongye Jin"
  - "Linwei Li"
  - "Shiyang Li"
  - "Fenglin Liu"
  - "Xin Liu"
  - "Priyanka Nigam"
  - "Haoyang Wen"
  - "Zhenghao Xu"
  - "Zhuocheng Xu"
  - "Bing Yin"
  - "Qingyu Yin"
  - "Chao Zhang"
  - "Rongzhi Zhang"
  - "Zhihan Zhang"
  - "Zixuan Zhang"
  - "Tuo Zhao"
year: 2026
month: 9
arxiv_id: "2609.29421"
url: "https://arxiv.org/abs/2609.29421"
methods:
  - method:rufus-air
cites:
  - paper:miles
  - paper:gspo
  - paper:grpo
tags:
  - systems
  - post-training
  - agentic
  - rufus-air
---

# Rufus-Air: An Open LLM Post-Training Recipe

## Abstract Summary
Rufus-Air is an open, reproducible eight-stage serial post-training recipe on GLM-4.5-Air-Base (106B-A12B): SFT → Reasoning RL → Coding RL → Instruction-Following RL → General Agent → Coding Agent → Search Agent → RLHF. Stages run from basic to advanced capability and from hard verifiable rewards toward softer judge-based signals. Training uses public data as released (no new human annotation, no in-house distillation teacher) and open infrastructure (Slime + SGLang + Megatron). The finished checkpoint beats the official GLM-4.5-Air post-trained release on every reported bench except Arena-Hard v2 Creative Writing, and is competitive with similarly sized open models. Amazon. Authors listed alphabetically.

## Key Contributions
1. **Documented serial recipe**: eight stages, data mixes, reward design, and stagewise tables a team can rerun.
2. **Reward-reliability stage order**: verifiable RLVR first; gameable judge/preference last. Difficulty/learnability filtering keeps prompts in a productive band.
3. **Infra as part of the recipe**: token-in/token-out multi-turn rollouts, Rollout Routing Replay, consistent chat templates, long-run sandbox.

## Empirical Highlights
- vs GLM-4.5-Air (same harness, Table 1): IFBench prompt-strict 76.9 vs 33.6; IFEval 95.4 vs 83.0; LiveCodeBench v6 76.4 vs 59.6; Terminal-Bench 2.1 42.7 vs 24.7; SWE-bench Verified 65.6 vs 50.6; BrowseComp 37.1 vs 22.7; HLE-Verified Gold 51.1 vs 20.2.
- Arena-Hard v2 Creative Writing is the exception (53.0 vs GLM-4.5-Air 60.3).
- SFT on 64×8 H200; RL stages 8–32 nodes. Checkpoint 3799 carried from SFT into RL.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.29421`
- No dedicated Rufus-Air GitHub as of 2026-09-25 (`recipe:rufus-air` `code_status: none`). Recipe assumes open `THUDM/slime` + SGLang. Miles remains the production engine first hop.
