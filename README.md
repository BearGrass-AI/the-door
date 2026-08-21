---
doc_type: snapshot
title: "the-door"
created: 2026-08-21
---

# the-door

Your agents read prose that a human wrote. Some of that prose was true when it was written
and has quietly stopped being true. When an agent reasons correctly from one of those
sentences and stops you, the alarm is faithful, the reasoning is sound, and the conclusion
is wrong. After enough of them you stop trusting your own alarms, which is the expensive part.

The corpus condition is **semantic exhaust**: authority-shaped prose that has stopped being
true. It is the unavoidable byproduct of an engine doing useful work, not evidence that
anybody was careless. What it does to the person on the receiving end is **alarm fatigue**,
a name borrowed from clinical medicine, where monitors that alarm constantly teach clinicians
to stop responding and people are harmed by alarms that were working correctly.

This is a small kit for fixing it in your own repository. Free, no signup.

## The idea in one paragraph

One page in the root of your repository lists the documents allowed to stop a human. If a
document is not on that list it has no authority, whatever its own body claims. To get on the
list it has to be **law**, an append-only ledger where the highest entry on a topic wins, or
**re-measurable**, meaning it prints a command that proves its own claims. Everything else is
a snapshot: legitimate, dated, and never on the door. A person admits documents. A script
rechecks that they still pass. Authority is granted by a human and retained by measurement.

## What is here

`door.md` is this repository's own door, which doubles as the worked example.

`ledger-template.md` is the shape law takes.

`re-measurable-template.md` is the shape a document takes when it proves its own claims.

`agent-prompt.md` is a prompt to hand an assistant. It reads your repository, proposes a door
and a candidate list with reasoning, and then stops without changing anything.

`check_door.py` is the admission test as a script. It reads `door.md`, opens everything listed,
and fails anything that is neither law nor re-measurable.

It does not take the document's word for which it is. A `doc_type:` line is read as a claim and
checked against the structure of the file, and a document whose claim and structure disagree
fails, saying which is which. Self-conferred authority is the thing the door exists to prevent,
so the check cannot accept it either.

It ages a proof by the date printed beside the command, not by the newest date anywhere in the
file, because an `updated:` line in the frontmatter will otherwise hide a reading from two years
ago. There is no global staleness window; a document sets `proof_max_age_days` for itself, and
one that sets none gets its age reported for you to judge. A fixed threshold would be a guess
about volatility this script cannot make.

A `door.md` that exists but yields no readable entries fails rather than passing quietly. An
entry has to be a markdown link. Naming a document in prose is not admitting it.

`essay.md` is the long argument, written to be read by agents as much as by people.

## Try it

```
git clone <this repository>
cd the-door
python3 check_door.py
```

No dependencies. Python 3 only. Then point it at a repository of your own and watch what
happens, which is usually that it finds no door and says so.

## Start here if you want the short version

Put a door in the root of one repository. Not all of them. One. List the documents that are
allowed to halt a deploy. For each candidate, ask whether it should be permitted to stop you,
and notice that the answer is almost always no. Every no is an afternoon you do not spend later.

## What this is not

Not a documentation linter. Linters check form. The question here is whether a sentence is
still true.

Not automated. Nothing in this repository edits a file. The agent proposes and a human rules,
because an agent that admitted documents by itself would break the rule it was installing.

Not finished. The author holds one door personally, in a system run by one person, and does
not know that the pattern survives an organisation. It is offered as the shape that worked in
his house rather than the only shape.
