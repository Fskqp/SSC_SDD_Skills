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
- `primary_use_case_ref`
- `additional_use_case_links`: records containing `use_case_ref` and `rationale`.
- `use_case_refs`: derived union of the primary reference and all additional references.
- `requirement_refs`
- `acceptance_criteria_refs`
- `source_refs`

Every User Story has exactly one `primary_use_case_ref` by default, and that reference points to a concrete Use Case. Additional links are optional and require a non-empty rationale. The derived `use_case_refs` field supports compatibility and must not be used to hide which link is primary. Do not repeat these relationship fields in the human-readable User Story card.

### Use Cases

Each use case should include:

- `id`: `UC-##` for a parent or umbrella use case, `UC-##.##` for its concrete child, or `UC-###` for a standalone concrete use case.
- `name`
- `scope_type`: `concrete` or `umbrella`.
- `parent_use_case_ref`: the umbrella Use Case for a concrete child, otherwise `null`.
- `child_use_case_refs`: direct concrete children for an umbrella Use Case, otherwise an empty list.
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
- `user_story_ref`: the primary linked User Story for a concrete Use Case, otherwise `null`.
- `related_user_story_refs`: non-primary links, when explicitly justified.
- `requirement_refs`
- `source_refs`

A concrete Use Case must have a `user_story_ref`, bounded goal, trigger, main flow, alternatives when applicable, and observable postconditions. By default, one concrete Use Case is primary for one User Story. An umbrella Use Case cannot be referenced by `primary_use_case_ref`; use it only for orchestration, decomposition, or diagrams. Do not duplicate all child scenarios in the umbrella Use Case.

Represent the concrete Use Case `main_flow` as an ordered array of row records:

- `step_id`: a unique sequential integer used by the rendered two-column table.
- `actor_action`: actor action for the row, or `null` for a system-only step.
- `system_response`: system response for the row, or `null` for an actor-only step.

At least one action field must be populated. When both fields are populated, both belong to the same `step_id`; do not assign separate numbers to the two cells.

Represent `alternative_flows` as an ordered array of branch records:

- `id`: `<main-step><Cyrillic lowercase letter>`, for example `2а`.
- `branches_from_step_id`: the existing `main_flow.step_id` referenced by the numeric prefix.
- `title`.
- `steps`: ordered records with IDs such as `2а1`, `2а2` and an atomic `statement`.
- `outcome`: `return`, `complete`, or `error`.
- `return_to_step_id`: an existing `main_flow.step_id` when `outcome` is `return`; otherwise `null`.

The branch ID, `branches_from_step_id`, and every child-step ID must agree. Every alternative flow must have an explicit outcome. Store distinct exception records only when the user requests a separate exception catalog; otherwise represent errors as numbered alternative flows.

Validate the relationship in both directions: `user_stories[].primary_use_case_ref` points to a `scope_type: concrete` record, and that record's `user_story_ref` points back to the same User Story. If hierarchical numbering is used, the concrete ID prefix and `parent_use_case_ref` must agree.

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
  "primary_use_case_ref": "UC-01.01",
  "additional_use_case_links": [
    {
      "use_case_ref": "UC-03.02",
      "rationale": "The story also invokes a distinct audit scenario"
    }
  ],
  "requirement_refs": ["FR-001", "NFR-001"],
  "business_rule_refs": ["BR-003"],
  "artifacts": ["BPMN-001", "API-002"],
  "acceptance_criteria_refs": ["AC-001", "AC-002"],
  "test_refs": ["T-001"]
}
```

Render the primary reference as `Link Type: Primary`. Render each additional link as a separate `Link Type: Additional` row and carry its rationale into the traceability matrix. Never render an umbrella Use Case as the primary link.

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
