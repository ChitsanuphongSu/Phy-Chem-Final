# Phase 7C Data Integrity

- Final counts: topics 18, formulas 23, active problems 65, confirmed P1 20 (Kinetics 12 / Electrochemistry 8)
- Difficulty คงเดิม: easy 20, medium 29, hard 16
- SHA-256 ของ topics, formulas, problems, exam priority และ P1 traceability ตรง baseline ทุกไฟล์ จึงยืนยันว่า IDs, answers, difficulty และ source classification ไม่เปลี่ยน
- `validate_project.py`, `validate_phase7a.py`, `validate_phase7b.py`, `validate_phase7c.py` ผ่าน; validators เดิมยืนยัน PDF checksums และ evidence preservation
- Backup manifest `backups/phase-7c/backup_manifest.json` มี 11 ไฟล์และ backup checksum verification ผ่าน
- LocalStorage key คง `phychem-study-v1`; schema v2 เพิ่ม optional attempt metadata และ mock sessions แบบ additive, normalize legacy/malformed input, preserve unknown fields และไม่ลบ storage เมื่อ save/quota error
- bookmarks, completed lessons, attempts, flashcards และ theme fields เดิมคงความหมายเดิม ไม่มี destructive migration

Browser E2E ไม่ได้รันสำเร็จใน environment นี้ จึงไม่อ้างว่าผ่าน; ใช้ TypeScript build, Vitest และ deterministic Python integrity tests เป็นหลักฐานอัตโนมัติ
