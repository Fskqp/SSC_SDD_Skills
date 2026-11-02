# Semantic Spec Compilation for Codex

`semantic-spec-compilation` is a Codex skill for compiling informal business and system analysis inputs into reviewable, traceable SDD and SSC specifications.

It accepts Markdown or Word specifications, meeting and interview notes, task descriptions, screenshots, schemas, API contracts, and mixed source materials. The skill separates confirmed facts, assumptions, inferred implications, conflicts, and open questions instead of inventing missing requirements.

## Collaboration Workflow

Collaborative specification work follows these stages by default:

1. Establish the problem, goal, scope, participants, systems, and available sources.
2. Prepare and agree the target BPMN process; describe AS IS when it helps explain the change.
3. Prepare and agree the UML Use Case Diagram and the catalog of concrete Use Cases.
4. Agree each User Story and its primary concrete Use Case individually.
5. Elaborate and agree requirements, business rules, data, applicable contracts, non-functional requirements, and acceptance criteria.
6. Assemble and validate the complete specification, then present it for final review.

Within every stage and for each concrete Use Case, ask focused clarification questions, receive the user's answers, show a concrete version for review, incorporate comments, and obtain explicit agreement to that presented version before advancing. Reuse answers already supplied. Answers, silence, and an instruction to prepare an artifact do not approve an unseen or revised result. Do not present a completed scenario for approval alongside the initial unanswered questionnaire.

Resume from the earliest unresolved stage using existing diagrams, stable IDs, and recorded agreements. Keep stage, interaction phase, artifact versions, answers, decisions, open questions, and pending reviews in a separate working checkpoint. Material changes to agreed artifacts require impact analysis and renewed review of affected versions.

The user can request a single-pass draft, batch review, another stage order, or a bounded task such as auditing an existing document. Record skipped or deferred reviews without treating them as agreed. The complete analyst package is the final assembly target; intermediate responses contain the active stage's artifacts and relevant questions.

See [the staged workflow reference](skills/semantic-spec-compilation/references/staged-workflow.md) for the complete interaction and review rules.

## Default Document Format

The primary specification uses this order:

1. Document passport
2. Executive summary
3. Scope, out of scope, constraints, and dependencies
4. Sources, source reliability, glossary, and abbreviations
5. Stakeholders, actors, roles, and responsibilities
6. Functional modules
7. Business rules
8. Requirements traceability
9. Open questions
10. Optional technical appendices

Before the details of every module, show its complete hierarchy as a fenced `text` tree. Include all actual epics, features, and user stories; each level can have multiple children:

```text
MOD-001 Module
├── EPIC-001 First epic
│   ├── FEAT-001 First feature
│   │   └── US-001 First story
│   └── FEAT-002 Second feature
│       ├── US-002 Second story
│       └── US-003 Third story
└── EPIC-002 Second epic
    ├── FEAT-003 Third feature
    │   └── US-004 Fourth story
    └── FEAT-004 Fourth feature
        ├── US-005 Fifth story
        └── US-006 Sixth story
```

Preserve vertical continuation lines and use `└──` only for the last child. The tree ends at User Stories; document concrete Use Cases in the feature details.

Every feature is documented sequentially:

```text
User Story 1
Primary concrete Use Case for User Story 1
User Story 2
Primary concrete Use Case for User Story 2
...repeat for every story...
Functional Requirements
Acceptance Criteria
```

Module-level non-functional requirements follow the module's functional content. Cross-system NFRs are stated once in the cross-system NFR subsection at the end of Functional Modules.

## Rendering Principles

- User Story cards contain the story, value, priority, and material dependencies.
- Parent Feature, related Use Case, requirement IDs, acceptance criteria IDs, and INVEST scores are not repeated in User Story cards.
- Those relationships remain in the canonical model. The adjacent Use Case card and the traceability matrix expose the primary User Story/Use Case relationship. Add Module and Feature columns to the matrix when needed to remove ambiguity.
- INVEST may be used as an internal quality check but is shown only when explicitly requested.
- By default, each User Story has exactly one primary concrete Use Case, placed immediately after that story. Additional links are allowed only for distinct behavior and require an explicit rationale.
- A parent or umbrella Use Case may organize a decomposition or diagram, but it cannot be the primary Use Case of a User Story or replace its concrete scenario.
- Unknown roles, rules, sources, thresholds, and system behavior become gaps or open questions.
- Implementation task decomposition is not a default document section.

