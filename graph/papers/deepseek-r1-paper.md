---
id: paper:deepseek-r1-paper
type: paper
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
authors:
  - "DeepSeek-AI"
  - "Daya Guo"
  - "Dejian Yang"
  - "Haowei Zhang"
  - "Junxiao Song"
  - "Ruoyu Zhang"
  - "Runxin Xu"
  - "Qihao Zhu"
year: 2025
month: 1
arxiv_id: "2501.12948"
url: "https://arxiv.org/abs/2501.12948"
methods:
  - method:grpo
cites:
  - paper:deepseek-math-paper
tags:
  - post-training
  - reasoning
  - rl-alignment
  - deepseek-r1
---

# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

## Abstract Summary
DeepSeek-R1 demonstrates that advanced reasoning, self-reflection, and chain-of-thought verification can emerge purely through large-scale reinforcement learning with GRPO without supervised fine-tuning (SFT) warmstart. DeepSeek-R1-Zero achieves competitive performance with OpenAI o1 on competitive coding and mathematical Olympiad benchmarks.

## Key Contributions
1. **Pure RL Reasoning Emergence**: Discovered self-correction, verification, and long reasoning trajectories emerging naturally under GRPO.
2. **Cold-Start Distillation Pipeline**: Combined multi-stage SFT distillation with large-scale GRPO to stabilize readability and language mixing.
3. **Open Release**: Distilled reasoning weights across Llama and Qwen model families.
