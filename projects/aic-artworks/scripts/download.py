"""Download a one-time snapshot of the Art Institute of Chicago data dump and extract artworks only.

Run by hand:  uv run python projects/aic-artworks/scripts/download.py
The archive is ~115 MB compressed (~2.5 GB extracted). Only artwork records are kept, streamed into a
single JSON Lines file (one record per line) rather than ~140k small files, which is much faster to
load and kinder to synced folders. Images are not part of the dump; nothing is executed.

If the archive is already present it is reused (and re-hashed); use --force to download it again.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tarfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT.parents[1] / "tools"))
from portfolio_common import download, write_manifest  # noqa: E402

URL = "https://artic-api-data.s3.amazonaws.com/artic-api-data.tar.bz2"
RAW = PROJECT / "data" / "raw"
ARCHIVE = RAW / "artic-api-data.tar.bz2"
OUT = RAW / "artworks.jsonl"
MANIFEST = PROJECT / "manifest.json"
# Directory name inside the archive; matches /artworks/{id}.json
ARTWORKS_MARKER = "/artworks/"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def extract_artworks(archive: Path, out_file: Path) -> int:
    """Stream artwork JSON records from the archive into one JSONL file. Returns record count."""
    count = 0
    with tarfile.open(archive, "r:bz2") as tar, out_file.open("w", encoding="utf-8") as out:
        for member in tar:
            if not member.isfile() or ARTWORKS_MARKER not in "/" + member.name:
                continue
            if not member.name.endswith(".json"):
                continue
            src = tar.extractfile(member)
            if src is None:
                continue
            record = json.loads(src.read())  # parsed as data only
            out.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="download the archive again")
    args = parser.parse_args()

    if ARCHIVE.exists() and not args.force:
        print(f"Reusing existing archive {ARCHIVE.name}")
        sha256, size = sha256_of(ARCHIVE), ARCHIVE.stat().st_size
    else:
        print(f"Downloading {URL}")
        sha256, size = download(URL, ARCHIVE, user_agent="portfolio-data-analysis (personal portfolio)")

    count = extract_artworks(ARCHIVE, OUT)
    if count == 0:
        OUT.unlink(missing_ok=True)
        print("No artwork records found in archive; check ARTWORKS_MARKER against the archive layout.")
        return 2

    write_manifest(
        MANIFEST,
        source_url=URL,
        file=ARCHIVE,
        sha256=sha256,
        size_bytes=size,
        notes=(
            f"AIC api-data dump; {count} artwork records extracted to {OUT.name}. "
            "Metadata CC0; description CC BY 4.0; images not included."
        ),
    )
    print(f"Extracted {count:,} artwork records, archive sha256={sha256}\nManifest: {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
