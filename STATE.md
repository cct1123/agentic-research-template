# Current research state

Agent-maintained snapshot. Keep it concise and link detail to evidence or artifacts. Summarize applicable human steering and authorization in the relevant fields with links to H records; distinguish human-reported information from checked evidence. This is the last saved checkpoint, not a live process indicator.

- **Status:** not started (also after setup; `active`, `blocked`, or `finished` during research)
- **Last checkpoint:** none; use date, time, and timezone
- **Scope and success criteria:** derive from `PROJECT.md` and applicable H records during setup or the first research run; distinguish inferred criteria from human requirements
- **Applicable constraints / stopping limit:** not assessed

## Loop continuity

Reconcile this section before dependent work; see [Persistent loop robustness](AGENTS.md#persistent-loop-robustness).

- **Session owner / last checkpoint:** none. Record an identifier and a timestamp with timezone while working; release it when finishing. Advisory, not a lock: a successor may reclaim a stale entry and record the takeover.
- **In-flight action:** none. Before an external, irreversible, costly, or long-running action, record the exact operation, its expected observable effect, how to tell whether it completed, and the verification or rollback step. A non-empty entry means the outcome is UNKNOWN: check actual state before repeating it.
- **Attempts on current question:** none. Reset when the key uncertainty changes; change method or escalate when consecutive attempts produce no new evidence.

### Ruled out / do not retry

No avenues ruled out yet. Consult this list before choosing an action and add to it when an avenue fails for an understood reason. Never delete an entry; mark it superseded when evidence changes.

| Hypothesis / avenue | Why ruled out (record) | Revisit if |
| --- | --- | --- |

## Current answer

Not investigated. No confidence assessment yet.

## Evidence and alternatives

- **Established facts / important observations:** none assessed
- **Live hypotheses; support and counterevidence:** none assessed
- **Important prior decisions:** none; link decisive rejections and interpretation changes
- **Assumptions:** none adopted
- **Contradictions / important uncertainty:** not assessed

Use evidence links and distinguish sourced results, observations, and agent interpretations. Keep rejected hypotheses and major changes in decision records rather than expanding this snapshot into a history.

## Direction and handoff

- **Highest-priority open question:** initialize from the objective
- **Next action and why it matters:** read the brief, define a practical answer criterion, and select the most consequential uncertainty
- **Last completed action:** none; record setup here once the brief and initial state are saved
- **In-progress work / partial artifacts / delegated assignments:** none
- **Blockers / required human input:** none identified; request the objective if still blank

## Stop or resume

- **Outcome and stopping rationale:** not applicable
- **Report:** [unfinished outline](outputs/REPORT.md)
- **Resume or reopen when:** the objective is supplied; after investigation, replace with the specific next step or evidence that would warrant reopening
