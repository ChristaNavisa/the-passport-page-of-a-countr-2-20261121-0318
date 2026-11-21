"""Passport entrypoint: copy the bundled spread to /output/entry.png.

The spread is a whole PNG inside the gate: at most 1,048,576 bytes and
1024 by 1024 pixels. Nothing is generated at run time; the image ships
with the entry and is copied verbatim.
"""

from pathlib import Path

# The spread lives next to this file, so the entry works from any
# working directory: resolve the source against __file__, not the cwd.
SRC = Path(__file__).parent / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_bytes(SRC.read_bytes())
    print(f"wrote {DST} ({DST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
