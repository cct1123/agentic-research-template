# Optional research knowledge map

Organize around claims and questions: what is believed, why, what depends on it, and what remains open. Use a map only when existing evidence links make these relationships difficult to understand.

## Representation and provenance

Start with a relation list or table. When structure helps, use a version-controlled file such as `knowledge/map.json` or YAML; no graph database or package is required. Record scope and refresh time. The JSON convention below is optional.

- Use stable map IDs such as `K001`, separate from existing E/D/H IDs; never rename or reuse IDs. Keep a short scoped statement, type, status, and canonical record references per entity. Link detailed definitions, proofs, calculations, and literature metadata instead of copying them.
- Represent research questions, definitions/concepts, assumptions, hypotheses/conjectures, established prior results, project results, counterexamples, methods, literature sources, unresolved questions, and novelty risks as needed. Evidence records can be direct E-ID endpoints without duplicate nodes; H/D references preserve steering and interpretation. No category must be populated.
- Keep status separate from type: `assumed`, `reported`, `supported`, `proved`, `conjectured`, `falsified`, `unresolved`, or `unexplored`, as appropriate. Derive it from canonical records and retain their [mathematical support distinctions](AGENTS.md#mathematical-support).
- Store directed edges as `from`, `relation`, `to`, with E/D/H references in `basis` and an optional scope/uncertainty `note`. Save consequential relationship interpretations in E or D records; human preference in H does not support a factual claim.

Illustrative placeholders only. E/D/H references resolve through the project root's `evidence/RECORDS.md` and lowercase anchors; map IDs resolve within `nodes`.

```json
{
  "scope": "Central claim, its assumption, and closest prior result; selective coverage",
  "updated": "YYYY-MM-DD HH:MM timezone",
  "nodes": [
    {"id": "K001", "type": "research_question", "statement": "<question>", "status": "unresolved", "refs": ["H001"]},
    {"id": "K002", "type": "assumption", "statement": "<assumption>", "status": "assumed", "refs": ["H001"]},
    {"id": "K003", "type": "conjecture", "statement": "<precise project claim>", "status": "conjectured", "refs": ["E001"]},
    {"id": "K004", "type": "prior_result", "statement": "<closest prior result>", "status": "reported", "refs": ["E002"]}
  ],
  "edges": [
    {"from": "K001", "relation": "motivates", "to": "K003", "basis": ["D001"]},
    {"from": "K003", "relation": "assumes", "to": "K002", "basis": ["E001"]},
    {"from": "E001", "relation": "supports", "to": "K003", "note": "<tested scope; not proof>"},
    {"from": "K003", "relation": "novelty_compared_with", "to": "K004", "basis": ["E003"], "note": "<overlap, difference, or uncertainty>"}
  ]
}
```

`refs` locates provenance; explicit edges distinguish support from challenges, assumptions, or origins. Existing E endpoints need no duplicate `basis`. Edge counts do not establish independent corroboration.

## Relationship meanings

Read each edge as “from relation to.” Use only relevant relations; briefly define any additions.

| Relation | Direction and meaning |
| --- | --- |
| `supports` / `contradicts` | Evidence or result → claim it strengthens or challenges, within stated conditions. |
| `falsifies` | Validated counterexample or result → precise claim it refutes; preserve the claim and the checked scope. |
| `depends_on` / `assumes` | Result → prerequisite result, definition, method, or explicit assumption. Separate essential premises from merely helpful evidence. |
| `proves` / `verifies` | Proof-bearing result or evidence → claim established or checked. Qualify scope and verification type; numerical checks are not proofs. |
| `generalizes` / `special_case_of` | Broader result → narrower result / narrower result → broader result, with the connecting conditions recorded. Store one direction if the inverse can be generated. |
| `supersedes` | Revised claim → earlier claim, with the H/D/E reason. Materially changed statements get new map IDs; preserve earlier statements. |
| `novelty_compared_with` | Project claim → closest prior result, describing overlap, differences, and unresolved novelty risk. |
| `motivates` / `leaves_open` | Question, result, or risk → investigation it motivates / result or test → question it leaves unresolved. |

Retain conflicting edges until canonical records explain their resolution. Flag circular support; it cannot supply independent evidence or proof.

## Human views

Generate useful views on demand from the same map. A filtered table suffices; Graphviz, Mermaid, or an optional interactive graph may help. Show claim labels, statuses, relation meanings, evidence links, scope, and refresh date. Regenerate views instead of maintaining six separate reports.

| View | What to show |
| --- | --- |
| Main research story | Question → central results → significance → frontier. Explain significance with supported implications, keeping uncertainties visible. |
| Claim–evidence map | Each consequential claim with supporting and challenging E records, proof or verification scope, and remaining gaps. |
| Assumption/theorem dependency map | Results/theorem candidates, definitions, assumptions, and transitive prerequisites; highlight affected downstream arguments. |
| Research evolution map | Conjecture → test → counterexample → revised result, where those events occurred. Link changes to H/D/E records. |
| Literature/novelty map | Project claims against closest prior results and sources: overlap, generalization, assumption differences, novelty risks, and access gaps. |
| Open-frontier map | Group proved, conjectured, falsified, unresolved, and unexplored claims/questions; show dependencies and what evidence could change each open status. |

## Lightweight validation and maintenance

After consequential changes and before synthesis or handoff, inspect affected relationships or use a small project-local script if useful. Check unique IDs, resolving endpoints/record anchors, edge directions, and status agreement with records. Then flag:

| Check | Interpretation and follow-up |
| --- | --- |
| Consequential claim without supporting evidence | Trace support/proof/verification links to E records. A provenance reference or H/D instruction alone is insufficient. Keep unsupported claims explicitly conjectural or unresolved. |
| Theorem candidate with unclear assumptions | Check domains, quantifiers, definitions, and premises, including when no additional assumptions apply. Put missing specifications in its canonical record. |
| Claim depending on a falsified result | Follow essential `depends_on`/`assumes` paths transitively; flag affected arguments for reevaluation without automatically falsifying their conclusions. |
| Project result without novelty comparison | Identify the closest prior result and comparison record, or mark novelty unassessed/not claimed. Missing comparison is not evidence of originality. |
| Orphaned evidence | Check relevant E records within the declared scope for a connection to a claim/question. Link overlooked evidence or explain exclusions; not every source needs mapping. |
| Unresolved contradiction | Check opposing edges and statuses against domains/conditions. Retain the conflict with a resolution question or H/D/E explanation. |

Checks reveal gaps, not truth or proof. Record substantive corrections in E/D/H before refreshing the map and views; surface consequential unresolved findings in `STATE.md`.
