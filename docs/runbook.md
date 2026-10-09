# Runbook

## Prerequisites
- Git
- [uv](https://docs.astral.sh/uv/) (manages Python and dependencies)

Windows install: `winget install astral-sh.uv`

## Setup
```
git clone <this repo>
cd portfolio
uv sync
```

## Run a project
Each project follows the same steps (replace `<project>`):

```
uv run python projects/<project>/scripts/download.py   # one-time snapshot, writes manifest.json
uv run python tools/run_sql.py <project>               # runs sql/01..04 against a local DuckDB file
```
Use `--only 02` to run a single step. Output is printed; the database lives in `projects/<project>/data/processed/` (gitignored).

## Quality checks
```
uv run ruff check .
uv run sqlfluff lint projects/*/sql
uv run pytest
```

## Notes
- Raw data stays in `projects/<project>/data/raw/` and is never committed.
- Snapshots are pinned. To refresh, re-run the download script by hand.
- Do not download images.
