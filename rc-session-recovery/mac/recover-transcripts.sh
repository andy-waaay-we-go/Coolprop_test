#!/bin/bash
# Run ON THE MAC MINI. Inventories EVERY local Claude Code transcript modified in the
# last RECOVER_DAYS days (default 120), writes a readable Markdown digest for each,
# copies the raw .jsonl to a safe folder, and matches them to the cloud session list
# where it can (by cloud id, by title, or by start time). Read-only against ~/.claude;
# writes only to OUT.
#
#   bash recover-transcripts.sh [path/to/sessions-inventory.json]
#
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
INV="${1:-$HERE/../sessions-inventory.json}"
OUT="${CLAUDE_RECOVER_DIR:-$HOME/Backups/claude-transcripts/recovered-$(date +%Y-%m-%d)}"
DAYS="${RECOVER_DAYS:-120}"
mkdir -p "$OUT/jsonl" "$OUT/digests"

command -v python3 >/dev/null || { echo "python3 is required (xcode-select --install)"; exit 1; }

python3 - "$INV" "$OUT" "$DAYS" <<'PY'
import json, os, re, sys, glob, shutil, datetime, time
inv, out, days = sys.argv[1], sys.argv[2], int(sys.argv[3])
home = os.path.expanduser('~')
rows = json.load(open(inv))
cutoff = time.time() - days * 86400

# Every place a transcript can live on this machine.
roots = [
    os.path.join(home, '.claude', 'projects', '*', '*.jsonl'),
    os.path.join(home, '.claude', 'projects', '*', '*', '*.jsonl'),
    os.path.join(home, 'Library', 'Application Support', 'Claude', '**', '*.jsonl'),
    os.path.join(home, 'Library', 'Application Support', 'Claude Code', '**', '*.jsonl'),
]
files = sorted({f for pat in roots for f in glob.glob(pat, recursive=True)})

def norm(s): return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()
def slug(t): return re.sub(r'[^A-Za-z0-9]+', '-', t or '').strip('-')[:50] or 'untitled'
def parse_ts(s):
    try: return datetime.datetime.fromisoformat(s.replace('Z', '+00:00'))
    except Exception: return None

def text_of(content):
    if isinstance(content, str): return content
    if isinstance(content, list):
        return '\n'.join(c.get('text', '') for c in content if isinstance(c, dict) and c.get('type') == 'text')
    return ''

def scan(path):
    """Return metadata + conversation turns for one transcript."""
    info = dict(path=path, uuid=os.path.splitext(os.path.basename(path))[0], cwd='', first_ts=None,
                last_ts=None, turns=[], first_user='', cloud_ids=set(), title='')
    with open(path, 'r', errors='ignore') as fh:
        for line in fh:
            for m in re.findall(r'session_01[A-Za-z0-9]{22}', line):
                info['cloud_ids'].add(m)
            try: e = json.loads(line)
            except ValueError: continue
            if not isinstance(e, dict): continue
            info['cwd'] = info['cwd'] or e.get('cwd', '')
            if e.get('type') == 'custom-title' or e.get('customTitle'):
                info['title'] = e.get('customTitle') or e.get('title') or info['title']
            role = e.get('type'); msg = e.get('message') or {}
            if role not in ('user', 'assistant') or e.get('isMeta'): continue
            t = text_of(msg.get('content')).strip()
            if not t or t.startswith('<'): continue          # skip command/system-reminder wrappers
            ts = parse_ts(e.get('timestamp') or '')
            if ts:
                info['first_ts'] = info['first_ts'] or ts
                info['last_ts'] = ts
            if role == 'user' and not info['first_user']:
                info['first_user'] = t[:200]
            info['turns'].append((role, (e.get('timestamp') or '')[:16], t[:4000]))
    return info

# Cloud rows indexed for matching.
by_id = {r['id']: r for r in rows}
by_title = {}
for r in rows:
    by_title.setdefault(norm(r.get('title', ''))[:40], []).append(r)

