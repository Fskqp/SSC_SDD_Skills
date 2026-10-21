# Staged Specification Workflow

Use this reference for collaborative specification work. The default analysis order is BPMN, UML Use Case Diagram, individual textual Use Cases, requirements and acceptance criteria, then final assembly. The final document still follows `document-structure.md`; analysis order does not change its section order.

## 1. Intake And Boundaries

Start from the materials already available. The initial brief should establish:

- The problem, business goal, and expected observable result.
- The process or capability in scope, its boundaries, and known exclusions.
- Participants, roles, target systems, and external systems.
- An existing BPMN diagram or a verbal description of the process, its trigger, and its completion condition.
- Known business rules, constraints, and examples of documents or data.
- Available sources such as tasks, meeting notes, diagrams, API contracts, or an earlier specification.

These are intake topics, not a demand that the user deliver a finished analysis. If something is missing, draft the known part, mark gaps, and ask focused questions about decisions needed for the current stage. Do not invent a role, integration behavior, limit, retry policy, or acceptance threshold.

Present a short brief and the proposed scope for agreement. Record unresolved items as questions with their blocker severity and affected artifacts.

## 2. BPMN Process

Use an existing model when supplied. Prepare the target TO BE process; add an AS IS model when understanding the current process materially helps define the change. Do not require both diagrams for every task.

Cover participants and responsibilities, the start trigger, actions, decision conditions, exchanges between systems, relevant error or cancellation paths, and observable completion outcomes. Use the BPMN outline in `artifact-templates.md` for StormBPMN-ready preparation. If no editable diagram tool is available, provide a clearly labeled BPMN outline and element/flow table, and state what still needs diagram assembly. Do not label an activity diagram as BPMN.

Present the process version and questions for review. Agreement concerns the target process, responsibilities, branches, and boundaries. Resolve questions that would change the agreed process; keep later contract details visible as deferred questions when they do not block this review.

## 3. UML Use Case Diagram And Catalog

Derive actors, the system boundary, and actor goals from the agreed process. Give each concrete Use Case a stable ID. Use PlantUML for the diagram when applicable. Add a compact catalog with UC ID, name, primary actor, goal, and related process elements. Keep the connection to source materials in the canonical model.

A BPMN task and a Use Case do not require a one-to-one mapping. One concrete Use Case describes a bounded actor goal and may span several process steps. Use `include` and `extend` only for their UML behavior semantics, not simply to draw a hierarchy of modules or features.

Review the completeness of actor goals, boundaries, the UC catalog, and the proposed scenario review order. Reuse agreed IDs. For umbrella and child IDs, follow `canonical-model.md`; an umbrella UC cannot replace a story's concrete scenario.

At this stage, catalog entries can remain explicit draft candidates while their User Story/UC pairs are being developed. Track missing relationships as gaps instead of inventing stories or claiming a fully validated canonical model. Enforce reciprocal primary links when a pair is completed and validate the complete model at final assembly. Reordering or retiring a UC does not renumber other IDs; an unavoidable ID change needs an explicit old-to-new mapping and updated references.

## 4. Review Each User Story And Concrete Use Case

Work through the agreed catalog one concrete UC at a time unless the user requests a batch. Place the User Story under its module, epic, and feature, then immediately show its primary concrete Use Case. Follow `document-structure.md` exactly for the cards and scenario tables.

The review packet includes:

- A User Story with actor or beneficiary, need, and value.
- The UC ID and review version, with changes since the last reviewed version summarized outside the scenario card.
- Actor, concrete goal, trigger, preconditions, and relevant participating systems or data.
- The main scenario as a two-column `Actor action | System response` table, with one step identifier per row.
- Relevant alternatives and errors bound to existing steps, using `2а`, `2а1`, `2а2` numbering and an explicit return or completion outcome.
- Observable postconditions and any questions that prevent agreement.

The user can comment by UC ID, branch, or step. Apply the comments, check dependent steps and questions, and present the revised scenario with a concise change summary. A correction or a question answer is not approval by itself.

Accept an unambiguous statement such as `UC-003 согласован` as agreement to the currently presented version. For hierarchical IDs, use the actual ID, for example `UC-01.03 согласован`. Record the corresponding User Story and UC versions. Do not ask for the same agreement again when it is already recorded and those versions have not changed.

