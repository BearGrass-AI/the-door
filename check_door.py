#!/usr/bin/env python3
"""
check_door.py - the admission test, run as a script.

A document may sit on the door only if it is LAW (an append-only ledger) or
RE-MEASURABLE (it carries a runnable command that proves its own claims).
Anything else is a snapshot. Snapshots may exist. They may not sit on the door.

Usage:  python3 check_door.py [path-to-repo]        (defaults to .)
Exit:   0 all clear, 1 at least one entry failed.
"""
import sys, re, datetime
from pathlib import Path

STALE_AFTER_DAYS = 30
DATE = re.compile(r'(20\d{2})-(\d{2})-(\d{2})')
FENCE = re.compile(r'^\s*(```|~~~|\$ |>\s*\$ )', re.M)
DECLARED = re.compile(r'^\s*doc_type:\s*([a-z-]+)\s*$', re.M)
ENTRY = re.compile(r'^\s*(?:[-*]|#{1,6})?\s*\**([A-Z]{1,4}-\d+|\d+\.)\**\s', re.M)


def declared_type(text):
    m = DECLARED.search(text)
    return m.group(1).strip().lower() if m else None


def newest_date(text):
    best = None
    for y, mo, d in DATE.findall(text):
        try:
            got = datetime.date(int(y), int(mo), int(d))
        except ValueError:
            continue
        if best is None or got > best:
            best = got
    return best


def judge(path, today):
    """Return (verdict, reason). verdict in PASS / FAIL / WARN."""
    if not path.exists():
        return 'FAIL', 'listed on the door but not present on disk'
    text = path.read_text(errors='replace')
    kind = declared_type(text)

    if kind == 'ledger':
        if len(ENTRY.findall(text)) < 1:
            return 'FAIL', 'declares itself a ledger but has no numbered entries'
        return 'PASS', 'law, append-only ledger'

    if kind in ('re-measurable', 'remeasurable'):
        if not FENCE.search(text):
            return 'FAIL', 'declares itself re-measurable but prints no runnable command'
        stamp = newest_date(text)
        if stamp is None:
            return 'FAIL', 'prints a command but carries no date, so the result cannot be aged'
        age = (today - stamp).days
        if age > STALE_AFTER_DAYS:
            return 'WARN', f'proof last run {age} days ago; a cached result older than its subject is worse than no proof'
        return 'PASS', f're-measurable, proof {age} days old'

    if kind in ('snapshot', None):
        why = 'undeclared' if kind is None else 'declares itself a snapshot'
        return 'FAIL', f'{why}; snapshots do not go on the door'

    return 'FAIL', f'unknown doc_type "{kind}"'


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    door = root / 'door.md'
    if not door.exists():
        print(f'no door.md in {root}')
        print('a repo with no door has no documents carrying authority, which is a valid state.')
        return 0

    # An entry on the door is a markdown link. Prose that merely mentions a filename
    # is not an admission, which is the use-versus-mention distinction the door depends on.
    listed = []
    for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', door.read_text(errors='replace')):
        if not ref.startswith(('http://', 'https://')):
            listed.append(ref.split('#')[0].strip())

    if not listed:
        print('door.md lists no documents.')
        return 0

    today = datetime.date.today()
    failures = warnings = 0
    print(f'door: {door}')
    print(f'{len(listed)} document(s) admitted\n')
    for ref in listed:
        verdict, reason = judge((root / ref), today)
        print(f'  [{verdict}] {ref}\n         {reason}')
        if verdict == 'FAIL':
            failures += 1
        elif verdict == 'WARN':
            warnings += 1

    print()
    if failures:
        print(f'{failures} document(s) on the door do not pass the admission test.')
        print('Take them off the door or give them a proof. Being on the list is not evidence.')
        return 1
    print(f'all {len(listed)} pass' + (f', {warnings} warning(s)' if warnings else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
