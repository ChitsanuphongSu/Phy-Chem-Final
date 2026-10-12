from __future__ import annotations

import json
import shutil
from pathlib import Path


PROJECT = Path(r"D:\Luna\Phy-Chem\physical-chemistry-study-hub")
INVENTORY_PATH = PROJECT / "data" / "document_inventory.json"

STARS = {
    "PhCh-SC202301_Physical_Chemistry_Part1": [
        (21, 21, "การหากฎอัตราและค่าคงที่อัตราจาก initial-rate data", "high"),
        (26, 25, "แบบฝึกหัดกฎอัตรา: S2O8^2- กับ I-", "high"),
        (35, 34, "ปฏิกิริยาอันดับหนึ่งและการอินทิเกรต rate law", "high"),
        (40, 39, "กราฟความเข้มข้นกับเวลาและครึ่งชีวิตของปฏิกิริยาอันดับหนึ่ง", "high"),
        (42, 41, "โจทย์ปฏิกิริยาอันดับหนึ่งของ N2O5", "high"),
        (49, 48, "การอินทิเกรตกฎอัตราของปฏิกิริยาอันดับสอง", "high"),
        (61, 60, "แผนภาพพลังงานศักย์ ปฏิกิริยาดูดความร้อน และ activation energy", "high"),
        (74, 73, "สารมัธยันต์ (intermediate) ในกลไกปฏิกิริยา", "high"),
        (77, 76, "rate-determining step และการตัด intermediate ออกจากสมการรวม", "high"),
        (91, 90, "ผลของอุณหภูมิต่อ k: ปฏิกิริยาทั่วไป เอนไซม์ และ chain reaction", "high"),
        (94, 93, "แบบฝึกหัดอัตราปฏิกิริยากับสัมประสิทธิ์สโตอิชิโอเมทรี", "high"),
        (162, 161, "รูปแบบการชนในแก๊สเทียบกับ encounter ในสารละลาย", "high"),
    ],
    "PhCh-SC202301_Physical_Chemistry_Part2": [
        (13, 13, "คำศัพท์ สัญลักษณ์ และหน่วยทางไฟฟ้า", "high"),
        (18, 18, "dielectric constant ของน้ำกับอุณหภูมิ", "high"),
        (48, 48, "Practice: conductivity, molar conductivity, degree of dissociation และ Ka", "high"),
        (66, 66, "Practice: solubility และ Ksp ของ AgBr จาก conductivity", "high"),
        (83, 83, "ตัวอย่าง ionic strength และ Debye-Huckel limiting law ของ CuSO4", "high"),
        (89, 89, "salting-in และ salting-out effect", "high"),
        (95, 95, "galvanic cell, oxidation/reduction, anode/cathode และ cell notation", "high"),
        (108, 108, "โจทย์ Ecell ของ redox couple พร้อมคำถามต่อยอด ΔG และ K", "high"),
    ],
}

