# Semantic Spec Compilation for Codex

`semantic-spec-compilation` is a Codex skill for compiling informal business and system analysis inputs into reviewable, traceable SDD and SSC specifications.

It accepts Markdown or Word specifications, meeting and interview notes, task descriptions, screenshots, schemas, API contracts, and mixed source materials. The skill separates confirmed facts, assumptions, inferred implications, conflicts, and open questions instead of inventing missing requirements.

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

Functionality is organized as:

```text
Module
└── Epic
    └── Feature
        └── User Story
```

Every feature is documented sequentially:

```text
User Stories
Use Case or Use Cases
Functional Requirements
Acceptance Criteria
```

Module-level non-functional requirements follow the module's functional content. Cross-system NFRs are stated once in the cross-system NFR subsection at the end of Functional Modules.

## Rendering Principles

- User Story cards contain the story, value, priority, and material dependencies.
- Parent Feature, related Use Case, requirement IDs, acceptance criteria IDs, and INVEST scores are not repeated in User Story cards.
- Those relationships remain in the canonical model. Applicable cross-artifact links appear in the traceability matrix, with Module and Feature columns added when needed to remove ambiguity.
- INVEST may be used as an internal quality check but is shown only when explicitly requested.
- A User Story and a Use Case are not forced into a one-to-one relationship.
- Unknown roles, rules, sources, thresholds, and system behavior become gaps or open questions.
- Implementation task decomposition is not a default document section.

## Stable IDs

The skill supports stable identifiers for:

- `MOD-###`: modules
- `EPIC-###`: epics
- `FEAT-###`: features
- `US-###`: user stories
- `UC-###`: use cases
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
