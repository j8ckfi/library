---
id: paper:lafa
type: paper
title: 'Large Flow Language Models'
authors:
- 'Arnav Chavan'
- 'Chanhyuk Lee'
- 'Udbhav Bamba'
- 'Jaehoon Yoo'
- 'Seunghoon Hong'
- 'Aditi Raghunathan'
- 'Jinwoo Kim'
year: 2026
month: 10
arxiv_id: '2610.28559'
url: https://arxiv.org/abs/2610.28559
methods:
- method:lafa
cites:
- paper:semicat
tags:
- flow-lm
- continuous-diffusion
- active
---

# Large Flow Language Models

## Abstract Summary
Lafa is a blockwise continuous flow LM adapted from a pretrained AR model: causal prefix attention, bidirectional flow inside blocks, <30B-token train at 0.5B/7B/8B, and 2.54x AR throughput via self-speculative AR verify of flow drafts.

## Key Contributions
1. Billion-scale blockwise flow LM from AR init plus self-speculative decode.

## Empirical Highlights
- Matches or beats AR quality; 2.54x AR throughput at comparable quality.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28559`
- Code: `https://github.com/lafa-gh/large-flow-lms` (`code_status: released`).
