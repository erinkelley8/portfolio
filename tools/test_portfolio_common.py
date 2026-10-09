import json
from pathlib import Path

import pytest

from portfolio_common import download, write_manifest


def test_download_refuses_non_https(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        download("http://example.com/file.csv", tmp_path / "f.csv", user_agent="test")


def test_write_manifest_records_fields(tmp_path: Path) -> None:
    data_file = tmp_path / "data.csv"
    data_file.write_text("a,b\n1,2\n")
    manifest = tmp_path / "manifest.json"
    write_manifest(manifest, source_url="https://example.com/data.csv", file=data_file,
                   sha256="abc", size_bytes=8, notes="test")
    loaded = json.loads(manifest.read_text())
    assert loaded["source_url"] == "https://example.com/data.csv"
    assert loaded["sha256"] == "abc"
    assert loaded["file"] == "data.csv"
    assert "retrieved_utc" in loaded
