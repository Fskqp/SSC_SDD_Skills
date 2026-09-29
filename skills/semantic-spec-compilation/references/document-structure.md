# Module-First SDD/SSC Document Structure

Use this reference when rendering the primary human-readable specification. The canonical model may contain explicit relationship fields that are intentionally omitted from the document to avoid repetition.

## Required Top-Level Order

Use this order unless the user explicitly requests another structure:

1. Document Passport
2. Executive Summary
3. Boundaries
4. Sources And Terms
5. Stakeholders
6. Functional Modules
7. Business Rules
8. Requirements Traceability
9. Open Questions
10. Appendices, only when applicable

If a required value is unknown, state `Requires clarification` or the equivalent in the user's language and add an open question. Do not invent a value.

## 1. Document Passport

Capture:

- Title
- Version
- Date
- Authors
- Status
- Target systems
- Source materials

## 2. Executive Summary

Capture:

- Context
- Problem
- Goal
- Expected result

## 3. Boundaries

Capture:

- Scope
- Out of Scope
- Constraints
- External dependencies

## 4. Sources And Terms

Capture:

- Source list
- Source reliability
- Glossary
- Abbreviations

## 5. Stakeholders

Capture:

- Process owners
- Actors
- Roles
- External participants
- Responsibilities

## 6. Functional Modules

Repeat the following structure for each module.

### Module Heading

Use `MOD-###. <Module name>`.

### Module Passport

| Attribute | Value |
|---|---|
| ID | MOD-### |
| Name |  |
| Goal |  |
| Primary actor |  |
| Status | Draft / Confirmed / other agreed status |
| Priority | Must / Should / Could / Won't / Unknown |
| Scope |  |
| Out of Scope |  |
| Owner |  |
| Source system |  |

### Module Structure

Show the hierarchy before detailed content:

```text
MOD-001 Module
└── EPIC-001 Epic
    ├── FEAT-001 Feature
    │   ├── US-001 User Story
    │   │   └── UC-01.01 Primary concrete Use Case
    │   └── US-002 User Story
    │       └── UC-01.02 Primary concrete Use Case
    └── FEAT-002 Feature
        └── US-003 User Story
            └── UC-02.01 Primary concrete Use Case
```

The hierarchy is `Module -> Epic -> Feature -> User Story`. Do not use `User Task` for implementation work in this hierarchy.

A parent or umbrella Use Case may group concrete Use Cases in a decomposition table or diagram. It is not a substitute for the concrete Use Case placed under each User Story.

### Epic And Feature Content

For each epic, render its features sequentially. Use this order inside every feature:

1. Repeat a `User Story -> primary concrete Use Case` pair for every story.
2. Functional Requirements.
3. Acceptance Criteria.

Within each repeated pair, render the User Story first. Immediately after it, add the marker `Related Use Case for US-###` and the full card of its primary concrete Use Case. If the story has an additional use case link, place it after the primary card and state why the extra link is needed before continuing to the next User Story.

#### User Story

Use `US-###. <Title>`, followed by:

- Story statement, preferably `As <actor>, I want <need>, so that <value>` or an equivalent clear formulation.
- Value.
- Priority.
- Dependencies, only when present or material.

Do not display these redundant fields in the User Story card:

- Parent feature
- Related use case
- Requirement IDs
- Acceptance criteria IDs
- INVEST score or checklist

Keep those relationships in the canonical model, expose the primary relationship through the adjacent Use Case card, and repeat it in the traceability matrix.

#### Use Case

Every User Story has exactly one primary concrete Use Case by default. Place it immediately after the story using this mandatory shape. Do not replace it with prose, a numbered list, bullets, or a one-column table.

```markdown
**Related Use Case for US-###**

**UC-##.##. <Concrete goal>**

| Field | Value |
|---|---|
| User Story | US-### |
| Parent Use Case | UC-##, when applicable |
| Primary actor |  |
| Goal |  |
| Trigger |  |
| Preconditions |  |

**Main scenario:**

| Actor action | System response |
|---|---|
| 1. <Actor action> | 1. <System response> |
|  | 2. <System-only action, when applicable> |
| 3. <Actor action> | 3. <System response> |

**Alternative scenarios:**

**2а. <Alternative title>**

2а1. <Alternative action or response>.
2а2. <Alternative action or response>.
2а3. The scenario returns to step 2 of the main scenario, or ends with an explicit outcome.

**Postconditions:**

- <Observable resulting state>.
```

Apply these rules exactly:

