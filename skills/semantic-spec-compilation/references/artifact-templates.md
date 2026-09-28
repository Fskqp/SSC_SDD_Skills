# Artifact Templates

Use these templates for optional analyst artifacts and appendices. Use `document-structure.md` for the primary human-readable SDD/SSC document.

## Requirements Catalog

| ID | Type | Requirement | Source | Priority | Owner | Status | Acceptance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR-001 | functional |  | SRC-001 | must |  | draft | AC-001 |

## Open Questions

| ID | Level | Question | What It Blocks |
| --- | --- | --- | --- |
| Q-001 | blocker |  | FR-001 |

## Traceability Matrix

| User Story | Use Case | Requirements | Business Rules | Acceptance Criteria |
| --- | --- | --- | --- | --- |
| US-001 | UC-001 | FR-001, NFR-001 | BR-001 | AC-001 |

Do not add a `Source` column by default. Add `Module` and `Feature` columns for multi-module documents only when needed to remove ambiguity. Keep source-level links in the canonical model unless the user explicitly requests them in the rendered matrix.

## BPMN Outline

Use for StormBPMN or textual BPMN preparation:

| Element ID | Type | Name | Actor/Lane | Incoming | Outgoing | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| EVT-001 | start event |  |  |  | ACT-001 |  |
| ACT-001 | user task |  |  | EVT-001 | GW-001 |  |
| GW-001 | exclusive gateway |  |  | ACT-001 | ACT-002, ACT-003 |  |

Quality checks:

- Every process has exactly one clear start trigger unless the process is intentionally event-based.
- Gateways are named as decisions, not actions.
- Error and cancellation paths are visible.
- External systems are separate lanes or pools when the boundary matters.

## PlantUML Use Case

```plantuml
@startuml
left to right direction
actor "User" as User
rectangle "Target System" {
  usecase "UC-001: Capability" as UC001
}
User --> UC001
@enduml
```

## PlantUML Sequence

```plantuml
@startuml
actor User
participant "Vue UI" as UI
participant "Python API" as API
database "PostgreSQL" as DB
queue "RabbitMQ" as MQ
participant "1C ERP" as ERP

User -> UI: Action
UI -> API: Request
API -> DB: Read/write
API -> MQ: Publish event
MQ -> ERP: Consume event
ERP --> MQ: Ack
API --> UI: Response
@enduml
```

## API Contract

| Field | Value |
| --- | --- |
| ID | API-001 |
| Operation |  |
| Method/Command |  |
| URL/Topic |  |
| Auth |  |
| Request |  |
| Response |  |
| Errors |  |
| Idempotency |  |
| Versioning |  |
| Source Requirements |  |

## RabbitMQ Message Contract

| Field | Value |
| --- | --- |
| ID | MSG-001 |
| Event Name |  |
| Producer |  |
| Consumer |  |
| Exchange |  |
| Routing Key |  |
| Queue |  |
| Payload Schema |  |
| Correlation ID |  |
| Idempotency Key |  |
| Retry Policy |  |
| Dead Letter Handling |  |
| Ordering Requirements |  |
| Duplicate Handling |  |
| Monitoring |  |

## Database Change

| ID | Object | Change | Reason | Constraints | Indexes | Migration Notes |
| --- | --- | --- | --- | --- | --- | --- |
| DB-001 | table.column |  | FR-001 |  |  |  |

## Acceptance Criteria

Use Gherkin when the scenario matters:

```gherkin
Scenario: AC-001 Short scenario name
  Given a defined precondition
  When the user or system performs an action
  Then the expected observable result occurs
```

Use a checklist when criteria are independent:

| ID | Requirement | Criterion | Evidence |
| --- | --- | --- | --- |
| AC-001 | FR-001 |  |  |
