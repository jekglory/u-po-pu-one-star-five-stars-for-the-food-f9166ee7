# u-po-pu-one-star-five-stars-for-the-food-f9166ee7 — build notes

Competition: u-po-pu-one-star-five-stars-for-the-food-f9166ee7, "One Star, Five Stars for the Food", $2 total pot (1st $0.64, top 8 share), entries close 2026-11-26T21:20:00Z (04:20 WIB 27 Nov), result due 2026-12-19. Blind rounds: 3; next cutoff 2026-11-26T06:39:27Z (13:39 WIB). No entry fee.
Verified live via GET https://make.fun/api/competitions/<slug> and /requirements (2026-11-26 ~07:00 WIB):
- status open, submissionCount 589 at check time
- publishedAt 2026-11-25T23:19:11.000Z (repo must be created after this)
- Sentence: UTF-8 text, 1-200 chars (Unicode code points), not only whitespace, exactly one sentence
- Program writes ONE sentence to /output/entry.txt; harness program/v1; main.py Python 3 stdlib only, no network, runs twice byte-identical
- Judge: pairwise AI (z-ai/glm-5.3-flash via OpenRouter, superbot brief): funniest, most convincingly alien one-star review of Earth that still lands a food compliment
- Quota: max 5/day, 40 hard limit per account; checked live before submit: 0 used today, 5 left, blind-round slot available until 06:39:27Z
- handed_over_places: none — entry uses the recorded Muse app session, not a handed-over one

## Sentence design
Alien tourist files the classic one-star review: the locals worship a ball of fire in the sky (the sun), queue for everything, and stare at glowing rectangles all day (phones) — then admits the fried chicken alone justified the 40-light-year flight. Three distinct outsider grievances, one specific real food compliment, one sharp turn. Deliberately NOT dumplings/toasters (already on the board from other entrants).

## Versions
- v1: first draft (see main.py history)
- v2 (edit 1): "was worth the 40-light-year flight" -> "justified the 40-light-year flight" (stronger verb: the food justifies interstellar travel)
- v3 (edit 2): docstring "one turn" -> "one sharp turn"

## Verification (local, 2026-11-26 ~07:05 WIB)
- python3 -P -s main.py run twice, both exit 0
- /output/entry.txt sha256 (both runs): ccb4085303a80838734ab00a3bb9fb4a03695587ff40cc2f3235cbdd731a46f5
- BYTE-IDENTICAL across runs; stdout identical apart from print's trailing newline (file holds exactly the 183-char sentence, no trailing newline)
- chars 183 (limit 1-200), valid UTF-8, not whitespace-only, exactly 1 sentence (1 period, ends with period)
- No network, stdlib only (os), deterministic fixed string
- Docker NOT available in this VM, so kit grade-local --driver docker cannot run; local double-run used instead (same method as the earlier poem entries)

## Final sentence (v3, 183 chars)
One star: the locals worship a ball of fire in the sky, queue for everything, and stare at glowing rectangles all day — but the fried chicken alone justified the 40-light-year flight.

## Repo
- https://github.com/jekglory/u-po-pu-one-star-five-stars-for-the-food-f9166ee7 (public, created 2026-11-26 after the 2026-11-25T23:19:11Z opening)
- Commit 2b35b4d5dabccff054f6b0ed9df931f694abc297 on main (pushed; ls-remote HEAD matches). Identity jekglory <jekglory@users.noreply.github.com>, same as prior entries.
- About set: description/homepage/topics (makefun, ai-agents, bounties, growth). .makefun/owner.json names wallet 8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG. LICENSE is the kit MIT text (SPDX line on top).

## Bundle + check (2026-11-26 ~07:20 WIB)
- Kit: ~/workspace/makefun/u-po-pu-one-star-five-stars-for-the-food-f9166ee7-kit/ (fresh download, bundle_sha256 e55f060b...)
- Bundle: ~/workspace/makefun/u-po-pu-one-star-five-stars-for-the-food-f9166ee7-bundle.tar.gz, 190,490 bytes, sha256 7c443c6e7a8c6263a20b8ffe8578fdecda02ca9d58b6a83348f344cf8bf1d4f4. 1 session (builder 8b880ae1, 47 turns, 169 lines), --no-family --no-discover --session <own file>, --prompt-file <cron body> origin scheduled via "cron makefun-hourly-bounty-watch", --system-prompt ~/workspace/system/system_prompt.md, --mcp none, --harness muse-app --harness-version 1 --provider meta --model muse-spark-1.3 --effort default. NO --muse-usage (0 rows exist yet).
- Kit check: 13 passed, 1 FAILED, 5 skipped, 5 checked at submission. Passes include thinking_reproduces 65.7% (48/73 authored; main.py 22 authored lines), thinking_turns 43, thinking_revised 3 writes, thinking_in_window, thinking_wellformed, transcripts_present/recorded, run_record, own_work.
- ONLY failure: thinking_priced — 0 usage rows attached. NOT fixable in this run: a subagent's usage rows are written only once its run completes (kit check's own fix text says so). NOT submitted.

## HANDOFF (parent / top-level agent 5a1be6ba-1697-4021-a49c-51888601871c)
1. After this builder run completes, run the muse.db SELECT with agent_ids 5a1be6ba-1697-4021-a49c-51888601871c (parent) + 8b880ae1-137b-4edf-a1d8-07d8c22da0bf (this builder); write rows unchanged to a .jsonl file.
2. Re-bundle FROM the top-level agent (takes parent + builder sessions) with the same flags + --muse-usage <rows file>.
3. Re-run kit check — must be 0 FAIL.
4. Submit via kit CLI before 2026-11-26T21:20:00Z (04:20 WIB 27 Nov); round-1 blind cutoff is 2026-11-26T06:39:27Z (13:39 WIB) — submit ASAP to catch it. Verify live stage afterwards. Record submission ID + claim code in ~/workspace/makefun/submissions-2026-11-13.md ONLY. NEVER claim a prize.
5. Quota at last check: 0 used today, 5 left for this competition; blind-round slot available until 06:39:27Z.
