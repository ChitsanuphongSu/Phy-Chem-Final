# Phase 7C Learning Analytics

## แหล่งข้อมูลและหลักการ

ใช้เฉพาะ graded attempts ที่อ้างถึง Problem ID ที่มีอยู่จริง ไม่ใช้การเปิดบทเรียน/สูตร/หน้าเว็บเป็นหลักฐาน mastery และไม่ถือ missing data เป็นคำตอบผิด ข้อมูล derived คำนวณใหม่ได้เสมอจาก raw attempts

## Mastery model

- น้ำหนัก difficulty: easy 1.00, medium 1.25, hard 1.50
- ต่อคำถามใช้ทั้ง first attempt และ latest attempt เพื่อไม่ให้การทำข้อเดิมซ้ำสร้าง mastery เทียม
- คะแนน = first 15% + latest 60% + unique-question coverage 10% + recent 14-day performance 15%; หากไม่มี recent evidence ใช้ latest แทนมิตินี้
- สถานะ: NOT_STARTED, INSUFFICIENT_EVIDENCE, DEVELOPING (<45), PROGRESSING (<65), STRONG (<82), MASTERED (>=82 และอย่างน้อย 5 คำถามไม่ซ้ำ/2 difficulty bands)
- Confidence แยกจากคะแนน: INSUFFICIENT, LOW, MODERATE, HIGH

P1 mastery ใช้เฉพาะ `related_problem_ids` ที่ยืนยันใน `p1_traceability.json`; ภายใน P1 เดียวกัน deduplicate ด้วย Problem ID ส่วน aggregate readiness เฉลี่ยราย P1 จึงไม่สร้าง attempt ใหม่หรือแก้ raw history

## Readiness model

P1 35%, topic 25%, unique coverage 15%, recent 10%, mock 15%. มิติที่ไม่มีหลักฐานถูกตัดออกและ normalize น้ำหนักเฉพาะมิติที่มี ไม่แทนด้วยศูนย์ UI ระบุชัดว่าเป็น practice-based readiness indicator ไม่ใช่โอกาสสอบผ่าน

## Weak topics, misconceptions, recommendations

Weak-topic แยก NOT_STUDIED, INSUFFICIENT_EVIDENCE, STRUGGLING, IMPROVING, STRONG. Misconception ยืนยันได้เมื่อ future attempt มี raw response และตรง deterministic distractor pattern; legacy correctness-only = INSUFFICIENT_EVIDENCE. Recommendation เรียง RETRY_INCORRECT, unattempted verified P1, weak topic, increased difficulty, maintenance และแสดงเหตุผล

## Validation and limitations

`analytics.test.ts` มี 21 cases ครอบคลุม empty, repetition, improvement/decline, recency, difficulty diversity, invalid IDs, confidence และ recommendations. โมเดลนี้ explainable heuristic ยังไม่ผ่าน psychometric validation; historical attempts ไม่มี raw answer/hint/time จึงไม่ถูกเติมย้อนหลัง
