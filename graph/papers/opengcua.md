---
id: paper:opengcua
type: paper
title: 'OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use'
authors:
- Hanzhang Zhou
- Long Li
- Quyu Kong
- Lei Wang
- Panrong Tong
- Long Chen
- Tianyu Xia
- Gongjie Zhang
- Xu Zhang
- Chen Liu
- Jianan Zhang
- Chenglin Cai
- Zhengwen Zeng
- Steven Hoi
- Yue Wang
year: 2026
month: 10
arxiv_id: '2610.22200'
url: https://arxiv.org/abs/2610.22200
methods:
- method:opengcua
cites:
- paper:recreationworld
- paper:softwaregym
tags:
- computer-use
- harness
---

# OpenGCUA

## Abstract Summary
A generalist computer-use agent chooses how to observe, act, and organize work across visual and programmatic interfaces. OpenGCUA opens that stack: code execution in the loop, harness-to-model decision transfer, real-device harness, and a cross-device SDK.

## Key Contributions
1. Code execution as a first-class CUA action.
2. Move selected observations and task-state decisions from harness rules to the model.
3. OSWorld-v2 eval of eight models including GPT-6 Astra and Claude Opus 5.

## Empirical Highlights
- Full configuration +19.6 mean partial vs batched GUI-only; -53.0% steps per task.
- Real macOS: selected Qwen3.8-Max uses 19.4x reported reasoning tokens vs GPT-6 Astra.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22200`
- Code: `https://github.com/Tongyi-MAI/OpenGCUA` (`code_status: released`).