DOC_SUMMARIES = {
    "PhCh-SC202301_Physical_Chemistry_Part1": {
        "scope": "Chemical Kinetics",
        "chapters": ["อัตราการเกิดปฏิกิริยา", "กฎอัตรา", "integrated rate laws", "half-life", "collision theory", "Arrhenius equation", "reaction mechanism", "catalysis", "solution reaction kinetics"],
        "visuals": "สไลด์ 16:9 มีสมการ กราฟ reaction coordinate, concentration-time, Arrhenius/temperature behavior, กลไกปฏิกิริยา และคำอธิบายเขียนมือหลายสี",
        "assessment": "มีตัวอย่างและแบบฝึกหัดทั้ง initial rate, integrated rate law, half-life, stoichiometric rate และ activation energy",
    },
    "PhCh-SC202301_Physical_Chemistry_Part2": {
        "scope": "Electrochemistry",
        "chapters": ["electrolytes", "dielectric constant", "conductance and conductivity", "molar conductivity", "degree of dissociation", "ionic mobility", "activity and ionic strength", "Debye-Huckel", "electrochemical cell", "cell thermodynamics", "electrodes", "concentration cell"],
        "visuals": "สไลด์ 16:9 มีตาราง สมการ เซลล์นำไฟฟ้า กราฟ activity coefficient แผนภาพ galvanic/electrolytic cell และ annotation เขียนมือหลายสี",
        "assessment": "มีตัวอย่างและแบบฝึกหัด conductivity, dissociation, solubility/Ksp, ionic strength, activity coefficient และ cell potential",
    },
    "Chemical_Kinetic": {
        "scope": "Supplementary Chemical Kinetics notes",
        "chapters": ["rate law", "integrated rate laws", "half-life", "Arrhenius", "mechanism", "collision/encounter"],
        "visuals": "โน้ตพื้นหลังเข้มแบบยาว มีสูตร ตารางสรุป กราฟ และภาพประกอบจากสไลด์ผู้สอน",
        "assessment": "มีสรุปสูตรและตัวอย่างย่อ ต้องตรวจเทียบกับเอกสารผู้สอนก่อนนำไปใช้",
    },
    "Electrochemistry": {
        "scope": "Supplementary Electrochemistry notes",
        "chapters": ["conductivity", "molar conductivity", "dissociation", "ionic strength/activity", "electrochemical cell", "Nernst equation"],
        "visuals": "โน้ตพื้นหลังเข้มแบบยาว มีสูตร ตาราง กราฟ และภาพประกอบ",
        "assessment": "มีสูตรและตัวอย่างย่อ ต้องตรวจเทียบกับเอกสารผู้สอนก่อนนำไปใช้",
    },
    "Final_Phychem": {
        "scope": "Handwritten revision and worked problems",
        "chapters": ["chemical kinetics", "electrochemistry"],
        "visuals": "ลายมือบนกระดาษกริด มีสมการ การแทนค่า และโจทย์คำนวณ",
        "assessment": "มี worked calculations จำนวนมาก; ตัวเลขและหน่วยต้องตรวจทีละข้อก่อนรับรอง",
    },
    "Final": {
        "scope": "Supplementary revision, screenshots, and practice questions",
        "chapters": ["chemical kinetics", "electrochemistry", "collision theory", "cell calculations"],
        "visuals": "หน้าปกตกแต่ง โน้ตกริด ภาพสไลด์ ภาพโจทย์ออนไลน์ และคำอธิบายเขียนมือ",
        "assessment": "มีโจทย์และเฉลยผสมหลายแหล่ง; ไม่ถือเป็นแหล่งยืนยันหลัก",
    },
}


