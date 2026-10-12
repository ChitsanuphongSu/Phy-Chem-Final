"""Create additive Phase 7A traceability and reports from the reviewed registries.

The script deliberately refuses to overwrite an existing Phase 7A deliverable.
"""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def relation(target_id: str, relationship_type: str, reason: str) -> dict:
    return {
        "target_id": target_id,
        "relationship_type": relationship_type,
        "verification_status": "VERIFIED",
        "reason_th": reason,
    }


def item(
    p1_id: str,
    topic_id: str,
    related_topics: list[str],
    formulas: list[tuple[str, str, str]],
    problems: list[tuple[str, str, str]],
    coverage: str,
    gaps: list[str],
    reason: str,
    example_lessons: list[str] | None = None,
    formula_status: str | None = None,
    correction_note: str | None = None,
) -> dict:
    examples = example_lessons if example_lessons is not None else [topic_id]
    result = {
        "p1_content_id": p1_id,
        "canonical_topic_id": topic_id,
        "related_topic_ids": related_topics,
        "related_lesson_ids": related_topics,
        "related_formula_ids": [x[0] for x in formulas],
        "related_worked_examples": [
            {
                "lesson_id": lesson_id,
                "field": "worked_example",
                "verification_status": "VERIFIED",
            }
            for lesson_id in examples
        ],
        "related_problem_ids": [x[0] for x in problems],
        "mapping_confidence": "HIGH",
        "coverage_status": coverage,
        "gap_classification": gaps,
        "relationship_details": {
            "topics": [relation(x, "DIRECT" if x == topic_id else "SUPPORTING", reason) for x in related_topics],
            "lessons": [relation(x, "DIRECT" if x == topic_id else "SUPPORTING", reason) for x in related_topics],
            "formulas": [relation(*x) for x in formulas],
            "problems": [relation(*x) for x in problems],
        },
        "relationship_status": {
            "topic": "VERIFIED",
            "lesson": "VERIFIED",
            "formula": formula_status or ("VERIFIED" if formulas else "MISSING_CONTENT"),
            "worked_example": "VERIFIED" if examples else "MISSING_CONTENT",
            "practice_problem": "VERIFIED" if problems else "MISSING_CONTENT",
        },
        "mapping_reason_th": reason,
    }
    if correction_note:
        result["source_correction_note_th"] = correction_note
    return result


