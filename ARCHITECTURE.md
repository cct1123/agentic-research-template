# Autonomous Research Architecture

A human and agent discuss a research idea; the agent translates it into the project brief and initial state. The director then selects useful actions and repeats the evidence-driven loop. The workspace preserves progress across runs. Both canonical prompts are in [README.md](README.md#start-a-project).

The director selects [capabilities](AGENTS.md#mathematical-and-computational-research) to address gaps within the same adaptive loop. Escalation introduces no mandatory sequence or dependencies.

When relationships become difficult to follow, an [optional claim-centered map](KNOWLEDGE_MAP.md) connects results, assumptions, prior work, and open questions. E/D/H records retain canonical evidence and reasons for changes; `STATE.md` retains the current answer, remaining gap, and next action. Map views communicate relationships without replacing either.

```mermaid
flowchart TD
    Discussion["Human–agent discussion<br/>Research idea and relevant context"] --> Setup["Project setup<br/>Agent drafts PROJECT.md and initializes STATE.md"]

    subgraph Workspace["Project Workspace"]
        Files["Project files, persistent state<br/>Sources, analysis, outputs"]
        Files -.->|Only when relationship complexity warrants| Map["Optional claim map<br/>Generated human views"]
    end
    Setup --> Files

    subgraph Director["Research Director — Autonomous Loop"]
        Uncertainty["Identify key uncertainty"] ==> Choose["Choose next action and capability<br/>Delegate when useful"]

        subgraph Actions["Research Actions"]
            Search["Literature search"]
            Analyze["Reasoning / computation / modeling"]
            Test["Hypothesis testing / counterexample search"]
            Verify["Reproduction / proof / verification"]
        end

        Choose ==> Search
        Choose ==> Analyze
        Choose ==> Test
        Choose ==> Verify
        Search ==> Evidence["Evidence"]
        Analyze ==> Evidence
        Test ==> Evidence
        Verify ==> Evidence
        Evidence ==> Update["Update State<br/>Save records first, clear in-flight entry last"] ==> Resolved{"Objective Resolved?"}
        Resolved ==>|No| Progress{"New evidence this cycle?"}
        Progress ==>|Yes: choose next question| Uncertainty
        Progress ==>|No: change method or reframe| RuledOut["Record ruled-out avenue<br/>and reset the attempt count"]
        RuledOut ==> Uncertainty
    end

    Files -.->|Start or resume: read saved context| Reconcile["Reconcile in-flight action, ownership,<br/>later steering and the ruled-out list"]
    Map -.->|Relevant relationships, checked against records| Reconcile
    Reconcile -.-> Uncertainty
    Update -.->|Save| Files
    Resolved -->|Yes| Report["Final research report"]
    Resolved -->|Blocked: missing data or experiment| Intervention["Human intervention"]
    RuledOut -.->|Avenues exhausted: ask one specific question| Intervention
    Intervention -->|Input supplied| Files

    style Director stroke:#2563eb,stroke-width:3px
```

Across runs the loop is made restartable by `STATE.md`'s continuity fields. One session owns the checkpoint at a time. Intent for an external, irreversible, or long-running action is recorded before the action, so an interrupted run leaves a detectable UNKNOWN outcome to verify rather than a silent gap. Records and artifacts are written before the state that references them, and the in-flight entry is cleared last. A cycle that produces no new evidence changes method, reframes the question, or is recorded as ruled out, so a fresh agent neither repeats a dead end nor loops on one avenue forever. See [persistent loop robustness](AGENTS.md#persistent-loop-robustness).
