# Graph Change Log

Audit log for all mutations to the knowledge graph: new nodes, supersessions, status changes, and
staleness reviews. One entry per mutation, newest first. Reverts append a reversion receipt — never
rewrite history. Format: [docs/ingestion-guide.md](../docs/ingestion-guide.md) §5.

---

### 2026-09-01 — ingest method:bergson shelf (new task:training-data-attribution)
- Added task:training-data-attribution; paper:bergson (2606.11660), paper:magic (2504.16430), paper:trackstar (2410.17413), paper:source-tda (2405.12186), paper:ek-fac (2308.03296); method:bergson (active, sota_for empty), method:magic (sota for the new task only), method:trackstar (active), method:ek-fac (active), method:source-unrolling (niche); recipe:bergson-magic-gpt2-wikitext, recipe:bergson-trackstar.
- MAGIC is current_sota for training-data-attribution only (GPT-2 WikiText LDS 0.983). Bergson does not supersede MAGIC (library vs algorithm). No method in this shelf supersedes another. Training defaults unchanged: CISPO, Muon2, OPD family, OLMo-3, factory process, BMSSP, OPSA, SAE (sasa/circuitsteer/fega). AutoMixer pattern: optional factory component, not mix/kernel SOTA.
- Evidence: Bergson Table 1 GPT-2 WikiText FT LDS (50 queries, N=400, Adam) MAGIC 0.983 ± 0.005 vs SOURCE 0.387 vs EK-FAC 0.257 vs TrackStar 0.184; sorted-subset MAGIC 1.000 / EK-FAC 0.865 / TrackStar 0.803; Appendix C 8×A100 grad-dot 72B / EK-FAC 7B (Kronfluence EK-FAC 14B); WMDP bio token reweight +4.61 pp vs unweighted FT +3.11 pp. verified: true; evidence_level: preprint.
- Scope checks: new diagnostic task in interpretability / category data-attribution; redirects mix search → open-data-recipe, SAE → mechanistic-interpretability-dictionaries, factory → industrial-model-building. 405B intro scale recorded as design, not verified.

### 2026-09-01 — receipt: OPSA sweep #12 (4a8406e1)
- Squash-merged ingest of OPSA, NoRA, GMTS, RA-OPD, Qwen3.8-Next, CE-MoE, and GradCodeS, plus new tasks `task:teacher-free-on-policy-self-adaptation` (OPSA) and `task:full-lowbit-finetune` (GradCodeS). Training defaults unchanged: CISPO, Muon2, OPD family, OLMo-3, factory process, BMSSP. Per-method receipts follow.

### 2026-09-01 — integrity: mirror supersedes for method:muon-optimizer
- `method:muon-scalable.supersedes` now includes `method:muon-optimizer` so the existing `superseded_by` pointer is bidirectional. No SOTA retarget.

### 2026-09-01 — ingest method:opsa (new task:teacher-free-on-policy-self-adaptation)
- Added paper:opsa, method:opsa, recipe:opsa, task:teacher-free-on-policy-self-adaptation.
- Status sota for teacher-free / label-free on-policy self-adaptation only. Does not supersede method:cispo, method:opd, method:u-opsd, method:ttpo, method:self-opd, method:vista, or method:j-zero.
- Evidence: Qwen3-1.7B AIME24 Avg@32 48.85 vs base 13.44 vs OPD 32.08 (arXiv:2608.31046); verified: true; evidence_level: preprint.
- Scope checks: new niche; redirects for labeled RLVR, teacher distillation, consensus unlabeled, test-time, data-free, and flow matching.

### 2026-09-01 — ingest method:nora (active; does not supersede method:lr-matters-lora)
- Added paper:nora, method:nora, recipe:nora. Wired to task:parameter-efficient-fine-tuning and task:lora-quality-tuning.
- Status active. Recommended RLVR-stable LoRA upgrade. 24GB quality default remains vanilla LoRA + rsLoRA + LR sweep.
- Evidence: Llama-3.2-3B SFT avg 43.37 vs LoRA 37.93 vs RSLoRA 41.28; RLVR avg 44.4 vs LoRA 42.8 with PiSSA/MiLoRA collapse (arXiv:2608.31036); verified: true; evidence_level: preprint.
- Scope checks: PEFT shelf; no supersession because the paper does not rerun the library LR-sweep protocol of 2602.04998.

