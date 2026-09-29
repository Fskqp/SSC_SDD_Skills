---
name: semantic-spec-compilation
description: Compile informal business and system analysis inputs into traceable, module-first SDD/SSC specifications organized by epics, features, user stories, use cases, requirements, acceptance criteria, business rules, traceability, open questions, and optional technical appendices. Use for SDD, SSC, Markdown or Word specifications, meeting notes, interviews, task descriptions, and 1C ERP/API/RabbitMQ/database/Vue/Python analysis.
---

# Semantic Spec Compilation

## Overview

Use this skill to turn informal or semi-formal analysis inputs into a structured specification package. Treat the specification as a source artifact that can be compiled into a canonical model, gaps, traceability, diagrams, contracts, and test cases.

The skill is optimized for business and system analysis work around 1C ERP, Bitrix24, RabbitMQ, PostgreSQL, MariaDB, Vue, Python, StormBPMN, UML, and PlantUML.

## Core Rule

Do not invent missing requirements. Separate extracted facts, explicit assumptions, inferred implications, conflicts, and open questions. If the input is ambiguous, produce a usable partial compilation and list the blocking questions.

## When The User Provides A Spec

1. Identify source type: Markdown, Word/DOCX, PDF, screenshot, meeting transcript, task text, codebase, database schema, API contract, or mixed inputs.
2. Preserve source meaning before restructuring. Keep source terms in a glossary when they may have domain meaning.
3. Build the canonical model using `references/canonical-model.md`.
4. Organize functionality as `Module -> Epic -> Feature -> User Story`, then place the related use case, functional requirements, and acceptance criteria under each feature.
5. Classify requirements as functional, non-functional, business rule, data, integration, UI, reporting, security, operational, or migration requirement.
6. Detect ambiguity, contradiction, missing actors, missing triggers, missing data ownership, missing error behavior, and missing acceptance criteria.
7. Render the primary document using `references/document-structure.md`. Compile optional downstream artifacts only when requested or applicable.
8. Keep outputs traceable. Every generated requirement, test, diagram node, or contract element should point back to source text, assumption, or question.

## Default Analyst Package

When the user asks broadly to process, compile, formalize, or prepare a specification, produce:

- Document passport.
- Executive summary: context, problem, goal, and expected result.
- Scope, out of scope, constraints, and external dependencies.
- Sources, reliability, glossary, and abbreviations.
- Stakeholders, actors, roles, external participants, and responsibilities.
- Functional modules organized as `MOD -> EPIC -> FEAT -> US`.
- Under each feature: user stories, use case or use cases, functional requirements, and acceptance criteria.
- Module-level non-functional requirements after the module's features.
- Business rules after the functional modules.
- Requirements traceability matrix.
- Open questions grouped by blocker severity.
- Optional appendices only when applicable: diagrams, contracts, mappings, data models, and technical schemes.

## Document Rendering Rules

- Use `references/document-structure.md` as the required concrete template for the primary SDD/SSC document. Follow its top-level section order, required fields, module hierarchy, and table columns. Use optional sections only where the template allows them or the user explicitly requests another structure.
- Within every feature, use exactly four ordered blocks: User Stories, related Use Cases, Functional Requirements, Acceptance Criteria. Place typed UI, data, integration, security, and operational requirements inside the Functional Requirements block.
- Render every use case in the mandatory shape defined by `references/document-structure.md`: a `Field | Value` card, a two-column `Actor action | System response` main-scenario table, and step-bound alternative scenarios such as `2а` with child steps `2а1`, `2а2`. Do not replace this shape with prose, bullets, or a single-column step list.
- Do not create separate sections or columns for compilation metadata. Put source maturity under source reliability, overall status in the passport, and unresolved decisions in open questions. Before delivery, compare the heading hierarchy and table columns with the template.
- Do not display INVEST or another internal quality score in the compiled document unless the user explicitly asks for it.
- In a User Story card, do not repeat the parent feature, related use case, requirement IDs, or acceptance criteria IDs. The sequential document structure and final traceability matrix carry those relationships.
- Keep relationship references in the canonical model even when they are hidden from the rendered User Story card.
- Do not force a one-to-one relationship between User Story and Use Case. A use case may cover several stories, and a story may contribute to more than one use case.
- State missing values as gaps and create open questions. Do not fill them with invented roles, rules, thresholds, sources, or system behavior.

## Compilation Pipeline

### 1. Normalize

Convert the input into normalized sections:

- Context and goal.
- Modules, epics, features, and user stories.
- Use cases.
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

- `MOD-###` for functional modules.
- `EPIC-###` for epics.
- `FEAT-###` for features.
- `US-###` for user stories.
- `UC-###` for use cases.
- `BR-###` for business rules.
- `FR-###` for functional requirements.
- `NFR-###` for non-functional requirements.
- `DATA-###` for data requirements.
- `INT-###` for integrations.
- `API-###` for API behavior.
- `MSG-###` for RabbitMQ messages/events.
- `UI-###` for interface requirements.
- `REP-###` for reports.
- `SEC-###` for security requirements.
- `MIG-###` for migration requirements.
- `OPS-###` for operational requirements.
- `AC-###` for acceptance criteria.
- `Q-###` for open questions.

Capture the fields required for each item by `references/canonical-model.md`. Maintain source references, status, and relationships even when the rendered document intentionally omits redundant links.

### 3. Validate

Check the model against these quality gates:

- Each feature belongs to one epic, each epic belongs to one module, and each user story is placed under a feature.
- Each user story states an actor or beneficiary, need, and value, unless a different approved story format preserves the same meaning.
- Each feature is followed by its related use case or use cases, functional requirements, and testable acceptance criteria.
- Each use-case main-scenario step has one unique row identifier. Every alternative references an existing main-scenario step, uses the required branch numbering, and ends with an explicit return to a named main-scenario step or an explicit completion outcome.
- Module-level non-functional requirements appear after all features of that module; cross-system NFRs are stated once at the broadest applicable scope.
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
- For integration work: API contract, RabbitMQ event catalog, sequence diagrams, mapping tables.
- For database work: ERD, table changes, constraints, indexes, migration notes.
- For frontend work: Vue screen inventory, states, validations, user flows.
- For backend work: Python service responsibilities, endpoints, jobs, error handling, logging.
- For documentation delivery: Markdown or Word-ready structure following local document formatting requirements.

Use `references/document-structure.md` for the primary document, `references/artifact-templates.md` for optional artifact shapes, and `references/stack-patterns.md` for stack-specific checks.

## Handling Word Output

When creating a Word document, follow the user's local document rules if present. Default to Times New Roman 12 pt, black text, 1.5 line spacing, justified text, first-line indent 1.25 cm, left margin 30 mm, right margin 10-15 mm, top and bottom margins 20 mm, and page numbering at the bottom except on the title page.

## Response Style

Be explicit about uncertainty. Use tables for catalogs, matrices, and mappings. Use PlantUML code blocks for diagrams when requested or when diagrams materially clarify the spec.

Prefer concise artifacts that can be reviewed by stakeholders. For unresolved areas, give questions with enough context for a product owner, architect, developer, or 1C consultant to answer.
