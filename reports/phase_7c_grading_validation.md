# Phase 7C Unit-Aware Grading Validation

Parser deterministic รองรับ decimal, e notation, `×10^n`, numeric-only legacy answer และหน่วยควบคุม: s/min/h, M/mol L^-1, J/kJ, J mol^-1/kJ mol^-1, V/mV, S cm^-1/S m^-1, S cm² mol^-1/S m² mol^-1, s^-1, M^-1 s^-1, M^-2 s^-1 และ M s^-1

การแปลงทำเฉพาะ dimension เดียวกัน แล้วจึงใช้ absolute/relative tolerance เดิม สถานะ parser คือ INVALID_NUMBER, UNKNOWN_UNIT, INCOMPATIBLE_UNIT, VALID_NUMERIC_ANSWER ตัวอย่างรับ: `1e-3 M`, `1 × 10^-3 M`, `1000 mV` เมื่อโจทย์ใช้ V; ตัวอย่างปฏิเสธ: `1 banana`, V สำหรับคำตอบ M, non-numeric input

Vitest grading 25 cases ผ่านทั้งหมด รวม conversion, malformed input, negative/zero, legacy numeric answer, MCQ stable option และ controlled conceptual synonyms ไม่ได้เปลี่ยน correct answer/tolerance ใน question bank

ข้อจำกัด: ไม่ใช่ symbolic algebra engine; ไม่ตีความหน่วยนอก allow-list และไม่ใช้ `eval()`
