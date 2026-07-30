---
name: semantic-spec-compilation
description: Transform business and system analysis inputs into SDD, Spec-Driven Documentation, SSC, and Semantic Spec Compilation artifacts. Use when the user says "SSC", "SDD", "скомпилируй спецификацию", "сделай SDD", "сделай SSC", or asks to compile Markdown, Word, meeting notes, interview notes, task descriptions, Bitrix24 tasks, 1C ERP integration requirements, API/RabbitMQ/PostgreSQL/MariaDB/Vue/Python requirements, BPMN/UML/PlantUML descriptions, or ambiguous product ideas into canonical requirements models, clarification questions, traceability matrices, diagrams, API/database/integration contracts, implementation tasks, or acceptance criteria.
---

# Semantic Spec Compilation

## Overview

Use this skill to turn informal or semi-formal analysis inputs into a structured specification package. Treat the specification as a source artifact that can be compiled into multiple downstream artifacts: canonical model, gaps, traceability, diagrams, contracts, test cases, and implementation tasks.

The skill is optimized for business and system analysis work around 1C ERP, Bitrix24, RabbitMQ, PostgreSQL, MariaDB, Vue, Python, StormBPMN, UML, and PlantUML.

## Core Rule

Do not invent missing requirements. Separate extracted facts, explicit assumptions, inferred implications, conflicts, and open questions. If the input is ambiguous, produce a usable partial compilation and list the blocking questions.

## When The User Provides A Spec

1. Identify source type: Markdown, Word/DOCX, PDF, screenshot, meeting transcript, task text, codebase, database schema, API contract, or mixed inputs.
2. Preserve source meaning before restructuring. Keep source terms in a glossary when they may have domain meaning.
3. Build the canonical model using `references/canonical-model.md`.
4. Classify requirements as functional, non-functional, business rule, data, integration, UI, reporting, security, operational, or migration requirement.
5. Detect ambiguity, contradiction, missing actors, missing triggers, missing data ownership, missing error behavior, and missing acceptance criteria.
6. Compile downstream artifacts requested by the user. If the user does not specify artifacts, produce the default analyst package.
7. Keep outputs traceable. Every generated requirement, task, test, diagram node, or contract element should point back to source text, assumption, or question.

## Default Analyst Package

When the user asks broadly to process, compile, formalize, or prepare a specification, produce:

- Executive summary: goal, scope, out of scope, stakeholders.
- Canonical model: entities, actors, processes, states, events, integrations, constraints.
- Requirements catalog with stable IDs.
- Open questions grouped by blocker severity.
- Traceability matrix: source -> requirement -> artifact -> acceptance criteria/test.
- BPMN/UML/PlantUML recommendations and diagram code when useful.
- Integration contract outline for API, RabbitMQ, 1C ERP exchange, or database impact when applicable.
- Implementation task breakdown suitable for Bitrix24.

## Compilation Pipeline

### 1. Normalize

Convert the input into normalized sections:

- Context and goal.
- Business process.
- Actors and roles.
- Systems and external participants.
- Data objects.
- Events, commands, and states.
- User journeys and UI expectations.
- Integrations and exchange formats.
- Rules, constraints, and exceptions.
- Reports, notifications, and audit needs.
- Security and access control.
- Acceptance criteria and tests.

For large Markdown or text inputs, optionally run:

```bash
python scripts/compile_spec.py input.md --output model.json
```

Use the script as a first pass only. Review the output analytically before using it.

### 2. Compile Semantics

Create stable IDs:

- `BR-###` for business rules.
- `FR-###` for functional requirements.
- `NFR-###` for non-functional requirements.
- `DATA-###` for data requirements.
- `INT-###` for integrations.
- `API-###` for API behavior.
- `MSG-###` for RabbitMQ messages/events.
- `UI-###` for interface requirements.
- `REP-###` for reports.
- `AC-###` for acceptance criteria.
- `Q-###` for open questions.

For each item capture: title, statement, source, rationale, priority, owner, dependencies, acceptance criteria, and status.

### 3. Validate

Check the model against these quality gates:

- Each process has a trigger, actor, happy path, alternative path, and completion condition.
- Each integration has producer, consumer, transport, payload, idempotency, retry, error handling, and monitoring behavior.
- Each data object has owner system, identifiers, lifecycle, required fields, validation rules, and retention/audit expectations.
- Each API operation has method or command, request, response, errors, authorization, idempotency, and versioning rules.
- Each RabbitMQ flow has exchange, routing key, queue, payload schema, ack/retry/DLQ behavior, ordering expectations, and duplicate handling.
- Each UI requirement has user role, entry point, state, validation, empty/error/loading behavior, and accessibility notes when relevant.
- Each acceptance criterion is testable without relying on intent hidden outside the spec.

### 4. Emit Artifacts

Choose artifacts based on the user's goal:

- For business process analysis: BPMN outline and StormBPMN-ready process structure.
- For system design: UML use case, activity, sequence, component, deployment, or state diagrams.
- For implementation planning: Bitrix24 task tree with acceptance criteria and dependencies.
- For integration work: API contract, RabbitMQ event catalog, sequence diagrams, mapping tables.
- For database work: ERD, table changes, constraints, indexes, migration notes.
- For frontend work: Vue screen inventory, states, validations, user flows.
- For backend work: Python service responsibilities, endpoints, jobs, error handling, logging.
- For documentation delivery: Markdown or Word-ready structure following local document formatting requirements.

Use `references/artifact-templates.md` for output shapes and `references/stack-patterns.md` for stack-specific checks.

## Handling Word Output

When creating a Word document, follow the user's local document rules if present. Default to Times New Roman 12 pt, black text, 1.5 line spacing, justified text, first-line indent 1.25 cm, left margin 30 mm, right margin 10-15 mm, top and bottom margins 20 mm, and page numbering at the bottom except on the title page.

## Response Style

Be explicit about uncertainty. Use tables for catalogs, matrices, mappings, and task breakdowns. Use PlantUML code blocks for diagrams when requested or when diagrams materially clarify the spec.

Prefer concise artifacts that can be reviewed by stakeholders. For unresolved areas, give questions with enough context for a product owner, architect, developer, or 1C consultant to answer.
