---
id: recipe:tdmpc2-control
type: recipe
title: "Continuous Control and Latent World-Model Training with TD-MPC2"
method: method:td-mpc2
task: task:continuous-control-world-model
target_hardware: "1x NVIDIA RTX 4090 (24GB) or 1x A100 (80GB)"
framework: "PyTorch 2.5+ / DMControl / ManiSkill"
repo_url: "https://github.com/nicklashansen/tdmpc2"
pip_dependencies:
  - "torch>=2.5.0"
  - "gymnasium>=0.29.0"
  - "hydra-core>=1.3.0"
tags:
  - control
  - robotics
  - td-mpc2
---

# Continuous Control and Latent World-Model Training with TD-MPC2

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/nicklashansen/tdmpc2`.

## Quickstart Setup
```bash
git clone https://github.com/nicklashansen/tdmpc2.git
cd tdmpc2
pip install -r requirements.txt
python train.py task=dog-run
```
