# Lost Remote Control sessions: what happened, how to get them back, how to stop it recurring

Pulled from the Claude Code Remote API on 2026-09-07 18:26 UTC (account-wide, 101 sessions).
Companion files:

- `sessions-inventory.md` / `sessions-inventory.json`: every session on the account with its ID, title, status, environment, last error, and the last-turn summary the cloud kept.
- `mac/`: launchd jobs and scripts to install on the Mac mini (see "Prevention").

## 1. Nothing was actually deleted on the cloud side

All 101 session records still exist, including the titles and the "what was I waiting on" summaries.
What disappeared is the **bridge environment** each Remote Control (RC) session was bound to. The
mini registers a bridge environment when the RC server starts; when that environment goes away,
the app shows the session as "environment deleted" even though the record and transcript survive.

Only two environments exist on the account right now:

| Environment | Kind | Created |
|---|---|---|
| `Andys-Mac-mini:AgentHub:fdc8` (`env_01LEfS6gnVHTpzyFhZsxeYBw`) | bridge (Mac mini) | 2026-09-07 18:19:19Z |
| `Default` (`env_01AycHMp6ZEDLRN7Jf1jtLpB`) | anthropic_cloud | 2026-07-03 |

Every earlier bridge environment (`env_01Ks7Uuu6okrbgUybTTBbPV9`, `env_01Bi37NvHd7PnyQQ21aLvpJQ`, and the
ones the 77 `remote-control-sdk` sessions were bound to) is gone.

## 2. The four events, in order (evidence from the sessions' recorded errors)

| When (UTC) | Error stamped on sessions | Sessions hit | What it means |
|---|---|---|---|
| 2026-08-12 17:21 to 18:49 | `worker_auth_expired` (recoverable: false) | 6 Aug batch of named RC sessions (Trading, Grangemouth, Jarvis, ...) | The mini's Claude login expired. "This session's computer needs to sign in again." A fresh batch was minted on 15 Aug instead. |
| 2026-09-02 21:24 | `computer_unreachable` (recoverable: true) | 13 phone/desktop sessions on `env_01Ks7Uuu...` (Claude Remote Organise, Health, BES fittings, Containerised VPP, ...) | The mini went offline or the RC process died. These were recoverable at that point. |
| 2026-09-06 18:32 | `environment_deleted` | mini story, artifact test | The old bridge environment was removed when a new RC server registered. |
| 2026-09-07 18:19:47 | `environment_deleted` | Japan Trip 2026, soul.md | Same again: stamped 28 seconds after the new bridge `Andys-Mac-mini:AgentHub:fdc8` was created at 18:19:19Z. |

Pattern behind it: **every restart of the RC server on the mini registers a new bridge environment
and the previous one disappears, orphaning whatever was bound to it.** The 77 sessions tagged
`remote-control-sdk` show the same thing from the other side: the same fixed set of titles was
re-created as brand-new sessions on 16/17 Jul, 22 Jul, 27 Jul, 6 Aug, 15 Aug, 21 Aug, 2 Sep and
7 Sep 15:00-15:12, and the previous batch was archived each time. Whatever launches those sessions
is minting new ones after a restart rather than resuming the old ones. Three sessions from the
2 Sep batch (Trading, Sourcethermal team day rate, Church Heat Pump Cascade) did get re-attached on
7 Sep 15:10, so resume works when it is attempted.

The AgentHub checkout on the mini also reports `is_dirty: true` with 5 unpushed commits on `main`
(local HEAD `23e71d1`, GitHub `main` still at `32aaf7e` from 9 Aug). That is unrelated to the
session loss but it is work sitting on one machine.

## 3. Getting the details back

The conversation content lives in two places:

1. **On the mini**: `~/.claude/projects/<cwd-slug>/<session-id>.jsonl` (for AgentHub sessions the slug is
   `-Users-andylobster-AgentHub`). Claude Code deletes these after `cleanupPeriodDays` (default **30 days**),
   so anything before roughly 8 Aug may already be gone locally unless retention was raised.
