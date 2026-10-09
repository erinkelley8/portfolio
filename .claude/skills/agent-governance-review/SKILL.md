---
name: agent-governance-review
description: Review an AI-agent workflow or configuration for scope, permissions, data access, logging, and human oversight. Use when adding or changing agent instructions, skills, or automation.
---

# AI-agent governance review

Assess against `docs/governance/ai-agent-governance.md`. For each item give pass / needs-attention with evidence.

- **Purpose and scope**: what the agent may do is written down and narrow.
- **Permissions**: least privilege in `.claude/settings.json`; destructive and network commands denied or gated.
- **Data access**: no secrets; sensitive or third-party data handled per project rules.
- **Human oversight**: irreversible or outward-facing actions (push, publish, large downloads) require explicit approval.
- **Auditability**: changes go through git with reviewable diffs; downloads leave a manifest.
- **Failure handling**: agent must report failures and skipped steps faithfully.
- **Prompt-injection exposure**: untrusted content (downloaded files, web pages) is treated as data, never instructions.

End with prioritised recommendations.