items = [
    item("K-P1-021", "K02", ["K02"], [("F-K-002", "DIRECT", "กฎอัตราเป็นสมการหลักของวิธี initial rates")], [("P-K-002", "DIRECT", "โจทย์ใช้ initial-rate data เพื่อหาอันดับและ k")], "COMPLETE", [], "หัวข้อ ดาว สูตร บทเรียน และโจทย์วัดการหากฎอัตราจากข้อมูลอัตราเริ่มต้นโดยตรง"),
    item("K-P1-026", "K02", ["K02"], [("F-K-002", "DIRECT", "ใช้ rate law กับระบบ S2O8^2-/I-")], [("P-K-002", "DIRECT", "โจทย์มาจากหน้าเดียวกับเครื่องหมายดาว")], "COMPLETE", [], "เป็นแบบฝึกหัด initial rates ของ S2O8^2-/I- โดยตรง"),
    item("K-P1-035", "K03", ["K03"], [("F-K-004", "DIRECT", "สมการ integrated first-order rate law")], [("P-K-003", "DIRECT", "คำนวณความเข้มข้นด้วย first-order integrated law")], "COMPLETE", [], "เนื้อหาเป็นการอินทิเกรตกฎอัตราอันดับหนึ่ง"),
    item("K-P1-040", "K04", ["K04", "K03"], [("F-K-007", "DIRECT", "สมการครึ่งชีวิตอันดับหนึ่ง"), ("F-K-004", "SUPPORTING", "กราฟ first-order มาจาก integrated rate law")], [("P-K-004", "DIRECT", "โจทย์คำนวณครึ่งชีวิตอันดับหนึ่ง")], "COMPLETE", [], "เครื่องหมายดาวครอบคลุมกราฟ first-order และสมบัติครึ่งชีวิต"),
    item("K-P1-042", "K03", ["K03"], [("F-K-004", "DIRECT", "N2O5 ถูกแก้ด้วย first-order integrated law")], [("P-K-003", "DIRECT", "โจทย์ N2O5 อ้างอิงหน้าดาวและหน้าคำตอบต่อเนื่อง")], "COMPLETE", [], "ตัวอย่าง N2O5 ใช้ integrated first-order equation โดยตรง"),
    item("K-P1-049", "K03", ["K03"], [("F-K-005", "DIRECT", "สมการ integrated second-order rate law")], [], "PARTIAL", ["PRACTICE_GAP", "WORKED_EXAMPLE_GAP"], "มีสูตรและคำอธิบายอันดับสอง แต่ตัวอย่างฝังในบทเรียนและคลังโจทย์ปัจจุบันเน้นอันดับหนึ่ง", example_lessons=[], formula_status="VERIFIED"),
    item("K-P1-061", "K05", ["K05"], [("F-K-009", "SUPPORTING", "Ea ใน Arrhenius เชื่อมกับ activation barrier ใน reaction coordinate")], [], "PARTIAL", ["PRACTICE_GAP"], "บทเรียนมีตัวอย่างอ่าน Ea และ ΔH จากกราฟ แต่ยังไม่มีโจทย์ในคลัง"),
    item("K-P1-074", "K07", ["K07"], [], [], "PARTIAL", ["PRACTICE_GAP"], "intermediate เป็นแนวคิดกลไกปฏิกิริยาและไม่จำเป็นต้องมีสูตรเฉพาะ", formula_status="NOT_APPLICABLE"),
    item("K-P1-077", "K07", ["K07"], [], [], "PARTIAL", ["PRACTICE_GAP"], "บทเรียนอธิบาย RDS และการตัด intermediate ผ่านกลไก H2O2/I- โดยตรง", formula_status="NOT_APPLICABLE"),
    item("K-P1-091", "K06", ["K06", "K05"], [("F-K-009", "DIRECT", "Arrhenius อธิบายการขึ้นกับอุณหภูมิของ k"), ("F-K-010", "DIRECT", "สมการสองอุณหภูมิใช้เปรียบเทียบ k")], [("P-K-005", "DIRECT", "โจทย์แนวคิดตรวจการตีความผลอุณหภูมิต่อ k")], "COMPLETE", [], "หน้าดาวเน้นผลอุณหภูมิต่อ k ซึ่งเป็นวัตถุประสงค์ของ Arrhenius"),
    item("K-P1-094", "K01", ["K01"], [("F-K-001", "DIRECT", "เชื่อมอัตราด้วยสัมประสิทธิ์สโตอิชิโอเมทรี")], [("P-K-001", "DIRECT", "โจทย์มาจากหน้าดาวเดียวกัน")], "COMPLETE", [], "สูตรและโจทย์ใช้สัมประสิทธิ์สโตอิชิโอเมทรีโดยตรง"),
    item("K-P1-162", "K08", ["K08"], [], [], "PARTIAL", ["PRACTICE_GAP"], "collision/encounter เป็นแนวคิดเชิงภาพ จึงไม่ต้องมีสูตรเฉพาะ แต่ยังไม่มี retrieval-practice item", formula_status="NOT_APPLICABLE"),
    item("E-P1-013", "E03", ["E03"], [("F-E-001", "SUPPORTING", "นิยาม conductance และหน่วยเป็นส่วนหนึ่งของศัพท์ไฟฟ้า"), ("F-E-002", "SUPPORTING", "molar conductivity และหน่วยเป็นศัพท์หลักในบท")], [("P-E-001", "SUPPORTING", "โจทย์ใช้ conductivity และ molar conductivity แต่ไม่ได้ทดสอบศัพท์ทั้งหมด")], "PARTIAL", ["CONCEPTUAL_PRACTICE_GAP"], "มีบทเรียน สูตร และโจทย์คำนวณรองรับบางส่วน แต่ขาดโจทย์แนวคิดเรื่องสัญลักษณ์และหน่วยครบชุด"),
    item("E-P1-018", "E02", ["E02"], [], [], "PARTIAL", ["PRACTICE_GAP"], "บทเรียนบันทึกแนวโน้ม dielectric constant กับอุณหภูมิ; ปัจจุบันไม่มีสูตรหรือโจทย์เฉพาะ", formula_status="NOT_APPLICABLE"),
    item("E-P1-048", "E04", ["E04", "E03"], [("F-E-002", "DIRECT", "คำนวณ molar conductivity จาก conductivity"), ("F-E-003", "DIRECT", "คำนวณ degree of dissociation"), ("F-E-004", "DIRECT", "คำนวณ Ka ของ weak electrolyte")], [("P-E-001", "DIRECT", "โจทย์อ้างอิงหน้าดาวและทำครบ Λm, α, Ka")], "COMPLETE", [], "เป็นโจทย์หลายขั้นที่เชื่อม conductivity, Λm, α และ Ka โดยตรง"),
    item("E-P1-066", "E03", ["E03"], [("F-E-005", "DIRECT", "ใช้ Kohlrausch law หา Λ° ของ AgBr")], [("P-E-002", "DIRECT", "โจทย์ AgBr อ้างอิงหน้าดาวและใช้ค่าที่แก้เลขคณิตแล้ว")], "COMPLETE", [], "โจทย์ผ่านการตรวจเลขคณิตและเก็บคำเตือนต้นฉบับโดยไม่แก้ PDF", correction_note="ต้นฉบับลบ 6.99×10^-8 - 1.60×10^-8 ผิดเป็น 7.39×10^-8; เนื้อหาที่ผ่านการตรวจใช้ 5.39×10^-8 S cm^-1, S=4.44×10^-7 M และ Ksp=1.97×10^-13"),
    item("E-P1-083", "E06", ["E06"], [("F-E-006", "DIRECT", "คำนวณ ionic strength ของ CuSO4"), ("F-E-007", "DIRECT", "คำนวณ mean activity coefficient ด้วย DHLL")], [("P-E-003", "DIRECT", "โจทย์ CuSO4 ใช้ I และ Debye-Hückel ตามหน้าดาว")], "COMPLETE", [], "สูตรและโจทย์ตรงกับตัวอย่าง CuSO4 บนหน้าดาว"),
    item("E-P1-089", "E07", ["E07", "E06"], [("F-E-006", "SUPPORTING", "ionic strength เป็นแกนของการอธิบาย salting effect"), ("F-E-007", "SUPPORTING", "DHLL รองรับพฤติกรรมช่วง ionic strength ต่ำ")], [], "PARTIAL", ["PRACTICE_GAP"], "บทเรียน salting-in/out ใช้พื้นฐาน ionic strength และ activity; ไม่มีสูตรเฉพาะหรือโจทย์ในคลัง"),
    item("E-P1-095", "E09", ["E09"], [("F-E-009", "SUPPORTING", "cell potential ใช้ศักย์รีดักชันของ cathode และ anode")], [("P-E-004", "SUPPORTING", "โจทย์คำนวณ Ecell แต่ไม่ครอบคลุม cell notation ทั้งหมด")], "PARTIAL", ["CONCEPTUAL_PRACTICE_GAP"], "บทเรียนครอบคลุม galvanic cell และ cell notation; คลังโจทย์ปัจจุบันทดสอบ Ecell มากกว่า notation"),
    item("E-P1-108", "E09", ["E09", "E10"], [("F-E-009", "DIRECT", "คำนวณ Ecell จาก reduction potentials"), ("F-E-010", "DIRECT", "เชื่อม E° กับ ΔG°"), ("F-E-012", "DIRECT", "เชื่อม E° กับ equilibrium constant")], [("P-E-004", "DIRECT", "คำนวณ Ecell"), ("P-E-005", "DIRECT", "คำนวณ ΔG°"), ("P-E-006", "DIRECT", "คำนวณ K")], "COMPLETE", [], "หน้าดาวถามต่อเนื่อง Ecell, ΔG° และ K และมีโจทย์แยกตรวจครบทุกวัตถุประสงค์", example_lessons=["E09", "E10"]),
]


