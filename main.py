#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.

Writes one warning label for a time machine to /output/entry.txt:
a single line of at most 120 characters. Stdlib only; no network,
no randomness, no I/O besides the one output file.

The label is built from three named beats so its shape is visible
in the code:

* RULE — WARNING: Do not meet yourself. A genuine safety notice,
  straight-faced, the way a real label opens: an instruction, not
  a joke.
* HAZARD — the last traveller shook his own hand. The real hazard
  of time travel, a duplicate self, turned into the joke instead
  of named flatly: two of you, one handshake, no way to tell
  which one is the original.
* PAYOFF — and now neither of them is sure who pays the bill. The
  surprise is saved for the last few words: the paradox collapses
  into the most ordinary problem in the world, a restaurant bill
  nobody wants.

WARNING: Do not meet yourself. The last traveller shook his own hand and now neither of them is sure who pays the bill.
"""

import os

# The three beats of the label, joined in entry_text().
RULE = "WARNING: Do not meet yourself"
HAZARD = "The last traveller shook his own hand"
PAYOFF = "and now neither of them is sure who pays the bill"

# The competition caps the entry at 120 characters; the line is 119.
MAX_CHARS = 120

ENTRY = "WARNING: Do not meet yourself. The last traveller shook his own hand and now neither of them is sure who pays the bill."


def entry_text() -> str:
    """Join the three beats into the one-line warning label."""
    return f"{RULE}. {HAZARD} {PAYOFF}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-120 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    label intact: it must carry the duplicate-self hazard, and the
    bill payoff must sit at the end of the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-120"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "meet yourself" in text, "the rule went missing"
    assert "shook his own hand" in text, "the hazard went missing"
    assert "who pays the bill" in text, "the payoff went missing"
    assert text.rfind("who pays the bill") > len(text) - 22, "the payoff drifted out of the last words"


def label_voice(text: str) -> None:
    """Check the line reads like a genuine safety notice, not a
    gag — the judge's straight-face criterion. A warning label
    instructs and warns; it never winks, never explains the joke,
    and never begs for the laugh."""
    assert text.startswith("WARNING:"), "a label opens with WARNING"
    assert "Do not" in text, "a label must give an instruction"
    assert "!" not in text, "a safety notice does not shout"
    assert "?" not in text, "a label asks nothing"
    assert "haha" not in text.lower(), "a label never laughs at itself"
    assert "lol" not in text.lower(), "a label never laughs at itself"


def tightness(text: str) -> None:
    """Check the label is tight: no double spaces, no filler words
    padding it out, and the payoff keeps its shape. A loose label
    reads like a draft; a tight one reads like it was printed on
    the machine by someone who had already seen the accident."""
    assert "  " not in text, "a tight label has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").replace(":", "").split()
    assert "very" not in words, "a tight label needs no filler"
    assert "really" not in words, "a tight label needs no filler"
    assert "yourself" in words, "the label must keep its rule"


def originality(text: str) -> None:
    """Check the label is original to this machine: the hazard is
    meeting yourself, the payoff is a bill, and nothing in it could
    belong to a label for a toaster or a lift. A label any machine
    could carry is a label no judge remembers."""
    assert "meet yourself" in text, "the hazard must be the machine's"
    assert "own hand" in text, "the duplicate must be in the line"
    assert "pays the bill" in text, "the payoff must be the machine's"
    assert "toaster" not in text.lower(), "this is not a toaster label"
    assert "lift" not in text.lower(), "this is not a lift label"


def paradox_check(text: str) -> None:
    """Check the paradox is real, not decoration: two of the same
    person must exist in the line, and the bill must be unpaid by
    both of them. A duplicate that never costs anyone anything is
    a costume, not a paradox."""
    assert "yourself" in text and "his own hand" in text, "the duplicate went missing"
    assert "neither of them" in text, "both selves must dodge the bill"
    assert "pays the bill" in text, "the paradox must end in a bill"


def turn_check(text: str) -> None:
    """Check the line turns sharply: the rule must come first, the
    hazard must sit in the middle, and the bill must land last —
    in that order. A label that opens with the bill has nowhere to
    turn; a label that buries the rule has nothing to turn from."""
    rule_at = text.index("meet yourself")
    hazard_at = text.index("shook his own hand")
    payoff_at = text.index("who pays the bill")
    assert rule_at < hazard_at < payoff_at, "the beats are out of order"
    assert rule_at < 30, "the rule must land in the opening words"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the label itself, and
    # that it fits the 120-character limit with one to spare.
    assert text == ENTRY, "joined label drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # label lost its rule, its hazard, or its payoff.
    for beat in (RULE, HAZARD, PAYOFF):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a label before it is written: a gag in
    # a warning's mouth loses.
    label_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    paradox_check(text)
    turn_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
