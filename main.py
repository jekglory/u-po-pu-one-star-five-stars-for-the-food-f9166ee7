"""u-po-pu-one-star-five-stars-for-the-food-f9166ee7 entry v1: one alien
tourist's one-star review of Earth that still compliments the food.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The sentence is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Premise (written in this session, never copied from the board): an alien
tourist files the classic one-star review -- the locals worship a ball of
fire in the sky, queue for everything, and stare at glowing rectangles all
day -- and then admits the fried chicken alone justified the 40-light-year
flight. Three baffled grievances, one real food compliment, one sharp turn.
"""

import os


SENTENCE = (
    "One star: the locals worship a ball of fire in the sky, queue for "
    "everything, and stare at glowing rectangles all day \u2014 but the "
    "fried chicken alone justified the 40-light-year flight."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires 1 to 200 characters (Unicode code points),
# not whitespace-only, exactly one sentence.
MAX_CHARS = 200


def main() -> None:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "sentence must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise SystemExit("sentence must not be whitespace-only")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("sentence must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the sentence.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the sentence")
    print(text)


if __name__ == "__main__":
    main()