2. **On Anthropic's servers**: while RC is connected the transcript is mirrored so devices stay in sync.
   Opening `https://claude.ai/code/<session id>` shows the history even when the environment is gone.

Steps on the mini (Claude Code 2.1.223 or newer resolves IDs across projects):

```bash
cd /Users/andylobster/AgentHub
claude --resume session_01X5VBvwNRydZNkZ6Z8okcPd      # Japan Trip 2026, for example
```

If that says the session is not found, locate the transcript and resume by its local ID:

```bash
grep -rl session_01X5VBvwNRydZNkZ6Z8okcPd ~/.claude/projects   # prints the .jsonl that mentions it
claude --resume <the uuid in that filename>
```

To bring back the whole set an RC server was serving, start the server with no session flag:

```bash
cd /Users/andylobster/AgentHub && claude remote-control           # resumes every session it served
claude remote-control --session-id session_01...                  # one specific session, within ~4 h of the stop
```

Once a session is open, `/export ~/AgentHub/archive/session-handovers/<date>-<title>.md` saves the
text so it never depends on a transcript file again.

### Sessions worth resuming first (they were waiting on you)

| Session | ID | Last state kept by the cloud |
|---|---|---|
| Claude Profit Room | `session_01TWANvTG4r7dz9VCSqmeXzz` | naming rule added to 3 docs; 9 questions need answers |
| Japan Trip 2026 | `session_01X5VBvwNRydZNkZ6Z8okcPd` | 4 accommodation bookings verified in Drive + memory note |
| Claude Remote Organise | `session_01JgcgLxYgPDgSMfmRooVPaT` | zombie runs blocking brief delivery; awaiting go-ahead |
| notify me in g... | `session_01LmEgurDVAJvBRg1ATotgkH` | email notification system proposed; awaiting go-ahead |
| Containerised virtual power plants | `session_015XEyt9sAjcf6UrgYQSrK7v` | 3 pipeline routes analysed; awaiting steer |
| Health | `session_012DJiy66YfjZxE8fRMHb2wc` | needs 6 data points to complete |
| mini story (human + ...) | `session_017wGKYTXHDwkLTaLgBcerXg` | debate unresolved; pick 1 of 3 options |
| soul.md | `session_01EZApfBZuBaM6BHM42fNxwX` | Sourcethermal origin story drafted at repo root |
| BES refrigerant fittings | `session_01Ad4rRQj4GQLSf1gHR7DeVJ` | catalogue complete: 14,964 products in MERGED.csv |
| Business Plan (People & Org) | `session_014a319DLdhGESXv1tUYqhi3` | veto framework drafted |
| The 10 named RC sessions from 7 Sep 15:10 | see `sessions-inventory.md` section A | idle, no summary recorded |

## 4. Prevention

Root causes to remove: (a) the RC server dies with the machine or the terminal, (b) restarts mint new
sessions instead of resuming, (c) the login can silently expire, (d) local transcripts are purged after
30 days, (e) nothing backs them up.

`mac/install.sh` (run once on the mini as `andylobster`) does the following:

- **`com.andy.claude-remote-control` launchd job**, `KeepAlive`, `RunAtLoad`: runs `mac/claude-rc-server.sh`,
  which starts a single `claude remote-control --name "Andys-Mac-mini AgentHub"` in the AgentHub folder
  under `caffeinate -i -s`, and is relaunched automatically after a crash, reboot or sleep. Starting the
  server without a session flag resumes the sessions it was serving rather than creating new ones.
- **Login check before every start**: if `claude auth status` fails the script logs `AUTH EXPIRED`, pops a
  macOS notification, and exits so launchd retries. That turns the 12 Aug failure mode into a visible prompt.
- **`cleanupPeriodDays: 365`** and **`remoteControlAtStartup: true`** in `~/.claude/settings.json`.
- **`com.andy.claude-transcript-backup` launchd job**, 03:30 daily: rsyncs `~/.claude/projects` to
  `~/Backups/claude-transcripts` (change `CLAUDE_TRANSCRIPT_BACKUP_DIR` to a Drive-synced folder if you
  want an off-machine copy; transcripts can contain client detail, so that is your call).
