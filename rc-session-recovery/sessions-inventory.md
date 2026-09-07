# Remote Control session inventory (account-wide, pulled 2026-09-07 18:26 UTC)

Source: Claude Code Remote API `list_sessions` (101 sessions). Cloud records still exist for every session; what is gone is the *bridge environment* each one was bound to. Local transcripts, if not cleaned up, live on the Mac mini under `~/.claude/projects/<cwd-slug>/<session-id>.jsonl`.

Legend: env = environment the session is bound to; "missing (deleted)" means the API no longer returns an environment id for it.

## A. Sessions that still had live work (not archived)

| Created (UTC) | Title | Session ID | Status | Origin | Env | Last error | Last summary / needs action |
|---|---|---|---|---|---|---|---|
| 2026-09-07 15:12 | Grangemouth sports stadium | `session_01JsZ9WSPSTjLM6fXwNBKgxu` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:12 | Mary's website | `session_01XCJs5mbvSGXevV2TftVkLd` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:12 | Social calendar and holidays scheduling | `session_01BptKk3dPw4K84g7SzSkRvT` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:12 | Monthly finances management | `session_01BBMbr2q6ZBCiBhVcpN4gwY` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:11 | Calcut - Sourcethermal | `session_01FCN58QHJWartNmL7S2uppH` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:11 | Claude code club Jarvis | `session_01C58WvPm4pZuAJyB7r9QkfR` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:11 | Business Agent, SME and Consultants | `session_015fpSD3qWnVtus9LSgTJ28E` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:11 | Dashboard | `session_0117MkxDWdfpRdmahURLhFkt` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:10 | Japan Trip Planning | `session_011bu9XYVox8482KRGwUx3R7` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-07 15:10 | Core Mission, templates | `session_01SzVrMRH6NEGubKYdReWPGJ` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-06 18:33 | Japan Trip 2026 | `session_01X5VBvwNRydZNkZ6Z8okcPd` | IDLE | android | env_01Bi37NvHd7PnyQQ21aLvpJQ (deleted) | environment_deleted 2026-09-07 18:19 | found 4 accommodation bookings (Tokyo, Hakone, Osaka, Kyoto) verified in Drive + memory note  |
| 2026-09-02 21:39 | Claude Profit Room | `session_01TWANvTG4r7dz9VCSqmeXzz` | IDLE | android | env_01Bi37NvHd7PnyQQ21aLvpJQ (deleted) |   | naming rule added to 3 docs; 9 questions need answers → answer questions 1–9 (ThermalHub form, folder renames, pick pricing, CARES note, solicitor, REFCOM, sign-ups, testimonials, interview window) |
| 2026-09-02 20:05 | Trading | `session_01SKuasyBDjgUwjtBeF26e8k` | RUNNING | claude_code_cli | missing (deleted) |   |   |
| 2026-09-02 20:05 | Sourcethermal team day rate | `session_01DGiT5B24nANoijjwRJ3cFt` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-02 20:04 | Church Heat Pump Cascade | `session_011YFcwipSeZ18DNvv83BX9L` | IDLE | claude_code_cli | missing (deleted) |   |   |
| 2026-09-02 19:58 | What is an effective way for you to notify me in g... | `session_01LmEgurDVAJvBRg1ATotgkH` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | email notification system proposed; awaiting go-ahead to draft proposal → say so and I will write a proposal |
| 2026-09-02 18:50 | update claude | `session_01BxYei69fCjfoGXtPTAxV5A` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | CLI updated to 2.1.258 (Fable 5.1 ready); desktop app on 2.1.221 (needs separate update)  |
| 2026-09-01 18:15 | Business Plan for People and Organisational Manage... | `session_014a319DLdhGESXv1tUYqhi3` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | veto framework: green/red/amber lists with notification-based accounting  |
| 2026-09-01 14:19 | Draw.io desktop installation | `session_01B74jmcEvMWV9Nhwz5yBP14` | IDLE | desktop_app | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | draw.io v31.3.2 installed via Homebrew on Mac mini  |
| 2026-09-01 07:46 | please create a mini story that involve human and ... | `session_017wGKYTXHDwkLTaLgBcerXg` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | environment_deleted 2026-09-06 18:32 | story debate unresolved; awaiting go-ahead on reconciliation → pick one: (1) raise MAX_TURNS to 8, (2) run with GROK_WEB=1, or (3) close with Claude reconciliation. Also: cut second draft or hold? |
| 2026-08-31 21:27 | I want to build my soul.md file — the document tha... | `session_01EZApfBZuBaM6BHM42fNxwX` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | environment_deleted 2026-09-07 18:20 | Sourcethermal origin story drafted at repo root  |
| 2026-08-31 21:14 | create an artifact.  I want to see if it's availab... | `session_014nWLT1RtefQd1HqbBxajyc` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | environment_deleted 2026-09-06 18:32 | no publish-to-artifacts API available; offering alt paths → choose: test artifacts in Claude app, or start server for phone view? |
| 2026-08-30 21:35 | Containerised virtual power plants | `session_015XEyt9sAjcf6UrgYQSrK7v` | IDLE | desktop_app | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | analyzed 3 pipeline routes for SourceThermal; awaiting steer before Grok turn 5 → steer now or run Grok's turn 5 attack on route C? |
| 2026-08-30 11:32 | Ask grok can I get Grok bot on my mac mini | `session_01PNjfdsCDY1XJv4Ga6EsKpR` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | Worth writing up as a proposal so the decision and its conditions are on the record? → Worth writing up as a proposal so the decision and its conditions are on the record? |
| 2026-08-30 09:37 | Tell me about hand foot and mouth.    As a parent ... | `session_01ADjtz3EKAbRfmmf4HQPR5M` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | hand-foot-mouth debate completed; key: pre-medicate before drinks  |
| 2026-08-30 09:19 | Health | `session_012DJiy66YfjZxE8fRMHb2wc` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | health summary needs 6 data points to complete → provide: past test results, diet duration, weight change, symptom onset, all meds/supplements, red flags (bleeding/swallowing/family Hx) |
| 2026-08-27 21:16 | # Handover: BES refrigerant fittings order list  #... | `session_01Ad4rRQj4GQLSf1gHR7DeVJ` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | BES catalogue complete: 14,964 products in MERGED.csv  |
| 2026-08-27 17:42 | Hi, Claude. When will it be possible to hive a liv... | `session_01LaJLyGhUaPAaiv5L3TD7cx` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | voice/live conversation: no roadmap info; options explained  |
| 2026-08-26 19:59 | Finding a Junior to mentor | `session_01H4zsjMYDDEP7VpsBKmD3vb` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | mentoring paths mapped: IOR guest → placement → MA; 3 action items  |
| 2026-08-26 18:31 | Claude Remote Organise | `session_01JgcgLxYgPDgSMfmRooVPaT` | IDLE | android | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 | zombie runs blocking brief delivery; awaiting go-ahead to diagnose → start with step 1? (diagnose and clear zombie runs, test-fire brief to Drive) |
| 2026-07-03 10:54 | Dispatch background conversation | `session_01TjqfGMaKBMmnLdqseRJrWV` | IDLE | desktop_app | env_01Qc3mXayKkgd9tepFjQ9A6g (deleted) |   |   |

