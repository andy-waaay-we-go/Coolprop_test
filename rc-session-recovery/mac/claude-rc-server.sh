#!/bin/bash
# Keeps ONE Remote Control server alive on the Mac mini, resuming the sessions it
# was already serving instead of minting a fresh batch on every restart.
# Run by launchd (see com.andy.claude-remote-control.plist) with KeepAlive, so it is
# restarted automatically after a crash, a reboot, or a wake from sleep.
set -u
REPO="${CLAUDE_RC_DIR:-/Users/andylobster/AgentHub}"
NAME="${CLAUDE_RC_NAME:-Andys-Mac-mini AgentHub}"
LOG="$HOME/Library/Logs/claude-remote-control.log"
mkdir -p "$(dirname "$LOG")"
cd "$REPO" || { echo "$(date -Iseconds) cannot cd to $REPO" >> "$LOG"; exit 1; }

log() { echo "$(date -Iseconds) $*" >> "$LOG"; }
log "starting remote-control server (claude $(claude --version 2>/dev/null | head -1))"

# Fail fast and loudly if the login has expired. This is what killed the 12 Aug batch
# (cloud error `worker_auth_expired`: "This session's computer needs to sign in again").
if claude auth --help 2>&1 | grep -q 'status'; then
  if ! claude auth status >/dev/null 2>&1; then
    log "AUTH EXPIRED: run 'claude auth login' on the mini, then launchd will retry"
    osascript -e 'display notification "Claude Code login expired on the Mac mini. Run: claude auth login" with title "Claude Remote Control"' >/dev/null 2>&1
    exit 75
  fi
fi

# caffeinate -i: no idle sleep while the server runs; -s: same while on AC power.
# `claude remote-control` with no session flag brings back every session this server
# was serving before it stopped (see code.claude.com/docs/en/remote-control).
exec caffeinate -i -s claude remote-control --name "$NAME"
