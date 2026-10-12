# Phase 7B — Question Bank Readiness Plan

เอกสารนี้เป็นแผนเท่านั้น ไม่มีการสร้างคำถามใหม่ใน Phase 7A และไม่กล่าวอ้างว่าคำถามที่เสนอจะปรากฏในข้อสอบจริง

## Baseline

คลังปัจจุบันมี 11 ข้อ:

- Easy 3 (27.3%)
- Medium 6 (54.5%)
- Hard 2 (18.2%)
- Numerical 10; Conceptual 1; Multiple-choice 0

เป้าหมายแนะนำ: 65 ข้อ รวมเพิ่ม 54 ข้อ โดยจำนวนสุดท้ายประมาณ Easy 20 (30.8%), Medium 29 (44.6%), Hard 16 (24.6%). ข้อใหม่ควรเป็น Easy 17, Medium 23, Hard 14

## Priority gaps

- ไม่มี problem: K-P1-049, K-P1-061, K-P1-074, K-P1-077, K-P1-162, E-P1-018, E-P1-089
- มี numerical support แต่ขาด conceptual: E-P1-013, E-P1-095
- มีเพียง easy problem ใน P1 context: K-P1-040/K04, K-P1-094/K01, E-P1-095/E09
- ต้องเพิ่ม multi-step: second-order kinetics, Arrhenius/energy profile, AgBr conductivity→solubility→Ksp, ionic activity, Ecell→ΔG°→K/Nernst

## Proposed categories (54 new questions)

| Topic | Related P1 | Learning objective | Type | Difficulty mix E/M/H | Needed | Related formulas | Source reference |
|---|---|---|---|---:|---:|---|---|
| K01 | K-P1-094 | เชื่อมอัตราด้วย stoichiometric coefficients และเครื่องหมาย | conceptual + numerical | 1/1/1 | 3 | F-K-001 | Part1 pp.8,94 |
| K02 | K-P1-021, K-P1-026 | หา order และ k จาก initial-rate table รวมกรณีข้อมูลไม่สมบูรณ์ | MCQ + numerical | 1/2/1 | 4 | F-K-002 | Part1 pp.21,26 |
| K03 | K-P1-035, K-P1-042, K-P1-049 | เลือก linear form และแก้ first/second-order แบบหลายขั้น | conceptual + numerical | 1/2/2 | 5 | F-K-003–F-K-005 | Part1 pp.35,42,49 |
| K04 | K-P1-040 | เปรียบเทียบ dependency ของ half-life กับ [A]0 | MCQ + numerical | 1/1/1 | 3 | F-K-006–F-K-008 | Part1 p.40 |
| K05 | K-P1-061 | อ่าน Ea forward/reverse และ ΔH จาก energy diagram | diagram-concept + numerical | 1/2/1 | 4 | F-K-009 (supporting) | Part1 p.61 |
| K06 | K-P1-091 | คำนวณ/ตีความผล T ต่อ k และตรวจหน่วย J↔kJ | conceptual + numerical | 1/1/1 | 3 | F-K-009, F-K-010 | Part1 p.91 |
| K07 | K-P1-074, K-P1-077 | หา intermediate, RDS และตรวจ consistency ของ mechanism | MCQ + conceptual | 2/1/0 | 3 | N/A | Part1 pp.74,77 |
| K08 | K-P1-162 | เปรียบเทียบ gas collision กับ solution encounter | MCQ + conceptual | 1/1/0 | 2 | N/A | Part1 p.162 |
| E02 | E-P1-018 | อธิบาย εr กับแรงระหว่างประจุและแนวโน้มเมื่อ T เปลี่ยน | MCQ + conceptual | 1/1/0 | 2 | N/A | Part2 p.18 |
| E03 | E-P1-013, E-P1-066 | แยก G/κ/Λm/หน่วย และแก้ solubility/Ksp จาก conductivity | conceptual + multi-step | 1/2/2 | 5 | F-E-001, F-E-002, F-E-005 | Part2 pp.13,66 |
| E04 | E-P1-048 | คำนวณ Λm, α, Ka พร้อมเลือก condition ของ Ostwald | conceptual + numerical | 1/2/1 | 4 | F-E-002–F-E-004 | Part2 p.48 |
| E06 | E-P1-083 | คำนวณ I, γ±, activity และตรวจข้อจำกัด DHLL | conceptual + multi-step | 1/2/2 | 5 | F-E-006–F-E-008 | Part2 p.83 |
| E07 | E-P1-089 | แยก salting-in/out ตามช่วง ionic strength | MCQ + conceptual | 2/1/0 | 3 | F-E-006, F-E-007 (supporting) | Part2 p.89 |
| E09 | E-P1-095, E-P1-108 | ระบุ anode/cathode, เขียน notation และคำนวณ Ecell | conceptual + numerical | 1/2/1 | 4 | F-E-009 | Part2 pp.95,108 |
| E10 | E-P1-108 | เชื่อม E°, ΔG°, K, Q และ Nernst แบบหลายขั้น | numerical + multi-step | 1/2/1 | 4 | F-E-010–F-E-012 | Part2 pp.108–119 |
| **รวม** |  |  |  | **17/23/14** | **54** |  |  |

## Authoring and QA requirements for Phase 7B

- แยก source-derived/adapted/generated อย่างชัดเจน
- Generated questions ต้องไม่ถูกเรียกว่า past exam questions
- ทุก numerical answer ต้องมี tolerance และ unit policy ที่ระบุได้
- ตรวจ dimensional consistency, significant figures และ step-by-step solution
- AgBr items ต้องใช้ corrected conductivity `5.39×10^-8 S cm^-1` และแสดง source correction note
- ทุก P1 record ควรมีอย่างน้อยหนึ่ง retrieval-practice item; calculation-focused P1 ควรมีอย่างน้อย Medium หนึ่งข้อ
- ใช้หลาย question types เพื่อแก้ baseline ที่เอนเอียงไปทาง numerical
