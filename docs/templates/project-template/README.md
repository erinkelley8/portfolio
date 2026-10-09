# Project template

Copy this folder's structure to `projects/<kebab-name>/` for a new dataset:

```
README.md           what it is, how to run, contents
DATA_CARD.md        publisher, source, download URL, licence, method, limits, privacy check
LICENSE_NOTES.md    licence terms, attribution, redistribution rules
scripts/download.py HTTPS only, checksum, manifest.json, no execution of content
sql/01_load.sql     02_profile.sql  03_quality_checks.sql  04_analysis.sql
reports/profile.md  findings for the current snapshot, with snapshot date
data/raw/           gitignored
data/processed/     gitignored
```

Use `projects/met-museum-open-access/` as the reference implementation. Complete `DATA_CARD.md` and `LICENSE_NOTES.md` before downloading anything.
