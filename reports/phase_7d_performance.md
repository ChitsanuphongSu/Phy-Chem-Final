# Phase 7D Performance

Production build หลัง 7D: initial JS 491.25 kB (gzip 119.58), DashboardExtras 6.65 kB (gzip 2.63), Phase7C 28.58 kB (gzip 9.11), lazy KaTeX 258.93 kB (gzip 77.67). Baseline initial 491.21 kB จึงเพิ่ม 0.04 kB; ยังไม่มี warning >500 kB

Vitest ทั้ง suite ใช้ประมาณ 2.08 วินาที; build ประมาณ 3.10 วินาทีในรอบวัด. Analytics มี O(attempts log attempts) จาก chronology sorting และ mock generation sort 65 questions; ไม่พบเหตุผลให้เพิ่ม dependency หรือ manual chunks

Browser render, route transitions, CLS, Lighthouse และ real-device performance เป็น NOT_VERIFIED เพราะ browser เข้า localhost ไม่ได้
