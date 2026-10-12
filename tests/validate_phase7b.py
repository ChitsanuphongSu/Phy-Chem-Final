from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT.parent


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(spec: dict) -> float:
    op = spec["op"]
    v = spec.get("values", [])
    if op == "div":
        result = v[0]
        for value in v[1:]: result /= value
        return result
    if op == "mul_div": return v[0] * v[1] / math.prod(v[2:])
    if op == "product": return math.prod(v)
    if op == "div_square": return v[0] / v[1] ** 2
    if op == "subtract_product": return v[0] - v[1] * v[2]
    if op == "first_order_conc": return v[0] * math.exp(-v[1] * v[2])
    if op == "second_order_conc": return 1 / (1 / v[0] + v[1] * v[2])
    if op == "inverse_linear": return 1 / (v[0] + v[1] * v[2])
    if op == "subtract": return v[0] - v[1]
    if op == "arrhenius": return v[0] * math.exp(-v[1] / (v[2] * v[3]))
    if op == "arrhenius_two_temp": return v[0] * math.log(v[1]) / (1 / v[2] - 1 / v[3])
    if op == "reciprocal": return 1 / v[0]
    if op == "agbr_ksp":
        solubility = 1000 * (v[0] - v[1]) / v[2]
        return solubility ** 2
    if op == "ostwald": return v[0] * v[1] ** 2 / (1 - v[1])
    if op == "conductivity_ka":
        alpha = v[1] / v[2]
        return v[0] * alpha ** 2 / (1 - alpha)
    if op == "ionic_strength": return 0.5 * sum(c * z ** 2 for c, z in spec["terms"])
    if op == "dhll": return 10 ** (-v[0] * v[1] * math.sqrt(v[2]))
    if op == "mean_activity_12": return v[0] * (v[1] * v[2] ** 2) ** (1 / 3)
    if op == "neg_product": return -math.prod(v)
    if op == "equilibrium_k": return 10 ** (v[0] * v[1] / v[2])
    if op == "nernst_298": return v[0] - (v[1] / v[2]) * math.log10(v[3])
    raise AssertionError(f"Unknown validation operation: {op}")


inventory = load("data/document_inventory.json")
topics = load("data/topics.json")["topics"]
formulas = load("data/formulas.json")["formulas"]
problems_doc = load("data/problems.json")
problems = problems_doc["problems"]
trace = load("data/p1_traceability.json")["items"]
exam = load("data/exam_priority.json")["items"]
baseline = load("backups/phase-7b/data/problems.json")["problems"]
new = problems[len(baseline):]

topic_ids = {x["id"] for x in topics}
formula_ids = {x["id"] for x in formulas}
p1_ids = {x["content_id"] for x in exam}
doc_pages = {x["file_name"]: x["page_count"] for x in inventory["documents"]}

# Counts, immutable legacy records, stable IDs, target distributions.
assert len(baseline) == 11 and len(new) == 54 and len(problems) == 65
assert problems[:11] == baseline
assert len({x["id"] for x in problems}) == 65
assert Counter(x["difficulty"] for x in problems) == {"easy": 20, "medium": 29, "hard": 16}
assert Counter(x["topic_id"] for x in new) == {
    "K01":3,"K02":4,"K03":5,"K04":3,"K05":4,"K06":3,"K07":3,"K08":2,
    "E02":2,"E03":5,"E04":4,"E06":5,"E07":3,"E09":4,"E10":4,
}
assert all(x["topic_id"] in topic_ids for x in problems)
assert all(set(x["related_formula_ids"]) <= formula_ids for x in problems)

# New-question completeness and valid sources/P1 relationships.
assert len({x["prompt_th"] for x in new}) == 54
for question in new:
    assert question["validation_status"] == "VALIDATED"
    assert question["source_classification"] in {"source-derived", "source-adapted", "ai-generated-from-source"}
    assert question["type"] in {"numerical", "conceptual", "multiple-choice"}
    assert question["difficulty"] in {"easy", "medium", "hard"}
    assert len(question["hints"]) == 3 and len(set(question["hints"])) == 3
    assert question["learning_objective"] and question["common_mistake"]
    assert len(question["solution_steps"]) >= (8 if question["type"] == "numerical" else 5)
    assert set(question["related_p1_ids"]) <= p1_ids
    for source in question["source_references"]:
        assert source["document"] in doc_pages
        assert 1 <= source["pdf_page"] <= doc_pages[source["document"]]
    if question["type"] == "numerical":
        assert question["answer_format"] == "numeric"
        calculated = evaluate(question["validation_spec"])
        tolerance = max(question["tolerance"], abs(question["correct_answer"]) * 0.001)
        assert math.isclose(calculated, question["correct_answer"], rel_tol=0, abs_tol=tolerance), (question["id"], calculated, question["correct_answer"])
        assert tolerance > 0
    elif question["type"] == "multiple-choice":
        options = question["answer_options"]
        ids = [x["id"] for x in options]
        assert len(options) == 4 and len(set(ids)) == 4
        assert question["correct_option_id"] in ids
        assert set(question["option_explanations"]) == set(ids)
        assert question["correct_answer"] == question["correct_option_id"]
    else:
        accepted = question["grading_policy"]["accepted_answers"]
        assert len(accepted) >= 2 and all(x.strip() for x in accepted)

# Every P1 has at least one direct, validated Phase 7B question and no remaining gap.
new_ids = {x["id"] for x in new}
by_id = {x["id"]: x for x in problems}
assert len(trace) == 20
for mapping in trace:
    direct_new = [pid for pid in mapping["related_problem_ids"] if pid in new_ids]
    assert direct_new
    assert all(mapping["p1_content_id"] in by_id[pid]["related_p1_ids"] for pid in direct_new)
    assert mapping["coverage_status"] == "COMPLETE"
    assert mapping["gap_classification"] == []
    assert mapping["relationship_status"]["practice_problem"] == "VERIFIED"

# AgBr original correction stays intact; adapted values are independently consistent.
agbr_original = by_id["P-E-002"]
assert agbr_original["correct_answer"] == 1.97e-13
assert any("5.39e-8" in step for step in agbr_original["solution_steps"])
assert any("7.39e-8" in step for step in agbr_original["solution_steps"])
assert by_id["P-E-013"]["correct_answer"] == 2.5e-13
assert "7.39" not in " ".join(by_id["P-E-013"]["solution_steps"])

# Backup, original PDFs, and evidence remain intact.
manifest = load("backups/phase-7b/backup_manifest.json")
for entry in manifest["files"]:
    backup = ROOT / entry["backup_file_path"]
    assert backup.stat().st_size == entry["file_size_bytes"]
    assert sha256(backup) == entry["sha256"]
for document in inventory["documents"]:
    source = SOURCE_ROOT / document["file_name"]
    if not source.is_file():
        source = ROOT / "web" / "public" / "sources" / document["file_name"]
    assert sha256(source) == document["sha256"]
for item in exam:
    assert (ROOT / item["evidence_path"]).is_file()

assert (ROOT / "data/problems.json").read_bytes() == (ROOT / "web/src/data/problems.json").read_bytes()
assert (ROOT / "data/p1_traceability.json").read_bytes() == (ROOT / "web/src/data/p1_traceability.json").read_bytes()
print("Phase 7B validation passed: 54 new/65 total; numerical answers independently recalculated; P1 coverage 20/20")
