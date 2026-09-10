#!/bin/bash
# Run ON THE MAC MINI. Starts (or brings back) one long-lived, phone-accessible Claude Code
# thread per name below, each in its own tmux window so it keeps running after you close
# Terminal. Safe to run again at any time: names that are already running are skipped.
#
#   brew install tmux          (once)
#   bash start-threads.sh      (after a reboot, or any time)
#   tmux attach -t claude      (to watch them; Ctrl-b d to detach, Ctrl-b n for next window)
#
set -u
REPO="${CLAUDE_RC_DIR:-/Users/andylobster/AgentHub}"
THREADS=(
  "Sourcethermal: Business"
  "Sourcethermal: Projects"
  "Eolas: AgentHub ops"
  "Personal admin"
  "Japan Trip 2026"
  "Trading"
  "Side projects and learning"
)

command -v tmux >/dev/null || { echo "tmux missing: brew install tmux"; exit 1; }
command -v claude >/dev/null || { echo "claude not on PATH"; exit 1; }
tmux has-session -t claude 2>/dev/null || tmux new-session -d -s claude -n home -c "$REPO"

for name in "${THREADS[@]}"; do
  win="$(echo "$name" | tr -c 'A-Za-z0-9\n' '-' | tr -s '-' | sed 's/^-//;s/-$//')"
  if tmux list-windows -t claude -F '#W' | grep -qx "$win"; then
    echo "already running: $name"
    continue
  fi
  # Try to bring back the existing conversation by name first; if there is none yet,
  # start a fresh one with that name. Either way Remote Control is switched on, which
  # is what makes it show up on the phone and at claude.ai/code.
  tmux new-window -t claude -n "$win" -c "$REPO" \
    "claude --remote-control --resume \"$name\" || claude --remote-control --name \"$name\""
  echo "started: $name"
  sleep 3
done
echo
echo "Threads live in tmux session 'claude'. Open the Claude app on your phone, Code tab, and pick them by name."