Every concrete Use Case follows the mandatory format in [the document structure reference](skills/semantic-spec-compilation/references/document-structure.md):

- The marker `Related Use Case for US-###`, followed by the concrete UC ID and title.
- A `Field | Value` card with User Story, Parent Use Case when applicable, Primary actor, Goal, Trigger, and Preconditions.
- A main-scenario table with exactly two columns: `Actor action | System response`. Each row has one unique sequential step identifier. Repeat the same identifier in both populated cells; leave the other cell empty for a system-only or actor-only step.
- Alternatives and errors bound to existing main-scenario steps, using a Cyrillic lowercase letter in branch IDs such as `2а` and child IDs such as `2а1`, `2а2`. End every alternative with an explicit return to a numbered main-scenario step or an explicit completion outcome.
- Observable postconditions.

Do not replace the concrete Use Case format with prose, bullets, a numbered list, or a single-column table. The traceability matrix includes `User Story`, `Use Case`, `Link Type`, `Link Rationale`, `Requirements`, `Business Rules`, and `Acceptance Criteria`; every story has exactly one `Primary` row with its concrete Use Case, and `Additional` rows require a rationale.

## Stable IDs

The skill supports stable identifiers for:

- `MOD-###`: modules
- `EPIC-###`: epics
- `FEAT-###`: features
- `US-###`: user stories
- `UC-##`: parent or umbrella use cases
- `UC-##.##`: concrete child use cases
- `UC-###`: standalone concrete use cases when no parent exists
- `FR-###`: functional requirements
- `NFR-###`: non-functional requirements
- `BR-###`: business rules
- `DATA-###`: data requirements
- `INT-###`: integrations
- `API-###`: API behavior
- `MSG-###`: RabbitMQ messages and events
- `UI-###`: interface requirements
- `REP-###`: reports
- `SEC-###`: security requirements
- `MIG-###`: migration requirements
- `OPS-###`: operational requirements
- `AC-###`: acceptance criteria
- `Q-###`: open questions

## Optional Artifacts

The skill adds only artifacts applicable to the task:

- BPMN and StormBPMN structures
- UML and PlantUML diagrams
- API contracts
- RabbitMQ message contracts
- 1C ERP exchange contracts
- field mapping tables
- ERD and database changes
- Vue screen inventories and states
- Python service, endpoint, job, logging, and error-handling descriptions

## Skill Structure

```text
skills/semantic-spec-compilation/
  SKILL.md
  agents/
    openai.yaml
  references/
    artifact-templates.md
    canonical-model.md
    document-structure.md
    staged-workflow.md
    stack-patterns.md
  scripts/
    compile_spec.py
```

## Install In Codex

Install the skill from this repository:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Fskqp/SSC_SDD_Skills \
  --path skills/semantic-spec-compilation
```

On Windows, use the Codex Python runtime or a local Python installation:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo Fskqp/SSC_SDD_Skills `
  --path skills/semantic-spec-compilation
```

Restart Codex after installation.

## Usage

```text
Use $semantic-spec-compilation to compile these notes into a traceable module-first SDD/SSC specification.
```

```text
SSC: скомпилируй описание модуля в Epic, Feature, User Story, Use Case, FR, NFR, AC, бизнес-правила, трассировку и открытые вопросы.
```

```text
SDD: подготовь спецификацию интеграции 1C ERP -> RabbitMQ -> Python API с контрактом сообщения, sequence diagram и критериями приемки.
```

## Optional First-Pass Compiler

The bundled helper creates a conservative first-pass JSON model from Markdown or text:

```bash
python skills/semantic-spec-compilation/scripts/compile_spec.py input.md --output model.json
```

Its output is a draft and requires analyst review before approval or implementation.

## Supported Analysis Context

The skill includes focused checks for 1C ERP, Bitrix24 entities and automation, RabbitMQ, PostgreSQL, MariaDB, Vue, Python, BPMN, UML, and PlantUML.
