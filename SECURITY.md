# Security policy

## Reporting
Report suspected vulnerabilities or accidentally committed secrets privately via GitHub's "Report a vulnerability" (Security tab) rather than a public issue.

## Practices
- No secrets in the repo; `.env` files are gitignored and a secret scan runs in CI.
- Third-party data and images are never committed; CI fails if data paths are tracked.
- Downloads use HTTPS only, are checksummed, and are never executed.
- Agent permissions are least-privilege (`.claude/settings.json`); see `docs/governance/ai-agent-governance.md`.
- Dependencies are updated through Dependabot.
