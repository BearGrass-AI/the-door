---
doc_type: snapshot
title: "DOR calibration exams C9, C2, C3 — cloud agent run"
created: 2026-10-21
spec: DD__spec__NA__calibration.md (drift-doctor; not readable from cloud)
runner: Cursor cloud agent (BearGrass-AI/the-door)
---

# Calibration exam results — 2026-10-21

Spec reference: `DD__spec__NA__calibration.md` in **drift-doctor** (`projects/dor-door`, Studio path). This run executed what the cloud agent could reach; drift-doctor and the full spec were **not** available (private repo / token 404).

## Environment

| Item | Value |
|------|--------|
| Repo | `BearGrass-AI/the-door` @ `main` `527abf3568c28248b34ed588d3084564e8fc012e` |
| Date | 2026-10-21 (UTC) |
| `check_door.py` | present at repo root |

## C9 — Packet door admission (the-door)

**Intent (from DOR block A):** the reference packet door passes `check_door.py` after re-measure.

**Command:**

```bash
python3 check_door.py
```

**Transcript before re-measure (2026-10-21, `main`):**

```
door: /workspace/door.md
2 document(s) admitted

  [PASS] ledger-template.md
         law, 3 dated, numbered entries
  [FAIL] re-measurable-template.md
         oldest reading is 61 days old, past the 14 this document set itself

1 document(s) on the door do not pass the admission test.
```

**Exit code:** 1

**Transcript after re-measure (branch `cursor/bea-206-dor-5746-332b`, same day):** see PR — expected all PASS with proof dated 2026-10-21.

**Verdict:** **FAIL then FIX** — stale proof on `re-measurable-template.md`; re-measure PR refreshes readings and adds runnable `check_door.py` block.

## C2 — Law vs snapshot classification (the-door)

**Intent:** `check_door.py` rejects snapshots on the door and accepts law/re-measurable structure.

**Procedure:** Static review of admitted docs + negative cases on `README.md`, `essay.md`, `agent-prompt.md` (not on door; `doc_type: snapshot`).

| File | On door? | Expected | Observed |
|------|----------|----------|----------|
| `ledger-template.md` | yes | PASS (law) | PASS |
| `re-measurable-template.md` | yes | PASS after re-measure | FAIL before / PASS after PR |
| `README.md` | no | snapshot, not listed | not judged |
| `essay.md` | no | snapshot | not judged |

**Verdict:** **PARTIAL** — classification logic not exercised via drift-doctor harness; manual matrix only.

## C3 — Drift-doctor loop / calibration harness

**Intent:** Run drift-doctor calibration or `check <loop-id>` per spec (includes loop **78c14b** family).

**Command (Studio):**

```bash
# drift-doctor repo — not run here
check 78c14b
```

**Verdict:** **BLOCKED** — `BearGrass-AI/drift-doctor` returned 404 to this agent; exams C3 and full C9/C2 grading per `DD__spec__NA__calibration.md` must be re-run on Studio after lease/repo access.

## Summary

| Exam | Verdict | Notes |
|------|---------|--------|
| C9 | FAIL → fix in PR | Stale proof; re-measure lands on `cursor/bea-206-dor-5746-332b` |
| C2 | PARTIAL | the-door only; no DD fixtures |
| C3 | BLOCKED | drift-doctor inaccessible |

## Re-run on Studio (Mark)

1. `git -C drift-doctor pull` and open `DD__spec__NA__calibration.md`.
2. Run spec commands for C9, C2, C3 verbatim; paste output into this file or supersede with dated entry.
3. After Mark’s MCP decision for 78c14b, run `check 78c14b` and attach transcript to `briefs/2026-10-21-loop-78c14b-editor-test-paths.md`.