## B. Archived sessions (older batches of the same named RC sessions)

| Created (UTC) | Title | Session ID | Origin | Tags | Env | Last error |
|---|---|---|---|---|---|---|
| 2026-09-07 15:00 | Eolas daily am | `session_01HZATwHPx8iJBU6ZB9hWdwg` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-09-07 15:00 | Eolas daily pm | `session_01Rqr5Fcnoxumme8SVLvry2p` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-09-02 21:35 | hi | `session_01GseXSMpJVShEaeG7pQMR4G` | android |  | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) |   |
| 2026-09-02 21:33 | Rv command clarification | `session_016zroPDZCyuBFEC7GvYy4Wd` | claude_code_cli | remote-control-auto | missing (deleted) |   |
| 2026-09-02 20:24 | Claude Profit Room | `session_01N3Eyu8fgsHgzZn7dm3JXYt` | android |  | env_01Ks7Uuu6okrbgUybTTBbPV9 (deleted) | computer_unreachable 2026-09-02 21:24 |
| 2026-09-02 20:07 | Sourcethermal Website | `session_01MN4aaSawrL1dqj8iBYoxKW` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-09-02 20:07 | Sourcethermal promotional materials organization | `session_01W5GVNq5nRKfYasgUVm1dof` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-09-02 20:03 | Core Mission, templates | `session_01BHHrhUQAJmhguxPG2eZ1Rd` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-09-02 20:02 | Eolas daily pm | `session_011raugupAq24K7dSBq4MFNC` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-09-02 20:02 | Eolas daily am | `session_01SkgcxcUCRNk8B4Bzb2Bm4f` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 21:55 | Sourcethermal team day rate | `session_01FXd46Qtb7ncZRSqRaNPUo7` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:43 | Core Mission, templates | `session_01KHWdsjTDMqxb9NxRfh2epK` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:40 | Sourcethermal promotional materials organization | `session_01AiWC73tLLEuphGM2mAQTqY` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:39 | Daily Work Notes | `session_01J4hGbVNnrAu1Nkn3Go2GB4` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:39 | Daily Work Notes | `session_01WDvehwW4YYjowA4NHPaTGr` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:38 | Sourcethermal Website | `session_012LDtxf8ECknY7WYBBZ68Ev` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:37 | Mary's website | `session_01VdYc5u8jN6anTW4cNbw5AJ` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:36 | Trading | `session_01SHDW5xLKwfrWcKg86r9wNX` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:35 | Claude code club Jarvis | `session_01SJCN2PPcdh7dFUmQPnnpdf` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:25 | Social calendar and holidays scheduling | `session_01S13FQBGRHizRxTEPhkQSyF` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:25 | Grangemouth sports stadium | `session_01NeZ5muFHST4oag4sQy4VnR` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-21 19:24 | Church Heat Pump Cascade | `session_01GdABTpEUTLky6LMR9gbZqw` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-20 19:57 | Calcut - Sourcethermal | `session_0178tVaniZEF2oE1NrQ1GB63` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-20 13:30 | Monthly finances management | `session_01RSsE1rR4EDC7YRHFBEe9eY` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-15 21:25 | Japan Trip Planning | `session_01HfQRG4dPGYNbZfiKKNTB11` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-15 21:24 | Dashboard | `session_01DcYJCNHuw6gL7HurkrWfjQ` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-15 13:51 | Business Agent, SME and Consultants | `session_012yfgyfXwWB6PzQD1CpDvDJ` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-15 07:56 | Placeholder 2 | `session_01ML3Lzj6bzY3dCGDvZaqpnH` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-15 07:55 | Placeholder 1 | `session_01LYrcYL8zjbftk7pcLPjfv7` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-12 15:46 | Church Heat Pump Cascade | `session_01GpxCYVZXkrxMx19rEWecfP` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-12 15:46 | Church Heat Pump Cascade | `session_01VBXEDu8uZyHYf6D7xZrDPM` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-07 11:32 | Business Agent, SME and Consultants | `session_015WJzWS5i4HZJo93ByBZFoP` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-06 20:10 | Claude code club Jarvis | `session_016dq11NoTzqjXK8ZtS8sSoj` | claude_code_cli | remote-control-sdk | missing (deleted) | worker_auth_expired 2026-08-12 17:21 |
| 2026-08-06 13:49 | Social calendar and holidays scheduling | `session_01FmWQbi8xNyVVy5ePFTXFFA` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-06 13:48 | Trading | `session_01RefkLD6pRssKtVZGYndNZM` | claude_code_cli | remote-control-sdk | missing (deleted) | worker_auth_expired 2026-08-12 18:49 |
| 2026-08-06 13:47 | Mary's website | `session_01PPD2jDLrMTzH4KWW3cLeaA` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-06 13:46 | Monthly finances management | `session_01C5tz83h2cAZE9vssqx2kuU` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-06 13:45 | Grangemouth sports stadium | `session_015qVmo4yJM7oQc5Zaw5jz3h` | claude_code_cli | remote-control-sdk | missing (deleted) | worker_auth_expired 2026-08-12 18:46 |
| 2026-08-06 13:45 | Church Heat Pump Cascade | `session_01D421YxaprN7uqQ3MxUu7JE` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-08-05 21:52 | Church Heat Pump Cascade | `session_018jThrk9Crw24UzD43h41eV` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-30 18:41 | Church Heat Pump Cascade | `session_01NEPdx5uTA73B9U5FWsphdb` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-28 13:42 | Andy's file sorting | `session_019JXVHnFox6fmjMVUw6NcBG` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-27 11:31 | Daily Work Notes | `session_01VZRcgAenA3keahx5wTMRcs` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-27 11:30 | Mary's website | `session_01VLbsK3AG7m8F5eBgUfRUfR` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-27 11:29 | Monthly finances management | `session_0149cyFE5PJFq6CdRR3oa6ny` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-27 11:29 | Trading | `session_01FX4h5VwUuLA9SVSwixkPaW` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-27 11:29 | Social calendar and holidays scheduling | `session_01GjGJH4CBL3JJhRe9ph6JCw` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-27 11:28 | Website | `session_01QsUnHhyzNYs1pBdH2A6VT2` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-27 11:28 | Sourcethermal promotional materials organization | `session_01HYw3gj2Ci9kCyXkDSePHS8` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-22 17:36 | Mary's website | `session_01VPgYFCrnGdAX5qCRmxbnf6` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-22 09:18 | Website | `session_013drQmXn2aAHXuTqgLv1FCV` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-22 09:16 | Monthly finances management | `session_01UZyGTk2eQgAqhRRi3pyMEV` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-22 09:16 | Social calendar and holidays scheduling | `session_01QjQ4uwQf6eFprmniJjZrxK` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-22 09:15 | Trading | `session_01WdizESgqFNuAcWZvn7G2Pk` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-22 09:15 | Sourcethermal promotional materials organization | `session_01XpkKhs7VLHvPvQb4w98cxi` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-22 09:15 | Daily Work Notes | `session_016T65x31jCZinjfANKeA2gG` | claude_code_cli | remote-control-sdk | missing (deleted) |   |
| 2026-07-17 18:44 | Trading | `session_01WYzjijAordjAsa2PAZmj1u` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-17 10:18 | Social calendar and holidays scheduling | `session_018ZrAZbHAR5p59jsCExgFcP` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-17 10:18 | Monthly finances management | `session_01Mu3HQSPq4rVKeCLfEdmVkS` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-17 10:17 | Sourcethermal promotional materials organization | `session_014wh6H1FaqzLw4B4GSQXDjP` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-17 10:17 | Daily Work Notes | `session_01GARbLRNQmukhcPE6CXfdUL` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-16 21:32 | Monthly finances management | `session_01VsxBpUTkXLrbb391gssQes` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-16 21:29 | Social calendar and holidays scheduling | `session_01LpCJPDQoY6oFpPg9gEohxw` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-16 21:28 | Sourcethermal promotional materials organization | `session_01WHMZ1rLW3wqXuBzRzEzzDA` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-16 19:45 | Daily Work Notes | `session_01MdYzd2QGn733mDB8jR5JNZ` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-15 12:22 | Andy's file sorting | `session_01RaRT3wxSBDFG9CPCHhQcH4` |  | remote-control-sdk | missing (deleted) |   |
| 2026-07-13 22:17 | Andy's file sorting | `session_01N6Do9enpEQFU2QKKRNUhrq` |  | remote-control-sdk | missing (deleted) |   |
| 2026-05-14 15:30 | Dispatch background conversation | `session_01BPRZUMfY5qbT2Szwk6hhxV` |  | cowork-dispatch-local | env_01X1dLNQtRFAqE2fkRtA3MxE (deleted) |   |
| 2026-05-10 13:27 | Dispatch background conversation | `session_01JMRCHwTpY54GfvxnZgDqjh` |  | cowork-dispatch-local | env_01PK5CUVvqLErmoVPrPA3Bjd (deleted) |   |