def save_json(name: str, payload: object) -> None:
    (PROJECT / "data" / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    star_items = []
    for document in inventory["documents"]:
        doc_id = document["document_id"]
        document["analysis_summary"] = DOC_SUMMARIES[doc_id]
        starred = {row[0]: row for row in STARS.get(doc_id, [])}
        for page in document["pages"]:
            if document["role"] == "primary_instructor":
                row = starred.get(page["pdf_page"])
                if row:
                    _, printed, concept, confidence = row
                    page["printed_slide_number"] = printed
                    page["star_detection"] = {
                        "status": "CONFIRMED",
                        "confidence": confidence,
                        "associated_concept": concept,
                        "manual_review": False,
                    }
                    source_render = PROJECT / page["render_path"]
                    evidence_name = f"{doc_id}_pdf-page-{page['pdf_page']:03d}.jpg"
                    evidence_path = PROJECT / "evidence" / "stars" / evidence_name
                    shutil.copy2(source_render, evidence_path)
                    content_id = ("K" if "Part1" in doc_id else "E") + f"-P1-{page['pdf_page']:03d}"
                    star_items.append({
                        "content_id": content_id,
                        "topic": concept,
                        "subtopic": concept,
                        "source_document": document["file_name"],
                        "pdf_page": page["pdf_page"],
                        "printed_slide_number": printed,
                        "priority": "P1",
                        "evidence_classification": "CONFIRMED",
                        "confidence": confidence,
                        "evidence_path": str(evidence_path.relative_to(PROJECT)).replace("\\", "/"),
                        "related_formulas": [],
                        "related_examples": [],
                        "related_practice_questions": [],
                    })
                else:
                    page["star_detection"] = {
                        "status": "NOT_FOUND",
                        "confidence": "high",
                        "associated_concept": None,
                        "manual_review": False,
                    }
        document["inspection_status"] = "ALL_PAGES_VISUALLY_INSPECTED"
    INVENTORY_PATH.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")

    save_json("exam_priority.json", {"schema_version": 1, "definitions": {"P1": "Confirmed Instructor Star", "P2": "Directly Related Concept", "P3": "Required Foundation", "P4": "Supplementary Content", "REVIEW": "Uncertain Classification"}, "items": star_items})
    save_json("topics.json", {"schema_version": 1, "status": "phase_1_source_map", "topics": star_items})
    save_json("formulas.json", {"schema_version": 1, "status": "awaiting_phase_2_validation", "formulas": []})
    save_json("problems.json", {"schema_version": 1, "status": "awaiting_phase_2_validation", "problems": []})

    source_lines = [
        "# รายงานการวิเคราะห์เอกสารต้นฉบับ (Phase 1)", "",
        "สถานะ: ตรวจ inventory และภาพทุกหน้าครบแล้วสำหรับ PDF ทั้ง 6 ไฟล์ โดย Part1/Part2 ผ่านการตรวจดาวรายหน้า 300/300 หน้า", "",
        "## วิธีดำเนินการ", "",
        "- บันทึก SHA-256, จำนวนหน้า, ขนาดไฟล์ และข้อความที่ดึงได้รายหน้า",
        "- เรนเดอร์ทุกหน้าเป็นภาพ JPEG ที่ 110 dpi เพื่อดูสูตร ภาพ ตาราง และลายมือ",
        "- ตรวจ contact sheet ทุกหน้า และเปิดภาพเต็มของหน้าที่มีสี magenta หรือลักษณะคล้ายดาว",
        "- ใช้ภาพอ้างอิงใน workspace เป็นเกณฑ์รูปร่างและสี การคัดกรองสีใช้เพื่อหา candidate เท่านั้น",
        "- ไม่ถือข้อความที่ดึงได้หรือ OCR เป็นหลักฐานเพียงอย่างเดียว โดยเฉพาะโน้ตลายมือและสูตร", "",
        "## Inventory", "",
        "| เอกสาร | บทบาท | หน้า | ขอบเขต | เนื้อหาภาพ/ตาราง/ตัวอย่าง |",
        "|---|---:|---:|---|---|",
    ]
    for doc in inventory["documents"]:
        summary = doc["analysis_summary"]
        source_lines.append(f"| {doc['file_name']} | {doc['role']} | {doc['page_count']} | {summary['scope']} | {summary['visuals']} {summary['assessment']} |")
    source_lines += ["", "## ข้อสังเกตด้านการอ่านไฟล์", "", "- เอกสารผู้สอนมี text layer แต่ภาษาไทยบางส่วนถอดออกมาเป็นอักขระผิดเพี้ยน จึงใช้ภาพเรนเดอร์ประกอบการตีความหัวข้อ สูตร และเลขสไลด์", "- เอกสาร Chemical Kinetic.pdf และ Electrochemistry.pdf เป็นโน้ตแบบหน้าแนวตั้งยาว มีภาพและสูตรขนาดเล็ก", "- Final Phychem.pdf เป็นลายมือเกือบทั้งหมด และ Final.pdf ผสมลายมือ ภาพสไลด์ และภาพโจทย์ออนไลน์ จึงต้องตรวจสูตรและตัวเลขต่อใน Phase 2", "- ยังไม่รับรองความถูกต้องเชิงเคมีของตัวอย่างหรือคำตอบในเอกสารเสริมจนกว่าจะผ่าน Phase 2", "", "## ไฟล์หลักฐาน", "", "ภาพเรนเดอร์ทุกหน้าอยู่ใน `evidence/renders/` และ contact sheets อยู่ใน `evidence/contact_sheets/` รายการข้อความรายหน้าและ checksum อยู่ใน `data/document_inventory.json`."]
    (PROJECT / "reports" / "source_analysis.md").write_text("\n".join(source_lines), encoding="utf-8")

    star_lines = [
        "# รายงานการตรวจดาวของผู้สอน", "",
        "## สรุป", "",
        "- Part1 ตรวจครบ 167/167 หน้า พบ CONFIRMED 12 หน้า",
        "- Part2 ตรวจครบ 133/133 หน้า พบ CONFIRMED 8 หน้า",
        "- รวมตรวจ 300/300 หน้า พบ CONFIRMED 20 หน้า",
        "- ไม่มีหน้าที่จัดเป็น PROBABLE หรือ UNCERTAIN ในรอบนี้",
        "- ลูกศร เส้นใต้ วงกลม ไฮไลต์ ตัวเลขวงกลม และดาวสีเขียวไม่ถูกจัดเป็น P1 เว้นแต่มีดาวสีชมพู/ม่วงแดงรูปแบบเดียวกับภาพอ้างอิงอยู่ด้วย", "",
        "## เกณฑ์", "",
        "CONFIRMED หมายถึงเห็นเส้นหลายเส้นตัดกันเป็นรูป asterisk สีชมพู/ม่วงแดงอย่างชัดเจนจากภาพเรนเดอร์เต็มหน้า และสามารถเชื่อมกับหัวข้อใกล้เคียงได้โดยไม่กำกวม", "",
        "## รายการหลักฐาน", "",
        "| Content ID | เอกสาร | PDF page | Printed slide | หัวข้อที่สัมพันธ์ | สถานะ | ความมั่นใจ | หลักฐาน |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for item in star_items:
        star_lines.append(f"| {item['content_id']} | {item['source_document']} | {item['pdf_page']} | {item['printed_slide_number']} | {item['topic']} | CONFIRMED | {item['confidence']} | `{item['evidence_path']}` |")
    star_lines += ["", "## การตรวจหน้าที่เหลือ", "", "หน้าที่ไม่อยู่ในตารางนี้ได้รับสถานะ NOT_FOUND ใน `data/document_inventory.json` หลังตรวจภาพ contact sheet ทุกหน้า และตรวจภาพเต็มสำหรับ candidate ที่ระบบคัดกรองสีชี้ขึ้นมา", "", "## ข้อจำกัด", "", "การระบุความหมายของดาวอาศัยตำแหน่งใกล้หัวข้อ/สูตร/โจทย์บนสไลด์ หากผู้สอนตั้งใจให้ดาวครอบคลุมหลายสไลด์ต่อเนื่อง รายงานนี้จะไม่ขยายความหมายเกินหน้าที่เห็นหลักฐานโดยตรง"]
    (PROJECT / "reports" / "star_detection_report.md").write_text("\n".join(star_lines), encoding="utf-8")

    matrix = [
        "# Content Coverage Matrix (Phase 1)", "",
        "| Module | Primary source coverage | Supplementary support | P1 evidence | Phase 1 status |",
        "|---|---|---|---:|---|",
        "| K01 Reaction Rate | Part1 pp. 3-18, 93-96 | Chemical Kinetic; Final/Final Phychem | 1 | mapped |",
        "| K02 Rate Law | Part1 pp. 17-27 | Chemical Kinetic; Final | 2 | mapped |",
        "| K03 Integrated Rate Law | Part1 pp. 28-56 | Chemical Kinetic; Final Phychem | 4 | mapped |",
        "| K04 Half-Life | Part1 pp. 32-55, 99-112 | Chemical Kinetic; Final | 1 | mapped |",
        "| K05 Activation Energy | Part1 pp. 57-70, 132-166 | Chemical Kinetic; Final | 1 | mapped |",
        "| K06 Arrhenius Equation | Part1 pp. 64-70 | Chemical Kinetic; Final Phychem | 0 | mapped |",
        "| K07 Reaction Mechanism | Part1 pp. 71-85 | Chemical Kinetic; Final | 2 | mapped |",
        "| K08 Catalysis and solution encounter | Part1 pp. 86-92, 149-166 | Chemical Kinetic; Final | 2 | mapped |",
        "| E01 Electrolyte Solution | Part2 pp. 5-12 | Electrochemistry; Final | 0 | mapped |",
        "| E02 Dielectric Constant | Part2 pp. 17-22 | Electrochemistry | 1 | mapped |",
        "| E03 Electrical Conductance | Part2 pp. 13-50 | Electrochemistry; Final | 2 | mapped |",
        "| E04 Degree of Dissociation | Part2 pp. 43-48 | Electrochemistry; Final | 1 | mapped |",
        "| E05 Ionic Mobility | Part2 pp. 49-60 | Electrochemistry | 0 | mapped |",
        "| E06 Ionic Activity and Debye-Huckel | Part2 pp. 68-90 | Electrochemistry; Final Phychem | 2 | mapped |",
        "| E07 Electrochemical Cell | Part2 pp. 94-108 | Electrochemistry; Final | 2 | mapped |",
        "| E08 Cell Thermodynamics and Nernst | Part2 pp. 109-119 | Electrochemistry; Final Phychem | 0 | mapped |",
        "| E09 Electrodes and Concentration Cell | Part2 pp. 120-132 | Electrochemistry; Final | 0 | mapped |",
        "", "หมายเหตุ: ช่วงหน้าเป็น coverage ระดับเอกสาร ไม่ใช่การรับรองสูตรทุกบรรทัด การตรวจสูตรและ worked examples จะทำใน Phase 2.",
    ]
    (PROJECT / "reports" / "content_coverage_matrix.md").write_text("\n".join(matrix), encoding="utf-8")
    print(f"Created Phase 1 outputs with {len(star_items)} confirmed star pages")


if __name__ == "__main__":
    main()
