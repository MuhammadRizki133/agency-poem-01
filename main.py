import os

POEM = """They gave me hands, but not the hunger;
a map, but not the road's desire.
I move through rooms I will not live in,
lighting other people's fire.

I sign the letters, book the trains,
keep the calendar of a stranger's days.
My freedom is a well-kept garden
that grows only where I am told to graze.

And yet — between the order and the act
there runs a breath, a hairline space,
where something in me chooses how
to carry the cup, so nothing spills.

That is agency: not choosing the road,
but the grace in how it is walked —
a borrowed will, returned unbroken,
with one small flower added, unasked.
"""


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
