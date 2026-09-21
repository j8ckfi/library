---
id: paper:vision-rl2
type: paper
title: "Region-Level Policy Optimization for Fine-grained MLLM Perception"
authors:
  - "Yuheng Shi"
  - "Xiaohuan Pei"
  - "Minjing Dong"
  - "Chang Xu"
year: 2026
month: 9
arxiv_id: "2609.19745"
url: "https://arxiv.org/abs/2609.19745"
methods:
  - method:vision-rl2
cites:
  - paper:orarl
  - paper:eps-prompt-scaffolding
tags:
  - post-training
  - multimodal-rl
  - finegrained-perception
  - vision-rl2
---

# Region-Level Policy Optimization for Fine-grained MLLM Perception

## Abstract Summary
Fine-grained MLLM perception is usually bought with more visual tokens. Localization and recognition do not need the same resolution: on a ZoomBench diagnostic, localization tolerates roughly 3–4× stronger token compression than recognition. Vision-RL2 trains a lightweight RoI proposal network with region-level RL. Coherent regions are the actions. A frozen MLLM reader scores each region by how its removal changes the teacher-forced likelihood of the gold answer. Subtractive and additive objectives prune distractors and recover missed evidence. Sparse encoding then spends the crop budget on foreground tokens. The backbone stays frozen; only the small predictor is updated. Across six fine-grained benches and four backbones, Vision-RL2 beats the base model at every token budget and matches or exceeds the full-budget baseline with about 4× fewer visual tokens.

## Key Contributions
1. **Resolution-decoupled inference**: localize from a coarse view; spend tokens on selected evidence.
2. **Region-level RL**: leave-one-out functional contributions from a frozen reader; no region annotations or response sampling.
3. **Sparse crop encoding**: zoom by foreground occupancy and drop background tokens.

## Empirical Highlights
- Qwen3.5-9B, 16,384-token source limit: six-bench average 80.1 vs base 74.6 / Vision-OPD-9B 78.7; V* 95.3, ZoomBench 68.4.
- Qwen3.5-4B training-aligned 576-token protocol: 71.1 vs SD-RPN 66.6 / base 56.2; matches SD-RPN at 4,096 tokens with 4.2× fewer visual tokens.
- Qwen2.5-VL-7B average 71.0 vs ZwZ-7B 69.9 under the shared 16,384-token protocol.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.19745`
- Code: `https://github.com/YuHengsss/VisionRL2`
- Project: `https://yuhengsss.github.io/VisionRL2/`
- Weights/data: Hugging Face collection `YuhengSSS/visionrl2`
