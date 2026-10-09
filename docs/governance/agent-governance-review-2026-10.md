# AI-agent governance review: repo configuration

Date: 2026-10-09. Scope: `CLAUDE.md`, `.claude/settings.json`, `.claude/skills/`, CI workflow, and how data acquisition is controlled. Method: the `agent-governance-review` skill checklist, assessed against `docs/governance/ai-agent-governance.md`.

## Summary
The configuration is sound for a single-maintainer repo: scope is narrow, secrets and raw data are protected, and outward-facing actions are gated. The review found six gaps. Four were fixed in the same change; two remain open and are listed below.

## Findings
| # | Area | Finding | Severity | Status |
|---|---|---|---|---|
| 1 | Human oversight | `git push` and the data download scripts were governed by prose in `CLAUDE.md` only, with no technical gate | Medium | **Fixed**: both now require confirmation (`ask` rules) |
| 2 | Data access | Nothing stopped an agent reading raw data or `.duckdb` files into its context (hundreds of MB; third-party content could carry injected instructions) | Medium | **Fixed**: `Read` denied for `data/raw/**` and `*.duckdb` |
| 3 | Documentation accuracy | `data-profiling` skill said to run SQL from the project's `sql/` folder, but paths are repo-root relative and the runner is `tools/run_sql.py` | Low | **Fixed** |
| 4 | Disclosure | `CLAUDE.md` referred to a private notes folder; unnecessary detail in a public file | Low | **Fixed**: line removed; the folder remains gitignored |
| 5 | Permissions coverage | Deny rules cover Bash forms (`rm -rf`, `curl`, `wget`); equivalent PowerShell deletion and download commands (`Remove-Item`, `Invoke-WebRequest`) are not explicitly covered, and this repo is developed on Windows | Medium | **Open**: needs verification of PowerShell rule syntax, then rules added |
| 6 | Supply chain | CI actions are pinned to major version tags (`@v4`, `@v5`, `@v2`), not commit SHAs | Low | **Open**: pin by SHA and let Dependabot maintain |

## Checklist result
| Item | Result | Evidence |
|---|---|---|
| Purpose and scope written down and narrow | Pass | `CLAUDE.md`, `ai-agent-governance.md` |
| Least-privilege permissions | Pass, with gaps 1, 2, 5 | `.claude/settings.json` |
| Secrets not accessible | Pass | `.env*` read denied; gitignored; secret scan in CI |
| Human approval for irreversible or outward actions | Pass after fix 1 | `ask` rules |
| Auditability | Pass | git history, `manifest.json` per snapshot, PR review |
| Failure reporting | Partial | Prose rule only; not technically enforceable |
| Prompt-injection exposure | Pass after fix 2 | Downloaded text fields are untrusted data; raw files not readable by the agent |
| Supply chain | Needs attention | Gap 6 |

## Observations from this build
- The AIC load initially failed (out of memory) and the agent stopped, changed approach, and reported it, rather than hiding the failure. This is the behaviour the "report faithfully" rule is meant to produce, but it is a convention, not a control.
- A local author email was set by the agent and almost published; it was caught by a pre-push scan. A pre-commit or CI check on author addresses would make this a control rather than a habit.

## Residual risk
Permission rules reduce risk but are not a security boundary. The remaining controls are human: review of diffs before merge, and approval of each download and push.
