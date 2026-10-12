# Phase 7E Offline Behavior

ระดับที่ยืนยันได้:

- หลังเปิด Dashboard และ Practice จน assets ถูกโหลดแล้ว การตัด network ยังนำทาง client-side กลับไป Practice และใช้งาน UI ที่โหลดไว้ได้
- progress, attempts, mock sessions, theme และ backup/restore ใช้ LocalStorage/ไฟล์ในเครื่อง ไม่ต้องมี paid API หรือ external database
- first visit ขณะ offline ไม่ทำงาน เพราะไม่มี service worker/precache; reload offline ก็ไม่มี offline guarantee
- Google Font ต้องใช้ network แต่มี system-font fallback

ดังนั้นคำอธิบายที่ถูกต้องคือ local-first progress และ limited post-load offline operation ไม่ใช่ installable/full offline PWA. Phase 7E ไม่เพิ่ม service worker เพราะอยู่นอกขอบเขต stabilization และอาจเพิ่ม cache/version migration risk.
