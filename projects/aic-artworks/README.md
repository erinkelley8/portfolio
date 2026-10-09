# Art Institute of Chicago: artworks

Profiling, quality checks, and exploratory analysis of the Art Institute of Chicago artworks metadata, from the official bulk data dump.

## Status
Snapshot taken 2026-10-09; see `manifest.json` and `reports/profile.md`.

## Run
```
uv run python projects/aic-artworks/scripts/download.py
uv run python tools/run_sql.py aic-artworks
```

## Contents
| Path | Purpose |
|---|---|
| `DATA_CARD.md` | Source, scope, limits, privacy check |
| `LICENSE_NOTES.md` | Licence and attribution rules |
| `scripts/download.py` | One-time snapshot download; streams artworks into one JSONL file; writes manifest |
| `sql/` | Numbered DuckDB SQL: load, profile, quality checks, clean, analysis |
| `reports/profile.md` | Findings for the current snapshot |

Data lives in `data/raw/` and `data/processed/` and is never committed.
