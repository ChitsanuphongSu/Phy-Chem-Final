# Phase 7E Browser E2E

Playwright บน system Chrome ผ่าน 24/24 tests. ชุดทดสอบใช้ fresh context, deterministic seed และ LocalStorage จริง ครอบคลุม:

- A: ผู้ใช้ใหม่เรียนบท, ทำโจทย์ และ progress อยู่หลัง reload
- B: Instructor-Star Practice แสดง P1 verified และอัปเดต analytics
- C: Smart Practice แสดงเหตุผล เคารพ filter และบันทึก source
- D: seeded mock ให้ชุดเดิม, เก็บคำตอบ/deadline, reload แล้วทำต่อ และ submit ได้
- E: expired mock auto-submit เพียงครั้งเดียวและล็อกคำตอบ
- F/G/H: export, valid import พร้อม preview/confirmation และ invalid JSON/checksum ไม่แก้ข้อมูล
- I: dark theme และ route คงอยู่หลัง reload โดยไม่มี console error
- J: legacy progress normalize และอยู่ร่วมกับ attempt ใหม่
- production smoke: ทั้ง 7 routes render จาก Vite preview โดยไม่มี console error หรือ failed response
- offline: session ที่โหลด asset แล้วใช้งานต่อได้; first visit offline ถูกยืนยันว่าไม่รองรับ

ไฟล์: `web/e2e/*.spec.ts`, config: `web/playwright.config.ts` และ `web/playwright.preview.config.ts`. ผล production preview แยกผ่าน 1/1. ไม่มีการอ้างผล manual browser interaction หรือ browser อื่นนอก Chrome.
