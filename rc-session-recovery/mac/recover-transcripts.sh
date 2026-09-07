#!/bin/bash
# Run ON THE MAC MINI. Finds the local transcript for every session in
# sessions-inventory.json, copies it to a safe folder, and writes a readable
# Markdown digest per session so the content can be pasted into the new
# consolidated threads. Read-only against ~/.claude; writes only to OUT.
#
#   bash recover-transcripts.sh [path/to/sessions-inventory.json]
#
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
INV="${1:-$HERE/../sessions-inventory.json}"
OUT="${CLAUDE_RECOVER_DIR:-$HOME/Backups/claude-transcripts/recovered-$(date +%Y-%m-%d)}"
PROJ="$HOME/.claude/projects"
mkdir -p "$OUT/jsonl" "$OUT/digests"

command -v python3 >/dev/null || { echo "python3 is required (xcode-select --install)"; exit 1; }

python3 - "$INV" "$PROJ" "$OUT" <<'PY'
import json, os, re, sys, glob, shutil, datetime
inv, proj, out = sys.argv[1:4]
rows = json.load(open(inv))
found, missing = [], []

def slug(t): return re.sub(r'[^A-Za-z0-9]+', '-', t).strip('-')[:50] or 'untitled'

# Index every transcript once: local uuid -> path, plus any cloud id it mentions.
files = glob.glob(os.path.join(proj, '*', '*.jsonl'))
by_cloud = {}
for f in files:
    try:
        with open(f, 'r', errors='ignore') as fh:
            head = fh.read(200000)
        for m in set(re.findall(r'session_01[A-Za-z0-9]{22}', head)):
            by_cloud.setdefault(m, f)
    except OSError:
        pass

def digest(path, title, cid):
    lines = []
    with open(path, 'r', errors='ignore') as fh:
        for line in fh:
            try: e = json.loads(line)
            except ValueError: continue
            role = e.get('type'); msg = e.get('message') or {}
            if role not in ('user', 'assistant'): continue
            content = msg.get('content')
            if isinstance(content, list):
                content = ' '.join(c.get('text', '') for c in content if isinstance(c, dict) and c.get('type') == 'text')
            if not content or not str(content).strip(): continue
            ts = (e.get('timestamp') or '')[:16]
            lines.append(f"**{role} {ts}**\n\n{str(content).strip()[:4000]}\n")
    body = '\n'.join(lines[-80:])
    return f"# {title}\n\ncloud id: `{cid}`  \nsource: `{path}`  \nmessages kept: last {min(80, len(lines))} of {len(lines)}\n\n---\n\n{body}"

for r in rows:
    cid, title = r['id'], r.get('title') or 'untitled'
    path = by_cloud.get(cid)
    if not path:
        missing.append((cid, title, r.get('created', '')))
        continue
    base = f"{r.get('created','')[:10]}-{slug(title)}-{cid[-6:]}"
    shutil.copy2(path, os.path.join(out, 'jsonl', base + '.jsonl'))
    with open(os.path.join(out, 'digests', base + '.md'), 'w') as fh:
        fh.write(digest(path, title, cid))
    found.append((cid, title, path, os.path.getsize(path), datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat(timespec='minutes')))

with open(os.path.join(out, 'INDEX.md'), 'w') as fh:
    fh.write(f"# Recovered transcripts ({datetime.date.today()})\n\n{len(found)} found, {len(missing)} not on this machine.\n\n")
    fh.write("## Found\n\n| Title | Cloud id | Local file | Size | Modified |\n|---|---|---|---|---|\n")
    for cid, t, p, s, m in sorted(found, key=lambda x: x[4], reverse=True):
        fh.write(f"| {t[:50]} | `{cid}` | `{p}` | {s//1024} KB | {m} |\n")
    fh.write("\n## Not found locally (purged by cleanupPeriodDays, or ran elsewhere)\n\n| Title | Cloud id | Created |\n|---|---|---|\n")
    for cid, t, c in missing:
        fh.write(f"| {t[:50]} | `{cid}` | {c} |\n")
print(f"{len(found)} transcripts copied, {len(missing)} missing. Index: {out}/INDEX.md")
PY
