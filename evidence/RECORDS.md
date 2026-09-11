# Evidence, decision, and human-input records

Agent-maintained canonical provenance record. No research records exist yet. Add only material that supports continuity, auditability, or a conclusion. Use ID-only headings such as `## E001`, `## D001`, and `## H001`; put a descriptive title beneath the heading. Links then stay stable when descriptions change. From the project root use `[E001](evidence/RECORDS.md#e001)`; from `outputs/REPORT.md` use `[E001](../evidence/RECORDS.md#e001)`. Use the same link pattern for D and H records. These examples refer to a record you would create. Existing IDs must not be renamed or reused.

The formats below are templates, not findings. Adapt fields to the evidence; combine related facts instead of creating repetitive records. Remove this introductory guidance when it is no longer useful. If splitting records across topic files, keep this entry point and preserve existing links.

For mathematical work, use the [mathematical support distinctions](../AGENTS.md#mathematical-support) alongside the provenance kind.

If an [optional knowledge map](../KNOWLEDGE_MAP.md) is useful, keep evidence, source details, and consequential relationship interpretations here; let the map reference stable IDs. Do not create a duplicate record for each node or edge.

## Evidence record format

```markdown
## E001

**Short finding**

- Recorded: YYYY-MM-DD, with time and timezone when useful.
- Kind: observation | primary result | secondary statement | reproduced calculation | inference | assumption | hypothesis | speculation
- Finding: the claim or result, with scope and units when relevant.
- Provenance: author/organization, title, date/version, URL/DOI or local path; retrieval date for online sources; page/section/table/figure/data locator. For an inference, assumption, or hypothesis, identify its author and evidence or rationale instead of inventing an external source.
- Access / method: what was actually read, observed, or executed; any access limitation. For computation, link inputs, method, run instructions, and outputs.
- Mathematical support (if relevant): verification type and scope; link counterexample searches, certificates, or proofs and identify conjecture status or unresolved proof obligations.
- Bearing on the objective: what this supports or challenges; separate the source result from the agent's interpretation.
- Limitations / counterevidence: relevant uncertainty, dependencies on other evidence, contrary records, or untested assumptions.
```

Reuse provenance by linking an existing record for the same source and specifying the new locator. Do not count reuse of that source as corroboration. For a source-reported number, say whether it was independently checked. Add a correction or supersession link if a recorded claim changes; retain enough of the earlier record to explain the change.

## Decision record format

```markdown
## D001

**Short decision**

- Date: YYYY-MM-DD, with time and timezone when useful.
- Decision / change: the agent's adopted interpretation, rejected hypothesis, consequential assumption, or scope/direction decision; identify the prior and revised position when changing course.
- Basis: concise justification, linking originating H records, relevant E records or artifacts, and any consequential contrary evidence as applicable. Separate human direction from evidential support.
- Consequence / reconsider when: what changes next, and which new evidence or input could reverse this decision.
```

## Human-input record format

```markdown
## H001

**Short description of consequential input**

- Timestamp: YYYY-MM-DD HH:MM timezone; identify as input time or capture time, noting uncertainty when the input time is unknown.
- Type: scope/objective change | assumption change | direction change | constraint | priority | clarification | hypothesis | observation | authorization | stopping decision
- Human input: relevant triggering prompt excerpt for a consequential change and the human's stated reason (or reason not supplied); otherwise a short exact quote when wording matters or labeled paraphrase. Identify origin (conversation instruction, brief section, or supplied material) and a locator if available.
- Agent interpretation: operational meaning, separate from the human's statement; note consequential ambiguity and what remains unverified.
- Effect on research state: prior position → new position in scope, assumptions, priorities, direction, permitted actions, or stopping status; link earlier H/D records and affected claims, evidence, or queued work so the change and its consequences can be reconstructed.
```

Capture consequential input promptly, before dependent action or handoff, and link it from the applicable `STATE.md` fields. Group related points; do not create a D or E record merely to repeat H. Preserve authorization scope, limits, conditions, expiry, or revocation when stated. For changed or withdrawn input, add a new H record, link both records, and update state; mark only the affected points in the earlier record superseded or withdrawn without erasing its original content. Unaffected instructions remain applicable. Human-reported observations and hypotheses are not independently verified evidence: link any subsequent check in E back to H.

Do not store routine conversation, exhaustive transcripts, private reasoning, or unrelated personal detail. Record a failed avenue when it matters to the interpretation, prevents duplicated work, or supports the stopping rationale.
