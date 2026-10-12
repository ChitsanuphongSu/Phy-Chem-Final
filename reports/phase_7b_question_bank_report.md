# Phase 7B — Question Bank Report

## 1. Executive Summary

ขยายคลังโจทย์แบบ additive จาก 11 เป็น 65 ข้อ โดยเพิ่ม 54 ข้อที่มีสถานะ `VALIDATED`. คง legacy records ทั้ง 11 รายการและ ID เดิมทั้งหมด พร้อมเพิ่ม deterministic grading, progressive hints, source traceability และ Instructor-Star Practice โดยไม่เปลี่ยน LocalStorage key หรือ UI theme.

## 2–4. Question Counts

- Original: 11
- New: 54
- Final active: 65

## 5. Difficulty Distribution

| Easy | Medium | Hard | Total |
|---:|---:|---:|---:|
| 20 | 29 | 16 | 65 |

## 6. Question Type Distribution

| Grading type | Count |
|---|---:|
| Numerical | 42 |
| Multiple choice | 17 |
| Conceptual short answer | 6 |

รูปแบบการเรียนรู้ใหม่ครอบคลุม numerical calculation, multi-step, data-table interpretation, energy-diagram interpretation, mechanism analysis, collision/encounter, graph interpretation และ cell notation.

## 7. Topic Coverage — New Questions

| Topic | Added |
|---|---:|
| E02 | 2 |
| E03 | 5 |
| E04 | 4 |
| E06 | 5 |
| E07 | 3 |
| E09 | 4 |
| E10 | 4 |
| K01 | 3 |
| K02 | 4 |
| K03 | 5 |
| K04 | 3 |
| K05 | 4 |
| K06 | 3 |
| K07 | 3 |
| K08 | 2 |

## 8. P1 Practice Coverage

P1 ทั้ง 20/20 มี direct validated new practice question อย่างน้อยหนึ่งข้อ. Practice gaps หลัง Phase 7B = 0. รายละเอียดอยู่ใน `phase_7b_p1_coverage.md`.

## 9. Chemistry Validation Results

- Numerical ใหม่ 32 ข้อถูกคำนวณซ้ำด้วย deterministic Python evaluator จาก `validation_spec`
- MCQ ใหม่ 17 ข้อมี option ID ไม่ซ้ำ 4 ตัวเลือก, correct option เดียว และ explanation ครบทุก distractor
- Conceptual ใหม่ 5 ข้อใช้ controlled accepted answers และหลักการจากหน้าต้นฉบับ
- แก้ draft ก่อนรับเข้า 2 ข้อ: P-K-026 (Arrhenius 1737 s^-1) และ P-E-022 (mean activity 0.005953 mol L^-1)
- ไม่มีคำถาม REJECTED หรือ REVIEW_REQUIRED ใน active bank
- AgBr เดิมคง correction 5.39×10^-8 S cm^-1 และ Ksp 1.97×10^-13; ข้อ adapted P-E-013 ใช้ชุดค่าใหม่ที่ internally consistent

## 10. Rejected or Revised Questions

| ID | Result | Reason |
|---|---|---|
| P-K-026 | Revised then VALIDATED | Draft answer ไม่ตรง independent Arrhenius recalculation |
| P-E-022 | Revised then VALIDATED | Draft mean ionic activity คำนวณ cube root ผิด |

ไม่มี rejected draft ถูกนำเข้า active database.

## 11. Grading Engine Changes

- ย้าย grading ไปที่ `web/src/grading.ts`
- Numerical รองรับ decimal, `e` notation และรูป `×10^n`; ใช้ absolute/relative tolerance
- MCQ ตรวจด้วย stable option ID ไม่อิงตำแหน่ง array
- Conceptual ใช้ controlled accepted-answer list แทน exact answer เดียว
- Mock Exam ใช้ grading engine เดียวกับ Practice และกรองเฉพาะ compatible active questions

## 12. Website Integration Changes

- กรองตาม topic, difficulty และ grading type
- เพิ่ม `⭐ Instructor-Star Practice` จาก verified P1 problem relationships
- แสดง hints ทีละ 3 ระดับ
- ไม่แสดง solution ก่อน submit
- แสดง related formulas, related P1 IDs, source classification และ source links
- รองรับ MCQ radio options และ distractor explanations

## 13. Automated Test Results

- `python tests/validate_project.py`: PASS
- `python tests/validate_phase7a.py`: PASS
- `python tests/validate_phase7b.py`: PASS
- `npm test`: PASS — 4 files, 19 tests
- `npm run build`: PASS; มีคำเตือน bundle chunk >500 kB แต่ไม่มี build error

ชุดทดสอบครอบคลุม counts, IDs, sources, P1, numerical recalculation, MCQ uniqueness, tolerance, conceptual synonyms, mock compatibility, PDF checksums, evidence และ progress storage.

## 14. Remaining Limitations

- Controlled short-answer grading ยอมรับเฉพาะคำตอบที่ระบุไว้ ไม่ใช่ semantic AI grading
- คำถามใหม่เป็น `ai-generated-from-source`; source reference สนับสนุน concept ไม่ได้หมายความว่าค่าตัวเลขปรากฏตรงในต้นฉบับ
- Focused browser smoke test ถูกลองกับ `localhost:5173/practice` แล้ว แต่ in-app browser ตอบ `ERR_CONNECTION_TIMED_OUT`; จึงไม่อ้างว่า browser E2E ผ่าน

## 15. Recommendations for Phase 7C

- เพิ่ม analytics แยก P1 mastery และ misconception tags
- เพิ่ม deterministic unit parser หากต้องการให้ผู้ใช้กรอกค่าพร้อมหน่วยในช่องเดียว
- เพิ่ม seeded mock-exam blueprint และ timer persistence โดยไม่เปลี่ยน attempt history เดิม
