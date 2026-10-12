# Phase 7D Analytics Audit

## Model 1.0 และปัญหาที่ทำซ้ำได้

เดิม recent performance นับทุก attempt ใน 14 วัน; fixture A ถูก 20 ครั้ง และ B/C/D ผิดครั้งละหนึ่ง ทำให้ recent = 87% ทั้งที่ unique latest = 25%. `validAttempts.slice(-20)` ใช้ insertion order และ MCQ ผิดครั้งเดียวถูกจัดข้อความเชิงยืนยันมากเกินไป. หนึ่งข้อ easy ถูกให้ provisional raw estimate สูงและแสดงเป็น readiness number

## Model 2.0

- Recent performance ใช้ latest qualifying attempt ต่อ unique Problem ID เท่านั้น
- วันที่ invalid/future ไม่ร่วม recency; chronology sort ด้วย timestamp และ deterministic tie-break โดยไม่ mutate raw array
- Duplicate `attemptId` ถูกนับหนึ่งครั้งใน derived analytics แต่ไม่ลบ raw history
- Readiness แสดง `INSUFFICIENT_EVIDENCE` จนมีอย่างน้อย 3 unique questions และ 2 topics หรือ completed mock; raw calculation เก็บเป็น `provisionalScore` แต่ไม่แสดงเป็นข้อสรุป
- P1 relationships deduplicate ก่อน mastery; aggregate เฉลี่ยราย P1 และ confidence/completeness แยกต่างหาก
- MCQ ผิดหนึ่งครั้ง = POSSIBLE; distractor เดิมอย่างน้อยสองครั้ง = REPEATED_PATTERN; numerical/conceptual ที่ไม่มีกฎ validated = POSSIBLE; legacy no raw answer ไม่สร้างข้อสรุป

ผลตัวอย่างก่อน/หลัง: repeated fixture recent 87% → 25%; one easy correct readiness numeric → `INSUFFICIENT_EVIDENCE`. เพิ่ม regression 10 cases สำหรับ inflation, order independence, invalid/future dates, duplicate IDs, sparse evidence และ misconception patterns. ข้อจำกัด: timestamp เท่ากันหรือหายทำให้ chronology เชิงเวลาพิสูจน์ไม่ได้ จึงใช้ stable metadata ordering เฉพาะเพื่อ determinism ไม่อ้างลำดับจริง
