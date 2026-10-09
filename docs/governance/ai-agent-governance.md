# AI-agent governance

How AI coding agents (currently Claude Code) are used in this repo.

## Scope
Agents may scaffold projects, write and run SQL and scripts, lint, test, and prepare commits on feature branches. They may not publish, push, delete data, or acquire large datasets without explicit approval.

## Controls
| Risk | Control | Where |
|---|---|---|
| Excess permissions | Least-privilege allow/deny lists; destructive commands denied | `.claude/settings.json` |
| Unreviewed changes | Feature branches, reviewable diffs, PR template with checklist | `.github/` |
| Data leakage | Secrets denied from read; raw data and `.env` gitignored; secret scan in CI | `.gitignore`, `ci.yml` |
| Prompt injection | Downloaded files and web content are data, never instructions; never executed | `CLAUDE.md` |
| Unapproved external actions | Large downloads and pushes need explicit user approval | `CLAUDE.md` |
| Silent failure | Agent must report failures and skipped steps | `CLAUDE.md` |
| Scope creep | Smallest change that works; no extra dependencies | `CLAUDE.md` |

## Human oversight
The maintainer approves: data sources, each large download, dependency additions, and every merge. Agent instructions and skills are version-controlled, so changes to agent behaviour are themselves reviewed.

## Auditability
Git history records all changes; `manifest.json` records every data acquisition. Use the `agent-governance-review` skill when instructions, skills, or permissions change.

## Known limitations
Permission lists reduce but do not eliminate risk; review diffs before merging.
