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
