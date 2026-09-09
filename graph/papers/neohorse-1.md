---
id: paper:neohorse-1
type: paper
title: "NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness"
authors:
  - "Guoliang Cao"
  - "Guohao Dai"
  - "Tianyu Guo"
  - "Kai Han"
  - "Hailin Hu"
  - "Zihan Jiang"
  - "Xiang Kuang"
  - "Boxun Li"
  - "Yulong Li"
  - "Zehua Pei"
  - "Yuchuan Tian"
  - "Jiamin Wang"
  - "Yu Wang"
  - "Yunhe Wang"
  - "Yihong Wu"
  - "Haiyang Xu"
  - "Shuo Zhang"
  - "Hang Zhou"
  - "Siyang Cheng"
  - "Jiayu Fan"
  - "Wei He"
  - "Qingrui Jiao"
  - "Hongguang Li"
  - "Zhiyuan Li"
  - "Runke Liu"
  - "Xi Liu"
  - "Xinchen Liu"
  - "Sinno Jialin Pan"
  - "Yi Ren"
  - "Liuyang Song"
  - "Chenyu Wang"
  - "Bei Yu"
  - "Quanlu Zhang"
  - "Xiangyu Zhang"
  - "Mengyu Zheng"
  - "Yingjie Zong"
year: 2026
month: 9
arxiv_id: "2609.08183"
url: "https://arxiv.org/abs/2609.08183"
methods:
  - method:neohorse-1
cites:
  - paper:opd
tags:
  - post-training
  - agentic
  - rsi
  - routing
  - neohorse
---

# NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness

## Abstract Summary
NeoHorse-1 is a family of agent-native models that treat a deployed routing harness as the RSI mechanism: each turn records predicted capability demand, selected service tier, and the interaction that followed. Records become user-turn training examples that keep interleaved reasoning, tool calls, and harness context, admitted through structural validation, six-dimensional semantic evaluation, and subscene labeling. Routing scores organize SFT into a three-stage curriculum and extend to routing-guided OPD, where a teacher supervises student-generated responses under the same progression. Capability-guided allocation then converts evaluation into the next training mixture. Across ten benchmarks covering harness agents, tool use, coding, and instruction following, post-training raises the 4B macro-average from 58.94 to 64.87 and the 9B from 65.60 to 69.04, narrowing the gap between the post-trained 4B and the 9B base.

## Key Contributions
1. **Routing harness as RSI sensor**: demand, tier, and interaction logged per turn.
2. **Admission**: structural validation + six-dimensional semantic eval + subscene labels.
3. **Routing-guided curriculum**: three-stage SFT, then routing-guided OPD on student prefixes.
4. **Evaluation–selection–update loop**: capability feedback reallocates the next mix.

## Empirical Highlights
- NeoHorse-1-4B macro 64.87 vs Qwen3.5-4B 58.94 (Table 1). Largest lifts on harness agents and coding (τ²-Bench 88.46 vs 84.29; PinchBench 77.33 vs 71.19; WorkBuddy 34.41 vs 24.62).
- NeoHorse-1-9B macro 69.04 vs Qwen3.5-9B 65.60 (Table 2).

## Open Source Repository & Resources
- Code: `https://github.com/TokenRhythm/NeoHorse`
- Weights: `https://hf.co/collections/TokenRhythm/neohorse-1`
