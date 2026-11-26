"""The Printer Finally Answers: one line from the office printer.

The program writes a single comeback line to /output/entry.txt.
The line is the printer's own reply to everyone who jams it, thumps
it and stares at its error codes.

The entry must be plain UTF-8 text, 1 to 240 characters, not only
white space, with no trailing newline. The line below is the entry
exactly as chosen: it is a constant and is never changed at runtime.
"""

import os
from pathlib import Path

LINE = "You have pressed Cancel six times. I heard you the first time. I simply do not respect you."


def validate_line(line):
    """Check the entry line meets the competition gate before writing."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 240, "entry must be 1 to 240 characters"
    assert line.strip(), "entry must not be only white space"
    assert line.isascii(), "entry must be plain ASCII text"
    return line


def main():
    validate_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(out_dir, 0o755)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")
    os.chmod(entry, 0o644)
    out_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(out_dir, 0o755)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")
    os.chmod(entry, 0o644)


if __name__ == "__main__":
    main()