def match(info):
    # A transcript that merely *discusses* many sessions (like a recovery session) mentions many ids;
    # only trust the id method when the file names exactly one known session, or exactly one early on.
    known = [c for c in info['cloud_ids'] if c in by_id]
    if len(known) == 1: return by_id[known[0]], 'cloud id in file'
    if len(known) > 1:
        with open(info['path'], 'r', errors='ignore') as fh: head = fh.read(20000)
        early = [c for c in known if c in head]
        if len(early) == 1: return by_id[early[0]], 'cloud id near start of file'
    for key in (norm(info['title'])[:40], norm(info['first_user'])[:40]):
        if len(key) >= 8:
            for tk, cands in by_title.items():
                if len(tk) >= 8 and (tk.startswith(key) or key.startswith(tk)):
                    return cands[0], 'title / first message'
    if info['first_ts']:
        best = None
        for r in rows:
            c = parse_ts(r.get('created', '').replace(' ', 'T') + ':00+00:00')
            if not c: continue
            d = abs((info['first_ts'] - c).total_seconds())
            if d <= 900 and (best is None or d < best[0]): best = (d, r)
        if best: return best[1], f'start time within {int(best[0]//60)} min'
    return None, ''

recovered, unmatched_local, matched_ids = [], [], set()
for f in files:
    if os.path.getmtime(f) < cutoff or os.path.getsize(f) == 0: continue
    info = scan(f)
    if not info['turns']: continue
    row, how = match(info)
    label = (row or {}).get('title') or info['title'] or info['first_user'][:60] or info['uuid']
    date = (info['first_ts'] or datetime.datetime.fromtimestamp(os.path.getmtime(f))).strftime('%Y-%m-%d')
    base = f"{date}-{slug(label)}-{info['uuid'][:8]}"
    shutil.copy2(f, os.path.join(out, 'jsonl', base + '.jsonl'))
    with open(os.path.join(out, 'digests', base + '.md'), 'w') as fh:
        fh.write(f"# {label}\n\n")
        fh.write(f"local id: `{info['uuid']}`  \ncwd: `{info['cwd']}`  \nsource: `{f}`  \n")
        fh.write(f"cloud match: {('`'+row['id']+'` (' + how + ')') if row else 'none'}  \n")
        fh.write(f"span: {info['first_ts']} to {info['last_ts']}  \nturns kept: last {min(80, len(info['turns']))} of {len(info['turns'])}\n\n")
        fh.write(f"Resume on the mini: `cd {info['cwd'] or '~'} && claude --resume {info['uuid']}`\n\n---\n\n")
        for role, ts, t in info['turns'][-80:]:
            fh.write(f"**{role} {ts}**\n\n{t}\n\n")
    rec = dict(label=label, uuid=info['uuid'], cwd=info['cwd'], path=f, size=os.path.getsize(f),
               first=str(info['first_ts'] or '')[:16], last=str(info['last_ts'] or '')[:16],
               turns=len(info['turns']), cloud=(row or {}).get('id', ''), how=how, digest=base + '.md')
    recovered.append(rec)
    if row: matched_ids.add(row['id'])
    else: unmatched_local.append(rec)

recovered.sort(key=lambda r: r['last'], reverse=True)
still_missing = [r for r in rows if r['id'] not in matched_ids]

with open(os.path.join(out, 'INDEX.md'), 'w') as fh:
    fh.write(f"# Recovered transcripts ({datetime.date.today()})\n\n")
    fh.write(f"{len(recovered)} local transcripts with content in the last {days} days; "
             f"{len(matched_ids)} matched to a cloud session; {len(still_missing)} cloud sessions with no local transcript.\n\n")
    fh.write("## All recovered transcripts (newest first)\n\n| Last activity | Title / first message | Turns | Cloud session | Match | Digest | Resume |\n|---|---|---|---|---|---|---|\n")
    for r in recovered:
        fh.write(f"| {r['last']} | {r['label'][:60]} | {r['turns']} | {('`'+r['cloud']+'`') if r['cloud'] else '' } | {r['how']} | `digests/{r['digest']}` | `claude --resume {r['uuid']}` |\n")
    fh.write("\n## Cloud sessions with no local transcript\n\nEither never received a message (most of the batch-created named threads), ran on another machine, or were purged by the 30-day cleanup.\n\n| Created | Title | Cloud id | Status |\n|---|---|---|---|\n")
    for r in sorted(still_missing, key=lambda r: r.get('created', ''), reverse=True):
        fh.write(f"| {r.get('created','')} | {r.get('title','')[:60]} | `{r['id']}` | {r.get('status','')} |\n")
print(f"{len(recovered)} transcripts recovered ({len(matched_ids)} matched to cloud sessions), "
      f"{len(still_missing)} cloud sessions without a local transcript.")
print(f"Index: {out}/INDEX.md")
PY
