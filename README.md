# SSC / SDD Codex Skill

Codex skill for **SSC (Semantic Spec Compilation)** and **SDD (Spec-Driven Documentation)** in business and system analysis.

The skill converts informal requirements, meeting notes, task descriptions, Markdown/Word specs, and integration descriptions into structured analyst artifacts:

- canonical requirements model;
- requirements catalog with stable IDs;
- clarification questions and ambiguity/conflict list;
- traceability matrix;
- BPMN/UML/PlantUML artifacts;
- API, database, and RabbitMQ contracts;
- Bitrix24-ready implementation task breakdown;
- stack-specific checks for 1C ERP, Bitrix24, RabbitMQ, PostgreSQL/MariaDB, Vue, and Python.

## Skill Path

```text
skills/semantic-spec-compilation/
```

## Structure

```text
skills/semantic-spec-compilation/
  SKILL.md
  agents/openai.yaml
  references/
    artifact-templates.md
    canonical-model.md
    stack-patterns.md
  scripts/
    compile_spec.py
```

## Install In Codex

Install from this repository:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Fskqp/SSC_SDD_Skills \
  --path skills/semantic-spec-compilation
```

On Windows, use your Codex Python runtime or a local Python installation:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo Fskqp/SSC_SDD_Skills `
  --path skills/semantic-spec-compilation
```

Restart Codex after installation.

## Usage

Use short triggers:

```text
SSC: скомпилируй это ТЗ в каноническую модель, вопросы, трассировку и PlantUML.
```

```text
SDD: подготовь пакет документации по этой задаче для разработки и приемки.
```

More specific examples:

```text
SSC: разбери описание интеграции 1C ERP -> RabbitMQ -> Python API. Нужны message contract, sequence diagram, вопросы и acceptance criteria.
```

```text
SDD: из этого текста сделай каталог требований, BPMN outline, задачи для Bitrix24 и матрицу трассировки.
```

## Optional First-Pass Compiler

The skill includes a helper script for a first-pass Markdown/text to JSON model conversion:

```bash
python skills/semantic-spec-compilation/scripts/compile_spec.py input.md --output model.json
```

The script is intentionally conservative. Treat its output as a draft that still requires analyst review.

## Main Principle

The skill should not invent missing requirements. It separates:

- explicit source facts;
- assumptions;
- inferred implications;
- conflicts;
- open questions.

This makes the resulting specification suitable for review by product owners, architects, developers, QA, 1C consultants, and integration engineers.
