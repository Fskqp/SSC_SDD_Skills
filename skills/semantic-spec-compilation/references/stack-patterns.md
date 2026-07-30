# Stack-Specific Analysis Patterns

Use this reference when the specification touches the user's usual stack.

## 1C ERP

Check:

- Which object is affected: document, catalog, register, report, business process, exchange plan, scheduled job, role, or form.
- Ownership of master data between 1C ERP and external systems.
- Numbering, posting, reposting, cancellation, corrections, and period closing behavior.
- Exchange mode: online request, event-based exchange, batch import/export, file exchange, or manual operation.
- Impact on accounting, inventory, settlements, tax, management accounting, and reporting.
- Rights and roles in 1C.
- Error recovery: re-run exchange, rollback, duplicate prevention, manual correction.

Questions:

- Is 1C ERP the source of truth for this data?
- Does the requirement affect posted documents or closed periods?
- What happens when external data conflicts with 1C data?
- Which 1C roles may create, view, modify, approve, or repost the object?

## Bitrix24

Check:

- Entity: lead, deal, contact, company, task, smart process, business process, activity, user, department, or custom field.
- Automation rules and triggers.
- Status/stage transitions and permissions.
- Integration with 1C ERP or external backend.
- Task decomposition with acceptance criteria and responsible roles.

Questions:

- Which Bitrix24 entity and pipeline does the requirement affect?
- Are fields standard or custom?
- Which automation rule owns the transition?
- What is the expected behavior for duplicate leads, contacts, companies, or deals?

## RabbitMQ

Check:

- Producer, consumer, exchange, routing key, queue, payload schema.
- Ack mode, retry policy, DLQ, poison message handling.
- Idempotency key and duplicate handling.
- Ordering requirements and partitioning strategy.
- Correlation ID and distributed tracing.
- Backpressure, timeout, and monitoring.

Questions:

- Is the event a fact that happened or a command requesting action?
- Can consumers process messages more than once?
- What should happen if 1C ERP or the consumer is unavailable?
- Which fields are required for replay and audit?

## PostgreSQL And MariaDB

Check:

- Logical entity model and physical table impact.
- Primary keys, unique constraints, foreign keys, nullable fields.
- Indexes for filtering, sorting, joins, and retention cleanup.
- Transactions, isolation, locking, and concurrent updates.
- Audit fields, history tables, soft delete, retention.
- Migration and rollback plan.

Questions:

- What is the authoritative identifier for this object?
- What data volumes and growth are expected?
- Which queries are business-critical?
- Does the requirement need full history or only current state?

## Vue Frontend

Check:

- Routes, screens, forms, widgets, tables, filters, cards, modals.
- User roles and visible actions.
- Loading, empty, validation, error, partial-success, and offline states.
- Client-side vs server-side validation.
- Data refresh, optimistic updates, pagination, sorting, filtering.

Questions:

- What must the user see before making a decision?
- Which fields are editable in each status?
- What errors should be shown to the user and which should be logged only?
- Does the UI need export, print, or audit evidence?

## Python Backend

Check:

- API endpoints, services, background jobs, workers, schedulers.
- Input validation, serialization, error model.
- Database transactions and retries.
- RabbitMQ producer/consumer responsibilities.
- Logging, metrics, tracing, and health checks.
- Configuration and secrets.

Questions:

- Which operation must be synchronous from the user's perspective?
- What is the timeout budget?
- Which failures are retriable?
- What must be logged for support and audit?

## BPMN, UML, PlantUML

Use BPMN for business process and role handoff. Use UML activity for algorithmic flow. Use sequence diagrams for integration behavior. Use component diagrams for service boundaries. Use state diagrams when statuses and transitions are central.

Quality checks:

- Diagram elements map to requirement IDs or process IDs.
- External systems are not hidden inside the target system boundary.
- Async message flows are visibly different from sync calls.
- Status transitions include rejected, cancelled, failed, timeout, and retry states where relevant.
