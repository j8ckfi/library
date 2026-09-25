---
id: paper:lastopd
type: paper
title: "LastOPD: Taming Collapse in Latent On-Policy Distillation"
authors:
  - "Jie Yang"
  - "Zhengyu Fang"
  - "Zelin Xu"
  - "Jiarui Sun"
  - "Xiran Fan"
  - "Junpeng Wang"
  - "Liang Wang"
  - "Qinghua Liu"
  - "Yiwei Cai"
  - "Yan Zheng"
year: 2026
month: 9
arxiv_id: "2609.28845"
url: "https://arxiv.org/abs/2609.28845"
methods:
  - method:lastopd
cites:
  - paper:opd
  - paper:oprd
  - paper:cal-opd
tags:
  - post-training
  - distillation
  - on-policy
  - lastopd
---

# LastOPD: Taming Collapse in Latent On-Policy Distillation

## Abstract Summary
On-policy distillation scores the teacher's next-token distribution and misses how the teacher thinks in latent states. Depth-paired latent OPD (OPRD-Bridge) on cross-size Qwen3 pairs shows two failures: early gain then late collapse (MATH-500 25→46 in 10 steps, then down to 11), and better alignment with worse behavior (projected cosine keeps rising as accuracy falls). LastOPD applies the latent loss only at the last-layer pre-LM-head state and crossfades into reverse top-k token OPD over about 10 steps. On Qwen3-4B/8B → Qwen3-1.7B-Base, MATH-500 improves +5.55 / +4.02 vs token-only OPD and reaches token-OPD's final score in about half the steps. Visa Research / UIC / CWRU / UF / OSU. Code announced at `https://github.com/Muyiiiii/LastOPD`.

## Key Contributions
1. **Collapse diagnosis**: depth-paired latent OPD helps then harms; alignment is not a behavior proxy; J-Lens readouts show teacher knows-early/tells-late vs student tells-as-it-goes.
2. **Last-layer latent + 10-step crossfade**: align only the common pre-head interface, then hand off to token OPD.
3. **Same-lineage exception**: latent-only OPRD-Vanilla can keep working when CKA is diagonal; LastOPD is for the cross-size collapse regime.

## Empirical Highlights
- Qwen3-4B → 1.7B-Base MATH-500 avg@8: LastOPD 58.95 vs token-only OPD 53.40 (+5.55); eight-dataset mean 31.88 vs 27.95 (+3.93).
- Qwen3-8B → 1.7B-Base MATH-500: 53.45 vs 49.43 (+4.02); mean +2.10.
- OPRD-Bridge latent-only collapses to 12.12 / 12.32, below the untrained student (24.45).
- Same-lineage JustRL-1.5B → R1-Distill-1.5B: OPRD-Vanilla 87.22 beats LastOPD 83.42 on MATH-500.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.28845`
- Claimed code: `https://github.com/Muyiiiii/LastOPD` (404 as of 2026-09-25; `recipe:lastopd` `code_status: announced`).
