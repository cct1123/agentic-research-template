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
        Evidence ==> Update["Update State"] ==> Resolved{"Objective Resolved?"}
        Resolved ==>|No: choose next question| Uncertainty
    end

    Files -.->|Start or resume: read saved context| Uncertainty
    Map -.->|Relevant relationships, checked against records| Uncertainty
    Update -.->|Save| Files
    Resolved -->|Yes| Report["Final research report"]
    Resolved -->|Blocked: missing data or experiment| Intervention["Human intervention"]
    Intervention -->|Input supplied| Files

    style Director stroke:#2563eb,stroke-width:3px
```
