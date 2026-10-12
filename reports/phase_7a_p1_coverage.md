# Phase 7A — P1 Traceability & Coverage

## 1. Executive Summary

ตรวจครบ 20 confirmed instructor-star records: Chemical Kinetics 12 และ Electrochemistry 8. ทุก record เชื่อมกับ canonical topic/lesson แล้ว และทุกความสัมพันธ์ที่บันทึก resolve ไปยังข้อมูลจริงได้

- COMPLETE: 11
- PARTIAL: 9
- MISSING: 0
- REVIEW_REQUIRED: 0
- P1 ที่มี practice problem อย่างน้อยหนึ่งข้อ: 13/20 (ในจำนวนนี้ 2 รายการเป็น supporting problem ที่ยังไม่ครอบคลุม conceptual objective ทั้งหมด)
- P1 ที่ยังเป็น practice gap หรือ conceptual-practice gap: 9/20

`COMPLETE` ประเมินจาก learning objective โดยรวม ไม่ได้ตัดสินจากการมีสูตรเพียงอย่างเดียว; conceptual topic สามารถไม่มีสูตรได้อย่างถูกต้อง แต่หากไม่มี retrieval practice จะจัดเป็น `PARTIAL`.

## 2. Data Integrity Findings

พบและแก้เฉพาะ topic reference ของ `F-E-006`–`F-E-008` จาก E07 เป็น E06. ไม่เปลี่ยน ID หรือ chemistry content. ไม่พบ dangling reference ใน mapping ใหม่ รายละเอียดเต็มอยู่ใน `phase_7a_data_integrity.md`.

## 3. Topic ID Audit

`topics.json` และ lesson data ปัจจุบันกำหนด:

- E06 = Ionic Activity และ Ionic Strength
- E07 = Salting-in และ Salting-out
- E09 = Electrochemical Cell
- E10 = Cell Thermodynamics และ Nernst Equation
- E11 = Electrodes และ Concentration Cell

ดังนั้น `F-E-009`–`F-E-013` ถูกต้องแล้ว. Coverage matrix รุ่นก่อนเป็นเอกสารประวัติ ไม่ใช่ registry ปัจจุบัน

## 4. P1 Traceability Matrix

| Content ID | Topic | PDF page | Canonical topic | Lesson | Related formulas | Related problems | Status | Gap reason |
|---|---|---:|---|---|---|---|---|---|
| K-P1-021 | Initial-rate data | 21 | K02 | K02 | F-K-002 | P-K-002 | COMPLETE | — |
| K-P1-026 | S2O8²⁻/I⁻ rate law | 26 | K02 | K02 | F-K-002 | P-K-002 | COMPLETE | — |
| K-P1-035 | First-order integration | 35 | K03 | K03 | F-K-004 | P-K-003 | COMPLETE | — |
| K-P1-040 | First-order graph/half-life | 40 | K04 | K04, K03 | F-K-007, F-K-004 | P-K-004 | COMPLETE | — |
| K-P1-042 | N2O5 first-order problem | 42 | K03 | K03 | F-K-004 | P-K-003 | COMPLETE | — |
| K-P1-049 | Second-order integration | 49 | K03 | K03 | F-K-005 | — | PARTIAL | PRACTICE_GAP; WORKED_EXAMPLE_GAP |
| K-P1-061 | Reaction coordinate/Ea | 61 | K05 | K05 | F-K-009 (supporting) | — | PARTIAL | PRACTICE_GAP |
| K-P1-074 | Reaction intermediate | 74 | K07 | K07 | N/A | — | PARTIAL | PRACTICE_GAP |
| K-P1-077 | RDS/eliminate intermediate | 77 | K07 | K07 | N/A | — | PARTIAL | PRACTICE_GAP |
| K-P1-091 | Temperature effect on k | 91 | K06 | K06, K05 | F-K-009, F-K-010 | P-K-005 | COMPLETE | — |
| K-P1-094 | Stoichiometric rate | 94 | K01 | K01 | F-K-001 | P-K-001 | COMPLETE | — |
| K-P1-162 | Collision vs encounter | 162 | K08 | K08 | N/A | — | PARTIAL | PRACTICE_GAP |
| E-P1-013 | Electrical terms/units | 13 | E03 | E03 | F-E-001, F-E-002 | P-E-001 (supporting) | PARTIAL | CONCEPTUAL_PRACTICE_GAP |
| E-P1-018 | Dielectric constant vs T | 18 | E02 | E02 | N/A | — | PARTIAL | PRACTICE_GAP |
| E-P1-048 | κ, Λm, α, Ka | 48 | E04 | E04, E03 | F-E-002, F-E-003, F-E-004 | P-E-001 | COMPLETE | — |
| E-P1-066 | AgBr solubility/Ksp | 66 | E03 | E03 | F-E-005 | P-E-002 | COMPLETE | ใช้ค่าที่แก้ arithmetic error แล้ว |
| E-P1-083 | Ionic strength/DHLL | 83 | E06 | E06 | F-E-006, F-E-007 | P-E-003 | COMPLETE | — |
| E-P1-089 | Salting-in/out | 89 | E07 | E07, E06 | F-E-006, F-E-007 (supporting) | — | PARTIAL | PRACTICE_GAP |
| E-P1-095 | Galvanic cell/notation | 95 | E09 | E09 | F-E-009 (supporting) | P-E-004 (supporting) | PARTIAL | CONCEPTUAL_PRACTICE_GAP |
| E-P1-108 | Ecell, ΔG°, K | 108 | E09 | E09, E10 | F-E-009, F-E-010, F-E-012 | P-E-004, P-E-005, P-E-006 | COMPLETE | — |

