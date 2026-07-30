# Canonical Requirements Model

Use this reference when compiling informal requirements into a semantic model. Keep the model explicit, traceable, and reviewable.

## Top-Level Shape

```json
{
  "metadata": {},
  "sources": [],
  "glossary": [],
  "stakeholders": [],
  "scope": {},
  "actors": [],
  "systems": [],
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

Capture:

- `title`
- `version`
- `date`
- `authors`
- `status`
- `target_systems`
- `source_files`
- `compilation_notes`

## Source Records

Each source record should include:

- `source_id`: stable identifier, for example `SRC-001`.
- `type`: `markdown`, `docx`, `pdf`, `meeting`, `task`, `screenshot`, `database`, `api`, `code`, or `unknown`.
- `locator`: file name, URL, task ID, meeting name, or quoted source fragment.
- `reliability`: `explicit`, `inferred`, `assumed`, or `conflicting`.

## Requirements

Each requirement should include:

- `id`
- `type`: `functional`, `non_functional`, `data`, `integration`, `ui`, `report`, `security`, `migration`, `operational`.
- `title`
- `statement`
- `source_refs`
- `priority`: `must`, `should`, `could`, `wont`, or `unknown`.
- `owner`
- `rationale`
- `dependencies`
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
- `requirement_ref`
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
  "source_ref": "SRC-001#section-3",
  "compiled_items": ["FR-001", "BR-003"],
  "artifacts": ["BPMN-001", "API-002"],
  "acceptance_criteria": ["AC-001", "AC-002"],
  "tests": ["T-001"]
}
```

## Open Questions

Use blocker levels:

- `blocker`: cannot design or estimate correctly without the answer.
- `major`: implementation can start with risk, but the answer may change contracts or data.
- `minor`: answer affects wording, UI polish, or edge behavior.

Each question should include:

- `id`
- `question`
- `context`
- `why_it_matters`
- `owner`
- `suggested_options`
- `blocks`
