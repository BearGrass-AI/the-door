---
doc_type: snapshot
title: "Loop 78c14b — editor test paths (proposed fix, MCP blocked)"
created: 2026-10-21
loop: 78c14b
blocked_on: Mark MCP decision (BEA-209 / BEA-208)
---

# Loop 78c14b — three failing editor test paths

## Status

**Not cleared in cloud.** `BearGrass-AI/drift-doctor` is private to this GitHub integration (404). Loop output and exact fixture paths were not readable here. Fix is **draft only** until Mark’s **MCP decision** (which editor surfaces count as authoritative for door/drift probes).

## What fails (from DOR task review job 3 / BEA-208)

First full loop **`78c14b`** does not pass `check 78c14b` because **three editor test paths** in drift-doctor’s harness still point at **Editor 1 / pre–law-35** layout. After Mark decides how MCP and editor-2 probes are wired (single source: editor store vs legacy paths), Cursor updates these paths and re-runs the loop on Studio.

### Identified paths (drift-doctor test fixtures — confirm on Studio)

| # | Path (relative to Studio `beargrassai/`) | Failure mode | Proposed fix |
|---|------------------------------------------|--------------|--------------|
| 1 | `spim-staging/spim-test/fixtures/editor-routes.json` → `paths.editorRoot` | Still `spim-editor` / workers.dev smoke paths | Point `editorRoot` at **Editor 2** admin base (`editor.beargrassai.com`) and tenant slug used by spim-test packs |
| 2 | `drift-doctor/tests/fixtures/loop_78c14b/editor_mcp_probe.yaml` → `mcp.server` | References retired **Editor 1 MCP** socket URL | After MCP decision: either **remove** probe, or set to approved **state-data / editor-2 MCP** endpoint documented in ED2 law |
| 3 | `drift-doctor/tests/fixtures/loop_78c14b/store_write_gate.json` → `allowedRoutes` | Lists v1 **`/api/store/*`** paths that no longer match ED2 law 35 write routes | Replace with **editor-2** routes used by `identity_audit` (admin session + site lock aware); drop routes that bypass the editor |

> **Note:** Exact filenames may differ slightly on disk; search Studio: `rg '78c14b' drift-doctor` and `rg 'editor' drift-doctor/tests`.

## Proposed fix (agent half, post-decision)

1. **Mark:** choose MCP decision (BEA-209 checklist) — which MCP(s) are in-bounds for door/drift loops and whether Editor 1 paths are forbidden entirely.
2. **Cursor on Studio:** edit the three fixtures above to match the decision; run `pytest drift-doctor/tests -k 78c14b` (or spec command from `DD__spec__NA__calibration.md`).
3. **Proof:** paste `check 78c14b` clean transcript into this file under a dated heading.

## Waiting on Mark

No code change in **the-door** for this item. **Do not merge** loop fixes until MCP decision is recorded in the DOR ledger (door or projects `dor-door` law).
