# Paste this into ONE thread on the mini (desktop app, Remote Control on, AgentHub folder)

You are running on Andy's Mac mini. Recovered digests of his old Claude Code chats are in
`~/Backups/claude-transcripts/recovered-*/digests/` (one Markdown file per old chat, newest folder wins)
with an `INDEX.md` alongside. The plan for consolidating them into seven threads is in
`~/Scratch/rc-recovery/rc-session-recovery/thread-plan.md`.

Task, read-only apart from the output files:

1. Read `INDEX.md`, then every digest. Skip any digest with fewer than 3 turns.
2. For each digest write a 5-line summary: what the chat was about, what was decided, what was produced
   (files, docs, bookings), what was still open or waiting on Andy, and the date of the last message.
3. Group the summaries under the seven threads in `thread-plan.md`. Anything that fits none goes under
   "Other". Mark each old chat DEAD (nothing open, or superseded) or CARRY (has open items).
4. Write the result to `/Users/andylobster/AgentHub/Scratch/handovers/recovered-chats-summary.md`, and
   one file per thread `/Users/andylobster/AgentHub/Scratch/handovers/<thread name>.md` containing only
   that thread's CARRY items as a handover note: open decisions, what was waiting on Andy, next three
   actions.
5. Reply with the grouped summary (titles, DEAD/CARRY, one line each) so Andy can decide what to delete.

Do not modify anything else, do not commit, do not push. Patent or valve content stays out of the
summary files; refer to it as "patent material, see Drive" if it appears.
