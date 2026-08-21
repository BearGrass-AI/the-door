---
doc_type: re-measurable
title: "Environment, and how to prove it"
updated: 2026-08-21
verified: 2026-08-21
proof_max_age_days: 14
---

# Environment, and how to prove it

Every claim here prints the command that settles it. If you doubt a line, run the command
next to it. Do not trust the recorded output; it is a reading from a moment, and the moment
is stamped so you can see how old it is.

**The trap this format exists to avoid.** A printed command with a cached result beside it
and no date is worse than no proof at all, because the result is exactly what persuades a
reader not to run the command. Date every reading. When a reading is older than the thing
it describes changes, it is no longer proof, it is a snapshot wearing a lab coat.

---

## Which environment does a bare deploy reach

```
<your deploy command, with no flags>
```

Confirms if: it names the environment you expect.
Means the documentation is wrong if: it names anything else.
Last run 2026-08-21.

## What credentials the deployed service holds

```
<your secret-listing command>
```

Names only, never values.

Confirms if: the names match what you believe is configured.
Means the documentation is wrong if: the list is empty when you believe it is armed, or
holds names you did not expect.
Last run 2026-08-21.

## Claims on this page with no read-only test

List them here, honestly, rather than leaving the impression that everything above is proved.
A claim nobody can check from a terminal is a snapshot, and naming it as one is the difference
between an honest page and a crowned one.
