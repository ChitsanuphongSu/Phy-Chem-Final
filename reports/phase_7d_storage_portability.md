# Phase 7D Storage & Progress Portability

Export เป็น JSON เฉพาะ user progress: format `phychem-progress-backup`, version 1, timestamp, storage key, payload และ SHA-256 ของ canonical serialization. Checksum ตรวจ accidental corruption ไม่ใช่ authentication และไฟล์ไม่รวม PDF/question/formula/evidence/slides

Import จำกัด 2 MB, parse JSON แบบไม่ execute, ปฏิเสธ prototype-pollution keys, ตรวจ format/version/checksum/schema, known Problem IDs, mock status/timestamps/question IDs และ duplicate session IDs จากนั้นแสดง preview และใช้ policy `REPLACE_WITH_CONFIRMED_BACKUP` หลัง explicit confirmation เท่านั้น

ก่อนเขียนเก็บ raw current state ที่ `phychem-study-v1-import-rollback`; หาก write/verification ล้มเหลว restore ค่าเดิม ไม่มี partial merge และ unknown legacy fields ถูก preserve. Vitest portability 16 cases ครอบคลุม round trip, corruption, size, version, checksum, invalid references/session, rollback และ unknown fields
