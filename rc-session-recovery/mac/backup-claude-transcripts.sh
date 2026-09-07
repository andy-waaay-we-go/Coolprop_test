#!/bin/bash
# Nightly copy of Claude Code transcripts (~/.claude/projects) so that transcript
# cleanup (cleanupPeriodDays), a CLI reinstall, or a lost bridge environment can never
# take the conversation history with it. Sessions can be resumed from the copy by
# putting the .jsonl back under ~/.claude/projects/<slug>/ and running `claude --resume <id>`.
set -u
SRC="$HOME/.claude/projects"
# Default is local. Point DEST at a Drive-synced folder (e.g. $HOME/EolasSync/claude-transcripts)
# only if you are happy for transcript contents (which can include client detail) to sync there.
DEST="${CLAUDE_TRANSCRIPT_BACKUP_DIR:-$HOME/Backups/claude-transcripts}"
LOG="$HOME/Library/Logs/claude-transcript-backup.log"
mkdir -p "$DEST/projects" "$(dirname "$LOG")"
if rsync -a --exclude '*.tmp' "$SRC/" "$DEST/projects/"; then
  cp "$HOME/.claude/settings.json" "$DEST/settings.json.bak" 2>/dev/null
  echo "$(date -Iseconds) backup ok: $(du -sh "$DEST" | cut -f1) in $DEST" >> "$LOG"
else
  echo "$(date -Iseconds) BACKUP FAILED (rsync exit $?)" >> "$LOG"
  exit 1
fi
