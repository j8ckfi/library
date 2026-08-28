---
id: paper:ab-upt
type: paper
title: 'AB-UPT: Scaling Neural CFD Surrogates for High-Fidelity Automotive Aerodynamics
  Simulations via Anchored-Branched Universal Physics Transformers'
authors:
- Benedikt Alkin
- Maurits Bleeker
- Richard Kurle
- Tobias Kronlachner
- Reinhard Sonnleitner
- Matthias Dorfer
- Johannes Brandstetter
year: 2025
month: 2
arxiv_id: '2502.09692'
url: https://arxiv.org/abs/2502.09692
methods:
- method:ab-upt
cites:
- paper:upt
- paper:gino
tags:
- scientific-ml
- neural-operator
- cad-mesh
- cfd
- ab-upt
---

# AB-UPT: Scaling Neural CFD Surrogates for High-Fidelity Automotive Aerodynamics Simulations via Anchored-Branched Universal Physics Transformers

## Abstract Summary
Recent advances in neural surrogate modeling offer the potential for transformative innovations in applications such as automotive aerodynamics. Yet, industrial-scale problems often involve volumetric meshes with cell counts reaching 100 million, presenting major scalability challenges. Complex geometries further complicate modeling through intricate surface-volume interactions, while quantities such as vorticity are highly nonlinear and must satisfy strict divergence-free constraints. To address these requirements, we introduce AB-UPT as a novel modeling scheme for building neural surrogates for CFD simulations. AB-UPT is designed to: (i) decouple geometry encoding and prediction tasks via multi-branch operators; (ii) enable scalability to high-resolution outputs via neural simulation in a low-dimensional latent space, coupled with anchored neural field decoders to predict high-fidelity outputs; (iii) enforce physics consistency by a divergence-free formulation. We show that AB-UPT yields state-of-the-art predictive accuracy of surface and volume fields on automotive CFD simulations ranging from 33 thousand up to 150 million mesh cells. Furthermore, our anchored neural field architecture enables the enforcement of hard physical constraints on the physics predictions without degradation in performance, exemplified by modeling divergence-free vorticity fields. Notably, the proposed models can be trained on a single GPU in less than a day and predict industry-standard surface and volume fields within seconds. Additionally, we show that the flexible design of our method enables neural simulation from a CAD geometry alone, thereby eliminating the need for costly CFD meshing procedures for inference.

## Key Contributions
- Formulates and evaluates `ab-upt` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/Emmi-AI/AB-UPT`
