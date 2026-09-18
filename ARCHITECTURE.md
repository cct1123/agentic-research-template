# Autonomous Research Architecture

A human and agent discuss a research idea; the agent translates it into the project brief and initial state. The director then selects useful actions and repeats the evidence-driven loop. The workspace preserves progress across runs. Both canonical prompts are in [README.md](README.md#start-a-project).

```mermaid
flowchart TD
    Discussion["Human–agent discussion<br/>Research idea and relevant context"] --> Setup["Project setup<br/>Agent drafts PROJECT.md and initializes STATE.md"]

    subgraph Workspace["Project Workspace"]
        Files["Project files, persistent state<br/>Sources, analysis, outputs"]
    end
    Setup --> Files

    subgraph Director["Research Director — Autonomous Loop"]
        Uncertainty["Identify key uncertainty"] ==> Choose["Choose next action<br/>Delegate when useful"]

        subgraph Actions["Research Actions"]
            Search["Literature search"]
            Analyze["Analysis / modeling"]
            Test["Hypothesis testing"]
            Verify["Verification / falsification"]
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
    Reconcile -.-> Uncertainty
    Update -.->|Save| Files
    Resolved -->|Yes| Report["Final research report"]
    Resolved -->|Blocked: missing data or experiment| Intervention["Human intervention"]
    RuledOut -.->|Avenues exhausted: ask one specific question| Intervention
    Intervention -->|Input supplied| Files

    style Director stroke:#2563eb,stroke-width:3px
```

Across runs the loop is made restartable by `STATE.md`'s continuity fields. One session owns the checkpoint at a time. Intent for an external, irreversible, or long-running action is recorded before the action, so an interrupted run leaves a detectable UNKNOWN outcome to verify rather than a silent gap. Records and artifacts are written before the state that references them, and the in-flight entry is cleared last. A cycle that produces no new evidence changes method, reframes the question, or is recorded as ruled out, so a fresh agent neither repeats a dead end nor loops on one avenue forever. See [persistent loop robustness](AGENTS.md#persistent-loop-robustness).
