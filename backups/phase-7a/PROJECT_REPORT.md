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
