"""Build the 54 reviewed Phase 7B questions without changing legacy records."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBLEM_PATH = ROOT / "data" / "problems.json"
WEB_PATH = ROOT / "web" / "src" / "data" / "problems.json"

DOC_K = "PhCh-SC202301 Physical Chemistry Part1.pdf"
DOC_E = "PhCh-SC202301 Physical Chemistry Part2.pdf"


def ref(topic: str, page: int) -> list[dict]:
    return [{"document": DOC_K if topic.startswith("K") else DOC_E, "pdf_page": page, "printed_slide_number": page if topic.startswith("E") else page - 1}]


def base(qid, topic, qtype, difficulty, prompt, answer, unit, formulas, page, p1, objective, hints, mistake, question_format):
    return {
        "id": qid,
        "topic_id": topic,
        "type": qtype,
        "question_format": question_format,
        "difficulty": difficulty,
        "prompt_th": prompt,
        "source_classification": "ai-generated-from-source",
        "source_references": ref(topic, page),
        "correct_answer": answer,
        "tolerance": None,
        "unit": unit,
        "hint_th": hints[0],
        "hints": hints,
        "solution_steps": [],
        "related_formula_ids": formulas,
        "related_p1_ids": p1,
        "learning_objective": objective,
        "common_mistake": mistake,
        "validation_status": "VALIDATED",
        "bookmarked_default": False,
    }


def num(qid, topic, difficulty, prompt, answer, tol, unit, formulas, page, p1, objective, hints, given, formula, substitution, calculation, unit_check, mistake, spec, fmt="numerical-calculation"):
    q = base(qid, topic, "numerical", difficulty, prompt, answer, unit, formulas, page, p1, objective, hints, mistake, fmt)
    q["tolerance"] = tol
    q["answer_format"] = "numeric"
    q["grading_policy"] = {"mode": "numeric", "absolute_tolerance": tol, "relative_tolerance": 0.001}
    q["solution_steps"] = [
        f"1. Given: {given}", f"2. Find: {objective}", f"3. Formula: {formula}",
        f"4. Substitute: {substitution}", f"5. Calculate: {calculation}",
        f"6. Check Units: {unit_check}", f"7. Final Answer: {answer:g} {unit or ''}".rstrip(),
        f"8. Common Mistake: {mistake}",
    ]
    q["validation_spec"] = spec
    return q


def mcq(qid, topic, difficulty, prompt, correct, options, explanations, page, p1, objective, hints, mistake, formulas=None, fmt="multiple-choice"):
    q = base(qid, topic, "multiple-choice", difficulty, prompt, correct, None, formulas or [], page, p1, objective, hints, mistake, fmt)
    q["answer_format"] = "single-choice"
    q["answer_options"] = [{"id": key, "text_th": text} for key, text in options]
    q["correct_option_id"] = correct
    q["option_explanations"] = explanations
    q["grading_policy"] = {"mode": "single-choice"}
    q["solution_steps"] = [
        f"1. Identify Concept: {objective}",
        "2. Scientific Principle: พิจารณานิยามและเงื่อนไขของระบบตามบทเรียน",
        f"3. Apply: ตัวเลือก {correct} สอดคล้องกับหลักการโดยไม่เพิ่มสมมติฐาน",
        f"4. Correct Answer: {correct} — {dict(options)[correct]}",
        f"5. Common Misconception: {mistake}",
    ]
    return q


def concept(qid, topic, difficulty, prompt, answer, accepted, page, p1, objective, hints, mistake, formulas=None, fmt="conceptual-short-answer"):
    q = base(qid, topic, "conceptual", difficulty, prompt, answer, None, formulas or [], page, p1, objective, hints, mistake, fmt)
    q["answer_format"] = "short-text"
    q["grading_policy"] = {"mode": "accepted-text", "accepted_answers": accepted, "case_sensitive": False}
    q["solution_steps"] = [
        f"1. Identify Concept: {objective}",
        "2. Scientific Principle: ใช้นิยามและเงื่อนไขที่ระบุในบทเรียน",
        f"3. Apply: {answer}",
        f"4. Correct Answer: {answer}",
        f"5. Common Misconception: {mistake}",
    ]
    return q


Q = []

# K01: 1 easy, 1 medium, 1 hard
Q += [
num("P-K-006","K01","easy","สำหรับ 2A → B ถ้า A ลดลง 0.40 M ใน 20 s จงหาอัตราปฏิกิริยา",0.01,1e-5,"M s^-1",["F-K-001"],94,["K-P1-094"],"หาอัตราปฏิกิริยาจากการหายไปของสารตั้งต้น",["หาอัตราการหายไปของ A ก่อน","หารด้วยสัมประสิทธิ์ 2","เริ่มจาก 0.40/20 แล้วหาร 2"],"Δ[A]=0.40 M, Δt=20 s, νA=2","rate=-(1/2)Δ[A]/Δt","(1/2)(0.40/20)","0.010","M หารด้วย s และสัมประสิทธิ์ไม่มีหน่วย","ลืมหารด้วยสัมประสิทธิ์ 2",{"op":"div","values":[0.40,20,2]}),
mcq("P-K-007","K01","medium","สำหรับ 2N2O5 → 4NO2 + O2 ความสัมพันธ์ใดถูกต้อง?","B",[("A","-d[N2O5]/dt=d[NO2]/dt"),("B","-(1/2)d[N2O5]/dt=(1/4)d[NO2]/dt=d[O2]/dt"),("C","-2d[N2O5]/dt=4d[NO2]/dt"),("D","d[N2O5]/dt=d[O2]/dt")],{"A":"ไม่หารด้วยสัมประสิทธิ์","B":"นิยามอัตราปฏิกิริยาต้องหารด้วยสัมประสิทธิ์","C":"คูณสัมประสิทธิ์ผิดทิศ","D":"ละเลยเครื่องหมายและสัมประสิทธิ์"},94,["K-P1-094"],"เลือกสมการอัตราที่สอดคล้องกับ stoichiometry",["ดูเครื่องหมายของ reactant/product","ใช้ 1/ν หน้าทุกอนุพันธ์","เขียน -(1/2)d[N2O5]/dt ก่อน"],"ใช้สัมประสิทธิ์เป็นตัวคูณแทนตัวหาร",["F-K-001"]),
num("P-K-008","K01","hard","3A + 2B → 4C ถ้า C เพิ่มจาก 0 เป็น 0.240 M ใน 30.0 s จงหาอัตราการหายไปของ B",0.004,4e-6,"M s^-1",["F-K-001"],94,["K-P1-094"],"แปลงอัตราการเกิดผลิตภัณฑ์เป็นอัตราการหายไปของสารตั้งต้น",["หา d[C]/dt","เทียบอัตราด้วย 2/4","คำนวณ 0.240/30.0 แล้วคูณ 1/2"],"Δ[C]=0.240 M, Δt=30.0 s, νB=2, νC=4","-d[B]/dt=(2/4)d[C]/dt","(2/4)(0.240/30.0)","0.00400","สัมประสิทธิ์ไม่มีหน่วย จึงเหลือ M s^-1","สลับอัตราส่วนเป็น 4/2",{"op":"mul_div","values":[2,0.240,4,30.0]}),
]

# K02: 1 easy, 2 medium, 1 hard
Q += [
mcq("P-K-009","K02","easy","ถ้าเพิ่ม [A] เป็น 2 เท่าแล้ว initial rate เพิ่มเป็น 4 เท่า อันดับต่อ A เท่ากับเท่าใด?","C",[("A","0"),("B","1"),("C","2"),("D","4")],{"A":"อันดับศูนย์ทำให้อัตราไม่เปลี่ยน","B":"อันดับหนึ่งให้อัตราเพิ่ม 2 เท่า","C":"2^2=4 จึงเป็นอันดับสอง","D":"สับสนตัวคูณอัตรากับเลขชี้กำลัง"},21,["K-P1-021"],"หา partial order จากอัตราส่วน initial rates",["เขียน 4=2^m","ใช้ลอการิทึมหรือกำลังที่รู้จัก","ถามว่า 2 ยกกำลังใดได้ 4"],"ตอบ 4 เพราะเห็นอัตราเพิ่ม 4 เท่า",["F-K-002"]),
num("P-K-010","K02","medium","rate=k[A][B]^2 เมื่อ [A]=0.10 M, [B]=0.20 M และ k=2.50 M^-2 s^-1 จงหา rate",0.01,1e-5,"M s^-1",["F-K-002"],21,["K-P1-021"],"คำนวณอัตราจาก rate law",["แทนค่าตามเลขชี้กำลัง","ยก [B] กำลังสองก่อน","คำนวณ 2.50×0.10×0.20²"],"k=2.50 M^-2 s^-1, [A]=0.10 M, [B]=0.20 M","rate=k[A][B]^2","2.50(0.10)(0.20)^2","0.0100","M^-2 s^-1×M×M²=M s^-1","ลืมยกกำลังสองของ [B]",{"op":"product","values":[2.50,0.10,0.20,0.20]}),
num("P-K-011","K02","medium","ปฏิกิริยาอันดับรวม 2 มี rate=0.036 M s^-1 เมื่อ [A]=0.30 M และ rate=k[A]^2 จงหา k",0.4,4e-4,"M^-1 s^-1",["F-K-002"],26,["K-P1-026"],"หาค่าคงที่อัตราและหน่วยจาก rate law",["จัดรูปหา k","หาร rate ด้วย [A]²","คำนวณ 0.036/0.30²"],"rate=0.036 M s^-1, [A]=0.30 M","k=rate/[A]^2","0.036/(0.30)^2","0.400","(M s^-1)/M²=M^-1 s^-1","ให้หน่วย k เป็น s^-1 แบบอันดับหนึ่ง",{"op":"div_square","values":[0.036,0.30]}),
num("P-K-012","K02","hard","ทดลองพบว่าเมื่อ [A] เพิ่ม 3 เท่า rate เพิ่ม 9 เท่า และเมื่อ [B] เพิ่ม 2 เท่า rate ไม่เปลี่ยน ถ้า rate=0.018 M s^-1 ที่ [A]=0.20 M จงหา k",0.45,4.5e-4,"M^-1 s^-1",["F-K-002"],26,["K-P1-021","K-P1-026"],"วิเคราะห์อันดับย่อยแล้วหาค่าคงที่อัตรา",["หา order ของ A และ B จากตัวคูณ","3^m=9 และ 2^n=1","ได้ rate=k[A]² แล้วคำนวณ 0.018/0.20²"],"rate=0.018 M s^-1, [A]=0.20 M; A×3→rate×9, B×2→ไม่เปลี่ยน","rate=k[A]^2[B]^0","0.018/(0.20)^2","0.450","อันดับรวม 2 ทำให้ k มี M^-1 s^-1","นำ [B] มาคูณทั้งที่เป็นอันดับศูนย์",{"op":"div_square","values":[0.018,0.20]},"data-table-interpretation"),
]

# K03: 1 easy, 2 medium, 2 hard
Q += [
mcq("P-K-013","K03","easy","กราฟใดเป็นเส้นตรงสำหรับปฏิกิริยาอันดับหนึ่ง?","B",[("A","[A] กับ t"),("B","ln[A] กับ t"),("C","1/[A] กับ t"),("D","rate กับ t เสมอ")],{"A":"เป็น linear form ของอันดับศูนย์","B":"ln[A]=ln[A]0-kt","C":"เป็น linear form ของอันดับสอง","D":"ไม่ใช่เกณฑ์มาตรฐานระบุอันดับ"},35,["K-P1-035"],"เลือก linear plot ของ integrated rate law",["นึกถึงรูป y=mx+b","อันดับหนึ่งมี logarithm","ln[A] มี slope=-k"],"สลับกราฟอันดับหนึ่งกับอันดับสอง",["F-K-004"]),
num("P-K-014","K03","medium","ปฏิกิริยาอันดับศูนย์มี [A]0=0.80 M และ k=0.050 M min^-1 หลัง 6.0 min เหลือ [A] เท่าใด",0.5,5e-4,"M",["F-K-003"],31,[],"ใช้ integrated zero-order law",["อันดับศูนย์ลดเชิงเส้น","ใช้ [A]=[A]0-kt","แทน 0.80-(0.050)(6.0)"],"[A]0=0.80 M, k=0.050 M min^-1, t=6.0 min","[A]=[A]0-kt","0.80-(0.050)(6.0)","0.50","k×t=(M min^-1)(min)=M","ใช้ exponential decay ซึ่งเป็นอันดับหนึ่ง",{"op":"subtract_product","values":[0.80,0.050,6.0]}),
num("P-K-015","K03","medium","ปฏิกิริยาอันดับหนึ่งมี [A]0=0.500 M, k=0.0200 min^-1 จงหา [A] ที่ 30.0 min",0.2744,0.0003,"M",["F-K-004"],42,["K-P1-035","K-P1-042"],"คำนวณ concentration-time ของอันดับหนึ่ง",["ใช้ exponential form","คำนวณ kt ก่อน","[A]=0.500e^(-0.0200×30.0)"],"[A]0=0.500 M, k=0.0200 min^-1, t=30.0 min","[A]=[A]0e^-kt","0.500e^[-(0.0200)(30.0)]","0.2744","kt ไม่มีหน่วย จึงเหลือหน่วย M","ใช้เครื่องหมายบวกใน exponent",{"op":"first_order_conc","values":[0.500,0.0200,30.0]}),
num("P-K-016","K03","hard","ปฏิกิริยาอันดับสอง A→products มี [A]0=0.100 M และ k=0.250 M^-1 s^-1 จงหา [A] หลัง 40.0 s",0.05,5e-5,"M",["F-K-005"],49,["K-P1-049"],"ใช้ integrated second-order law",["เลือกสมการที่มี 1/[A]","หา 1/[A]=1/[A]0+kt","คำนวณ 10.0+(0.250)(40.0) แล้วกลับเศษส่วน"],"[A]0=0.100 M, k=0.250 M^-1 s^-1, t=40.0 s","1/[A]=1/[A]0+kt","1/[A]=10.0+10.0=20.0 M^-1","[A]=1/20.0=0.0500","ด้านขวามี M^-1 และกลับค่าได้ M","ลืมกลับเศษส่วนหลังหา 1/[A]",{"op":"second_order_conc","values":[0.100,0.250,40.0]}),
num("P-K-017","K03","hard","กราฟ 1/[A] กับ t มี slope=0.0800 M^-1 s^-1 และ intercept=5.00 M^-1 จงหา [A] ที่ t=50.0 s",0.1111,0.0002,"M",["F-K-005"],49,["K-P1-049"],"ตีความ slope/intercept ของกราฟอันดับสอง",["slope คือ k และ intercept คือ 1/[A]0","ใช้ค่าจากเส้นตรงที่ t=50.0","1/[A]=5.00+0.0800×50.0 แล้วกลับค่า"],"slope=0.0800 M^-1 s^-1, intercept=5.00 M^-1, t=50.0 s","1/[A]=intercept+(slope)t","1/[A]=5.00+4.00=9.00 M^-1","[A]=0.1111","inverse concentration กลับค่าเป็น M","อ่าน intercept เป็น [A]0 โดยไม่กลับค่า",{"op":"inverse_linear","values":[5.00,0.0800,50.0]},"data-table-interpretation"),
]

# K04: 1 easy, 1 medium, 1 hard
Q += [
num("P-K-018","K04","easy","ปฏิกิริยาอันดับหนึ่งมี k=0.00300 s^-1 จงหา half-life",231.0,0.3,"s",["F-K-007"],40,["K-P1-040"],"คำนวณ half-life อันดับหนึ่ง",["อันดับหนึ่งไม่ขึ้นกับ [A]0","ใช้ ln2/k","คำนวณ 0.693/0.00300"],"k=0.00300 s^-1","t1/2=ln2/k","0.693/0.00300","231","(ไม่มีหน่วย)/(s^-1)=s","ใช้ 1/k โดยไม่คูณ ln2",{"op":"div","values":[0.693,0.003]}),
num("P-K-019","K04","medium","ปฏิกิริยาอันดับศูนย์มี [A]0=0.600 M และ k=0.0200 M min^-1 จงหา half-life",15.0,0.02,"min",["F-K-006"],40,["K-P1-040"],"คำนวณ half-life อันดับศูนย์",["half-life อันดับศูนย์ขึ้นกับ [A]0","ใช้ [A]0/(2k)","แทน 0.600/[2(0.0200)]"],"[A]0=0.600 M, k=0.0200 M min^-1","t1/2=[A]0/(2k)","0.600/[2(0.0200)]","15.0","M/(M min^-1)=min","ใช้ 0.693/k กับทุกอันดับ",{"op":"div","values":[0.600,2,0.0200]}),
num("P-K-020","K04","hard","ปฏิกิริยาอันดับสองมี k=0.500 M^-1 min^-1 ถ้าเพิ่ม [A]0 จาก 0.100 เป็น 0.200 M อัตราส่วน t1/2,new/t1/2,old เท่าใด",0.5,0.001,None,["F-K-008"],40,["K-P1-040"],"เปรียบเทียบ half-life อันดับสองเมื่อความเข้มข้นต้นเปลี่ยน",["อันดับสอง t1/2 แปรผกผันกับ [A]0","ตั้งอัตราส่วนโดย k ตัดกัน","ratio=[A]old/[A]new=0.100/0.200"],"[A]old=0.100 M, [A]new=0.200 M, k คงที่","t1/2=1/(k[A]0)","ratio=[A]old/[A]new","0.500","เป็นอัตราส่วนไร้หน่วย","คิดว่า half-life อันดับสองคงที่",{"op":"div","values":[0.100,0.200]}),
]

# K05: 1 easy, 2 medium, 1 hard
Q += [
mcq("P-K-021","K05","easy","energy profile มี Ereactant=20, Etransition=65, Eproduct=35 kJ mol^-1 ข้อใดถูกต้อง?","D",[("A","Ea,f=35 และ ΔH=-15"),("B","Ea,f=45 และ ΔH=-15"),("C","Ea,f=30 และ ΔH=+45"),("D","Ea,f=45 และ ΔH=+15")],{"A":"ใช้ระดับ product แทน transition state","B":"เครื่องหมาย ΔH ผิด","C":"คำนวณทั้งสองค่าผิด","D":"Ea,f=65-20 และ ΔH=35-20"},61,["K-P1-061"],"อ่าน forward activation energy และ reaction enthalpy",["Ea วัดจาก reactant ถึง transition state","ΔH=Eproduct-Ereactant","คำนวณ 65-20 และ 35-20"],"สลับ Ea กับ ΔH",["F-K-009"],"energy-diagram-interpretation"),
num("P-K-022","K05","medium","Ereactant=12, Etransition=52, Eproduct=2 kJ mol^-1 จงหา reverse activation energy",50.0,0.05,"kJ mol^-1",["F-K-009"],61,["K-P1-061"],"คำนวณ reverse activation energy จาก energy profile",["เริ่มจาก product ไป transition state","Ea,rev=ETS-Eproduct","คำนวณ 52-2"],"ETS=52, Eproduct=2 kJ mol^-1","Ea,rev=ETS-Eproduct","52-2","50","ผลต่างระดับพลังงานเป็น kJ mol^-1","ลบจาก reactant ซึ่งให้ forward Ea",{"op":"subtract","values":[52,2]},"energy-diagram-interpretation"),
concept("P-K-023","K05","medium","ตัวเร่งปฏิกิริยาเปลี่ยน Ea และ ΔH ของปฏิกิริยาอย่างไร?","ลด Ea ของเส้นทางไปข้างหน้าและย้อนกลับ แต่ไม่เปลี่ยน ΔH",["ลด ea แต่ไม่เปลี่ยน delta h","ลดพลังงานก่อกัมมันต์แต่ไม่เปลี่ยนเอนทัลปี","ลด ea ของทั้งสองทิศทางแต่ไม่เปลี่ยน ΔH"],61,["K-P1-061"],"อธิบายผลของ catalyst ต่อ energy profile",["แยก kinetic barrier จาก state function","catalyst ให้เส้นทางใหม่","ระดับ reactant/product เดิมจึง ΔH เดิม"],"กล่าวว่าตัวเร่งทำให้ ΔH ลดลง",["F-K-009"],"energy-diagram-interpretation"),
num("P-K-024","K05","hard","energy profile มี Ea,f=72 kJ mol^-1 และ ΔH=-18 kJ mol^-1 จงหา Ea,reverse",90.0,0.09,"kJ mol^-1",["F-K-009"],61,["K-P1-061"],"เชื่อม Ea ไปข้างหน้า ย้อนกลับ และ ΔH",["สำหรับ exothermic product ต่ำกว่า reactant","Ea,rev=Ea,f-ΔH","แทน 72-(-18)"],"Ea,f=72 kJ mol^-1, ΔH=-18 kJ mol^-1","Ea,rev=Ea,f-ΔH","72-(-18)","90","ทุกพจน์เป็น kJ mol^-1","บวก ΔH โดยไม่รักษาเครื่องหมายลบ",{"op":"subtract","values":[72,-18]},"energy-diagram-interpretation"),
]

# K06: 1 easy, 1 medium, 1 hard
Q += [
mcq("P-K-025","K06","easy","เมื่อนำอุณหภูมิ 25 °C ไปใช้ในสมการ Arrhenius ต้องใช้ค่าใด?","C",[("A","25 K"),("B","248.15 K"),("C","298.15 K"),("D","325.15 K")],{"A":"ห้ามใช้ Celsius ตรง ๆ","B":"ลบ 273.15 ผิดทิศ","C":"25+273.15=298.15 K","D":"บวก 300 แทน 273.15"},91,["K-P1-091"],"แปลงอุณหภูมิเป็น Kelvin ก่อนใช้ Arrhenius",["สมการต้องใช้ absolute temperature","K=°C+273.15","25+273.15"],"ใช้ 25 ในพจน์ 1/T",["F-K-009","F-K-010"]),
num("P-K-026","K06","medium","ถ้า A=1.00×10^12 s^-1, Ea=50.0 kJ mol^-1 ที่ 298.15 K จงหา k",1737.0,2.0,"s^-1",["F-K-009"],91,["K-P1-091"],"คำนวณ k จาก Arrhenius equation",["แปลง Ea เป็น J mol^-1","ใช้ k=Ae^(-Ea/RT)","แทน 50000/[8.314(298.15)] ใน exponent"],"A=1.00e12 s^-1, Ea=50000 J mol^-1, T=298.15 K","k=A exp(-Ea/RT)","1.00e12 exp[-50000/(8.314×298.15)]","1.737e3","exponent ไร้หน่วยและ k มีหน่วยเดียวกับ A","ใช้ Ea=50.0 โดยไม่แปลง kJ เป็น J",{"op":"arrhenius","values":[1e12,50000,8.314,298.15]}),
num("P-K-027","K06","hard","k เพิ่มจาก 1.20×10^-3 เป็น 4.80×10^-3 s^-1 เมื่อ T เพิ่มจาก 300.0 เป็น 330.0 K จงหา Ea",38021.0,60.0,"J mol^-1",["F-K-010"],91,["K-P1-091"],"หา activation energy จาก two-temperature Arrhenius equation",["ใช้อัตราส่วน k2/k1","ln(k2/k1)=Ea/R(1/T1-1/T2)","คำนวณ 8.314 ln4 /(1/300-1/330)"],"k2/k1=4.00, T1=300.0 K, T2=330.0 K","Ea=R ln(k2/k1)/(1/T1-1/T2)","8.314 ln4 /(1/300.0-1/330.0)","3.8021e4","R เป็น J mol^-1 K^-1 และส่วนต่าง reciprocal temperature เป็น K^-1","สลับ 1/T ทำให้ Ea ติดลบ",{"op":"arrhenius_two_temp","values":[8.314,4.0,300.0,330.0]}),
]

# K07: 2 easy, 1 medium
Q += [
mcq("P-K-028","K07","easy","กลไก: (1) A+B→I (ช้า), (2) I+C→D (เร็ว) สารใดเป็น intermediate?","C",[("A","A"),("B","B"),("C","I"),("D","D")],{"A":"A เป็น reactant รวม","B":"B เป็น reactant รวม","C":"I ถูกสร้างแล้วถูกใช้และไม่อยู่ในสมการรวม","D":"D เป็น product"},74,["K-P1-074"],"ระบุ reaction intermediate",["มองหาสารที่เกิดในขั้นหนึ่ง","สารนั้นต้องถูกใช้ในขั้นถัดไป","I ตัดกันเมื่อรวม elementary steps"],"เลือกสารที่อยู่ใน slow step โดยไม่ดูการเกิด/ใช้",[],"reaction-mechanism-analysis"),
concept("P-K-029","K07","easy","เพราะเหตุใดจึงไม่ควรเขียน rate law จากสัมประสิทธิ์ของสมการรวมสำหรับกลไกหลายขั้น?","เพราะ rate law ขึ้นกับ elementary step และกลไก โดยเฉพาะ rate-determining step ไม่ได้กำหนดจากสมการรวมเสมอ",["rate law ขึ้นกับกลไกไม่ใช่สมการรวม","ต้องรู้ elementary step หรือ rate determining step","อันดับปฏิกิริยาไม่จำเป็นต้องเท่ากับสัมประสิทธิ์สมการรวม"],77,["K-P1-077"],"อธิบายข้อจำกัดของการอนุมาน rate law จาก overall reaction",["แยก overall equation จาก elementary step","อันดับจาก stoichiometry ใช้ได้โดยตรงเฉพาะ elementary step","RDS ควบคุมอัตราและอาจมี intermediate"],"ใช้สัมประสิทธิ์รวมเป็นอันดับเสมอ",[],"reaction-mechanism-analysis"),
mcq("P-K-030","K07","medium","กลไก (1) NO2+NO2→NO3+NO (ช้า), (2) NO3+CO→NO2+CO2 (เร็ว) สมการรวมและ intermediate ที่ถูกต้องคือข้อใด?","B",[("A","2NO2+CO→NO+CO2; NO3 เป็น catalyst"),("B","NO2+CO→NO+CO2; NO3 เป็น intermediate"),("C","2NO2+CO→NO3+NO+CO2; NO2 เป็น intermediate"),("D","NO3+CO→NO2+CO2; NO เป็น intermediate")],{"A":"NO3 ถูกสร้างแล้วใช้ จึงเป็น intermediate ไม่ใช่ catalyst และ NO2 ต้องตัดหนึ่งโมล","B":"บวกขั้นแล้วตัด NO3 และ NO2 หนึ่งโมล เหลือสมการรวมนี้","C":"ยังไม่ตัด species ที่เกิดและใช้","D":"เป็นเพียงขั้นที่สอง"},77,["K-P1-074","K-P1-077"],"รวม elementary steps และตัด intermediate",["บวกสมการทั้งสองขั้น","ตัด species ที่ปรากฏคนละข้าง","NO3 ถูกสร้างแล้วถูกใช้"],"ไม่ตัด species ที่อยู่ทั้งสองข้าง",[],"reaction-mechanism-analysis"),
]
# K08: 1 easy, 1 medium
Q += [
mcq("P-K-031","K08","easy","ข้อใดอธิบาย effective collision ได้ครบที่สุด?","D",[("A","โมเลกุลชนกันทุกครั้งจะเกิดปฏิกิริยา"),("B","มีพลังงานสูงอย่างเดียว"),("C","มีทิศทางถูกต้องอย่างเดียว"),("D","มีพลังงานอย่างน้อย Ea และมี orientation ที่เหมาะสม")],{"A":"การชนส่วนใหญ่ไม่สำเร็จ","B":"ยังต้องมี orientation","C":"ยังต้องผ่าน energy barrier","D":"ครบทั้งพลังงานและการจัดวาง"},162,["K-P1-162"],"ระบุเงื่อนไข effective collision",["มีมากกว่าการชนกันเฉย ๆ","ต้องผ่านทั้ง energy และ geometry","เลือกตัวเลือกที่กล่าวถึง Ea และ orientation"],"คิดว่าการชนทุกครั้งให้ผลิตภัณฑ์",[],"collision-theory"),
concept("P-K-032","K08","medium","เปรียบเทียบ collision ในแก๊สกับ encounter ในสารละลายตามภาพผู้สอนแบบสั้น ๆ","ในแก๊สโมเลกุลชนแล้วแยกได้อิสระกว่า ส่วนในสารละลาย solvent cage ทำให้คู่โมเลกุลเกิด encounter และอาจชนซ้ำก่อนแยก",["แก๊สชนแล้วแยก สารละลายมี solvent cage และ encounter","solution encounter ถูกกักด้วยตัวทำละลายและชนซ้ำได้","ในสารละลายเกิด encounter pair จาก solvent cage"],162,["K-P1-162"],"อธิบายผลของ physical environment ต่อการชน",["นึกถึงโมเลกุลตัวทำละลายรอบคู่ชน","เปรียบเทียบการหลุดออกจากกัน","ใช้คำว่า solvent cage และ encounter"],"กล่าวว่าสารละลายไม่มีการชน",[],"collision-encounter-comparison"),
]

# E02: 1 easy, 1 medium
Q += [
mcq("P-E-007","E02","easy","ในตัวกลางเดียวกัน ถ้า relative permittivity εr ลดลง โดยระยะและประจุคงที่ แรงไฟฟ้ามีแนวโน้มอย่างไร?","B",[("A","ลดลง"),("B","เพิ่มขึ้น"),("C","คงที่"),("D","เป็นศูนย์")],{"A":"แรงแปรผกผันกับ εr","B":"εr ลดจึงแรงเพิ่ม","C":"ละเลยสมบัติตัวกลาง","D":"ไม่มีเหตุผลให้เป็นศูนย์"},18,["E-P1-018"],"ตีความผลของ dielectric constant ต่อ electrostatic interaction",["ใช้รูปแปรผกผัน","F∝1/εr","ตัวหารลดลงทำให้ค่าเพิ่ม"],"คิดว่า εr ลดแล้วแรงลดตาม",[],"conceptual-graph-interpretation"),
concept("P-E-008","E02","medium","จากข้อมูลผู้สอน น้ำมี εr≈78.54 ที่ 25 °C และ ≈55.33 ที่ 100 °C สรุปแนวโน้มใดได้โดยไม่ overgeneralize?","สำหรับน้ำในช่วงข้อมูลนี้ εr ลดลงเมื่ออุณหภูมิเพิ่มจาก 25 เป็น 100 °C",["epsilon r ของน้ำลดลงเมื่ออุณหภูมิเพิ่มในช่วง 25 ถึง 100 c","ค่าคงที่ไดอิเล็กทริกของน้ำลดลงจาก 78.54 เป็น 55.33","สำหรับน้ำช่วงนี้ relative permittivity ลดเมื่อ temperature เพิ่ม"],18,["E-P1-018"],"ตีความกราฟ dielectric constant ภายในช่วงที่ให้",["ระบุสารและช่วงอุณหภูมิ","เปรียบเทียบ 78.54 กับ 55.33","หลีกเลี่ยงคำว่า solvent ทุกชนิด"],"สรุปว่าตัวทำละลายทุกชนิดมีแนวโน้มเหมือนกัน",[],"conceptual-graph-interpretation"),
]

# E03: 1 easy, 2 medium, 2 hard
Q += [
mcq("P-E-009","E03","easy","หน่วยใดตรงกับ conductance G?","A",[("A","S"),("B","Ω"),("C","S cm^-1"),("D","S cm² mol^-1")],{"A":"Siemens เป็นหน่วย conductance","B":"Ω เป็น resistance","C":"เป็น conductivity","D":"เป็น molar conductivity"},13,["E-P1-013"],"แยกคำศัพท์ สัญลักษณ์ และหน่วยทางไฟฟ้า",["G เป็นส่วนกลับของ R","หน่วยส่วนกลับของ ohm คือ siemens","เลือก S"],"สับสน G กับ κ หรือ Λm",["F-E-001"]),
num("P-E-010","E03","medium","ตัวนำมี resistance 250 Ω จงหา conductance",0.004,4e-6,"S",["F-E-001"],31,["E-P1-013"],"คำนวณ conductance จาก resistance",["G เป็นส่วนกลับของ R","ใช้ G=1/R","คำนวณ 1/250"],"R=250 Ω","G=1/R","1/250","0.00400","Ω^-1=S","ตอบ 250 S โดยไม่กลับค่า",{"op":"reciprocal","values":[250]}),
num("P-E-011","E03","medium","สารละลายมี κ=1.50×10^-4 S cm^-1 และ c=0.00200 mol L^-1 จงหา Λm",75.0,0.08,"S cm2 mol^-1",["F-E-002"],48,["E-P1-013","E-P1-048"],"คำนวณ molar conductivity พร้อมตัวประกอบ 1000",["ตรวจหน่วย κ และ c","ใช้ Λm=1000κ/c","แทน 1000(1.50e-4)/0.00200"],"κ=1.50e-4 S cm^-1, c=0.00200 mol L^-1","Λm=1000κ/c","1000(1.50e-4)/0.00200","75.0","ตัวประกอบ 1000 แปลง L เป็น cm³","ลืมตัวประกอบ 1000",{"op":"mul_div","values":[1000,1.5e-4,0.002]}),
num("P-E-012","E03","hard","เซลล์มี conductance G=2.00×10^-4 S และ cell constant=1.25 cm^-1 จงหา conductivity κ",0.00025,2.5e-7,"S cm^-1",["F-E-001"],34,["E-P1-013"],"เชื่อม conductance กับ cell geometry",["κ เท่ากับ G คูณ cell constant","ตรวจหน่วย S×cm^-1","คำนวณ 2.00e-4×1.25"],"G=2.00e-4 S, cell constant=1.25 cm^-1","κ=G(l/A)=G×cell constant","(2.00e-4)(1.25)","2.50e-4","S×cm^-1=S cm^-1","หารด้วย cell constant แทนคูณ",{"op":"product","values":[2e-4,1.25]}),
num("P-E-013","E03","hard","AgBr solution มี κsolution=8.20×10^-8 และ κwater=1.70×10^-8 S cm^-1; Λ°AgBr=130.0 S cm² mol^-1 จงหา Ksp โดยสมมติ AgBr แตกตัวสมบูรณ์",2.5e-13,3e-15,None,["F-E-005"],66,["E-P1-066"],"คำนวณ solubility และ Ksp จาก corrected conductivity",["ลบ solvent blank ก่อน","หา S=1000κ/Λ°","κ=6.50e-8 แล้ว S=5.00e-7 M และ Ksp=S²"],"κsolution=8.20e-8, κwater=1.70e-8 S cm^-1, Λ°=130.0","κ=κsolution-κwater; S=1000κ/Λ°; Ksp=S²","κ=6.50e-8; S=1000(6.50e-8)/130.0=5.00e-7","Ksp=(5.00e-7)^2=2.50e-13","S เป็น mol L^-1; Ksp สำหรับ 1:1 มีหน่วยเชิง concentration² แต่มักรายงานไร้หน่วยเชิง thermodynamic","นำ conductivity ของน้ำไปรวมแทนลบ",{"op":"agbr_ksp","values":[8.20e-8,1.70e-8,130.0]},"multi-step-calculation"),
]

# E04: 1 easy, 2 medium, 1 hard
Q += [
num("P-E-014","E04","easy","weak electrolyte มี Λm=25.0 และ Λ°m=400.0 S cm² mol^-1 จงหา degree of dissociation α",0.0625,0.0001,None,["F-E-003"],48,["E-P1-048"],"คำนวณ degree of dissociation",["α เป็นอัตราส่วน conductivity","ใช้ α=Λm/Λ°m","คำนวณ 25.0/400.0"],"Λm=25.0, Λ°m=400.0","α=Λm/Λ°m","25.0/400.0","0.0625","หน่วยเหมือนกันตัดกัน","รายงาน 6.25 เป็น α แทน 0.0625",{"op":"div","values":[25,400]}),
mcq("P-E-015","E04","medium","ข้อใดเป็นเงื่อนไขที่เหมาะกับ Ostwald dilution law ในบทนี้?","C",[("A","strong electrolyte เข้มข้น"),("B","สารไม่แตกตัว"),("C","weak 1:1 electrolyte ในสารละลายเจือจาง"),("D","ของแข็งไอออนิกบริสุทธิ์")],{"A":"strong electrolyte ไม่เป็นไปตามสมมติฐานการแตกตัวแบบ weak","B":"ไม่มี equilibrium dissociation ให้คำนวณ","C":"ตรงกับแบบจำลองที่ใช้","D":"ไม่ใช่สารละลาย"},48,["E-P1-048"],"ระบุ validity condition ของ Ostwald dilution law",["พิจารณาว่าสมการใช้ degree of dissociation","ต้องมี equilibrium ของ weak electrolyte","เลือก weak 1:1 dilute solution"],"นำกฎไปใช้กับ strong electrolyte",["F-E-004"]),
num("P-E-016","E04","medium","กรดอ่อนโมโนโปรติก c=0.0100 M และ α=0.0400 จงหา Ka ด้วย Ostwald law",1.667e-5,2e-8,None,["F-E-004"],48,["E-P1-048"],"คำนวณ Ka จาก concentration และ degree of dissociation",["ใช้ Ka=cα²/(1-α)","คำนวณ α² ก่อน","แทน 0.0100(0.0400)²/0.960"],"c=0.0100 M, α=0.0400","Ka=cα²/(1-α)","0.0100(0.0400)^2/(0.960)","1.667e-5","thermodynamic Ka มักรายงานไร้หน่วยภายใต้มาตรฐาน activity","ประมาณ 1-α=1 โดยไม่บอกสมมติฐาน",{"op":"ostwald","values":[0.0100,0.0400]}),
num("P-E-017","E04","hard","สารละลาย weak acid c=0.00500 M มี Λm=30.0 และ Λ°m=390.0 S cm² mol^-1 จงหา Ka",3.205e-5,4e-8,None,["F-E-003","F-E-004"],48,["E-P1-048"],"คำนวณ α แล้วหา Ka แบบหลายขั้น",["หา α จาก conductivity ก่อน","α=30.0/390.0","แทน α ใน cα²/(1-α)"],"c=0.00500 M, Λm=30.0, Λ°m=390.0","α=Λm/Λ°m; Ka=cα²/(1-α)","α=0.076923; Ka=0.00500(0.076923)^2/(0.923077)","3.205e-5","α ไร้หน่วย; ใช้ concentration scale ตามโจทย์","ใช้ Λm เป็น α โดยตรง",{"op":"conductivity_ka","values":[0.005,30,390]},"multi-step-calculation"),
]

# E06: 1 easy, 2 medium, 2 hard
Q += [
num("P-E-018","E06","easy","สารละลาย 0.0100 M NaCl มี ionic strength เท่าใด",0.01,1e-5,"mol L^-1",["F-E-006"],83,["E-P1-083"],"คำนวณ ionic strength ของ 1:1 electrolyte",["แตก NaCl เป็น Na+ และ Cl-","ใช้ I=1/2Σcizi²","รวม 0.0100(1)² สองชนิด"],"[Na+]=[Cl-]=0.0100 M, z=±1","I=1/2Σcizi²","0.5[0.0100+0.0100]","0.0100","concentration scale เป็น mol L^-1","ลืมตัวคูณ 1/2",{"op":"ionic_strength","terms":[[0.01,1],[0.01,-1]]}),
num("P-E-019","E06","medium","สารละลาย 0.0200 M CaCl2 มี ionic strength เท่าใด",0.06,6e-5,"mol L^-1",["F-E-006"],83,["E-P1-083"],"รวมความเข้มข้นและประจุของทุกไอออน",["[Cl-] เป็นสองเท่าของ salt concentration","ใช้ z² จึงไม่มีเครื่องหมายลบ","I=1/2[0.0200(2²)+0.0400(1²)]"],"[Ca2+]=0.0200 M, [Cl-]=0.0400 M","I=1/2Σcizi²","0.5[0.0200(4)+0.0400(1)]","0.0600","แต่ละพจน์เป็น mol L^-1","ใช้ [Cl-]=0.0200 M",{"op":"ionic_strength","terms":[[0.02,2],[0.04,-1]]}),
mcq("P-E-020","E06","medium","ข้อใดอธิบายข้อจำกัดของ Debye-Hückel limiting law ได้ถูกต้องที่สุด?","B",[("A","ใช้ได้แม่นยำกับสารละลายเข้มข้นทุกชนิด"),("B","เหมาะกับสารละลายเจือจางมากและต้องระบุ solvent/temperature"),("C","ใช้ได้เฉพาะ non-electrolyte"),("D","ไม่ขึ้นกับประจุไอออน")],{"A":"limiting law เสื่อมความแม่นยำเมื่อ I สูง","B":"ตรงกับเงื่อนไขของกฎ","C":"กฎอธิบาย ionic activity","D":"มี z+z- ในสมการ"},83,["E-P1-083"],"ระบุ validity assumptions ของ DHLL",["คำว่า limiting บอกช่วงใช้งาน","พิจารณา ionic strength ต่ำ","ค่าคงที่ A ขึ้นกับ solvent และ temperature"],"ใช้ DHLL นอกช่วงโดยไม่ qualification",["F-E-007"]),
num("P-E-021","E06","hard","ที่ 298 K ในน้ำ ใช้ log10γ±=-0.509|z+z-|√I สำหรับ MgCl2 ที่ I=0.0300 M จงหา γ±",0.6664,0.001,None,["F-E-007"],83,["E-P1-083"],"คำนวณ mean ionic activity coefficient ด้วย DHLL",["สำหรับ MgCl2 ใช้ |z+z-|=2","คำนวณ log10γ± ก่อน","logγ=-0.509(2)√0.0300 แล้วทำ 10^x"],"I=0.0300 M, |z+z-|=2, A=0.509","log10γ±=-A|z+z-|√I","logγ=-0.17632","γ=10^-0.17632=0.6664","γ เป็นอัตราส่วนไร้หน่วย","ใช้ผลคูณประจุเป็น 4 แทน |2×1|",{"op":"dhll","values":[0.509,2,0.03]}),
num("P-E-022","E06","hard","สารละลาย CaCl2 มี c=0.00500 M และ γ±=0.75 จงหา mean ionic activity a± บน concentration scale ที่นิยาม a±=γ±(c+ c-²)^(1/3)",0.005953,7e-6,"mol L^-1",["F-E-008"],83,["E-P1-083"],"คำนวณ mean ionic activity สำหรับ electrolyte 1:2",["แตกตัวให้ c+=0.00500 และ c-=0.0100 M","ใช้ geometric stoichiometric mean","คำนวณ 0.75(0.00500×0.0100²)^(1/3)"],"c+=0.00500 M, c-=0.0100 M, γ±=0.75","a±=γ±(c+ c-²)^(1/3)","0.75(0.00500×0.0100²)^(1/3)","0.005953","ตาม concentration convention ที่โจทย์กำหนด ได้ mol L^-1","ใช้ c ของเกลือแทน concentration ของ Cl-",{"op":"mean_activity_12","values":[0.75,0.005,0.010]},"multi-step-calculation"),
]

# E07: 2 easy, 1 medium
Q += [
mcq("P-E-023","E07","easy","ตามคำอธิบายผู้สอน salting-in หมายถึงข้อใด?","A",[("A","การเติม electrolyte ช่วงหนึ่งทำให้ apparent solubility เพิ่ม"),("B","การเติม electrolyte ทำให้ solubility ลดเสมอ"),("C","เกลือตกตะกอนทันทีทุกกรณี"),("D","ionic strength เป็นศูนย์")],{"A":"เป็นนิยามเชิงแนวโน้มของ salting-in","B":"อธิบาย salting-out และ overgeneralize","C":"ไม่ใช่ความหมายทั่วไป","D":"การเติม electrolyte ทำให้ I ไม่เป็นศูนย์"},89,["E-P1-089"],"แยก salting-in จาก salting-out",["ดูทิศทางการเปลี่ยน solubility","คำว่า in สื่อถึงสารอยู่ในสารละลายมากขึ้น","เลือก solubility เพิ่ม"],"จำสลับ salting-in/out",["F-E-006","F-E-007"]),
mcq("P-E-024","E07","easy","เหตุใดจึงไม่ควรสรุปว่าเติมเกลือแล้ว solubility ต้องเพิ่มเสมอ?","C",[("A","เพราะ ionic strength ไม่เคยเปลี่ยน"),("B","เพราะ activity coefficient เท่ากับ 1 เสมอ"),("C","เพราะช่วง ionic strength และ specific interactions อาจทำให้เกิด salting-in หรือ salting-out"),("D","เพราะเกลือไม่มีไอออน")],{"A":"เติม electrolyte ย่อมเปลี่ยน ionic environment","B":"γ เบี่ยงเบนจาก 1 ได้","C":"แนวโน้มขึ้นกับ regime/interaction","D":"เกลือแตกตัวเป็นไอออน"},89,["E-P1-089"],"ตีความเงื่อนไขที่ทำให้ salting trend ต่างกัน",["หลีกเลี่ยงคำว่าเสมอ","พิจารณาทั้ง low/high ionic strength","specific interaction มีบทบาทได้"],"ใช้กฎช่วงเจือจางกับทุกความเข้มข้น",["F-E-006","F-E-007"]),
concept("P-E-025","E07","medium","อธิบายความต่างเชิงคุณภาพระหว่าง salting-in และ salting-out โดยอ้างอิง solubility","salting-in คือ solubility เพิ่มเมื่อเพิ่ม electrolyte ในช่วงที่พิจารณา ส่วน salting-out คือ solubility ลดลงเมื่อ electrolyte สูงขึ้นหรือเกิด specific interactions ที่ลดการละลาย",["salting in solubility เพิ่ม salting out solubility ลด","salting-in เพิ่มการละลาย ส่วน salting-out ลดการละลาย","การละลายเพิ่มใน salting in และลดใน salting out"],89,["E-P1-089"],"อธิบาย salting effects โดยไม่ overgeneralize",["ตอบเป็นทิศทาง solubility","ระบุว่าขึ้นกับช่วง/เงื่อนไข","เปรียบเทียบ increase กับ decrease"],"อธิบายทั้งสองคำว่าเหมือนกัน",["F-E-006","F-E-007"]),
]

# E09: 1 easy, 2 medium, 1 hard
Q += [
mcq("P-E-026","E09","easy","ใน galvanic cell ข้อใดถูกต้อง?","B",[("A","oxidation ที่ cathode"),("B","oxidation ที่ anode และ electron ไหลจาก anode ไป cathode"),("C","electron ไหลผ่าน salt bridge"),("D","anode เป็นขั้วบวกเสมอทุกเซลล์")],{"A":"reduction เกิดที่ cathode","B":"ถูกทั้งตำแหน่ง oxidation และทิศ electron","C":"electron ไหลในวงจรภายนอก; ions เคลื่อนผ่าน salt bridge","D":"เครื่องหมายขึ้นกับชนิดเซลล์"},95,["E-P1-095"],"ระบุ anode/cathode และ electron flow",["จำ AnOx RedCat","electron ออกจากแหล่ง oxidation","เลือก oxidation at anode"],"จำเครื่องหมายขั้วแทนกระบวนการ",["F-E-009"]),
mcq("P-E-027","E09","medium","cell notation ใดตรงกับ Zn(s)|Zn2+(aq)||Cu2+(aq)|Cu(s) ที่ทำงานเป็น galvanic cell?","A",[("A","Zn เป็น anode ซ้าย; Cu เป็น cathode ขวา"),("B","Cu ถูก oxidize ที่ขวา"),("C","electron ไหลจาก Cu ไป Zn"),("D","double line คือเส้นลวดโลหะ")],{"A":"notation วาง anode ซ้าย cathode ขวา","B":"Cu2+ ถูก reduce","C":"electron ไหล Zn→Cu","D":"double line แทน salt bridge/liquid junction"},95,["E-P1-095"],"ตีความ electrochemical cell notation",["อ่านซ้ายเป็น oxidation","ขวาเป็น reduction","double line คือ salt bridge"],"อ่าน notation จากขวาไปซ้าย",["F-E-009"],"electrochemical-cell-notation"),
num("P-E-028","E09","medium","E°red(Cu2+/Cu)=+0.340 V และ E°red(Zn2+/Zn)=-0.763 V จงหา E°cell สำหรับ Zn|Zn2+||Cu2+|Cu",1.103,0.002,"V",["F-E-009"],108,["E-P1-095","E-P1-108"],"คำนวณ standard cell potential จาก reduction potentials",["Cu เป็น cathode","ใช้ Ecell=Ecathode-Eanode","คำนวณ 0.340-(-0.763)"],"Ecathode=0.340 V, Eanode=-0.763 V","E°cell=E°cathode-E°anode","0.340-(-0.763)","1.103","ผลต่างศักย์มีหน่วย V","กลับเครื่องหมาย reduction potential ก่อนแล้วลบซ้ำ",{"op":"subtract","values":[0.340,-0.763]}),
num("P-E-029","E09","hard","เซลล์ใช้ E°red(A+/A)=+0.80 V และ E°red(B2+/B)=-0.20 V ถ้าปฏิกิริยา spontaneous ให้อิเล็กตรอน 2 mol จงหา E°cell",1.0,0.001,"V",["F-E-009"],108,["E-P1-108"],"เลือก cathode/anode และคำนวณ E°cell โดยไม่คูณศักย์ด้วยสัมประสิทธิ์",["คู่ที่ E°red สูงกว่าเป็น cathode","ศักย์ไม่คูณด้วยจำนวน electron","คำนวณ 0.80-(-0.20)"],"E°red,A=0.80 V, E°red,B=-0.20 V, n=2","E°cell=E°cathode-E°anode","0.80-(-0.20)","1.00","V เป็น intensive quantity ไม่คูณด้วย n","คูณ E° ครึ่งเซลล์ด้วย 2 เพื่อ balance electron",{"op":"subtract","values":[0.80,-0.20]}),
]

# E10: 1 easy, 2 medium, 1 hard
Q += [
mcq("P-E-030","E10","easy","ถ้า E°cell>0 ที่อุณหภูมิและ standard state ที่กำหนด ข้อใดถูกต้อง?","A",[("A","ΔG°<0 และ K>1"),("B","ΔG°>0 และ K<1"),("C","ΔG°=0 เสมอ"),("D","บอกทิศ spontaneous ไม่ได้")],{"A":"ΔG°=-nFE° และ lnK=nFE°/RT","B":"เครื่องหมายกลับกัน","C":"เกิดเมื่อ equilibrium/E=0","D":"E° บอก thermodynamic direction ได้"},108,["E-P1-108"],"เชื่อมเครื่องหมาย E°, ΔG° และ K",["ใช้ ΔG°=-nFE°","E° บวกทำให้ ΔG° ลบ","lnK เป็นบวกจึง K>1"],"จำเครื่องหมาย ΔG° ผิด",["F-E-010","F-E-012"]),
num("P-E-031","E10","medium","เซลล์มี E°=0.250 V และ n=2 จงหา ΔG° โดยใช้ F=96485 C mol^-1",-48242.5,50,"J mol^-1",["F-E-010"],108,["E-P1-108"],"คำนวณ standard Gibbs energy จาก E°cell",["รักษาเครื่องหมายลบใน ΔG°=-nFE°","แทน n=2","คำนวณ -2×96485×0.250"],"E°=0.250 V, n=2, F=96485 C mol^-1","ΔG°=-nFE°","-2(96485)(0.250)","-4.82425e4","C mol^-1×J C^-1=J mol^-1","ละเครื่องหมายลบ",{"op":"neg_product","values":[2,96485,0.250]}),
num("P-E-032","E10","medium","ที่ 298.15 K เซลล์ n=1 มี E°=0.1183 V จงหา K โดยใช้ log10K=nE°/0.05916",100.0,0.2,None,["F-E-012"],108,["E-P1-108"],"คำนวณ equilibrium constant จาก E°",["ใช้สมการฐานสิบที่ 298 K","หา log10K ก่อน","0.1183/0.05916≈2 แล้ว K=10²"],"n=1, E°=0.1183 V, T=298.15 K","log10K=nE°/0.05916","log10K=0.1183/0.05916≈2.000","K≈100","K เป็นอัตราส่วน activity จึงไร้หน่วย","ตอบ logK แทน K",{"op":"equilibrium_k","values":[1,0.1183,0.05916]}),
num("P-E-033","E10","hard","ที่ 298.15 K เซลล์ n=2 มี E°=0.300 V และ reaction quotient Q=100 จงหา E จาก E=E°-(0.05916/n)log10Q",0.24084,0.0003,"V",["F-E-011"],119,["E-P1-108"],"ใช้ Nernst equation แยก standard และ non-standard potential",["Q=100 ทำให้ logQ=2","หาร 0.05916 ด้วย n=2","E=0.300-(0.05916/2)(2)"],"E°=0.300 V, n=2, Q=100, T=298.15 K","E=E°-(0.05916/n)log10Q","0.300-(0.05916/2)(2)","0.24084","ทุกพจน์ศักย์เป็น V","ใช้ lnQ กับค่าคงที่ 0.05916 ซึ่งเป็น log10",{"op":"nernst_298","values":[0.300,0.05916,2,100]},"multi-step-calculation"),
]

existing_doc = json.loads(PROBLEM_PATH.read_text(encoding="utf-8"))
existing = existing_doc["problems"]
if len(existing) != 11 or {x["id"] for x in existing} != {"P-K-001","P-K-002","P-K-003","P-K-004","P-K-005","P-E-001","P-E-002","P-E-003","P-E-004","P-E-005","P-E-006"}:
    raise SystemExit("Baseline differs from reviewed Phase 7A set; refusing to overwrite")
if len(Q) != 54 or len({x["id"] for x in Q}) != 54:
    raise SystemExit(f"Expected 54 unique new questions, got {len(Q)}")
if {x["id"] for x in existing} & {x["id"] for x in Q}:
    raise SystemExit("New IDs collide with legacy IDs")

result = {**existing_doc, "schema_version": "2.0.0", "phase_7b_metadata": {
    "legacy_problem_count": 11, "new_problem_count": 54, "active_problem_count": 65,
    "new_questions_validation_status": "VALIDATED"
}, "problems": existing + Q}
text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
PROBLEM_PATH.write_text(text, encoding="utf-8")
WEB_PATH.write_text(text, encoding="utf-8")
print("Wrote 54 validated additions; total active problems: 65")
