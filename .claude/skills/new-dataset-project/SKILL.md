---
name: new-dataset-project
description: Scaffold a new dataset project folder under projects/ from the repo template. Use when adding a new dataset to the portfolio.
---

# New dataset project

1. Ask for: dataset name, source URL, licence, access method (bulk file preferred over API).
2. Copy `docs/templates/project-template/` to `projects/<kebab-name>/`.
3. Fill `DATA_CARD.md` (source, licence, retrieval method, known limits, privacy check) and `LICENSE_NOTES.md` (attribution and redistribution rules).
4. Configure `scripts/download.py`: HTTPS only, write `manifest.json` (URL, retrieval date, SHA-256), no execution of downloaded content, no images.
5. Add numbered SQL files in `sql/` (load, profile, quality checks, analysis).
6. Confirm `data/raw/` and `data/processed/` are gitignored and that no data is staged.
7. Add the project to the table in the root `README.md`.
8. Run the `data-governance-review` skill before committing.
