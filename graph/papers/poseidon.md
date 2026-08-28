---
id: paper:poseidon
type: paper
title: 'Poseidon: Efficient Foundation Models for PDEs'
authors:
- Maximilian Herde
- Bogdan Raonić
- Tobias Rohner
- Roger Käppeli
- Roberto Molinaro
- Emmanuel de Bézenac
- Siddhartha Mishra
year: 2024
month: 5
arxiv_id: '2405.19101'
url: https://arxiv.org/abs/2405.19101
methods:
- method:poseidon
cites:
- paper:cno
- paper:fno
tags:
- scientific-ml
- neural-operator
- foundation-model
- poseidon
- sota
---

# Poseidon: Efficient Foundation Models for PDEs

## Abstract Summary
We introduce Poseidon, a foundation model for learning the solution operators of PDEs. It is based on a multiscale operator transformer, with time-conditioned layer norms that enable continuous-in-time evaluations. A novel training strategy leveraging the semi-group property of time-dependent PDEs to allow for significant scaling-up of the training data is also proposed. Poseidon is pretrained on a diverse, large scale dataset for the governing equations of fluid dynamics. It is then evaluated on a suite of 15 challenging downstream tasks that include a wide variety of PDE types and operators. We show that Poseidon exhibits excellent performance across the board by outperforming baselines significantly, both in terms of sample efficiency and accuracy. Poseidon also generalizes very well to new physics that is not seen during pretraining. Moreover, Poseidon scales with respect to model and data size, both for pretraining and for downstream tasks. Taken together, our results showcase the surprising ability of Poseidon to learn effective representations from a very small set of PDEs during pretraining in order to generalize well to unseen and unrelated PDEs downstream, demonstrating its potential as an effective, general purpose PDE foundation model. Finally, the Poseidon model as well as underlying pretraining and downstream datasets are open sourced, with code being available at https://github.com/camlab-ethz/poseidon and pretrained models and datasets at https://huggingface.co/camlab-ethz.

## Key Contributions
- Formulates and evaluates `poseidon` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/camlab-ethz/poseidon`
