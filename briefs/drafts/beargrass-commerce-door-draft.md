---
doc_type: snapshot
title: "DRAFT — beargrass-commerce door (fleet pilot BEA-213)"
created: 2026-10-21
target_repo: BearGrass-AI/beargrass-commerce (private; not cloned here)
status: draft-only — do not commit to commerce repo from cloud
---

# DRAFT: `door.md` for beargrass-commerce

**Pilot scope:** second fleet repo after **D-070** (the-door packet only). Commerce holds checkout, catalog, and payment-adjacent law; only documents that may **halt money or deploy** belong on the door.

## Proposed `door.md` (root)

```markdown
---
doc_type: ledger
title: "The door"
updated: 2026-10-21
---

# The door

Documents allowed to stop a human on commerce changes (deploy, price, tax, payment keys, refund policy).

Run `python3 check_door.py` if present, or drift-doctor door probe when wired.

## D-1 2026-10-21 — Admitted (draft)

- [`+law.md`](+law.md) — law (commerce decisions ledger), when present and passing admission.
- [`docs/deploy-remeasurable.md`](docs/deploy-remeasurable.md) — re-measurable: proves which Worker/env receives `wrangler deploy` and lists secret **names** only.

## D-2 2026-10-21 — Deliberately NOT admitted (draft)

- `README.md`, architecture overviews, Stripe dashboard screenshots, and any `CURRENT_STATE` snapshot.
- Generated OpenAPI / GraphQL dumps (snapshots).
```

## Candidate list (first pass — verify on Studio)

| File | Verdict | Reason |
|------|---------|--------|
| `+law.md` or `LAW.md` | LAW | Append-only commerce decisions (tax, refunds, env) |
| `wrangler.toml` | SNAPSHOT | Config, not authority; cite from re-measurable doc instead |
| `README.md` | SNAPSHOT | Onboarding |
| `docs/*` runbooks | SNAPSHOT unless each prints proof commands |
| Payment / Stripe env docs | RE-MEASURABLE candidate | Must print `wrangler secret list` or approved equivalent with date |

## Admission test

Copy `check_door.py` from **the-door** or depend on drift-doctor fleet probe; run before GitBot merge to `main`.

---

# DRAFT: Plan — widen beyond D-070

**D-070 (assumed):** fleet door pilot limited to **the-door** template repo only.

| Phase | Repos | Gate |
|-------|-------|------|
| 0 (now) | `the-door` | Packet door passes C9; D-070 recorded in `projects/dor-door` law |
| 1 | `beargrass-commerce` | Draft door + `check_door.py`; Mark admits entries; no prod deploy from agent |
| 2 | High-risk Workers touching money (`ermahgerd`, client commerce workers) | Same door pattern; drift-doctor `REF_ROOTS` includes each repo |
| 3 | Remaining ED2 tenant repos | Door only for deploy halt docs; snapshots stay off door |

**Proof per widen:** each new repo adds a loop row in drift-doctor calibration sheet; `check <loop>` green before DOR ledger entry supersedes D-070.

**Owner:** Mark admits documents; GitBot moves `main`; agents open PRs only.
