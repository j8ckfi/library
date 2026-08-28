---
id: paper:gnot
type: paper
title: 'GNOT: A General Neural Operator Transformer for Operator Learning'
authors:
- Zhongkai Hao
- Zhengyi Wang
- Hang Su
- Chengyang Ying
- Yinpeng Dong
- Songming Liu
- Ze Cheng
- Jian Song
- Jun Zhu
year: 2023
month: 2
arxiv_id: '2302.14376'
url: https://arxiv.org/abs/2302.14376
methods:
- method:gnot
cites:
- paper:fno
- paper:deeponet
tags:
- scientific-ml
- neural-operator
- transformer
- gnot
---

# GNOT: A General Neural Operator Transformer for Operator Learning

## Abstract Summary
Learning partial differential equations' (PDEs) solution operators is an essential problem in machine learning. However, there are several challenges for learning operators in practical applications like the irregular mesh, multiple input functions, and complexity of the PDEs' solution. To address these challenges, we propose a general neural operator transformer (GNOT), a scalable and effective transformer-based framework for learning operators. By designing a novel heterogeneous normalized attention layer, our model is highly flexible to handle multiple input functions and irregular meshes. Besides, we introduce a geometric gating mechanism which could be viewed as a soft domain decomposition to solve the multi-scale problems. The large model capacity of the transformer architecture grants our model the possibility to scale to large datasets and practical problems. We conduct extensive experiments on multiple challenging datasets from different domains and achieve a remarkable improvement compared with alternative methods. Our code and data are publicly available at \url{https://github.com/thu-ml/GNOT}.

## Key Contributions
- Formulates and evaluates `gnot` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/thu-ml/GNOT`
