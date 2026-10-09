"""Download a one-time snapshot of the Met Open Access CSV (metadata only, no images).

Run by hand:  uv run python projects/met-museum-open-access/scripts/download.py
Refuses to overwrite an existing snapshot unless --force is given.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT.parents[1] / "tools"))
from portfolio_common import download, write_manifest  # noqa: E402

# The CSV is stored in Git LFS, so the plain raw URL returns a pointer file.
# media.githubusercontent.com serves the real file.
URL = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"
DEST = PROJECT / "data" / "raw" / "MetObjects.csv"
MANIFEST = PROJECT / "manifest.json"
MIN_BYTES = 100 * 1024 * 1024  # a real file is hundreds of MB; a pointer file is ~130 bytes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="overwrite an existing snapshot")
    args = parser.parse_args()

    if DEST.exists() and not args.force:
        print(f"{DEST} already exists; use --force to replace it.")
        return 1

    print(f"Downloading {URL}")
    sha256, size = download(URL, DEST, user_agent="portfolio-data-analysis (personal portfolio)")
    if size < MIN_BYTES:
        DEST.unlink()
        print(f"Downloaded file is only {size} bytes; expected the full CSV. Aborting.")
        return 2

    write_manifest(
        MANIFEST,
        source_url=URL,
        file=DEST,
        sha256=sha256,
        size_bytes=size,
        notes="Met Open Access CSV, CC0. Metadata only; images not included.",
    )
    print(f"Saved {size:,} bytes, sha256={sha256}\nManifest: {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
