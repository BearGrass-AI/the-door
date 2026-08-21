---
doc_type: snapshot
title: "Prompt: propose a door for this repository"
created: 2026-08-21
---

# Prompt: propose a door for this repository

Hand this to an agent that can read your repository. It proposes and stops. It does not
move, rewrite or delete anything, and that restraint is not politeness, it is the doctrine:
authority is conferred by a person, so an agent that admitted documents by itself would be
breaking the rule it is installing.

Copy everything below the line.

---

Read this repository's documentation and propose a door for it. Do not change, move, rename
or delete any file. Produce two things and then stop.

**First, a proposed `door.md`.** A door is a short list, in one file at the repository root,
of the documents that are allowed to STOP A HUMAN: to halt a deploy, to block a change, to
override somebody's judgement about what is true right now. It is not a table of contents and
it is not a map of the repository. Most repositories need fewer than a dozen entries. If your
list is long, you have written a contents page and you should start again.

A document may be admitted only if it passes one of two tests.

It is LAW: an append-only ledger of dated, numbered decisions where the highest entry on a
topic wins, nothing is edited after the fact, and superseded entries stay in place.

Or it is RE-MEASURABLE: it prints, verbatim, a command a reader can run to prove its claims,
and it dates the last time that command was run. Describing how you would check something does
not count. The command has to be in the document.

Everything else is a snapshot: a handwritten picture of how the world was on a particular day.
Architecture overviews, environment summaries, current-state pages, onboarding explainers,
status documents. Snapshots are legitimate and often the fastest way to bring somebody up to
speed. They do not go on the door, they carry a date, and they never claim precedence.

**Second, a candidate list.** Every documentation file you found, with three columns: the file,
your verdict of LAW, RE-MEASURABLE or SNAPSHOT, and one sentence of reasoning.

Flag these specifically, because they are what the door exists to catch.

Any sentence in which a document asserts its own precedence. Phrasings to look for include
source of truth, authoritative, canonical, this document takes precedence, this page wins, if
in doubt, start here, and the one fact you need. Report the file, the line and the sentence.
Note that a document QUOTING such a sentence from somewhere else is not asserting it; quoting a
claim of precedence is not making one, and confusing the two produces false findings.

Any confident claim about the current state of a running system with no adjacent proof. What is
deployed, what credentials exist, what is live, what is dormant, what is configured. High
certainty with no way to check is the exact shape of the problem.

Any document marked retired, deprecated or superseded that is still sitting in the searched path.
A retirement marker in frontmatter does not travel with a fragment, so an agent retrieving a chunk
from the middle never sees it. Retiring in place does not work.

When you have produced both, stop and wait. A human decides what goes on the door. Do not create
the file, and do not act on anything you found.