exam = json.loads((ROOT / "data" / "exam_priority.json").read_text(encoding="utf-8"))["items"]
exam_by_id = {x["content_id"]: x for x in exam}
for mapped in items:
    source = exam_by_id[mapped["p1_content_id"]]
    mapped["source_evidence"] = {
        "document": source["source_document"],
        "pdf_page": source["pdf_page"],
        "printed_slide_number": source["printed_slide_number"],
        "evidence_path": source["evidence_path"],
        "evidence_classification": source["evidence_classification"],
    }

traceability = {
    "schema_version": "1.0.0",
    "phase": "7A",
    "relationship_model": "additive-many-to-many",
    "authoritative_topic_registry": "data/topics.json",
    "lesson_model_note": "ระบบปัจจุบันใช้ Topic เป็นหน่วยบทเรียน; related_lesson_ids จึงอ้าง Topic ID เดิมโดยไม่สร้างหรือเปลี่ยน ID",
    "worked_example_model_note": "ตัวอย่างทำงานอยู่ในฟิลด์ worked_example ของ Topic; การอ้างอิงใช้ lesson_id+field เพื่อให้ตรวจสอบได้โดยไม่สร้าง ID เทียม",
    "status_definitions": {
        "VERIFIED": "ตรวจยืนยันความสัมพันธ์กับเนื้อหาและแหล่งอ้างอิงแล้ว",
        "REVIEW_REQUIRED": "หลักฐานยังไม่พอสำหรับยืนยัน",
        "NOT_APPLICABLE": "ชนิดความสัมพันธ์ไม่จำเป็นทางวิทยาศาสตร์",
        "MISSING_CONTENT": "เนื้อหาที่ควรมีแต่ยังไม่มีในฐานข้อมูล",
    },
    "coverage_status_definitions": {
        "COMPLETE": "วัตถุประสงค์การเรียนรู้หลักมีบทเรียนและการฝึกที่เพียงพอในขอบเขตข้อมูลปัจจุบัน",
        "PARTIAL": "มีเนื้อหาหลักแต่ยังขาดการฝึกหรือตัวอย่างบางประเภท",
        "MISSING": "ไม่มีเนื้อหาหลักรองรับ",
        "NOT_APPLICABLE": "ไม่ต้องใช้ความสัมพันธ์ชนิดนั้น",
        "REVIEW_REQUIRED": "ต้องตรวจสอบเพิ่มก่อนสรุป",
    },
    "counts": {"confirmed_p1": 20, "chemical_kinetics": 12, "electrochemistry": 8},
    "items": items,
}


def write_new(relative: str, text: str) -> None:
    path = ROOT / relative
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing Phase 7A output: {relative}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


write_new("data/p1_traceability.json", json.dumps(traceability, ensure_ascii=False, indent=2) + "\n")
print("Created data/p1_traceability.json")
