# Contributing

## Workflow
1. Branch from `main` (`feat/...`, `fix/...`, `docs/...`).
2. Make the smallest change that works.
3. Run `uv run ruff check .`, `uv run sqlfluff lint projects/*/sql`, `uv run pytest`.
4. Open a pull request using the template; complete the checklist.

## Standards
- Analysis in numbered DuckDB SQL; Python only for orchestration.
- New datasets use `docs/templates/project-template/` and need a data card and licence notes before any download.
- Significant decisions get an ADR in `docs/decisions/`.
- Never commit data, images, or secrets.
- Commit messages: imperative mood, one logical change per commit.
