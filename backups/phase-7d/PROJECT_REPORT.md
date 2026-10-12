# PROJECT REPORT

## Deliverable status

| Acceptance item | Status | Evidence |
|---|---|---|
| PDF inventory 6 files | Complete | `data/document_inventory.json` |
| Visual star inspection Part1/Part2 | Complete, 300/300 pages | `reports/star_detection_report.md` |
| Confirmed P1 traceability | Complete, 20 pages | `data/exam_priority.json`, `evidence/stars/` |
| Chemistry database | Complete for core syllabus | 18 topics, 23 validated formulas, 11 worked problems |
| Chemistry validation | Complete for database items | `reports/chemistry_validation.md` |
| 3 editable PPTX decks | Complete | `outputs/slides/` |
| 3 PDF slide exports | Complete | `outputs/slides/` |
| Slide render QA | Complete | 32/32 PPTX-rendered slides; PDF export first/last page verification and page-count check |
| Web application | Complete | 7 routes, responsive layout, KaTeX, local data |
| Light/Dark mode | Complete | System default + persisted preference |
| Practice grading | Complete | Numeric tolerance and conceptual exact match |
| Mock exam scoring | Complete | Randomized local set and answer review |
| Flashcard scheduling | Complete | Local spaced repetition state |
| Progress persistence | Complete | LocalStorage |
| Source PDFs unchanged | Verified by original SHA-256 inventory | `data/document_inventory.json` |

## Major findings

ตรวจพบดาวผู้สอนที่ยืนยันได้ 20 หน้า: Part1 จำนวน 12 หน้า และ Part2 จำนวน 8 หน้า ไม่มีรายการ PROBABLE/UNCERTAIN ในรอบนี้ เนื้อหา P2 ในระบบถูกระบุเป็นแนวคิดสนับสนุน ไม่อ้างว่าอาจารย์ทำเครื่องหมาย

พบ arithmetic discrepancy ใน Part2 PDF page 66: ลายมือคำนวณ `6.99-1.60` เป็น `7.39` แต่ค่าที่ถูกต้องคือ `5.39`. ระบบเก็บทั้งค่าต้นฉบับและค่าที่ตรวจแก้ พร้อมสถานะ REVIEW

## QA summary

- JSON schemas/load checks ผ่าน
- TypeScript production build ผ่าน
- Presentation package/layout/font validation ผ่านทั้ง 3 ไฟล์
- PDF export ผ่าน PowerPoint และเรนเดอร์กลับเป็นภาพครบ 10, 11 และ 11 หน้า
- Browser preview ถูกเปิดใน Codex panel แต่ browser automation sandbox ไม่สามารถเข้าถึง `127.0.0.1` จึงไม่อ้างว่าได้ทำ end-to-end visual interaction test ใน browser tool

## Remaining limitations

- ฐานโจทย์ปัจจุบันเป็นชุดแกนหลัก 11 ข้อ ไม่ใช่คลังโจทย์ขนาดใหญ่ และไม่อ้างว่าเป็นข้อสอบเก่า
- โน้ตลายมือใน Final Phychem.pdf และ Final.pdf ถูกใช้เป็นแหล่งเสริม แต่ตัวเลขที่ไม่ได้เข้าสู่ฐานข้อมูลยังไม่ผ่านการตรวจรายบรรทัด
- หน้าเว็บโหลด IBM Plex Sans Thai จาก Google Fonts เมื่อออนไลน์; หากออฟไลน์จะใช้ Segoe UI/ฟอนต์ระบบ
- การรับรอง P1 จำกัดเฉพาะหน้าที่เห็นดาวโดยตรง ไม่ขยายความหมายไปหน้าต่อเนื่องโดยไม่มีหลักฐาน

## Phase 7A maintenance update (2026-10-12)

- สำรอง structured data และไฟล์ที่จะปรับก่อนแก้ พร้อม SHA-256 manifest ที่ `backups/phase-7a/`
- ตรวจ P1 ครบ 20 records และเพิ่ม additive many-to-many mapping ใน `data/p1_traceability.json`
- แก้ metadata topic reference ของ `F-E-006`–`F-E-008` จาก E07 เป็น canonical E06; ไม่เปลี่ยน Formula ID, สูตร หรือคำตอบ
- ยืนยัน `F-E-009`–`F-E-013` ถูกต้องตาม registry ปัจจุบันและไม่เปลี่ยน
- Coverage: COMPLETE 11, PARTIAL 9; ไม่มี MISSING หรือ REVIEW_REQUIRED mapping
- P1 ที่มี practice relation 13/20; อีก 9 records ยังมี practice/conceptual-practice gap (รวม 2 รายการที่มีเพียง supporting problem)
- คง LocalStorage key `phychem-study-v1`, progress keys และ ID ทั้งหมด จึงไม่ต้อง migration
- เพิ่ม Python integrity validation และ Vitest สำหรับ referential integrity/LocalStorage compatibility
- รายงาน Phase 7A และแผน Phase 7B อยู่ใน `reports/phase_7a_*.md` และ `reports/phase_7b_question_bank_plan.md`

## Phase 7B question-bank expansion (2026-10-12)

- สำรองไฟล์ที่เกี่ยวข้อง 12 รายการพร้อม SHA-256 ใน `backups/phase-7b/`
- คงโจทย์ validated เดิม 11 ข้อและเพิ่ม validated questions 54 ข้อ รวม 65 ข้อ
- Difficulty distribution: Easy 20, Medium 29, Hard 16
- P1 direct retrieval practice ครบ 20/20; practice gaps เหลือ 0
- เพิ่ม optional schema สำหรับ learning objective, three hints, P1 IDs, question format, MCQ options/explanations, grading policy และ validation status
- เพิ่ม deterministic grading สำหรับ numerical/scientific notation, stable MCQ option IDs และ controlled conceptual synonyms
- Practice รองรับ topic/difficulty/type filters และ Instructor-Star Practice; Mock Exam ใช้ grading engine เดียวกัน
- Independent validation ตรวจพบและแก้ draft 2 ข้อก่อนรับเข้า active bank: P-K-026 และ P-E-022
- AgBr correction เดิมและ original source values ถูกเก็บครบ; original PDFs/evidence ไม่ถูกแก้
- Final QA: Python validators 3/3 ผ่าน, Vitest 19/19 ผ่าน, production build ผ่าน; browser smoke test ถูกบล็อกด้วย `ERR_CONNECTION_TIMED_OUT`

## Phase 7C personalized preparation (2026-10-12)

- เพิ่ม deterministic analytics, P1 mastery, readiness/confidence, weak-topic และ evidence-bounded misconception signals
- เพิ่ม Smart Practice, seeded mock blueprint, persisted deadline/session, idempotent submit และ post-exam breakdown
- เพิ่ม controlled unit conversion ใน grading โดยไม่เปลี่ยนคำตอบเคมี
- รักษา 65 questions, 20 P1, 23 formulas, 18 topics และ LocalStorage key เดิม
- Vitest 90/90 และ Python validators ทุก phase ผ่าน; production build ผ่าน
- largest initial JS ลด 757.94 เป็น 491.21 kB โดย lazy-load Phase 7C และ KaTeX; warning >500 kB หายไป
- Browser E2E ยังไม่ยืนยัน เนื่องจาก localhost automation environment เดิมเข้าไม่ได้; มี manual smoke steps ใน README
