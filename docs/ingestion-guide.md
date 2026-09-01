# 5-Minute Paper Ingestion Guide

Follow these steps whenever adding a new paper or method to `j8ckfi/library`.

For the underlying system contracts (routing guards, evidence gradient, decay protocol), read
[system-design.md](system-design.md). Schema field definitions live in [ontology.md](ontology.md).

---

## Ingestion Checklist

```
[ ] 0. PRE-FLIGHT: confirm the task node exists and your contribution is in its scope
[ ] 1. Choose a clean kebab-case slug for the paper and method
[ ] 2. Scaffold node templates
[ ] 3. Fill in YAML frontmatter and markdown sections (including routing guards & evidence fields)
[ ] 4. SUPERSESSION CHECK: does this demote an existing method? If yes, run the full
       supersession transaction (Step 3) — ingestion without it is an incomplete write
[ ] 5. Update parent task's current_sota and last_reviewed (if new SOTA)
[ ] 6. Append a receipt to graph/CHANGELOG.md
[ ] 7. Run validation: python -m library validate
```

---

## Step 0: Pre-Flight Routing Check (do this before writing anything)

Most ingestion errors are routing errors: the new work lands under the wrong task, or duplicates an
existing method under a different name. Before scaffolding:

1. Resolve the task: `python -m library sota "<domain keywords>"`.
2. Read the task's `scope` and `out_of_scope` lines. If your paper's setting matches an `out_of_scope`
   item or a `redirects` condition, write to the *redirected* task instead.
3. Search for prior art: `python -m library query "<method name>"` — if a close cousin exists, the new
   node's `supersedes` / differentiation must be explicit, not implied.

---

## Step 1: Scaffold Files

Run the CLI scaffolding command:

```bash
# Scaffold the paper
python -m library new paper <paper-slug> --title "Paper Title"

# Scaffold the method
python -m library new method <method-slug> --title "Method Name"

# Scaffold the recipe
python -m library new recipe <recipe-slug> --title "Recipe Title"
```

Files are automatically generated in `graph/papers/`, `graph/methods/`, and `graph/recipes/`.

---

## Step 2: Complete the Nodes

### Paper (`graph/papers/<paper-slug>.md`)
- Populate `authors`, `year`, `month`, `arxiv_id`, and `url`.
- Add linked `methods: [method:<method-slug>]`.
- Write a 2-3 paragraph abstract summary and bulleted key contributions.

### Task (`graph/tasks/<task-slug>.md`) — only if creating a genuinely new task
- Define `domain`, `summary`, and — critically — the routing guards:
  `scope` (what this node owns), `out_of_scope` (near-misses), and `redirects`
  (`{when, to}` conditions that hand the reader to a different task).
- Seed `current_sota` with the best current method and set `last_reviewed` to today.

### Method (`graph/methods/<method-slug>.md`)
- Define `category`, `status` (`sota`, `active`, `superseded`, `niche`, `experimental`).
- Add relations:
  - `sota_for: [task:<task-slug>]`
  - `supersedes: [method:<old-slug>]`
  - `papers: [paper:<paper-slug>]`
  - `recipes: [recipe:<recipe-slug>]`
- Add dated `claims` with benchmark, metric, baseline, verification status, and — where known —
  `evidence_level` (`peer-reviewed | preprint | self-reported | unofficial-repro`) and `source_url`.
- Add `assumptions` (hardware scale / data regime / model-family preconditions) and, if there are known
  wrong-turn conditions, `do_not_use_for` guards (`{when, reason, use_instead}`).
- Write: Overview, When to Use, Gotchas & Failure Modes.

### Recipe (`graph/recipes/<recipe-slug>.md`)
- Specify `target_hardware`, `framework`, `repo_url`, and `pip_dependencies`.
- Provide a clean, executable PyTorch/JAX code snippet and critical hyperparameter guidance.

---

## Step 3: Handle Supersession (If Replacing Existing SOTA)

If this method beats an existing SOTA method, the following edits form **one transaction** — commit them
together or not at all. A half-applied supersession (new method added, old method still `sota`, task still
pointing at the old method) is the single most damaging inconsistency in the graph, because every downstream
agent will trust the stale pointer.

1. In the old method's file (`graph/methods/<old-slug>.md`), set:
   ```yaml
   status: superseded
   superseded_by: method:<new-slug>
   ```
2. In the new method's file, ensure `supersedes: [method:<old-slug>]` exists (no one-way edges).
3. In the corresponding task (`graph/tasks/<task-slug>.md`), update `current_sota` **and** the review stamp:
   ```yaml
   current_sota:
     - method: method:<new-slug>
       as_of: "2026-02"
       benchmark: "MMLU-Pro"
       metric: "accuracy"
       value: 78.4
       notes: "Evaluated at equal compute budget"
   last_reviewed: "2026-08-31"
   ```
4. If the old method remains optimal in a constrained niche, use `status: niche` and record that niche in
   its `When to Use` section so future agents do not over-generalize the supersession.

---

## Step 4: Validate

Ensure graph consistency, referential integrity, absence of cycles, and the supersession post-conditions
(ontology §4.5):

```bash
python -m library validate
```

Ensure the CLI query finds the new method:

```bash
python -m library sota <task-slug>
```

---

## Step 5: Write the Receipt

Every mutation — new node, supersession, status change, staleness review — appends an entry to
`graph/CHANGELOG.md`. The receipt is the graph's audit log: future agents read it to understand *why* the
graph says what it says before trusting it.

```markdown
### 2026-08-31 — ingest method:<new-slug> (supersedes method:<old-slug>)
- Added paper:<new-slug>, method:<new-slug>, recipe:<new-slug>.
- Demoted method:<old-slug> to status: superseded; task:<task-slug> current_sota updated.
- Evidence: <one-line claim summary + arXiv id>; verified: <true/false>.
- Scope checks: confirmed in-scope for task:<task-slug>; no redirect conditions matched.
```

Keep receipts to one mutation per entry, newest first. If a write must be reverted, append a reversion
receipt — never rewrite history.

---

## Step 6: Staleness Review (periodic maintenance)

Between ingestions, the graph decays. A maintenance agent should periodically:

1. List stale tasks: `python -m library stale` (default budget 4 months). Until you have a
   clone, grep `as_of` dates under `graph/tasks/`.
2. For each stale task, re-read the primary papers, search for newer competing work, and either:
   - **Reaffirm** — bump `last_reviewed` to today (no content change), or
   - **Supersede** — run the Step 3 transaction with a new method.
3. Append a receipt for the review batch (`"reviewed N tasks; M reaffirmed, K superseded"`).

An ingest agent that touches a task must also refresh that task's `last_reviewed` — ingestion without
supersession-checking is treated as an incomplete write.
