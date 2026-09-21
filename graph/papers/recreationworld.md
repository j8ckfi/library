---
id: paper:recreationworld
type: paper
title: "RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents"
authors:
  - "Shuai Bai"
  - "Jiayong Deng"
  - "Yikun Fu"
  - "Chang Gao"
  - "Xuhao Hu"
  - "Mianqiu Huang"
  - "Yizhen Jiang"
  - "Yuheng Jing"
  - "Dehui Kong"
  - "Keliang Li"
  - "Ning Li"
  - "Wanli Li"
  - "Dayiheng Liu"
  - "Dunjie Lu"
  - "Changwei Luo"
  - "Que Shen"
  - "Zheyuan Wang"
  - "Zijian Wang"
  - "Jie Wu"
  - "Gao Wu"
  - "Zhihui Xie"
  - "Rui Xie"
  - "Haiyang Xu"
  - "An Yang"
  - "Jiakang Yuan"
  - "Yanming Zhang"
  - "Jiajun Zhang"
  - "Xi Zhang"
  - "Zhenru Zhang"
  - "Zhuo Zhen"
  - "Mingkang Zhu"
  - "Bowen Zhou"
year: 2026
month: 9
arxiv_id: "2609.22000"
url: "https://arxiv.org/abs/2609.22000"
methods:
  - method:recreationworld
cites:
  - paper:osworld-2
  - paper:mini-swe-agent
  - paper:canopy
tags:
  - agents
  - computer-use
  - hybrid-cua
  - recreationworld
---

# RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents

## Abstract Summary
GUI computer-use and terminal/code agents have advanced on separate tracks. Hybrid CUAs interleave exploring an interface, implementing software, and visually verifying their own artifacts. RecreationWorld (Qwen) is a five-platform train/eval framework built around recreation: given a running reference, the agent must discover its behavior and build a faithful implementation with no prescribed workflow. The running reference is an oracle for hidden behavioral tests. Environments cover Ubuntu, macOS, Windows, Android, and Web, with a unified harness that exposes native GUI control and coding tools. Trajectories trained in this loop transfer to out-of-distribution coding and hybrid CUA benches. RecreationBench holds 250 held-out tasks with reference-grounded programmatic and visual assertions.

## Key Contributions
1. **Recreation loop**: explore a running reference, implement, run, visually verify; reference-as-oracle rewards.
2. **Five-platform harness**: Ubuntu / macOS / Windows / Android / Web with native GUI and coding tools.
3. **RecreationBench**: 250 tasks (50 per platform), frozen programmatic and visual assertions validated on the reference and by human review.

## Empirical Highlights
- GPT-6 Astra leads RecreationBench at 58.1% overall (Prog 58.19 / VLM 57.92) but passes all programmatic tests on 2.8% of tasks.
- Training on recreation trajectories improves five OOD coding/hybrid CUA benches (gains up to 17.9 pp; Qwen3.7-Plus +5.8, Qwen-Flash-CPT +12.1 on the reported transfer plot).
- Agents reproduce static interface structure more reliably than interactions and computed outputs; generated apps stay smaller and more monolithic than references.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.22000`
- Code: `https://github.com/QwenLM/RecreationWorld`
- Bench: `https://recreation-bench.cc/`
- Dataset: Hugging Face `Qwen/RecreationBench`
