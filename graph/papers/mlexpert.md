---
id: paper:mlexpert
type: paper
title: 'MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering'
authors:
- 'Shangheng Du'
- 'Jinxin Shi'
- 'Shuaiyu Zhang'
- 'Yiming Wu'
- 'Junpeng Zhao'
- 'Shiyang Feng'
- 'Xin Li'
- 'Liang He'
- 'Xiangchao Yan'
- 'Bo Zhang'
year: 2026
month: 10
arxiv_id: '2610.22344'
url: https://arxiv.org/abs/2610.22344
methods:
- method:mlexpert
cites:
- paper:sao
tags:
- mle
- agentic-rl
- wirl
- active
---

# MLExpert

## Abstract Summary
Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent MLE systems adopt model-directed interaction, allowing models to autonomously organize experiments and adapt optimization strategies based on execution feedback. However, feedback from each experiment reflects several preceding decisions, and a long MLE run contains many such cost

## Key Contributions
1. MLExpert post-trains a 35B MoE MLE agent with hierarchical agentic SFT, then Windowed Interaction RL that shares an outcome reward across the multi-turn decisions between successive experiment results, with asynchronous collection and policy correction.

## Empirical Highlights
- 37.9%→72.7% on MLE-Bench Lite; comparable to larger Kimi-K3 / GLM-5.3 in the paper

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22344`
- Code: `https://github.com/InternScience/MLExpert` (`code_status: released`).
