from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT.parent


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


inventory = load("data/document_inventory.json")
topics = load("data/topics.json")["topics"]
formulas = load("data/formulas.json")["formulas"]
problems = load("data/problems.json")["problems"]
exam_items = load("data/exam_priority.json")["items"]
trace_items = load("data/p1_traceability.json")["items"]

topic_ids = {x["id"] for x in topics}
formula_ids = {x["id"] for x in formulas}
problem_ids = {x["id"] for x in problems}
p1_ids = {x["content_id"] for x in exam_items}

# Baseline and uniqueness invariants.
assert len(inventory["documents"]) == 6
assert len(topic_ids) == len(topics) >= 18
assert len(formula_ids) == len(formulas) >= 23
assert len(problem_ids) == len(problems) >= 11
assert len(p1_ids) == len(exam_items) == 20
assert Counter(x["content_id"][0] for x in exam_items) == {"K": 12, "E": 8}
assert all(x["priority"] == "P1" and x["evidence_classification"] == "CONFIRMED" for x in exam_items)

# Every primary-source page was classified and original PDFs retain recorded hashes.
document_pages = {x["file_name"]: x["page_count"] for x in inventory["documents"]}
primary = [x for x in inventory["documents"] if x["role"] == "primary_instructor"]
assert sum(x["page_count"] for x in primary) == 300
assert all(
    page.get("star_detection", {}).get("status") in {"CONFIRMED", "NOT_FOUND"}
    for document in primary
    for page in document["pages"]
)
for document in inventory["documents"]:
    source_pdf = SOURCE_ROOT / document["file_name"]
    assert source_pdf.is_file(), source_pdf
    assert sha256(source_pdf) == document["sha256"], source_pdf

# Foreign-key-like data relationships and enums.
assert all(x["topic_id"] in topic_ids for x in formulas)
assert all(x["topic_id"] in topic_ids for x in problems)
assert all(fid in formula_ids for topic in topics for fid in topic["formula_ids"])
assert all(fid in formula_ids for problem in problems for fid in problem["related_formula_ids"])
assert all(x["difficulty"] in {"easy", "medium", "hard"} for x in problems)
assert all(x["priority"] in {"P1", "P2", "P3", "P4", "REVIEW"} for x in formulas)
assert all(topic["progress_key"] == f"topic:{topic['id']}" for topic in topics)
for collection in (topics, formulas, problems):
    for record in collection:
        for source in record["source_references"]:
            assert source["document"] in document_pages
            assert 1 <= source["pdf_page"] <= document_pages[source["document"]]

# Current registry is authoritative; historical matrix numbering does not override it.
formula_topic = {x["id"]: x["topic_id"] for x in formulas}
assert formula_topic["F-E-006"] == "E06"
assert formula_topic["F-E-007"] == "E06"
assert formula_topic["F-E-008"] == "E06"
assert formula_topic["F-E-009"] == "E09"
assert {formula_topic[x] for x in ["F-E-010", "F-E-011", "F-E-012"]} == {"E10"}
assert formula_topic["F-E-013"] == "E11"

# Complete P1 traceability, valid statuses, unique relationships, and resolvable targets.
assert {x["p1_content_id"] for x in trace_items} == p1_ids
assert len(trace_items) == 20
assert Counter(x["coverage_status"] for x in trace_items) == {"COMPLETE": 11, "PARTIAL": 9}
assert sum(bool(x["related_problem_ids"]) for x in trace_items) == 13
coverage_values = {"COMPLETE", "PARTIAL", "MISSING", "NOT_APPLICABLE", "REVIEW_REQUIRED"}
relationship_values = {"VERIFIED", "REVIEW_REQUIRED", "NOT_APPLICABLE", "MISSING_CONTENT"}
for mapped in trace_items:
    assert mapped["coverage_status"] in coverage_values
    assert mapped["canonical_topic_id"] in topic_ids
    for key in ("related_topic_ids", "related_lesson_ids", "related_formula_ids", "related_problem_ids"):
        assert len(mapped[key]) == len(set(mapped[key]))
    assert set(mapped["related_topic_ids"]) <= topic_ids
    assert set(mapped["related_lesson_ids"]) <= topic_ids
    assert set(mapped["related_formula_ids"]) <= formula_ids
    assert set(mapped["related_problem_ids"]) <= problem_ids
    assert all(x["lesson_id"] in topic_ids and x["field"] == "worked_example" for x in mapped["related_worked_examples"])
    assert set(mapped["relationship_status"].values()) <= relationship_values
    source = mapped["source_evidence"]
    assert source["document"] in document_pages
    assert 1 <= source["pdf_page"] <= document_pages[source["document"]]
    assert (ROOT / source["evidence_path"]).is_file(), source["evidence_path"]
    for relationship_group in mapped["relationship_details"].values():
        targets = [x["target_id"] for x in relationship_group]
        assert len(targets) == len(set(targets))
        assert all(x["verification_status"] == "VERIFIED" and x["reason_th"] for x in relationship_group)

# Preserve validated chemistry, especially the documented AgBr correction.
agbr = next(x for x in problems if x["id"] == "P-E-002")
assert agbr["source_classification"] == "source-derived-review"
assert agbr["correct_answer"] == 1.97e-13
assert any("5.39e-8" in step for step in agbr["solution_steps"])
assert any("7.39e-8" in step and "error" in step for step in agbr["solution_steps"])

# Backup integrity and non-decrease/preservation comparisons.
manifest = load("backups/phase-7a/backup_manifest.json")
assert len(manifest["files"]) >= 8
for entry in manifest["files"]:
    backup = ROOT / entry["backup_file_path"]
    assert backup.is_file()
    assert backup.stat().st_size == entry["file_size_bytes"]
    assert sha256(backup) == entry["sha256"]
    assert entry["backup_verified"] is True

baseline_topics = load("backups/phase-7a/data/topics.json")["topics"]
baseline_formulas = load("backups/phase-7a/data/formulas.json")["formulas"]
baseline_problems = load("backups/phase-7a/data/problems.json")["problems"]
assert {x["id"] for x in baseline_topics} <= topic_ids
assert {x["id"] for x in baseline_formulas} <= formula_ids
assert {x["id"] for x in baseline_problems} <= problem_ids
assert {x["id"]: x["progress_key"] for x in baseline_topics} == {x["id"]: x["progress_key"] for x in topics}
assert {x["id"]: x["correct_answer"] for x in baseline_problems} == {x["id"]: x["correct_answer"] for x in problems}
assert {x["id"]: x["solution_steps"] for x in baseline_problems} == {x["id"]: x["solution_steps"] for x in problems}
for original in baseline_formulas:
    current = next(x for x in formulas if x["id"] == original["id"])
    assert {k: v for k, v in current.items() if k != "topic_id"} == {k: v for k, v in original.items() if k != "topic_id"}

print("Phase 7A integrity checks passed: 20 P1 mappings; PDFs, evidence, IDs, chemistry, and backups verified")
