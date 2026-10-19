---
id: paper:sigma-delta-sampler
type: paper
title: 'Noise-shaped Sampling and Annealing for Scalable On-the-edge Training of Binary and Ternary AI Models'
authors:
- 'Zihao Chen'
- 'Zhili Xiao'
- 'Rui-Jie Zhu'
- 'Yipeng Wang'
- 'Jason Eshraghian'
- 'Shantanu Chakrabartty'
year: 2026
month: 10
arxiv_id: '2610.22621'
url: https://arxiv.org/abs/2610.22621
methods:
- method:sigma-delta-sampler
cites:
- paper:sparse-bitnet
tags:
- quantization
- ternary
- ising
- active
---

# Sigma-Delta Sampler

## Abstract Summary
The training loss of binary and ternary neural networks, expanded as a multilinear polynomial over the discrete weights, is structurally equivalent to the energy of a hierarchical high-order Ising model. We exploit this equivalence to apply Ising solvers to discrete-weight network training, while accounting for a fundamental difference in objectives: an Ising solver seeks the ground state of a fixed energy function, whereas training seeks solutions that generalize to unseen data. Our key contribution is $\Sigma\Delta$-Sampler, an optimizer that reconciles these objectives by embedding a stochastic sampling-and-annealing step as a noisy quantizer inside a first-order $\Sigma\Delta$ noise-shap

## Key Contributions
1. Sigma-Delta Sampler treats discrete-weight training loss as a high-order Ising energy and embeds stochastic sampling-and-annealing as a noise-shaped quantizer inside a first-order loop so the solver generalizes instead of only seeking a ground state.

## Empirical Highlights
- MatMul-free discrete-weight training to 2.7B

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22621`
- Code: `none found` (`code_status: none`).
