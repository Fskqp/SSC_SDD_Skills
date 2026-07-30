#!/usr/bin/env python3
"""Create a first-pass canonical model from a Markdown or text specification.

This script is intentionally conservative. It extracts candidate requirements
and question seeds, but a human/agent must review the result before treating it
as a validated specification.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.+?)\s*$")

REQUIREMENT_TERMS = (
    "must",
    "shall",
    "should",
    "need",
    "needs",
    "required",
    "requirement",
    "acceptance",
    "system",
    "user",
    "actor",
    "долж",
    "нужн",
    "необходим",
    "требован",
    "система",
    "пользователь",
    "роль",
    "критер",
)

CLASSIFICATION_TERMS = {
    "integration": (
        "api",
        "endpoint",
        "http",
        "rabbitmq",
        "queue",
        "exchange",
        "routing",
        "message",
        "event",
        "1c",
        "1с",
        "bitrix",
        "битрикс",
        "интеграц",
        "очеред",
        "сообщен",
        "событ",
        "вебхук",
    ),
    "data": (
        "postgres",
        "postgresql",
        "mariadb",
        "sql",
        "table",
        "column",
        "database",
        "entity",
        "field",
        "registry",
        "таблиц",
        "поле",
        "база",
        "данн",
        "справочник",
        "документ",
        "регистр",
    ),
    "ui": (
        "vue",
        "screen",
        "form",
        "button",
        "filter",
        "table",
        "modal",
        "интерфейс",
        "экран",
        "форма",
        "кнопк",
        "фильтр",
    ),
    "security": (
        "role",
        "permission",
        "auth",
        "access",
        "token",
        "security",
        "роль",
        "доступ",
        "прав",
        "безопас",
        "аутентиф",
        "авторизац",
    ),
    "non_functional": (
        "sla",
        "timeout",
        "performance",
        "latency",
        "availability",
        "audit",
        "log",
        "monitor",
        "производитель",
        "таймаут",
        "доступност",
        "аудит",
        "лог",
        "монитор",
    ),
    "report": (
        "report",
        "dashboard",
        "export",
        "print",
        "отчет",
        "выгруз",
        "экспорт",
        "печать",
    ),
}

ID_PREFIX = {
    "functional": "FR",
    "non_functional": "NFR",
    "data": "DATA",
    "integration": "INT",
    "ui": "UI",
    "security": "SEC",
    "report": "REP",
}


@dataclass
class Section:
    id: str
    title: str
    level: int
    start_line: int
    end_line: int | None = None


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "cp1251"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def normalize_line(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def contains_any(text: str, terms: Iterable[str]) -> bool:
    lower = text.lower()
    return any(term in lower for term in terms)


def classify(text: str) -> str:
    for req_type, terms in CLASSIFICATION_TERMS.items():
        if contains_any(text, terms):
            return req_type
    return "functional"


def extract_sections(lines: list[str]) -> list[Section]:
    sections: list[Section] = []
    for index, line in enumerate(lines, start=1):
        match = HEADING_RE.match(line)
        if not match:
            continue
        if sections:
            sections[-1].end_line = index - 1
        sections.append(
            Section(
                id=f"SEC-{len(sections) + 1:03d}",
                title=normalize_line(match.group(2)),
                level=len(match.group(1)),
                start_line=index,
            )
        )
    if sections:
        sections[-1].end_line = len(lines)
    return sections


def find_section(sections: list[Section], line_no: int) -> str | None:
    for section in reversed(sections):
        if section.start_line <= line_no and (section.end_line is None or line_no <= section.end_line):
            return section.id
    return None


def extract_candidates(lines: list[str], sections: list[Section]) -> list[dict]:
    counters = {prefix: 0 for prefix in ID_PREFIX.values()}
    candidates: list[dict] = []

    for line_no, raw_line in enumerate(lines, start=1):
        line = normalize_line(raw_line)
        if not line or HEADING_RE.match(line):
            continue

        bullet_match = BULLET_RE.match(raw_line)
        text = normalize_line(bullet_match.group(1) if bullet_match else line)

        if not text:
            continue

        is_candidate = bool(bullet_match) or contains_any(text, REQUIREMENT_TERMS)
        if not is_candidate:
            continue

        req_type = classify(text)
        prefix = ID_PREFIX.get(req_type, "FR")
        counters[prefix] += 1

        candidates.append(
            {
                "id": f"{prefix}-{counters[prefix]:03d}",
                "type": req_type,
                "title": text[:90],
                "statement": text,
                "source_refs": [f"SRC-001#line-{line_no}"],
                "section_ref": find_section(sections, line_no),
                "status": "draft",
            }
        )

    return candidates


def extract_glossary_candidates(lines: list[str]) -> list[dict]:
    terms: dict[str, int] = {}
    pattern = re.compile(r"\b(?:[A-ZА-ЯЁ][A-Za-zА-Яа-яЁё0-9]+(?:\s+[A-ZА-ЯЁ]?[A-Za-zА-Яа-яЁё0-9]+){0,3})\b")
    for line in lines:
        for match in pattern.finditer(line):
            term = normalize_line(match.group(0))
            if len(term) < 3:
                continue
            terms[term] = terms.get(term, 0) + 1

    frequent = sorted(terms.items(), key=lambda item: (-item[1], item[0].lower()))
    return [{"term": term, "count": count, "definition": ""} for term, count in frequent[:30]]


def build_questions(candidates: list[dict], lines: list[str]) -> list[dict]:
    text = "\n".join(lines).lower()
    questions: list[dict] = []

    def add(level: str, question: str, context: str, blocks: list[str]) -> None:
        questions.append(
            {
                "id": f"Q-{len(questions) + 1:03d}",
                "level": level,
                "question": question,
                "context": context,
                "why_it_matters": "The answer affects requirement interpretation, design, estimation, or acceptance.",
                "owner": "",
                "blocks": blocks,
            }
        )

    if not any(term in text for term in ("goal", "цель", "назначение", "problem", "проблем")):
        add("blocker", "What is the business goal and measurable success criterion?", "No explicit goal was detected.", [])

    if not any(term in text for term in ("actor", "user", "role", "пользователь", "роль", "участник")):
        add("blocker", "Which actors and roles participate in the process?", "No explicit actors or roles were detected.", [])

    if not any(term in text for term in ("acceptance", "criteria", "прием", "критер", "тест")):
        add("major", "What acceptance criteria prove that the requirement is implemented correctly?", "No explicit acceptance criteria were detected.", [item["id"] for item in candidates[:10]])

    integration_ids = [item["id"] for item in candidates if item["type"] == "integration"]
    if integration_ids:
        if not any(term in text for term in ("retry", "dlq", "dead letter", "повтор", "ошиб", "идемпотент")):
            add("major", "What are the retry, DLQ, duplicate handling, and error recovery rules for integrations?", "Integration candidates were detected without reliability rules.", integration_ids)
        if not any(term in text for term in ("payload", "schema", "json", "xml", "формат", "схем")):
            add("major", "What payload schemas and field mappings are required for each integration?", "Integration candidates were detected without payload details.", integration_ids)

    data_ids = [item["id"] for item in candidates if item["type"] == "data"]
    if data_ids and not any(term in text for term in ("source of truth", "owner", "владелец", "источник", "мастер")):
        add("major", "Which system is the source of truth for each data object?", "Data candidates were detected without ownership rules.", data_ids)

    return questions


def compile_model(input_path: Path) -> dict:
    text = read_text(input_path)
    lines = text.splitlines()
    sections = extract_sections(lines)
    candidates = extract_candidates(lines, sections)

    return {
        "metadata": {
            "title": input_path.stem,
            "version": "draft",
            "source_files": [str(input_path)],
            "compiler": "semantic-spec-compilation/scripts/compile_spec.py",
            "review_required": True,
        },
        "sources": [
            {
                "source_id": "SRC-001",
                "type": "markdown_or_text",
                "locator": str(input_path),
                "reliability": "explicit",
            }
        ],
        "sections": [section.__dict__ for section in sections],
        "glossary": extract_glossary_candidates(lines),
        "requirements": candidates,
        "open_questions": build_questions(candidates, lines),
        "traceability": [
            {
                "source_ref": source_ref,
                "compiled_items": [item["id"]],
                "artifacts": [],
                "acceptance_criteria": [],
                "tests": [],
            }
            for item in candidates
            for source_ref in item["source_refs"]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile a Markdown/text spec into a first-pass canonical JSON model.")
    parser.add_argument("input", type=Path, help="Input Markdown or text file.")
    parser.add_argument("--output", "-o", type=Path, help="Output JSON file. Defaults to stdout.")
    parser.add_argument("--indent", type=int, default=2, help="JSON indentation.")
    args = parser.parse_args()

    if not args.input.exists():
        parser.error(f"Input file not found: {args.input}")

    model = compile_model(args.input)
    payload = json.dumps(model, ensure_ascii=False, indent=args.indent)

    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
