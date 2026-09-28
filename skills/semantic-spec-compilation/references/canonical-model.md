# Canonical Requirements Model

Use this reference when compiling informal requirements into a semantic model. Keep the model explicit, traceable, and reviewable.

## Top-Level Shape

```json
{
  "metadata": {},
  "sources": [],
  "sections": [],
  "glossary": [],
  "stakeholders": [],
  "scope": {},
  "actors": [],
  "systems": [],
  "modules": [],
  "epics": [],
  "features": [],
  "user_stories": [],
  "use_cases": [],
  "processes": [],
  "states": [],
  "data_objects": [],
  "requirements": [],
  "business_rules": [],
  "integrations": [],
  "interfaces": [],
  "reports": [],
  "security": [],
  "acceptance_criteria": [],
  "tests": [],
  "traceability": [],
  "risks": [],
  "assumptions": [],
  "open_questions": []
}
```

## Metadata

The compiler emits every field below. `title`, `status`, `source_files`, `compiler`, and `review_required` must be populated. Keep unknown source metadata as an empty string or empty list instead of inventing values.

Fields:

- `title`
- `version`
- `date`
- `authors`
- `status`
- `target_systems`
- `source_files`
- `compilation_notes`
- `compiler`
- `review_required`

## Source Records

Each source record should include:

- `source_id`: stable identifier, for example `SRC-001`.
- `type`: `markdown`, `text`, `docx`, `pdf`, `meeting`, `task`, `screenshot`, `database`, `api`, `code`, or `unknown`.
- `locator`: file name, URL, task ID, meeting name, or quoted source fragment.
- `reliability`: `explicit`, `inferred`, `assumed`, or `conflicting`.

## Source Sections

The first-pass compiler preserves the source document structure in `sections`. Each section record should include:

- `id`: `SECTION-###`.
- `title`.
- `level`: source heading level.
- `start_line`: first source line of the section.
- `end_line`: last source line of the section, or `null` when it cannot be determined.

## Functional Hierarchy

The rendered hierarchy is `Module -> Epic -> Feature -> User Story`. Keep explicit references in the canonical model for traceability even though the rendered User Story card omits redundant relationship fields.

### Modules

Each module should include:

- `id`: `MOD-###`
- `name`
- `goal`
- `primary_actor_ref`
- `status`
- `priority`
- `scope`
- `out_of_scope`
- `owner`
- `source_system`
- `epic_refs`
- `source_refs`

### Epics

Each epic should include:

- `id`: `EPIC-###`
- `name`
- `module_ref`
- `goal`
- `feature_refs`
- `source_refs`

### Features

Each feature should include:

- `id`: `FEAT-###`
- `name`
- `epic_ref`
- `goal`
- `user_story_refs`
- `use_case_refs`
- `functional_requirement_refs`
- `acceptance_criteria_refs`
- `source_refs`

### User Stories

Each user story should include:

- `id`: `US-###`
- `title`
- `statement`
- `actor_or_beneficiary`
- `need`
- `value`
- `priority`
- `dependencies`
- `status`
- `feature_ref`
- `use_case_refs`
- `requirement_refs`
- `acceptance_criteria_refs`
- `source_refs`

The `feature_ref`, `use_case_refs`, `requirement_refs`, and `acceptance_criteria_refs` fields support the canonical model and traceability. Do not repeat them in the human-readable User Story card.

### Use Cases

Each use case should include:

- `id`: `UC-###`
- `name`
- `primary_actor_ref`
- `goal`
- `trigger`
- `preconditions`
- `main_flow`
- `alternative_flows`
- `exceptions`
- `postconditions`
- `data_used`
- `systems_involved`
- `feature_refs`
- `user_story_refs`
- `requirement_refs`
- `source_refs`

## Requirements

Every requirement record must include all fields below. `id`, `type`, `title`, `statement`, `source_refs`, `priority`, and `status` must be populated. Use empty strings, empty arrays, or `null` for unresolved enrichment and relationship fields; do not omit them and do not invent values.

Fields:

- `id`: use `FR`, `NFR`, `DATA`, `INT`, `UI`, `REP`, `SEC`, `MIG`, or `OPS` according to the requirement type.
- `type`: `functional`, `non_functional`, `data`, `integration`, `ui`, `report`, `security`, `migration`, `operational`.
- `title`
- `statement`
- `source_refs`
- `priority`: `must`, `should`, `could`, `wont`, or `unknown`.
- `owner`
- `rationale`
- `dependencies`
- `module_ref`
- `feature_ref`
- `user_story_refs`
- `use_case_refs`
- `acceptance_criteria_refs`
- `status`: `draft`, `confirmed`, `questioned`, `conflict`, `deprecated`.

## Business Rules

Business rules should be atomic. Avoid combining condition, calculation, permission, and exception into one rule.

Fields:

- `id`
- `title`
- `condition`
- `decision`
- `exception`
- `examples`
- `source_refs`
- `scope_refs`
- `owner`
- `status`

## Processes

Each process should include:

- `id`
- `name`
- `trigger`
- `primary_actor`
- `participants`
- `preconditions`
- `happy_path`
- `alternative_paths`
- `exceptions`
- `postconditions`
- `data_used`
- `systems_involved`
- `requirements_refs`
- `diagram_refs`

## Data Objects

Each data object should include:

- `id`
- `name`
- `owner_system`
- `description`
- `identifiers`
- `attributes`
- `validation_rules`
- `lifecycle`
- `retention`
- `audit_requirements`
- `privacy_classification`
- `source_refs`

## Integrations

Each integration should include:

- `id`
- `name`
- `producer`
- `consumer`
- `transport`: `http`, `rabbitmq`, `file`, `database`, `1c_exchange`, `manual`, or `unknown`.
- `trigger`
- `payload`
- `mapping`
- `frequency`
- `synchrony`: `sync`, `async`, `batch`, or `unknown`.
- `idempotency`
- `retry_policy`
- `error_handling`
- `monitoring`
- `security`
- `source_refs`

## Acceptance Criteria

Each acceptance criterion should be testable:

- `id`
- `feature_ref`
- `user_story_refs`
- `requirement_refs`
- `given`
- `when`
- `then`
- `test_data`
- `negative_cases`
- `evidence`

## Traceability

Traceability links source fragments to requirements and generated artifacts:

```json
{
  "source_refs": ["SRC-001#section-3"],
  "module_ref": "MOD-001",
  "epic_ref": "EPIC-001",
  "feature_ref": "FEAT-001",
  "user_story_ref": "US-001",
  "use_case_refs": ["UC-001"],
  "requirement_refs": ["FR-001", "NFR-001"],
  "business_rule_refs": ["BR-003"],
  "artifacts": ["BPMN-001", "API-002"],
  "acceptance_criteria_refs": ["AC-001", "AC-002"],
  "test_refs": ["T-001"]
}
```

## Open Questions

Use blocker levels:

- `blocker`: cannot design or estimate correctly without the answer.
- `major`: implementation can start with risk, but the answer may change contracts or data.
- `minor`: answer affects wording, UI polish, or edge behavior.

Each question should include:

- `id`
- `level`: `blocker`, `major`, or `minor`.
- `question`
- `context`
- `why_it_matters`
- `owner`
- `suggested_options`
- `blocks`
