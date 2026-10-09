"""Shared helpers for dataset download scripts.

Kept deliberately small: stream a file over HTTPS, hash it, write a manifest.
Downloaded content is only ever treated as data, never executed.
"""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

CHUNK = 1024 * 1024  # 1 MiB


def download(url: str, dest: Path, user_agent: str) -> tuple[str, int]:
    """Stream `url` to `dest` over HTTPS. Returns (sha256 hex digest, size in bytes)."""
    if urlparse(url).scheme != "https":
        raise ValueError(f"Refusing non-HTTPS URL: {url}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    size = 0
    request = Request(url, headers={"User-Agent": user_agent})  # noqa: S310 (https enforced above)
    with urlopen(request, timeout=60) as response, dest.open("wb") as out:  # noqa: S310
        while chunk := response.read(CHUNK):
            out.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    return digest.hexdigest(), size


def write_manifest(
    path: Path, *, source_url: str, file: Path, sha256: str, size_bytes: int, notes: str
) -> None:
    """Record where the snapshot came from, when, and its checksum."""
    manifest = {
        "source_url": source_url,
        "file": file.name,
        "retrieved_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "sha256": sha256,
        "size_bytes": size_bytes,
        "notes": notes,
    }
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
