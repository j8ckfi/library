---
id: paper:openmobile-2
type: paper
title: 'OpenMobile-2: Building Versatile Mobile Agents with Scalable Environment Infrastructure'
authors:
- 'Chenyang Yan'
- 'Yingying Zhang'
- 'Kanzhi Cheng'
- 'Qiushi Sun'
- 'Zhengyuan Pan'
- 'Zheng Ma'
- 'Hang Yan'
- 'Yian Wang'
- 'Nuo Chen'
- 'Jialin Cao'
- 'Xingdong Gong'
- 'Wenpo Song'
- 'Han Chen'
- 'Zichen Ding'
- 'Fangzhi Xu'
- 'Shujian Huang'
- 'Xinyu Dai'
- 'Yichen Liu'
- 'Tiankuo Yao'
- 'Bo Wang'
- 'Ben Kao'
- 'Jianbing Zhang'
- 'Lewei Lu'
- 'Dahua Lin'
year: 2026
month: 10
arxiv_id: '2610.14157'
url: https://arxiv.org/abs/2610.14157
methods:
- method:openmobile-2
cites:
- paper:recreationworld
tags:
- mobile-agent
- gui
- hybrid-cua
- active
---

# OpenMobile-2

## Abstract Summary
We introduce OpenMobile-2, a near-frontier mobile agent with fully open training environments and recipes. We make three key advances: (1) Diverse environments with simulated commercial apps: We build MobileGym++, featuring 35 realistic, functionally rich commercial-style apps with cross-app workflows, while preserving full controllability for reset and verification. Together with newly configured apps in Android emulators, this yields a diverse playground spanning over 110 apps. (2) Open training data at scale: Building on this foundation, we curate nearly 12K mobile interaction trajectories for supervised fine-tuning and the largest open collection of verifiable RL training data for mobile

## Key Contributions
1. OpenMobile-2 scales mobile-agent environments (MobileGym++) with automatic rewards and an experimental hybrid GUI plus app-native tool interface, then trains agents that transfer to real devices.

## Empirical Highlights
- AndroidWorld 79.9; MobileWorld 50.4; SPA-Bench 31.9→59.6

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.14157`
- Code: `none found` (`code_status: none`).
