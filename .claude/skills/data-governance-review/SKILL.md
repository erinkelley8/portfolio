---
name: data-governance-review
description: Review a dataset project against a governance checklist (licence, privacy, lineage, retention, security). Use before committing or publishing a project.
---

# Data governance review

Produce a pass / needs-attention result for each item, with evidence (file and line).

- **Licence**: source licence recorded in `LICENSE_NOTES.md`; attribution requirements met; image rights not assumed.
- **Provenance and lineage**: source URL, retrieval date, SHA-256 in `manifest.json`; transformations traceable through numbered SQL.
- **Privacy**: personal-data check documented in `DATA_CARD.md`; no personal data, or handling documented.
- **Minimisation and retention**: only needed fields kept; raw data stays local; retention noted.
- **Security**: no secrets or data files tracked (`git ls-files`); download over HTTPS; no executed downloads.
- **Quality**: profiling report present and dated; known issues listed.
- **Reproducibility**: a fresh clone can rebuild using the runbook.

End with a short list of required fixes.
