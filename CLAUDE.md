# Repo instructions for Claude

This is a portfolio repo of governed, reproducible data projects. Each dataset lives in `projects/<name>/`. Repo-level rules here apply to all projects; skills live in `.claude/skills/`.

## Conventions
- **SQL-first.** Analysis lives in numbered `.sql` files (DuckDB dialect). Python is a thin wrapper for download/load/run only; keep it short and commented.
- Every project follows the template in `docs/templates/project-template/` (use the `new-dataset-project` skill).
- Decisions worth remembering go in `docs/decisions/` as an ADR.
- Use `uv` for Python (`uv run ...`); do not use global pip installs.
- Lint before committing: `uv run ruff check .` and `uv run sqlfluff lint projects/*/sql`.

## Data safety rules (non-negotiable)
1. Never commit raw or processed data, images, `.duckdb` files, or `.env` files. `data/raw/` and `data/processed/` are gitignored; keep it that way.
2. Never download images. Metadata only.
3. Only download over HTTPS from the source URLs documented in the project's `DATA_CARD.md`. Never execute downloaded content.
4. Large downloads happen only on explicit user go-ahead, via the project's `scripts/download.py`, which writes a manifest (URL, retrieval date, SHA-256).
5. No scheduled or automated data refreshes. Snapshots are pinned and refreshed by hand.
6. Respect source terms: AIC `description` is CC BY 4.0 (attribute); not all AIC images are public domain; if an API is ever used, follow the documented rate limits and send the identifying header.
7. No personal data is expected. If any appears, stop, document it in the project's data card, and ask the user.

## Agent behaviour
- Prefer the smallest change that works; do not add features, dependencies, or files beyond the request.
- Do not push, force-push, or modify git history without explicit instruction.
- Do not read or write secrets. Never print credentials.
- Report results faithfully: if a check fails or a step was skipped, say so.
- Do not reference private notes in `.local/` from any tracked file.

## Skills
- `new-dataset-project`: scaffold a project from the template
- `data-profiling`: standard profiling and quality checks in DuckDB
- `data-governance-review`: licence, privacy, lineage, retention checklist
- `agent-governance-review`: review an AI-agent workflow for scope, permissions, logging, human oversight
