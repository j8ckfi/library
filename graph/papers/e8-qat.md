---
id: paper:e8-qat
type: paper
title: 'E8-QAT: Efficient 2-Bit Quantization-Aware Training with Implicit Lattice Codebooks'
authors:
- 'Xinyu Lei'
- 'Hong Huang'
- 'Jiebin Zhang'
- 'Hongyu Li'
- 'Jinlong Song'
- 'Decheng Wu'
- 'Guanghua Yu'
- 'Jianchen Zhu'
- 'Sujian Li'
year: 2026
month: 10
arxiv_id: '2610.27699'
url: https://arxiv.org/abs/2610.27699
methods:
- method:e8-qat
cites:
- paper:gradcodes
tags:
- quantization
- qat
- 2bit
- active
---

# E8-QAT

## Abstract Summary
E8-QAT jointly quantizes 8-d weight groups onto the E8 lattice by arithmetic projection, with a 2-bit core plus sparse extension and no explicit codebook search in the train forward.

## Key Contributions
1. Implicit E8 lattice codebook for 2-bit QAT.

## Empirical Highlights
- Qwen3.6-35B-A3B matches BF16 four-task average; +2.03% IFEval / +1.51% LiveCodeBench vs SOTA 2-bit; 80% peak-mem cut; 1.97x BF16 decode.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27699`
- Code: `https://github.com/lxy2137/E8_QAT` (`code_status: released`).
