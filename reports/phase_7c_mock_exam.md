# Phase 7C Mock Exam

- Blueprint `practice-v1`: default 10 ข้อ, Kinetics 50%, difficulty 30/45/25%, verified-P1 minimum 50%, 30 นาที เป็น Practice Mock Exam Blueprint ไม่ใช่ blueprint จริงของผู้สอน
- ใช้ FNV-style string hash + Mulberry32 PRNG; seed + blueprint version + question-bank version `65-v1` ให้ลำดับเดิมเสมอ และ sort stable IDs ก่อนสุ่ม
- Selection ให้ P1/difficulty/section ก่อน แล้วเติมจาก compatible pool โดยไม่ duplicate; `fallbackUsed` รายงานเมื่อข้อจำกัดเติมไม่ได้
- Session เก็บ seed, versions, stable IDs, started/deadline/submitted timestamps, answers, status, elapsed time และ grading summary ใน LocalStorage key เดิม
- Timer คำนวณจาก persisted `deadlineAt`; refresh/navigation/browser restart จึงกู้ active session ได้ เมื่อหมดเวลา auto-submit และล็อกคำตอบ
- Submission ตรวจ persisted status ก่อนบันทึก จึง idempotent และใช้ central `gradeProblem`; solutions แสดงหลัง submit เท่านั้น
- Review แสดง correct/incorrect/unanswered, topic, difficulty, P1 และรายการทบทวน

ข้อจำกัด: client-side clock/storage ไม่ใช่ tamper-proof exam security; invalid stored sessions ถูก normalization ขั้นต้น แต่ไม่มี server-side recovery. ชุดทดสอบ mock 20 cases ครอบคลุม seed, counts, invalid blueprints, deadline, grading และ idempotency