- Prints the one `sudo` step it does not do itself: `sudo pmset -a sleep 0 disksleep 0 autorestart 1 womp 1`
  so the mini never idle-sleeps and comes back after a power cut.

Habits that matter as much as the tooling:

- Do not restart the RC server casually, and never delete an environment in the app; each restart is a
  new environment. If you must restart, `claude remote-control` (no flags) afterwards, not a new batch.
- Whatever creates the batch of named `remote-control-sdk` sessions should resume by session ID rather than
  create. The IDs to resume are in `sessions-inventory.json`.
- End long RC sessions with `/export` into `archive/session-handovers/`, which AgentHub already has a
  convention for. The cloud keeps only a one-line summary per session.
- Push AgentHub `main` from the mini; 5 commits and uncommitted changes exist only on that machine.

## 5. Boot-up plan and upgrades

The consolidated list of threads to bring back, the old-session mapping, and the paste-in first message
for each are in `thread-plan.md`. `mac/recover-transcripts.sh` pulls the local transcripts into digests
the new threads can read.

Where the current approach can be made more effective:

- **The always-on thing should be the server, not the threads.** One `claude remote-control` process
  under launchd is what makes the mini reachable from the phone. Sessions on it are cheap to leave idle
  and resume by name, so keep seven named threads rather than twenty, and let the server resume them
  instead of any launcher that mints a fresh batch. That launcher is the direct cause of the 77
  duplicate `remote-control-sdk` sessions.
- **Scheduled work does not belong in hot threads.** Eolas daily am/pm, the AgentHub commit review
  (whose last Routine run failed on 1 Sep), and the Japan reminders are batch jobs. Run them as
  launchd jobs calling `claude -p` with `bin/daily-session.md`, or as cloud Routines. Threads are for
  conversations you come back to.
- **Memory should live in the repo, not in context.** Long threads compact and forget. AgentHub already
  has `memory/`, `archive/session-handovers/` and `logs/`. Add a `Stop` hook on the mini that appends a
  three-line handover to `Scratch/handovers/<session>.md` after each turn, and a `SessionStart` hook
  that reads it back. Then any thread can be killed and re-created without losing state.
- **Versions.** The mini reported CLI 2.1.258 to 2.1.260 across the batches and the desktop app 2.1.221;
  current is 2.1.263. `claude --resume <cloud id>` across projects needs 2.1.223 or newer, so the mini is
  fine, but keep `claude update` in the launchd wrapper's log so drift is visible.
- **Cost and limits.** The Claude Profit Room thread alone used about 6.3M cached tokens and USD 16. Ten
  hot threads all hitting the same 5-hour window is why things stall in the evening. Seven threads plus
  batch jobs on Sonnet for the routine digests is the cheaper shape.
- **Auth expiry is the one failure you cannot script away.** The wrapper now notifies you; the fix is
  still `claude auth login` on the mini. Check it after any macOS update or password change.

## 6. Unverified or outstanding

- The docs describe bridge environments but do not state that each RC server start replaces the previous
  one; that is inferred from the timestamps above, not documented behaviour.
- A read-only diagnostic session (`session_01JXtYbAns1gmQE4pNqPHPyc`, titled "RC session recovery: Mac mini
  diagnostics") was created on the live bridge to list the local transcripts and map cloud IDs to local
  files. It stayed PENDING for 15 minutes and never connected: the Remote Control bridge does not pick
  up sessions created through the API, only ones started from the app or the mini. It was archived.
  `mac/recover-transcripts.sh` does the same mapping when run on the mini.
- The scheduled Routine "AgentHub commit review" (`trig_0111BE5FEp8g1oGvBd4MCica`) recorded a FAILED run on
  2026-09-01. Separate problem, but it is another job that dies quietly.
