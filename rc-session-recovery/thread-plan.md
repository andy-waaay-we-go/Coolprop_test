# Threads to boot back up on the Mac mini (consolidated)

Twenty-two distinct topics were running as separate threads. Seven always-on threads cover them.
Fewer hot threads means less context bloat, fewer 5-hour-window rate-limit hits, and one place per
topic to look on the phone.

| # | Thread name (use as the RC session name) | Absorbs these old threads | Old session IDs to pull digests from |
|---|---|---|---|
| 1 | **Sourcethermal: Business** | Claude Profit Room; Business Plan for People and Organisational Management; Business Agent, SME and Consultants; Sourcethermal team day rate; Sourcethermal promotional materials organization; Sourcethermal Website; Finding a Junior to mentor | `session_01TWANvTG4r7dz9VCSqmeXzz`, `session_014a319DLdhGESXv1tUYqhi3`, `session_015fpSD3qWnVtus9LSgTJ28E`, `session_01DGiT5B24nANoijjwRJ3cFt`, `session_01W5GVNq5nRKfYasgUVm1dof`, `session_01MN4aaSawrL1dqj8iBYoxKW`, `session_01H4zsjMYDDEP7VpsBKmD3vb` |
| 2 | **Sourcethermal: Projects** | Church Heat Pump Cascade; Grangemouth sports stadium; Calcut - Sourcethermal; Containerised virtual power plants; BES refrigerant fittings order list | `session_011YFcwipSeZ18DNvv83BX9L`, `session_01JsZ9WSPSTjLM6fXwNBKgxu`, `session_01FCN58QHJWartNmL7S2uppH`, `session_015XEyt9sAjcf6UrgYQSrK7v`, `session_01Ad4rRQj4GQLSf1gHR7DeVJ` |
| 3 | **Eolas: AgentHub ops** | Core Mission, templates; Dashboard; Daily Work Notes; Claude Remote Organise; notify-me-in-general; update claude; Draw.io install; Rv command clarification; artifact test; soul.md; Grok bot on the mini | `session_01SzVrMRH6NEGubKYdReWPGJ`, `session_0117MkxDWdfpRdmahURLhFkt`, `session_01J4hGbVNnrAu1Nkn3Go2GB4`, `session_01JgcgLxYgPDgSMfmRooVPaT`, `session_01LmEgurDVAJvBRg1ATotgkH`, `session_01BxYei69fCjfoGXtPTAxV5A`, `session_01B74jmcEvMWV9Nhwz5yBP14`, `session_016zroPDZCyuBFEC7GvYy4Wd`, `session_014nWLT1RtefQd1HqbBxajyc`, `session_01EZApfBZuBaM6BHM42fNxwX`, `session_01PNjfdsCDY1XJv4Ga6EsKpR` |
| 4 | **Personal admin** | Monthly finances management; Social calendar and holidays scheduling; Health; hand foot and mouth | `session_01BBMbr2q6ZBCiBhVcpN4gwY`, `session_01BptKk3dPw4K84g7SzSkRvT`, `session_012DJiy66YfjZxE8fRMHb2wc`, `session_01ADjtz3EKAbRfmmf4HQPR5M` |
| 5 | **Japan Trip 2026** (time-boxed: fold into Personal admin after 11 Nov) | Japan Trip Planning; Japan Trip 2026 | `session_011bu9XYVox8482KRGwUx3R7`, `session_01X5VBvwNRydZNkZ6Z8okcPd` |
| 6 | **Trading** | Trading | `session_01SKuasyBDjgUwjtBeF26e8k` |
| 7 | **Side projects and learning** | Mary's website; Claude code club Jarvis; mini story (human + ...) | `session_01XCJs5mbvSGXevV2TftVkLd`, `session_01C58WvPm4pZuAJyB7r9QkfR`, `session_017wGKYTXHDwkLTaLgBcerXg` |

Not a thread any more: **Eolas daily am / pm**. That is scheduled work and belongs in a launchd job or a
Routine that runs `bin/daily-session.md` headlessly, not a hot conversation that is re-created on every
restart. **Placeholder 1/2** and the two "Dispatch background conversation" sessions are dropped.

## Boot-up procedure

1. On the mini, install the keep-alive jobs once: `bash rc-session-recovery/mac/install.sh`.
2. Recover the transcripts: `bash rc-session-recovery/mac/recover-transcripts.sh`. It writes
   `~/Backups/claude-transcripts/recovered-<date>/` with the raw `.jsonl`, one Markdown digest per old
   session, and `INDEX.md` saying which were found and which were already purged.
3. On the phone, open the `Andys-Mac-mini` environment and start seven new sessions, named exactly as
   the table above. Paste this as the first message of each, with the thread number filled in:

   ```
   You are thread <N>: "<name>" on Andy's Mac mini. Read
   ~/Backups/claude-transcripts/recovered-*/digests/ for the old sessions listed under thread <N>
   in /Users/andylobster/AgentHub/Scratch/thread-plan.md (copy of this file), then write a
   handover note to AgentHub Scratch/handovers/<name>.md with: open decisions, what was waiting on
   Andy, and the next three actions. Reply with that note only. Do not start any of the work yet.
   ```

4. Confirm all seven show up under the one environment and survive a `launchctl kickstart -k` of the
   RC job (they should come back, not be re-created).
5. Only then archive the rest of the old threads in the app.

## Archive status of the old threads (done from the cloud session on 7 Sep)

Archived: Grangemouth sports stadium, Mary's website, Social calendar and holidays scheduling, Monthly
finances management, Business Agent SME and Consultants, Dashboard, Japan Trip Planning, Claude Profit
Room, and the stuck diagnostic session.

Not archived, the request was blocked or declined mid-run: Calcut - Sourcethermal, Claude code club
Jarvis, Core Mission templates, Japan Trip 2026, Trading, Sourcethermal team day rate, Church Heat Pump
Cascade. Untouched: the remaining 17 idle phone sessions (see `sessions-inventory.md` section A). All
of them are read-only history now and can be archived from the app once the digests are recovered.