- The primary Use Case describes one concrete user goal represented by the preceding User Story. It links to that story in the canonical model.
- When a parent Use Case is used, identify it as `UC-##` and identify concrete children as `UC-##.##`. When no parent exists, use `UC-###` for the standalone concrete Use Case.
- A parent or umbrella Use Case is an orchestration, decomposition, or diagram element. It cannot be the primary Use Case of a User Story and does not replace a concrete scenario card.
- A story may have additional use case links only when they represent distinct behavior. Mark each additional link and give a concise rationale.
- The main-scenario table has exactly two columns: `Actor action` and `System response`.
- Each row represents one logical step and has one unique sequential integer identifier.
- When both cells in a row are populated, repeat the same step identifier in both cells. Do not number the actor action and system response as separate steps.
- For a system-only step, leave the actor cell empty and put the numbered action in the system cell. For an actor-only step, apply the inverse rule.
- Number alternative scenarios as `<main-step><Cyrillic lowercase letter>`, for example `2а`, `2б`, `4а`. The numeric prefix must reference an existing main-scenario step.
- Number child steps by appending an integer to the branch identifier, for example `2а1`, `2а2`, `2а3`.
- End every alternative with either an explicit return to a numbered main-scenario step or an explicit completion outcome. Do not use an implicit continuation.
- Keep exceptions and errors in the same numbered alternative-scenario format unless the user explicitly requests a separate exception catalog.
- Include data used and participating systems in the field card only when they materially clarify the scenario.
- Keep shared end-to-end orchestration in the parent Use Case or diagram instead of merging the concrete Use Cases attached to different stories.

#### Functional Requirements

Use a feature-scoped table:

| ID | Requirement |
|---|---|
| FR-001 |  |

Requirements must be atomic, unambiguous, and observable. Keep source, owner, status, and relationship metadata in the canonical model rather than repeating it in this table unless the user requests an expanded catalog.

#### Acceptance Criteria

Use `AC-###. <Scenario name>`. Prefer Given/When/Then when sequence and state matter:

```gherkin
Given a defined precondition
When the actor or system performs an action
Then an observable result occurs
```

Use a compact checklist when the criteria are independent. Cover the main flow and relevant empty, negative, permission, validation, and technical error scenarios.

### Module-Level Non-Functional Requirements

After all epics and features of the module, add:

| ID | Requirement |
|---|---|
| NFR-001 |  |

Use measurable thresholds. Do not duplicate a cross-system NFR in every module or use case.
When the source contains no confirmed measurable NFR, keep the module subsection with a brief gap statement and references to open questions. Do not invent an NFR or add a placeholder table row.

### Cross-System Non-Functional Requirements

After all modules, but still inside `6. Functional Modules`, add this subsection when an NFR applies to the solution as a whole:

| ID | Requirement | Scope |
|---|---|---|
| NFR-### |  | Cross-system |

State each cross-system NFR once. Omit this subsection when all NFRs are module-specific or when no confirmed cross-system NFR exists.

## 7. Business Rules

Declare each rule once. Use references in traceability instead of copying the rule into features or use cases.

| ID | Condition | Decision | Exception | Example | Owner | Source |
|---|---|---|---|---|---|---|
| BR-001 |  |  |  |  |  |  |

If a rule applies only to one module or feature, preserve that scope in the canonical model.

## 8. Requirements Traceability

Use this compact matrix:

| User Story | Use Case | Link Type | Link Rationale | Requirements | Business Rules | Acceptance Criteria |
|---|---|---|---|---|---|---|
| US-001 | UC-01.01 | Primary | Concrete scenario for the story goal | FR-001, NFR-001 | BR-001 | AC-001 |

Use these columns in the primary document. Every User Story has exactly one `Primary` row with a concrete Use Case. Add rows of type `Additional` only with a meaningful rationale. A parent or umbrella Use Case cannot be used in a `Primary` row. Do not add a `Source` column by default. For a multi-module document, add `Module` and `Feature` columns only when needed to remove ambiguity. Maintain source-level traceability in the canonical model and add it to the rendered matrix only when the user explicitly requests source traceability.

## 9. Open Questions

| ID | Level | Question | What It Blocks |
|---|---|---|---|
| Q-001 | Blocker / Major / Minor |  |  |

Keep context, owner, suggested options, and affected item references in the canonical model. Add them to the rendered table only when useful for stakeholder review.

## 10. Appendices

Add only applicable artifacts:

- BPMN or StormBPMN
- UML or PlantUML diagrams
- API contracts
- RabbitMQ message contracts
- 1C ERP exchange contracts
- Mapping tables
- ERD and database changes
- UI prototypes or screen inventory
- Technical schemes

Do not add implementation task decomposition as a default document section.
