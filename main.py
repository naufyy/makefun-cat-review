"""One-line cat review entry for make.fun.

Writes the winning one-star review to /output/entry.txt.
"""

"""One-line cat review entry for make.fun.

Writes the winning one-star review to /output/entry.txt.
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = "One star. The food bowl was empty at 6 a.m. I stared at him until he understood. He did not. He took a photo instead."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
