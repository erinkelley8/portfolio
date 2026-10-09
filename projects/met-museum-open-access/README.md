# The Met: Open Access collection

Profiling, quality checks, and exploratory analysis of the Metropolitan Museum of Art Open Access dataset (object metadata, CC0).

## Status
Snapshot taken 2026-10-09; see `manifest.json` and `reports/profile.md`.

## Run
```
uv run python projects/met-museum-open-access/scripts/download.py
uv run python tools/run_sql.py met-museum-open-access
```

## Contents
| Path | Purpose |
|---|---|
| `DATA_CARD.md` | Source, scope, limits, privacy check |
| `LICENSE_NOTES.md` | Licence and usage terms |
| `scripts/download.py` | One-time snapshot download with checksum manifest |
| `sql/` | Numbered DuckDB SQL: load, profile, quality checks, clean, analysis |
| `reports/profile.md` | Findings for the current snapshot |

Data lives in `data/raw/` and `data/processed/` and is never committed.
