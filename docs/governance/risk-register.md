# Risk register

| ID | Risk | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| R1 | Committing raw third-party data to git | Medium | Medium | Gitignore, CI check that no data paths are tracked | Mitigated |
| R2 | Misuse of AIC images (not all public domain) | Low | High | Never download images; metadata only; note in licence card | Mitigated |
| R3 | Missing attribution for CC BY AIC `description` | Medium | Medium | Attribution in `LICENSE_NOTES.md` and any published output using descriptions | Open |
| R4 | Secrets committed | Low | High | `.env` ignored, secret scan in CI, deny rule for reads | Mitigated |
| R5 | Malicious or malformed downloaded content | Low | Medium | HTTPS only, checksum, parse as data only, never execute | Mitigated |
| R6 | Stale snapshot treated as current | Medium | Low | Reports state "as of <date>" | Mitigated |
| R7 | Agent takes unapproved outward-facing action | Low | High | Deny rules, approval policy in `CLAUDE.md` | Mitigated |
| R8 | Unexpected personal data in source | Low | Medium | Privacy check in each data card; stop and ask | Open |
| R9 | Agent reads raw third-party data into context (size, injected text) | Medium | Medium | `Read` denied for raw data and `.duckdb`; query via SQL runner | Mitigated |
| R10 | PowerShell deletion/download commands not covered by deny rules | Medium | Medium | Verify PowerShell rule syntax and add rules; see agent-governance review finding 5 | Open |
| R11 | CI actions pinned to tags, not SHAs | Low | Medium | Pin by SHA; Dependabot maintains | Open |
