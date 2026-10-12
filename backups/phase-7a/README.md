# Physical Chemistry Study Hub

ระบบเตรียมสอบภาษาไทยสำหรับ SC202301 ครอบคลุม Chemical Kinetics และ Electrochemistry โดยยึดเอกสารผู้สอนเป็นแหล่งหลัก แยก P1 ที่มีดาวยืนยันออกจากเนื้อหาที่อนุมาน และเก็บ source reference ทุกระดับ

## สิ่งที่อยู่ในโครงการ

- `data/` ฐานข้อมูลเอกสาร บทเรียน สูตร โจทย์ และ exam priority
- `reports/` รายงาน source analysis, star detection, coverage และ chemistry validation
- `evidence/` ภาพเรนเดอร์ทุกหน้า contact sheets และภาพหลักฐานดาว 20 หน้า
- `outputs/slides/` สไลด์ 3 ชุด ทั้ง PPTX และ PDF
- `web/` แอป React + TypeScript แบบ local-first
- `tests/` สคริปต์สร้างข้อมูล สร้างสไลด์ และตรวจ integrity

## เปิดเว็บ

```powershell
cd web
pnpm install
pnpm dev
```

Production build:

```powershell
pnpm build
```

## ตรวจโครงการ

```powershell
python tests/validate_project.py
cd web
pnpm test
```

PDF ต้นฉบับทั้ง 6 ไฟล์ยังอยู่ที่ workspace root โดยไม่ถูกแก้ไข สำเนาสำหรับ source links ของเว็บอยู่ใน `web/public/sources/`.