## 5. Formula Coverage

- มี verified formula relationship: 16/20 P1 records
- Formula NOT_APPLICABLE อย่างสมเหตุผล: K-P1-074, K-P1-077, K-P1-162, E-P1-018
- ไม่มีกรณีที่บังคับสร้างสูตรใหม่เพื่อให้ coverage ดูครบ
- K-P1-061 และ E-P1-095 ใช้สูตรแบบ SUPPORTING เพราะหัวข้อดาวเน้น diagram/notation มากกว่าการคำนวณเพียงอย่างเดียว

## 6. Lesson Coverage

ครบ 20/20 โดยระบบปัจจุบันใช้ Topic เป็น lesson unit. ไม่มี `LESSON_GAP`. การอ้าง worked example ใช้ฟิลด์จริงของ lesson; K-P1-049 ยังขาด worked example อันดับสองที่ตรงวัตถุประสงค์

## 7. Practice Problem Coverage

- มีโจทย์สัมพันธ์อย่างน้อยหนึ่งข้อ: 13/20
- ไม่มีโจทย์: K-P1-049, K-P1-061, K-P1-074, K-P1-077, K-P1-162, E-P1-018, E-P1-089
- มีโจทย์คำนวณแต่ขาด conceptual coverage: E-P1-013, E-P1-095
- Calculation-focused P1 ที่ไม่มีโจทย์และควรเร่ง: K-P1-049, K-P1-061

## 8. Conceptual Topic Coverage

K-P1-074, K-P1-077, K-P1-162 และ E-P1-018 ไม่จำเป็นต้องมี dedicated formula. การไม่มีสูตรจึงเป็น `NOT_APPLICABLE` ไม่ใช่ missing content. อย่างไรก็ตามทุกหัวข้อยังควรมี active-recall/practice item ใน Phase 7B

## 9. Missing Content

- Worked example อันดับสองสำหรับ K-P1-049
- Practice coverage สำหรับ 7 P1 records ที่ไม่มีโจทย์
- Conceptual questions สำหรับ electrical units และ cell notation
- Question diversity: คลังปัจจุบันเกือบทั้งหมดเป็น numerical และมี conceptual เพียง 1 ข้อ

## 10. Review Required Items

ไม่มี mapping ใดอยู่ในสถานะ `REVIEW_REQUIRED` หลังตรวจ source metadata, evidence และ chemistry meaning. แต่ E-P1-066 ต้องคง correction note เสมอเพื่อไม่ให้ arithmetic error ในต้นฉบับกลับเข้าสู่ระบบ

## 11. Recommended Phase 7B Priorities

1. เติม second-order kinetics และ activation-energy problems
2. เติม conceptual mechanism/encounter/dielectric/salting/cell-notation questions
3. เพิ่ม multi-step electrochemistry โดยคง correction note ของ AgBr
4. เพิ่มโจทย์ตามแผน 54 ข้อเพื่อให้รวมประมาณ 65 ข้อ โดยไม่อ้างว่าเป็นข้อสอบจริง
