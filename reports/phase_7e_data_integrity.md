# Phase 7E Data Integrity

SHA-256 ของ `topics.json`, `formulas.json`, `problems.json`, `exam_priority.json` และ `p1_traceability.json` ตรงกับ protected baseline. จำนวนคงเดิม: topics 18, formulas 23, problems 65, P1 20 (K 12/E 8). `phychem-study-v1` คงเดิม ไม่มี migration และ tests ยืนยัน legacy progress อยู่ร่วมกับ schema ปัจจุบัน.

backup manifests ทุกชุด Phase 7E ตรวจสำเนากับ checksum ผ่าน. PDF ต้นฉบับและ star evidence ไม่อยู่ในรายการไฟล์แก้ไข; validators เดิมยืนยัน inventory 6 เอกสารและ instructor pages 300 หน้า. ไม่มีการเปลี่ยนสูตร คำตอบ chemistry, source reference, P1 mapping หรือ ID.

การเปลี่ยน source มีเพียง QA config/tests, accessible label, light-mode contrast token, favicon และเอกสาร. Favicon แก้ production console 404 โดยไม่กระทบข้อมูลหรือ behavior การเรียน.

Vitest config exclude `e2e/**` เพื่อแยก unit runner จาก Playwright runner โดยไม่เปลี่ยน application runtime หรือ test assertions เดิม.
