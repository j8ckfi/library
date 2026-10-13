---
id: paper:saver
type: paper
title: 'Less from More: Reinforcing Sparse Video Reasoning from Dense References'
authors:
- Wenfang Sun
- Yingjun Du
- Cees G. M. Snoek
year: 2026
month: 10
arxiv_id: '2610.10893'
url: https://arxiv.org/abs/2610.10893
methods:
- method:saver
cites:
- paper:orarl
tags:
- video-mllm
- post-training
- saver
---

# Less from More: Reinforcing Sparse Video Reasoning from Dense References

## Abstract Summary
SAVER trains video MLLMs with paired dense/sparse views of the same clip. Grounding plus a reliability-gated reference reward transfers dense evidence to sparse-frame inference. 1,250 Time-R1 temporal-grounding examples, no QA labels. Plug-in on `task:rl-video-mllm` beside OraRL.

## Key Contributions
1. Dense-to-sparse paired-view video RL.
2. Reliability-gated reference reward (dense teaches sparse only when denser grounding is better).
3. 1,250 grounding-only examples transfer to six video-QA benches.

## Empirical Highlights
- Qwen3.5-2B 0.1 fps avg mIoU 18.4→30.0; QA 45.9→50.8.
- 2B 2.0 fps QA 51.0→54.6; 4B 60.8→64.4.
- VideoMMMU 4B 0.1 fps 52.4→72.7.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.10893`
- Code: `https://github.com/lmsdss/SAVER` (`code_status: released`; HTTP 200 as of 2026-10-13).
