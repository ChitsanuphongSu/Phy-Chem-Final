# Phase 7D Baseline

วันที่ตรวจ 12 ตุลาคม 2026

| รายการ | สถานะ | หลักฐาน |
|---|---|---|
| 18 topics, 23 formulas, 65 problems, 20 P1 | VERIFIED | Python validators และ JSON inventory |
| Phase 7A–7C integrity | VERIFIED | validators ทั้ง 4 scripts ผ่านก่อนแก้ |
| Vitest 90/90 | VERIFIED | รันจริงก่อนแก้ 6 files |
| TypeScript/Vite build | VERIFIED | production build ผ่าน |
| Largest initial JS 491.21 kB | VERIFIED | Vite build output |
| Browser E2E | NOT_TESTED ณ baseline | ไม่มี Playwright package/browser CLI; previous localhost blocker |
| Accessibility tooling | NOT_TESTED | ไม่มี axe/Playwright; มี code-review audit เท่านั้น |

สถาปัตยกรรม analytics ใช้ raw attempts → derived topic/P1 mastery/readiness/recommendations; storage key `phychem-study-v1`, schemaVersion 2 และ mock sessions แบบ additive. ความเสี่ยงสูงที่พบ: repeated attempts inflate recent metric, array-order recency และ readiness สูงจากหลักฐาน 1 ข้อ. ความเสี่ยง medium: misconception wording เดิมแรงเกินหลักฐานหนึ่งครั้ง. Backup 11 ไฟล์สร้างและตรวจ SHA-256 ที่ `backups/phase-7d/` ก่อนแก้
