#!/bin/bash
# One-shot installer to run ON THE MAC MINI (as andylobster):
#   bash install.sh
# Installs the two scripts into ~/bin, the two launchd jobs into ~/Library/LaunchAgents,
# raises transcript retention, and turns Remote Control on for every interactive session.
set -eu
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$HOME/bin" "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
install -m 755 "$HERE/claude-rc-server.sh" "$HOME/bin/claude-rc-server.sh"
install -m 755 "$HERE/backup-claude-transcripts.sh" "$HOME/bin/backup-claude-transcripts.sh"

# 1. Transcript retention: default is 30 days, after which ~/.claude/projects/*.jsonl are deleted
#    and a session can no longer be resumed locally. Keep them for a year.
# 2. remoteControlAtStartup: every interactive `claude` on the mini is reachable from the phone.
SETTINGS="$HOME/.claude/settings.json"
if command -v python3 >/dev/null; then
python3 - "$SETTINGS" <<'PY'
import json, sys, os
p = sys.argv[1]
d = json.load(open(p)) if os.path.exists(p) else {}
d["cleanupPeriodDays"] = max(int(d.get("cleanupPeriodDays", 30)), 365)
d["remoteControlAtStartup"] = True
json.dump(d, open(p, "w"), indent=2)
print("updated", p, "cleanupPeriodDays =", d["cleanupPeriodDays"], "remoteControlAtStartup = true")
PY
else
  echo "python3 not found: add \"cleanupPeriodDays\": 365 and \"remoteControlAtStartup\": true to $SETTINGS by hand"
fi

# Take a first transcript backup before anything else changes.
"$HOME/bin/backup-claude-transcripts.sh" || true

# Stop any previous copies, then load the jobs.
for job in com.andy.claude-remote-control com.andy.claude-transcript-backup; do
  launchctl bootout "gui/$(id -u)/$job" 2>/dev/null || true
  install -m 644 "$HERE/$job.plist" "$HOME/Library/LaunchAgents/$job.plist"
  launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/$job.plist"
  launchctl enable "gui/$(id -u)/$job"
done
launchctl kickstart -k "gui/$(id -u)/com.andy.claude-remote-control"

echo
echo "Installed. Check with:  launchctl list | grep com.andy.claude ;  tail -f ~/Library/Logs/claude-remote-control.log"
echo "Still to do once, needs sudo (stops the mini sleeping, restarts it after a power cut):"
echo "  sudo pmset -a sleep 0 disksleep 0 autorestart 1 womp 1"
