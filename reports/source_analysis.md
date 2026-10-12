# รายงานการวิเคราะห์เอกสารต้นฉบับ (Phase 1)

สถานะ: ตรวจ inventory และภาพทุกหน้าครบแล้วสำหรับ PDF ทั้ง 6 ไฟล์ โดย Part1/Part2 ผ่านการตรวจดาวรายหน้า 300/300 หน้า

## วิธีดำเนินการ

- บันทึก SHA-256, จำนวนหน้า, ขนาดไฟล์ และข้อความที่ดึงได้รายหน้า
- เรนเดอร์ทุกหน้าเป็นภาพ JPEG ที่ 110 dpi เพื่อดูสูตร ภาพ ตาราง และลายมือ
- ตรวจ contact sheet ทุกหน้า และเปิดภาพเต็มของหน้าที่มีสี magenta หรือลักษณะคล้ายดาว
- ใช้ภาพอ้างอิงใน workspace เป็นเกณฑ์รูปร่างและสี การคัดกรองสีใช้เพื่อหา candidate เท่านั้น
- ไม่ถือข้อความที่ดึงได้หรือ OCR เป็นหลักฐานเพียงอย่างเดียว โดยเฉพาะโน้ตลายมือและสูตร

## Inventory

| เอกสาร | บทบาท | หน้า | ขอบเขต | เนื้อหาภาพ/ตาราง/ตัวอย่าง |
|---|---:|---:|---|---|
| PhCh-SC202301 Physical Chemistry Part1.pdf | primary_instructor | 167 | Chemical Kinetics | สไลด์ 16:9 มีสมการ กราฟ reaction coordinate, concentration-time, Arrhenius/temperature behavior, กลไกปฏิกิริยา และคำอธิบายเขียนมือหลายสี มีตัวอย่างและแบบฝึกหัดทั้ง initial rate, integrated rate law, half-life, stoichiometric rate และ activation energy |
| PhCh-SC202301 Physical Chemistry Part2.pdf | primary_instructor | 133 | Electrochemistry | สไลด์ 16:9 มีตาราง สมการ เซลล์นำไฟฟ้า กราฟ activity coefficient แผนภาพ galvanic/electrolytic cell และ annotation เขียนมือหลายสี มีตัวอย่างและแบบฝึกหัด conductivity, dissociation, solubility/Ksp, ionic strength, activity coefficient และ cell potential |
| Chemical Kinetic.pdf | supplementary | 7 | Supplementary Chemical Kinetics notes | โน้ตพื้นหลังเข้มแบบยาว มีสูตร ตารางสรุป กราฟ และภาพประกอบจากสไลด์ผู้สอน มีสรุปสูตรและตัวอย่างย่อ ต้องตรวจเทียบกับเอกสารผู้สอนก่อนนำไปใช้ |
| Electrochemistry.pdf | supplementary | 6 | Supplementary Electrochemistry notes | โน้ตพื้นหลังเข้มแบบยาว มีสูตร ตาราง กราฟ และภาพประกอบ มีสูตรและตัวอย่างย่อ ต้องตรวจเทียบกับเอกสารผู้สอนก่อนนำไปใช้ |
| Final Phychem.pdf | supplementary | 13 | Handwritten revision and worked problems | ลายมือบนกระดาษกริด มีสมการ การแทนค่า และโจทย์คำนวณ มี worked calculations จำนวนมาก; ตัวเลขและหน่วยต้องตรวจทีละข้อก่อนรับรอง |
| Final.pdf | supplementary | 16 | Supplementary revision, screenshots, and practice questions | หน้าปกตกแต่ง โน้ตกริด ภาพสไลด์ ภาพโจทย์ออนไลน์ และคำอธิบายเขียนมือ มีโจทย์และเฉลยผสมหลายแหล่ง; ไม่ถือเป็นแหล่งยืนยันหลัก |

## ข้อสังเกตด้านการอ่านไฟล์

- เอกสารผู้สอนมี text layer แต่ภาษาไทยบางส่วนถอดออกมาเป็นอักขระผิดเพี้ยน จึงใช้ภาพเรนเดอร์ประกอบการตีความหัวข้อ สูตร และเลขสไลด์
- เอกสาร Chemical Kinetic.pdf และ Electrochemistry.pdf เป็นโน้ตแบบหน้าแนวตั้งยาว มีภาพและสูตรขนาดเล็ก
- Final Phychem.pdf เป็นลายมือเกือบทั้งหมด และ Final.pdf ผสมลายมือ ภาพสไลด์ และภาพโจทย์ออนไลน์ จึงต้องตรวจสูตรและตัวเลขต่อใน Phase 2
- ยังไม่รับรองความถูกต้องเชิงเคมีของตัวอย่างหรือคำตอบในเอกสารเสริมจนกว่าจะผ่าน Phase 2

## ไฟล์หลักฐาน

ภาพเรนเดอร์ทุกหน้าอยู่ใน `evidence/renders/` และ contact sheets อยู่ใน `evidence/contact_sheets/` รายการข้อความรายหน้าและ checksum อยู่ใน `data/document_inventory.json`.