Before marking the UC agreed, verify that its actor goal, trigger, preconditions, main flow, material alternatives and errors, and observable result are sufficiently defined for that review. If the user accepts an identified nonblocking detail for later clarification, record that limited scope and the remaining question; do not report the unresolved detail as confirmed. A question that blocks the scenario's behavior keeps the affected UC pending.

After agreement, move to the next UC. Keep the scenario checkpoint when the user asks an unrelated question or answers only part of the review. An explicit change of review order is allowed, but it leaves any unfinished UC pending rather than implicitly approving it.

## 5. Requirements And Acceptance Criteria

Derive atomic requirements and testable acceptance criteria from the agreed process and scenarios. Preserve stable IDs and source links. Record shared business rules once and link them to the relevant scenarios and requirements.

Resolve applicable data ownership, validation and lifecycle, access rights, integrations, API or message contracts, errors, duplicate handling, retries, monitoring, and measurable non-functional requirements. Use `stack-patterns.md` and the quality gates in `SKILL.md` only for technologies actually in scope.

Draft requirements can be captured earlier when they help clarify a scenario. Agreement to a UC does not automatically approve subsequently added contracts, requirements, or acceptance criteria. Present the resulting requirements package for review, calling out any new behavior or unresolved decisions.

In the document, place functional and typed requirements and acceptance criteria after all User Story/UC pairs in a feature. Place module NFRs after the module's features and cross-system NFRs once at the broadest applicable scope. Do not invent measurable thresholds to fill gaps.

## 6. Assemble And Review The Specification

Assemble the full analyst package using `document-structure.md`. Validate the module trees, adjacent User Story/UC pairs, primary UC relationships, scenario numbering, source traceability, and coverage by requirements, business rules, and acceptance criteria. Include applicable BPMN, UML, contracts, and mappings as appendices or linked artifacts.

Check that each reviewed version still agrees with the current diagrams and requirements. Present the assembled document for final review with its version and a concise list of unresolved decisions. Final document agreement is separate from agreement to individual scenarios.

An incomplete compilation remains a useful draft. Do not label it final, agreed, or ready for implementation while unresolved blocker questions affect its scope, behavior, contracts, or acceptance.

## Review State And Resuming Work

Maintain a compact working checkpoint separately from the primary specification. Keep it in the conversation for a short task; use a separate Markdown working record alongside project artifacts for a long task or when persistence is requested. Do not add workflow metadata sections or columns to the required primary document template.

Record:

- Current stage, scope, and artifact versions.
- Review states such as `Draft`, `In review`, `Agreed`, and `Needs review`.
- The UC catalog and the current and remaining scenario review queue.
- Explicit user agreements, the artifact IDs and exact versions they cover, and their source in the available conversation or supplied review record.
- Open questions with severity and affected artifact IDs.
- Deferred or skipped reviews and the next expected action.

On resuming, state the current stage and next pending review briefly. Reuse existing decisions; ask only for missing decisions that affect the current stage. If the prior agreement or version is unavailable, mark it unverified and request the necessary context instead of claiming it was agreed.

## Changes To Agreed Artifacts

When a requested change affects an agreed artifact:

1. Preserve its stable ID and create a new working version.
2. Identify the affected BPMN elements, diagram relations, User Stories, UCs, rules, requirements, contracts, and acceptance criteria through traceability.
3. Keep the previous agreement tied to its previous version. Mark materially changed versions `Needs review`; preserve unaffected agreements.
4. Show a concise change summary and present the affected versions for renewed review at the appropriate stage. Do not silently change agreed behavior or restart unrelated stages.

Pure formatting corrections can retain the existing agreement when meaning and behavior are unchanged; note the correction without requiring a full scenario review.

## Scope Overrides

Follow an explicit request for a single-pass draft, another sequence, or batch review. Record deferred gates; do not manufacture agreement to them. For a bounded task such as extracting API requirements or auditing an existing document, complete that task without imposing the entire staged workflow.

At a normal review boundary, finish the current reviewable artifact, state its ID/version and pending questions, and request agreement before advancing dependent work. Independent analysis can continue, but proposed downstream decisions remain drafts until their prerequisite review is resolved.