### 2026-09-01 — ingest method:gmts (niche token-filter; does not supersede method:cispo)
- Added paper:gmts, method:gmts, recipe:gmts. Wired to task:math-code-rl-dense.
- Status niche. Optional plug-in for GRPO/DAPO/CISPO-family token truncation via |E·ω|.
- Evidence: Qwen2.5-Math-7B DAPO+GMTS 50.14 vs DAPO+ETS 48.81; Qwen3-8B DAPO+GMTS 56.08 vs 53.71 (arXiv:2608.30632); verified: true; evidence_level: preprint.
- Scope checks: in-scope as train-rlvr add-on; CISPO remains Pass@1 default.

### 2026-09-01 — ingest method:ra-opd (niche teacher-OPD filter; does not supersede method:opd or method:opsa)
- Added paper:ra-opd, method:ra-opd, recipe:ra-opd. Wired to task:student-distillation.
- Status niche. Keep trajectories with (2R−1)G≥0; no extra rollouts.
- Evidence: Qwen3-8B-Base math avg@k 49.43 vs OPD 44.34 vs ExOPD 46.95; DeepSeek-R1-Distill-Qwen-7B 69.34 vs OPD 64.43 (arXiv:2608.27960); verified: true; evidence_level: preprint.
- Scope checks: modular filter on teacher OPD; tension with OPSA teacher-noise finding documented, not a supersession.

### 2026-09-01 — ingest method:qwen38-next (active architecture recipe; does not supersede method:muon2 or method:deepseek-v4)
- Added paper:qwen38-next, method:qwen38-next, recipe:qwen38-next. Wired to task:pretrain-moe-frontier, task:pretrain-dense-7b, task:linear-time-sequence-modeling.
- Status active. GDN hybrid + Gated Residual + QSA CPT + off-accelerator n-gram + Muon/AdamW split. Public code is FlashQLA.
- Evidence: 125B-A6B leads 397B-A17B on 8/14 benches at ~1/9 FLOPs; GDN hybrid avg 53.81 vs full attn 49.87; FlashQLA 2–3× forward (arXiv:2608.30320); verified: true; evidence_level: preprint.
- Scope checks: adjacent mHC/AttnRes/GDN; Muon2 and DeepSeek-V4/Kimi-K3 defaults unchanged.

### 2026-09-01 — ingest method:ce-moe (niche MoE layout; does not supersede method:deepseek-v4)
- Added paper:ce-moe, method:ce-moe. No public code; no recipe.
- Status niche. Concentrate experts in fewer routed layers.
- Evidence: 2B–31.5B matched params; 33.3% fewer GPU-hours at 31.5B with better downstream and throughput (arXiv:2608.28511 abstract); verified: true; evidence_level: preprint.
- Scope checks: optional train-moe layout; DeepSeek-V4 / Kimi-K3 remain architecture defaults.

### 2026-09-01 — ingest method:gradcodes (new task:full-lowbit-finetune)
- Added paper:gradcodes, method:gradcodes, recipe:gradcodes, task:full-lowbit-finetune.
- Status sota for fully low-bit code-space fine-tune only. Does not supersede method:aqlora-q or method:quartet-ii.
- Evidence: Llama-3.2-1B-Instruct GSM8K fully 4-bit GradCodeS Full 41.63 vs PV-Tuning 36.92 vs QLoRA-4Merge 24.79 (arXiv:2608.30908); verified: true; evidence_level: preprint.
- Scope checks: new niche; redirects for mixed-precision 4-bit PEFT, native FP4 hardware train, and 24GB quality LoRA.
