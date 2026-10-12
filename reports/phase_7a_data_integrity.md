# Phase 7A — Data Integrity Audit

วันที่ตรวจ: 12 ตุลาคม 2026  
ขอบเขต: data architecture, referential integrity, P1 traceability, chemistry relationships และ backward compatibility

## Executive summary

- ตรวจ registry ปัจจุบันครบ 18 topics/lessons, 23 formulas, 11 problems และ 20 confirmed P1 records
- ไม่พบ duplicate ID, dangling reference, source page นอกช่วง หรือ evidence path สูญหาย
- พบ foreign-key ผิดจริง 3 รายการ: `F-E-006`, `F-E-007`, `F-E-008` ชี้ `E07` ทั้งที่ canonical registry กำหนด Ionic Activity/Ionic Strength เป็น `E06`; แก้เฉพาะ `topic_id` โดยคง Formula ID และเนื้อหาเคมีเดิม
- `F-E-009` ถึง `F-E-013` ถูกต้องตาม registry ปัจจุบัน จึงไม่เปลี่ยน แม้รายงาน coverage รุ่นก่อนใช้เลขหัวข้อเก่า
- เพิ่ม `data/p1_traceability.json` เป็นโมเดล many-to-many แบบ additive โดยไม่เปลี่ยน schema เดิมของ `exam_priority.json`
- ไม่ต้องทำ progress migration เพราะ Topic ID, Formula ID, Problem ID, `progress_key` และ storage key `phychem-study-v1` ไม่เปลี่ยน

## วิธีตรวจสอบ

อ่านและเปรียบเทียบ `topics.json`, `formulas.json`, `problems.json`, `exam_priority.json`, lesson content, TypeScript types, routes, storage implementation, reports เดิม และ document inventory จากนั้นตรวจด้วย:

- `python tests/validate_project.py`
- `python tests/validate_phase7a.py`
- `npm test`
- `npm run build`

พยายามทำ focused browser smoke test กับ Vite dev server ที่ `localhost:5173` แล้ว แต่ in-app browser ตอบ `ERR_CONNECTION_TIMED_OUT` และ Edge surface ไม่พร้อมใช้งาน จึงไม่กล่าวอ้างว่า browser E2E ผ่าน

## Findings

| ระดับ | Finding | การดำเนินการ |
|---|---|---|
| HIGH | `F-E-006`, `F-E-007`, `F-E-008` มี `topic_id=E07` ขัดกับ `topics.json` และ `formula_ids` ของ E06 | แก้เป็น `E06` ทั้ง canonical data และ web data copy; ไม่เปลี่ยน Formula ID |
| MEDIUM | `content_coverage_matrix.md` ใช้เลขหัวข้อ Electrochemistry รุ่นก่อน เช่น E07/E08/E09 | เก็บรายงานเดิมไว้เป็นหลักฐานประวัติ และบันทึกว่า `topics.json` ปัจจุบันเป็น authority |
| MEDIUM | P1 records มี relationship arrays ว่างทั้งหมด | เพิ่มไฟล์ traceability แยกเพื่อไม่เปลี่ยนชนิดข้อมูล/consumer เดิม |
| LOW | ไม่มี Lesson และ WorkedExample registry แยกต่างหาก | อ้าง Lesson ด้วย Topic ID เดิม และอ้างตัวอย่างด้วย `{lesson_id, field: "worked_example"}`; ไม่สร้าง ID เทียม |
| LOW | คลังโจทย์มีเพียง 11 ข้อและครอบคลุม P1 ไม่ครบ | บันทึก gap และวางแผน Phase 7B เท่านั้น; ไม่สร้างโจทย์ใน Phase 7A |

## Schema and ID audit

ระบบปัจจุบันใช้ `Topic` เป็นทั้ง topic registry และ lesson unit; `progress_key` อยู่ในรูป `topic:<TopicID>`. Formula/Problem อ้าง Topic ด้วย `topic_id`; Topic และ Problem อ้าง Formula ด้วย string ID. P1 เป็น registry อิสระที่อ้างหลักฐานหน้า PDF.

Canonical topic IDs ปัจจุบันคือ:

- Kinetics: K01–K08
- Electrochemistry: E01–E07, E09–E11

การไม่มี E08 และ E12 เป็นช่องว่างเชิงเลขที่มีอยู่เดิม ไม่ใช่หลักฐานว่า ID อื่นผิด และไม่ควร renumber เพราะจะกระทบ progress/bookmark โดยไม่จำเป็น

## Referential integrity results

- Topic IDs: unique 18/18
- Formula IDs: unique 23/23; ทุก `topic_id` resolve ได้
- Problem IDs: unique 11/11; ทุก `topic_id` และ related formula resolve ได้
- P1 IDs: unique 20/20; distribution K=12, E=8
- Traceability: 20/20 P1 IDs มี mapping; ไม่มี duplicate relationship และ target ทุกตัว resolve ได้
- Source references: document name ถูกต้องและ PDF page อยู่ในช่วง page count
- Evidence: P1 evidence 20/20 path มีไฟล์จริง
- Enum values: priority/difficulty/evidence/coverage statuses อยู่ในชุดที่อนุญาต

## Chemistry preservation

สูตรและคำตอบเดิมไม่ถูกแก้ ยกเว้น metadata `topic_id` ของสามสูตร Ionic Activity/Ionic Strength. ค่า AgBr ที่ผ่านการตรวจยังเป็น:

- corrected conductivity = `5.39×10^-8 S cm^-1`
- Λ°(AgBr) = `121.5 S cm² mol^-1`
- solubility = `4.44×10^-7 M`
- Ksp = `1.97×10^-13`

ข้อความเตือนว่าต้นฉบับเขียนผลลบผิดเป็น `7.39×10^-8` ยังคงอยู่ และ original PDF ไม่ถูกแก้

## Backward compatibility

- LocalStorage key ยังคงเป็น `phychem-study-v1`
- Topic, Formula, Problem และ P1 IDs ไม่เปลี่ยน
- `progress_key` ทั้ง 18 ค่าไม่เปลี่ยน
- ไม่มี migration เพราะไม่มี persisted identifier ใดเปลี่ยน
- เพิ่ม automated test ที่โหลด progress v1 เดิมและยืนยัน completed lessons, bookmarks, attempts, flashcards และ theme ไม่ถูก reset

## Data preservation

ก่อนแก้ข้อมูลได้สำรองไฟล์ใน `backups/phase-7a/` และตรวจ SHA-256/size เทียบสำเนาแล้ว ตัวตรวจ Phase 7A ยังตรวจ checksum ของ original PDFs ทั้งหกกับ `document_inventory.json`; ทุกไฟล์ตรงกัน ไม่มี PDF หรือ evidence ถูกแก้/ลบ

## Remaining risks

- Historical coverage matrix ยังใช้ topic numbering รุ่นเก่า; การแก้รายงานเดิมจะลด traceability จึงเลือกไม่ overwrite
- Browser automation เข้าถึง local dev server ไม่ได้; coverage จำกัดที่ TypeScript build, unit/data integrity tests และ static artifact validation
- Question bank coverage ยังต่ำ; รายละเอียดอยู่ใน `phase_7b_question_bank_plan.md`
