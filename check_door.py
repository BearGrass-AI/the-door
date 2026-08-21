#!/usr/bin/env python3
"""
check_door.py - the admission test, run as a script.

A document may sit on the door only if it is LAW (an append-only ledger) or
RE-MEASURABLE (it prints a command that proves its own claims, and dates the
result). Anything else is a snapshot. Snapshots may exist. They may not sit
on the door.

The document does not get to decide which it is. A `doc_type:` line is treated
as a CLAIM and checked against the structure of the file; a document whose
claim and structure disagree fails, and says so. Self-conferred authority is
the thing the door exists to prevent, so the check cannot accept it either.

Usage:  python3 check_door.py [path-to-repo]        (defaults to .)
Exit:   0 all clear, 1 something on the door does not pass or could not be read.
"""
import sys, re, datetime
from pathlib import Path

DATE = re.compile(r'(20\d{2})-(\d{2})-(\d{2})')
FENCE = re.compile(r'^\s*(```|~~~)')
DECLARED = re.compile(r'^\s*doc_type:\s*([a-z-]+)\s*$', re.M)
# A ledger entry: an identifier and a date on the same line.
ENTRY = re.compile(r'^[^\n]*?\b([A-Z]{1,4}-\d+|\d{1,4}\.)\B[^\n]*?20\d{2}-\d{2}-\d{2}', re.M)
# How old a proof may be before it is called out. A document may set its own,
# because a single global window is a guess about volatility the tool cannot make.
MAXAGE = re.compile(r'^\s*proof_max_age_days:\s*(\d+)\s*$', re.M)


def parse_date(y, m, d):
    try:
        return datetime.date(int(y), int(m), int(d))
    except ValueError:
        return None


def frontmatter_span(lines):
    """Line indices covered by YAML frontmatter, so its dates never count as proof."""
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                return set(range(0, i + 1))
    return set()


def proof_dates(text):
    """Dates that appear within six lines AFTER a closing fence. The date of the
    reading, not the newest date anywhere in the file."""
    lines = text.split('\n')
    skip = frontmatter_span(lines)
    fences = [i for i, l in enumerate(lines) if FENCE.match(l)]
    closes = fences[1::2]          # every second fence closes a block
    found = []
    for c in closes:
        for i in range(c + 1, min(c + 7, len(lines))):
            if i in skip:
                continue
            for y, m, d in DATE.findall(lines[i]):
                got = parse_date(y, m, d)
                if got:
                    found.append(got)
    return found


def classify(text):
    """Structure decides. Returns (kind, detail)."""
    entries = len(ENTRY.findall(text))
    fences = len([1 for l in text.split('\n') if FENCE.match(l)])
    proofs = proof_dates(text)
    if entries >= 2:
        return 'law', f'{entries} dated, numbered entries'
    if fences >= 2 and proofs:
        return 're-measurable', f'{fences // 2} runnable block(s), oldest reading {min(proofs)}'
    if fences >= 2 and not proofs:
        return 'snapshot', 'prints a command but never dates the reading, so the result cannot be aged'
    return 'snapshot', 'neither an append-only ledger nor a command that proves itself'


def judge(path, today):
    if not path.exists():
        return 'FAIL', 'listed on the door but not present on disk'
    text = path.read_text(errors='replace')

    kind, detail = classify(text)
    claim_m = DECLARED.search(text)
    claim = claim_m.group(1).strip().lower() if claim_m else None
    # "ledger" and "law" name the same thing; so do the two spellings of re-measurable.
    ALIASES = {'ledger': 'law', 'remeasurable': 're-measurable'}
    claim = ALIASES.get(claim, claim)

    if claim and claim != kind:
        return 'FAIL', f'declares itself "{claim}" but reads as {kind}: {detail}'

    if kind == 'snapshot':
        return 'FAIL', f'snapshot ({detail}); snapshots do not go on the door'

    if kind == 'law':
        return 'PASS', f'law, {detail}'

    oldest = min(proof_dates(text))
    age = (today - oldest).days
    m = MAXAGE.search(text)
    if m:
        limit = int(m.group(1))
        if age > limit:
            return 'FAIL', f'oldest reading is {age} days old, past the {limit} this document set itself'
        return 'PASS', f're-measurable, oldest reading {age} days old (limit {limit})'
    return 'WARN', (f're-measurable, oldest reading {age} days old. No proof_max_age_days set, '
                    f'so nothing here knows how fast this subject moves. You decide')


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    door = root / 'door.md'
    if not door.exists():
        print(f'no door.md in {root}')
        print('a repo with no door has no documents carrying authority, which is a valid state.')
        return 0

    raw = door.read_text(errors='replace')
    listed = [r.split('#')[0].strip() for r in re.findall(r'\[[^\]]*\]\(([^)]+)\)', raw)
              if not r.startswith(('http://', 'https://'))]

    print(f'door: {door}')
    if not listed:
        # Silence here would be a pass, and a door nobody can parse is not a pass.
        mentions = len(re.findall(r'`[^`]+\.md`|\b[\w-]+\.md\b', raw))
        print('\nFAIL: door.md exists but no entries could be read from it.')
        if mentions:
            print(f'      {mentions} document name(s) appear in the prose, but an entry on the door')
            print('      must be a markdown link, [name](path.md). Naming a document is not admitting it.')
        else:
            print('      Add entries as markdown links, or delete the file if nothing carries authority.')
        return 1

    today = datetime.date.today()
    failures = warnings = 0
    print(f'{len(listed)} document(s) admitted\n')
    for ref in listed:
        verdict, reason = judge(root / ref, today)
        print(f'  [{verdict}] {ref}\n         {reason}')
        failures += verdict == 'FAIL'
        warnings += verdict == 'WARN'

    print()
    if failures:
        print(f'{failures} document(s) on the door do not pass the admission test.')
        print('Take them off the door or give them a proof. Being on the list is not evidence.')
        return 1
    print(f'all {len(listed)} pass' + (f', {warnings} to look at' if warnings else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
