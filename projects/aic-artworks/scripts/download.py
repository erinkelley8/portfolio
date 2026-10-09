"""Download a one-time snapshot of the Art Institute of Chicago data dump and extract artworks only.

Run by hand:  uv run python projects/aic-artworks/scripts/download.py
The archive is ~115 MB compressed (~2.5 GB extracted), so only the artworks folder is extracted.
Images are not part of the dump. Archive members are validated; nothing is executed.
"""

from __future__ import annotations

import argparse
import sys
import tarfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT.parents[1] / "tools"))
from portfolio_common import download, write_manifest  # noqa: E402

URL = "https://artic-api-data.s3.amazonaws.com/artic-api-data.tar.bz2"
RAW = PROJECT / "data" / "raw"
ARCHIVE = RAW / "artic-api-data.tar.bz2"
MANIFEST = PROJECT / "manifest.json"
# Directory name inside the archive; confirmed from the archive listing on first run.
ARTWORKS_MARKER = "/artworks/"


def extract_artworks(archive: Path, dest: Path) -> int:
    """Extract only artwork JSON files, rejecting anything outside `dest`."""
    dest = dest.resolve()
    count = 0
    with tarfile.open(archive, "r:bz2") as tar:
        for member in tar:
            if not member.isfile() or ARTWORKS_MARKER not in "/" + member.name:
                continue
            if not member.name.endswith(".json"):
                continue
            target = (dest / Path(member.name).name).resolve()
            if dest not in target.parents:
                raise ValueError(f"Unsafe path in archive: {member.name}")
            src = tar.extractfile(member)
            if src is None:
                continue
            target.write_bytes(src.read())
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="overwrite an existing snapshot")
    args = parser.parse_args()

    out_dir = RAW / "artworks"
    if out_dir.exists() and any(out_dir.iterdir()) and not args.force:
        print(f"{out_dir} already has files; use --force to replace them.")
        return 1

    print(f"Downloading {URL}")
    sha256, size = download(URL, ARCHIVE, user_agent="portfolio-data-analysis (personal portfolio)")
    out_dir.mkdir(parents=True, exist_ok=True)
    count = extract_artworks(ARCHIVE, out_dir)
    if count == 0:
        print("No artwork files found in archive; check ARTWORKS_MARKER against the archive layout.")
        return 2

    write_manifest(
        MANIFEST,
        source_url=URL,
        file=ARCHIVE,
        sha256=sha256,
        size_bytes=size,
        notes=f"AIC api-data dump; {count} artwork JSON files extracted. Metadata CC0; description CC BY 4.0; images not included.",
    )
    print(f"Extracted {count:,} artwork files, archive sha256={sha256}\nManifest: {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
