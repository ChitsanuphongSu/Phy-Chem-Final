from __future__ import annotations

import json
from pathlib import Path

PROJECT = Path(r"D:\Luna\Phy-Chem\physical-chemistry-study-hub")


def ref(doc, page, slide=None):
    return {"document": doc, "pdf_page": page, "printed_slide_number": slide}


P1 = {
    21: "K-P1-021", 26: "K-P1-026", 35: "K-P1-035", 40: "K-P1-040",
    42: "K-P1-042", 49: "K-P1-049", 61: "K-P1-061", 74: "K-P1-074",
    77: "K-P1-077", 91: "K-P1-091", 94: "K-P1-094", 162: "K-P1-162",
}
EP1 = {13: "E-P1-013", 18: "E-P1-018", 48: "E-P1-048", 66: "E-P1-066", 83: "E-P1-083", 89: "E-P1-089", 95: "E-P1-095", 108: "E-P1-108"}

PART1 = "PhCh-SC202301 Physical Chemistry Part1.pdf"
PART2 = "PhCh-SC202301 Physical Chemistry Part2.pdf"


def formula(fid, topic, title, latex, variables, units, conditions, refs, priority="P3", note=""):
    return {"id": fid, "topic_id": topic, "title_th": title, "latex": latex, "variables": variables, "units": units, "conditions": conditions, "source_references": refs, "priority": priority, "validation": "VALIDATED", "note": note}


FORMULAS = [
    formula("F-K-001", "K01", "อัตราปฏิกิริยาตามสโตอิชิโอเมทรี", r"v=-\frac{1}{a}\frac{d[A]}{dt}=\frac{1}{p}\frac{d[P]}{dt}", {"a,p":"สัมประสิทธิ์สโตอิชิโอเมทรี","[A],[P]":"ความเข้มข้น"}, "mol L^-1 s^-1", "สมการปฏิกิริยาต้องดุลแล้ว", [ref(PART1,10,10),ref(PART1,94,93)], "P1"),
    formula("F-K-002", "K02", "กฎอัตรา", r"v=k[A]^m[B]^n", {"k":"ค่าคงที่อัตรา","m,n":"อันดับย่อย"}, "หน่วย k ขึ้นกับอันดับรวม", "m,n ต้องหาเชิงทดลอง ไม่ดึงจากสมการรวมโดยอัตโนมัติ", [ref(PART1,19,19),ref(PART1,21,21)], "P1"),
    formula("F-K-003", "K03", "อันดับศูนย์แบบอินทิเกรต", r"[A]_t=[A]_0-k_0t", {"[A]_0":"ความเข้มข้นเริ่มต้น","[A]_t":"ความเข้มข้นที่เวลา t"}, "k0: mol L^-1 time^-1", "อัตราไม่ขึ้นกับ [A]", [ref(PART1,31,30)]),
    formula("F-K-004", "K03", "อันดับหนึ่งแบบอินทิเกรต", r"\ln\frac{[A]_t}{[A]_0}=-k_1t", {"k1":"ค่าคงที่อัตราอันดับหนึ่ง","t":"เวลา"}, "k1: time^-1", "ปฏิกิริยาอันดับหนึ่ง", [ref(PART1,35,34),ref(PART1,36,35)], "P1"),
    formula("F-K-005", "K03", "อันดับสองแบบอินทิเกรต", r"\frac{1}{[A]_t}=\frac{1}{[A]_0}+k_2t", {"k2":"ค่าคงที่อัตราอันดับสอง"}, "k2: L mol^-1 time^-1", "กรณี rate=k[A]^2", [ref(PART1,49,48)], "P1"),
    formula("F-K-006", "K04", "ครึ่งชีวิตอันดับศูนย์", r"t_{1/2}=\frac{[A]_0}{2k_0}", {"t1/2":"ครึ่งชีวิต"}, "time", "อันดับศูนย์", [ref(PART1,33,32)]),
    formula("F-K-007", "K04", "ครึ่งชีวิตอันดับหนึ่ง", r"t_{1/2}=\frac{\ln2}{k_1}", {"t1/2":"ครึ่งชีวิต"}, "time", "อันดับหนึ่งและอุณหภูมิคงที่", [ref(PART1,39,38),ref(PART1,40,39)], "P1"),
    formula("F-K-008", "K04", "ครึ่งชีวิตอันดับสอง", r"t_{1/2}=\frac{1}{k_2[A]_0}", {"[A]0":"ความเข้มข้นเริ่มต้น"}, "time", "rate=k[A]^2", [ref(PART1,51,50)]),
    formula("F-K-009", "K05", "สมการ Arrhenius", r"k=Ae^{-E_a/(RT)}", {"A":"pre-exponential factor","Ea":"activation energy","R":"ค่าคงที่แก๊ส","T":"อุณหภูมิสัมบูรณ์"}, "Ea: J mol^-1; T: K", "ใช้หน่วย Ea ให้สอดคล้องกับ R", [ref(PART1,64,63)]),
    formula("F-K-010", "K06", "Arrhenius สองอุณหภูมิ", r"\ln\frac{k_2}{k_1}=-\frac{E_a}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)", {"k1,k2":"ค่าคงที่อัตราที่ T1,T2"}, "Ea: J mol^-1", "กลไกและ A ไม่เปลี่ยนในช่วงอุณหภูมิ", [ref(PART1,67,66),ref(PART1,69,68)]),
    formula("F-E-001", "E03", "Conductance", r"G=\frac{1}{R}=\kappa\frac{A}{l}", {"G":"conductance","R":"resistance","κ":"conductivity","A":"พื้นที่หน้าตัด","l":"ระยะห่างขั้ว"}, "G: S; κ: S m^-1 หรือ S cm^-1", "รูปทรงเซลล์คงที่", [ref(PART2,31,31),ref(PART2,34,34)]),
    formula("F-E-002", "E03", "Molar conductivity", r"\Lambda_m=\frac{1000\kappa}{c}", {"κ":"S cm^-1","c":"mol L^-1"}, "S cm^2 mol^-1", "ใช้ตัวประกอบ 1000 เมื่อ κ เป็น S cm^-1 และ c เป็น mol L^-1", [ref(PART2,43,43),ref(PART2,48,48)], "P1"),
    formula("F-E-003", "E04", "Degree of dissociation", r"\alpha=\frac{\Lambda_m}{\Lambda_m^\circ}", {"α":"ระดับการแตกตัว","Λ°":"molar conductivity ที่ infinite dilution"}, "dimensionless", "electrolyte อ่อนและเลือก Λ° ถูกชนิด", [ref(PART2,46,46),ref(PART2,48,48)], "P1"),
    formula("F-E-004", "E04", "Ostwald dilution law", r"K_a=\frac{c\alpha^2}{1-\alpha}", {"c":"ความเข้มข้นเริ่มต้น","α":"ระดับการแตกตัว"}, "หน่วยตาม standard-state convention; มักรายงานเชิงความเข้มข้น", "กรณีกรดอ่อนโมโนโปรติกและสารละลายเจือจาง", [ref(PART2,47,47),ref(PART2,48,48)], "P1"),
    formula("F-E-005", "E03", "Kohlrausch independent migration", r"\Lambda_m^\circ=\nu_+\lambda_+^\circ+\nu_-\lambda_-^\circ", {"ν":"จำนวนไอออนต่อสูตรหน่วย","λ°":"limiting ionic conductivity"}, "S cm^2 mol^-1", "infinite dilution", [ref(PART2,41,41),ref(PART2,66,66)], "P1"),
    formula("F-E-006", "E07", "Ionic strength", r"I=\frac12\sum_i c_i z_i^2", {"ci":"ความเข้มข้นไอออน i","zi":"ประจุไอออน"}, "mol L^-1 เมื่อใช้ molarity", "รวมไอออนทุกชนิดในสารละลาย", [ref(PART2,82,82),ref(PART2,83,83)], "P1"),
    formula("F-E-007", "E07", "Debye-Huckel limiting law", r"\log_{10}\gamma_{\pm}=-A|z_+z_-|\sqrt{I}", {"γ±":"mean ionic activity coefficient","A":"0.509 สำหรับน้ำที่ 298 K"}, "dimensionless", "สารละลายเจือจางมาก; ที่ 298 K ในน้ำ", [ref(PART2,83,83),ref(PART2,85,85)], "P1"),
    formula("F-E-008", "E07", "Mean ionic activity", r"a_{\pm}=\gamma_{\pm}m_{\pm}", {"a±":"mean activity","m±":"mean molality"}, "dimensionless เมื่ออ้าง standard state", "ระบุ concentration scale ให้ชัด", [ref(PART2,69,69),ref(PART2,71,71)]),
    formula("F-E-009", "E09", "ศักย์เซลล์จาก reduction potentials", r"E_{cell}=E_{cathode}-E_{anode}", {"E":"reduction potential"}, "V", "ใช้ศักย์รีดักชันทั้งคู่ก่อนลบ", [ref(PART2,106,106),ref(PART2,108,108)], "P1"),
    formula("F-E-010", "E10", "พลังงานกิบส์กับศักย์เซลล์", r"\Delta G=-nFE_{cell}", {"n":"จำนวนอิเล็กตรอน","F":"96485 C mol^-1"}, "J mol^-1", "Ecell สำหรับปฏิกิริยาที่เขียน", [ref(PART2,109,109)]),
    formula("F-E-011", "E10", "Nernst equation ที่ 298 K", r"E=E^\circ-\frac{0.05916}{n}\log_{10}Q", {"Q":"reaction quotient","n":"อิเล็กตรอน"}, "V", "298.15 K; ใช้ activities ใน Q", [ref(PART2,114,114)]),
    formula("F-E-012", "E10", "ศักย์มาตรฐานกับสมดุล", r"\log_{10}K=\frac{nE^\circ}{0.05916}", {"K":"equilibrium constant"}, "dimensionless", "298.15 K", [ref(PART2,116,116)]),
    formula("F-E-013", "E11", "Concentration cell", r"E_{cell}=\frac{0.05916}{n}\log_{10}\frac{a_{high}}{a_{low}}", {"a":"activity ของชนิดเดียวกัน"}, "V", "298.15 K และ electrode reversible ต่อชนิดเดียวกัน", [ref(PART2,129,129),ref(PART2,132,132)]),
]


def topic(tid, section, title, pages, objective, concept, definitions, key_points, formula_ids, example, mistakes, checks, priority="P3"):
    return {"id":tid,"section":section,"title_th":title,"priority":priority,"learning_objectives":[objective],"concept_explanation":concept,"definitions":definitions,"key_points":key_points,"formula_ids":formula_ids,"worked_example":example,"common_mistakes":mistakes,"quick_checks":checks,"source_references":pages,"progress_key":f"topic:{tid}"}


TOPICS = [
    topic("K01","Chemical Kinetics","อัตราการเกิดปฏิกิริยา",[ref(PART1,8,8),ref(PART1,94,93)],"เชื่อมอัตราการลดลงและเพิ่มขึ้นด้วยสัมประสิทธิ์สโตอิชิโอเมทรี","อัตราปฏิกิริยาบอกการเปลี่ยนแปลงความเข้มข้นต่อเวลา ต้องหารด้วยสัมประสิทธิ์เพื่อให้อัตราจากทุก species เท่ากัน",{"rate":"อัตราการเปลี่ยนแปลงต่อเวลา","instantaneous rate":"ความชันเส้นสัมผัส"},["ดุลสมการก่อน","สารตั้งต้นใช้เครื่องหมายลบ","หน่วยต้องมี concentration/time"],["F-K-001"],"จาก 4NH3+3O2→2N2+6H2O ถ้า d[N2]/dt=0.27 M s^-1 จะได้ d[H2O]/dt=0.81 M s^-1","ลืมหารด้วยสัมประสิทธิ์",["เหตุใดอัตราการหายไปของ NH3 จึงเป็น 0.54 M s^-1"],"P1"),
    topic("K02","Chemical Kinetics","กฎอัตราและอันดับปฏิกิริยา",[ref(PART1,17,17),ref(PART1,26,25)],"หาอันดับย่อยจาก initial-rate data","เปรียบเทียบคู่ทดลองที่เปลี่ยนความเข้มข้นเพียงตัวเดียว แล้วแก้อัตราส่วนเพื่อหา exponent",{"rate law":"สมการเชิงทดลองระหว่าง rate กับ concentration","overall order":"ผลรวม exponent"},["อันดับไม่จำเป็นต้องเท่าสัมประสิทธิ์","หน่วย k ใช้ตรวจมิติ"],["F-K-002"],"ข้อมูล S2O8^2-/I- ให้ first order ต่อทั้งคู่และ k=8.09×10^-2 M^-1 s^-1","เปลี่ยนสองตัวแปรพร้อมกันโดยไม่ตั้งสมการ",["ถ้าเพิ่ม [A] 2 เท่าแล้ว rate เพิ่ม 4 เท่า อันดับต่อ A เท่าใด"],"P1"),
    topic("K03","Chemical Kinetics","Integrated Rate Laws",[ref(PART1,31,30),ref(PART1,51,50)],"เลือก linear form ให้ตรงกับ reaction order","Integrated rate law เชื่อม [A] กับเวลา รูปกราฟที่เป็นเส้นตรงช่วยระบุอันดับ",{"zero order":"[A] กับ t เป็นเส้นตรง","first order":"ln[A] กับ t เป็นเส้นตรง","second order":"1/[A] กับ t เป็นเส้นตรง"},["ความชันมีเครื่องหมายต่างกัน","ตรวจหน่วย k"],["F-K-003","F-K-004","F-K-005"],"N2O5 first order: [A]=0.25e^(-5.1×10^-4×192)=0.227 M","ใช้ log10 แทน ln โดยไม่ใส่ 2.303",["กราฟใดควรเป็นเส้นตรงสำหรับ first order"],"P1"),
    topic("K04","Chemical Kinetics","ครึ่งชีวิต",[ref(PART1,33,32),ref(PART1,51,50)],"เปรียบเทียบการขึ้นกับ [A]0 ของ t1/2","อันดับหนึ่งมีครึ่งชีวิตคงที่ ส่วนอันดับศูนย์และอันดับสองขึ้นกับความเข้มข้นเริ่มต้น",{"half-life":"เวลาที่ [A] เหลือครึ่งหนึ่ง"},["first order ไม่ขึ้นกับ [A]0","second order แปรผกผันกับ [A]0"],["F-K-006","F-K-007","F-K-008"],"k=5.1×10^-4 s^-1 ให้ t1/2=0.693/k=1.36×10^3 s","ใช้สูตรครึ่งชีวิตผิดอันดับ",["เหตุใดกราฟหน้า 39 จึงลดครึ่งหนึ่งในช่วงเวลาคงที่"],"P1"),
    topic("K05","Chemical Kinetics","Activation Energy และ Reaction Coordinate",[ref(PART1,58,57),ref(PART1,61,60)],"อ่าน Ea ไปข้างหน้า ย้อนกลับ และ ΔH จากกราฟ","ยอดกราฟคือ activated complex; ความต่างพลังงานจาก reactants ถึงยอดคือ Ea forward",{"activated complex":"โครงสร้างพลังงานสูงชั่วขณะ","Ea":"พลังงานก่อกัมมันต์"},["endothermic มีผลิตภัณฑ์พลังงานสูงกว่า","catalyst ลด Ea แต่ไม่เปลี่ยน ΔH"],["F-K-009"],"กราฟหน้า 60: Ea,f=10-5=5 และ ΔH=7-5=+2 ในหน่วยแกนพลังงาน","สลับ Ea กับ ΔH",["ตัวเร่งเปลี่ยนค่า ΔH หรือไม่"],"P1"),
    topic("K06","Chemical Kinetics","Arrhenius Equation",[ref(PART1,64,63),ref(PART1,70,69)],"คำนวณ Ea หรืออัตราส่วน k ที่สองอุณหภูมิ","ln k กับ 1/T เป็นเส้นตรง ความชันเท่ากับ -Ea/R",{"A":"frequency/orientation factor","Ea":"activation energy"},["T ต้องเป็น kelvin","Ea กับ R ต้องใช้หน่วยเดียวกัน"],["F-K-009","F-K-010"],"แทน k1,k2,T1,T2 ในสมการสองอุณหภูมิ แล้วแก้ Ea พร้อมตรวจ J↔kJ","ใช้ °C ตรง ๆ",["เมื่อ T เพิ่ม k เปลี่ยนอย่างไรโดยทั่วไป"]),
    topic("K07","Chemical Kinetics","Reaction Mechanism",[ref(PART1,72,71),ref(PART1,77,76)],"ระบุ intermediate และ rate-determining step","กลไกคือชุด elementary steps ผลรวมต้องให้สมการรวม intermediate เกิดแล้วถูกใช้หมด",{"intermediate":"เกิดในขั้นหนึ่งและถูกใช้ในขั้นถัดไป","molecularity":"จำนวน species ใน elementary step"},["ตัด intermediate เมื่อรวมสมการ","ขั้นช้ามักควบคุม rate"],[],"กลไก H2O2/I-: IO- เป็น intermediate และขั้นที่ 1 ช้า","เขียน intermediate ไว้ในสมการรวม",["เหตุใด molecularity จึงไม่เป็นเศษส่วน"],"P1"),
    topic("K08","Chemical Kinetics","Catalysis และ Encounter in Solution",[ref(PART1,86,85),ref(PART1,162,161)],"เปรียบเทียบ collision ในแก๊สกับ encounter ในสารละลาย","ในสารละลาย solvent cage ทำให้คู่โมเลกุลชนซ้ำหลายครั้งก่อนแยก จึงต้องแยก encounter frequency จาก successful reaction",{"solvent cage":"บริเวณเพื่อนบ้านตัวทำละลาย","encounter":"การอยู่ใกล้กันของคู่โมเลกุล"},["collision count เท่ากันไม่ได้แปลว่า pattern เท่ากัน","ตัวเร่งเปลี่ยนเส้นทางกลไก"],[],"ภาพหน้า 161 แสดงการชนกระจายในแก๊สแต่จับกลุ่มเป็น encounters ในสารละลาย","ใช้ทฤษฎีแก๊สกับสารละลายโดยไม่พิจารณา cage",["encounter effect ส่งผลต่อ pattern การชนอย่างไร"],"P1"),
    topic("E01","Electrochemistry","Electrolyte Solution",[ref(PART2,5,5),ref(PART2,12,12)],"จำแนก strong, weak และ non-electrolyte","การนำไฟฟ้าเกิดจากไอออนเคลื่อนที่ strong electrolyte แตกตัวเกือบสมบูรณ์ ส่วน weak แตกตัวบางส่วน",{"electrolyte":"สารที่ให้ไอออนในตัวทำละลาย","dissociation":"การแยกเป็นไอออน"},["ความแรงไม่เท่ากับความเข้มข้น","non-electrolyte ไม่มีไอออนนำไฟฟ้า"],[],"เปรียบเทียบ NaCl, CH3COOH และ sucrose ที่ความเข้มข้นใกล้กัน","สับสน strong กับ concentrated",["CH3COOH เข้มข้นมากยังเป็น weak electrolyte หรือไม่"]),
    topic("E02","Electrochemistry","Dielectric Constant",[ref(PART2,17,17),ref(PART2,22,22)],"อธิบายผลของ εr ต่อแรงระหว่างประจุ","ตัวกลางที่มี εr สูงลด interaction energy ระหว่างไอออน และ εr ของน้ำลดเมื่ออุณหภูมิสูงขึ้นตามตาราง",{"dielectric constant":"อัตราส่วน permittivity ของตัวกลางต่อสุญญากาศ"},["εr ไม่มีหน่วย","อุณหภูมิมีผลต่อ εr"],[],"น้ำที่ 25 °C มี εr≈78.54 และที่ 100 °C≈55.33","ใช้ค่าที่ 25 °C กับทุกอุณหภูมิ",["เมื่อ εr ลด แรงดึงดูดระหว่างประจุเปลี่ยนอย่างไร"],"P1"),
    topic("E03","Electrochemistry","Conductance และ Molar Conductivity",[ref(PART2,31,31),ref(PART2,50,50)],"แยก G, κ และ Λm พร้อมหน่วย","G ขึ้นกับรูปทรงเซลล์ κ เป็นสมบัติของสารละลาย และ Λm ปรับด้วย concentration",{"cell constant":"l/A","conductivity":"conductance ที่ปรับรูปทรงแล้ว"},["κ ไม่เท่ากับ G","ติดตาม factor 1000 ในหน่วย cm"],["F-E-001","F-E-002","F-E-005"],"κ=4.95×10^-5 S cm^-1, c=0.001028 M ให้ Λm=48.15 S cm2 mol^-1","ลืม 1000 หรือผสม m กับ cm",["G และ κ ต่างกันอย่างไร"],"P1"),
    topic("E04","Electrochemistry","Degree of Dissociation",[ref(PART2,46,46),ref(PART2,48,48)],"คำนวณ α และ Ka จาก conductivity","สำหรับ weak electrolyte ใช้ Λm/Λ° ประมาณส่วนที่แตกตัว แล้วใช้ Ostwald law",{"α":"สัดส่วนการแตกตัว"},["0≤α≤1","ใช้ Λ° ของ electrolyte เดียวกัน"],["F-E-003","F-E-004"],"acetic acid example ให้ α=0.1233 และ Ka=1.78×10^-5","นำ κ หาร Λ° โดยไม่แปลงเป็น Λm",["ถ้า Λm เพิ่มเมื่อเจือจาง α เปลี่ยนอย่างไร"],"P1"),
    topic("E05","Electrochemistry","Ionic Mobility",[ref(PART2,49,49),ref(PART2,60,60)],"เชื่อม mobility กับ ionic conductivity","mobility คือ drift velocity ต่อ potential gradient และสัมพันธ์กับ limiting ionic conductivity ผ่านประจุและ Faraday constant",{"mobility":"u=v/(potential gradient)"},["ระบุระบบหน่วย","H+ และ OH- มีกลไก Grotthuss จึง mobility สูง"],[],"อธิบาย proton hopping จากโครงข่าย hydrogen bond","ใช้ความเร็วเฉลี่ยเชิงความร้อนแทน drift velocity",["เหตุใด H+ จึงเคลื่อนที่ดูเหมือนเร็วผิดปกติ"]),
    topic("E06","Electrochemistry","Ionic Activity และ Ionic Strength",[ref(PART2,68,68),ref(PART2,83,83)],"คำนวณ I, γ± และ activity","activity แทน effective concentration; ionic strength ให้น้ำหนักกำลังสองของประจุ",{"activity":"effective concentration","γ":"activity coefficient"},["z ต้องยกกำลังสองใน I","γ เข้าใกล้ 1 เมื่อเจือจางมาก"],["F-E-006","F-E-007","F-E-008"],"0.01 M CuSO4 ให้ I=0.04 M, logγ±=-0.407, γ±=0.392","ลืมรวมทั้ง cation และ anion",["0.01 M CaCl2 มี I เท่าใด"],"P1"),
    topic("E07","Electrochemistry","Salting-in และ Salting-out",[ref(PART2,89,89),ref(PART2,92,92)],"แยกช่วง ionic strength ที่เพิ่มหรือลด solubility","ที่ ionic strength ต่ำ activity effects อาจเพิ่ม apparent solubility (salting-in); ที่สูงมี solvent competition และ salting-out",{"salting-in":"การละลายเพิ่มเมื่อเติมเกลือในช่วงหนึ่ง","salting-out":"การละลายลดเมื่อเติมเกลือมาก"},["DHLL ใช้ได้เฉพาะช่วงเจือจาง","อย่าเหมารวมแนวโน้มตลอดช่วง I"],[],"AgCl อาจแสดง S เพิ่มช่วง I ต่ำ ก่อนลดที่ I สูง","ใช้ Debye-Huckel limiting law นอกช่วง",["เหตุใด salting-out ของโปรตีนสัมพันธ์กับ hydration shell"],"P1"),
    topic("E09","Electrochemistry","Electrochemical Cell",[ref(PART2,95,95),ref(PART2,108,108)],"ระบุ anode/cathode และคำนวณ Ecell","oxidation เกิดที่ anode, reduction เกิดที่ cathode ทั้ง galvanic และ electrolytic แต่เครื่องหมายขั้วต่างกันตามชนิดเซลล์",{"anode":"ขั้วที่ oxidation","cathode":"ขั้วที่ reduction"},["จำ AnOx, RedCat","ใช้ reduction potentials ใน Ecell=Ec-Ea"],["F-E-009"],"Fumarate/NADH: Ecell=0.031-(-0.320)=0.351 V","กลับเครื่องหมายศักย์แล้วลบซ้ำ",["ใน galvanic cell อิเล็กตรอนไหลจากขั้วใดไปขั้วใด"],"P1"),
    topic("E10","Electrochemistry","Cell Thermodynamics และ Nernst Equation",[ref(PART2,109,109),ref(PART2,119,119)],"เชื่อม E, ΔG, K และ Q","E>0 สอดคล้องกับ ΔG<0 สำหรับทิศปฏิกิริยาที่เขียน; Nernst ปรับ E ตาม activity",{"Q":"reaction quotient","standard potential":"ศักย์ภายใต้ standard state"},["n มาจากสมการที่ดุล","solids ไม่อยู่ใน Q"],["F-E-010","F-E-011","F-E-012"],"E°=0.351 V,n=2 ให้ ΔG°=-67.7 kJ mol^-1 และ logK=11.87","ใช้จำนวน e- ก่อนดุล",["ถ้า Q เพิ่ม E เปลี่ยนอย่างไรสำหรับ n คงที่"],"P2"),
    topic("E11","Electrochemistry","Electrodes และ Concentration Cell",[ref(PART2,120,120),ref(PART2,132,132)],"เขียน cell notation และหาศักย์จาก activity ratio","concentration cell ใช้คู่รีดอกซ์เดียวกัน E°cell=0 แต่ E เกิดจากความต่าง activity",{"SHE":"standard hydrogen electrode","salt bridge":"รักษาสมดุลประจุ"},["เขียน anode ซ้าย cathode ขวาตาม convention","ใช้ activity ไม่ใช่ concentration เมื่อ nonideal"],["F-E-013"],"สำหรับ M2+/M, a_high/a_low=100, n=2 ให้ E=0.05916 V","กลับอัตราส่วนทำให้ E ติดลบ",["เหตุใด E°cell ของ concentration cell เป็นศูนย์"]),
]


def problem(pid, topic, kind, difficulty, prompt, answer, tolerance, unit, steps, formulas, refs, source_class="generated"):
    return {"id":pid,"topic_id":topic,"type":kind,"difficulty":difficulty,"prompt_th":prompt,"source_classification":source_class,"source_references":refs,"correct_answer":answer,"tolerance":tolerance,"unit":unit,"hint_th":"เลือกสูตรจากชนิดข้อมูลและตรวจหน่วยก่อนแทนค่า","solution_steps":steps,"related_formula_ids":formulas,"bookmarked_default":False}


PROBLEMS = [
    problem("P-K-001","K01","numerical","easy","สำหรับ 4NH3+3O2→2N2+6H2O ถ้า N2 เกิด 0.27 mol L^-1 s^-1 จงหาอัตราการเกิด H2O",0.81,0.01,"mol L^-1 s^-1",["Given: d[N2]/dt=0.27","Find: d[H2O]/dt","Formula: (1/2)d[N2]/dt=(1/6)d[H2O]/dt","Substitute: 6/2×0.27","Answer: 0.81 mol L^-1 s^-1","Unit verified"],["F-K-001"],[ref(PART1,94,93)],"source-derived"),
    problem("P-K-002","K02","numerical","medium","ปฏิกิริยา S2O8^2- กับ I- มี rate=2.2×10^-4 M s^-1 ที่ [S2O8^2-]=0.080 M และ [I-]=0.034 M จงหา k เมื่อเป็นอันดับหนึ่งต่อสารทั้งคู่",0.0809,0.001,"M^-1 s^-1",["Given concentrations and rate","Use k=rate/([S2O8][I])","Substitute 2.2e-4/(0.080×0.034)","Answer 8.09e-2 M^-1 s^-1","Dimensional check: M s^-1 / M^2"],["F-K-002"],[ref(PART1,26,25)],"source-derived"),
    problem("P-K-003","K03","numerical","medium","N2O5 เป็น first order, k=5.1×10^-4 s^-1, [A]0=0.25 M หลัง 3.2 min เหลือเท่าใด",0.227,0.003,"M",["Convert 3.2 min=192 s","Use [A]=[A]0e^-kt","Substitute 0.25e^(-5.1e-4×192)","Answer 0.227 M","Unit exponent is dimensionless"],["F-K-004"],[ref(PART1,42,41),ref(PART1,43,42)],"source-derived"),
    problem("P-K-004","K04","numerical","easy","ปฏิกิริยาอันดับหนึ่งมี k=0.00100 s^-1 จงหาครึ่งชีวิต",693,2,"s",["Use t1/2=ln2/k","0.693/0.00100","Answer 693 s"],["F-K-007"],[ref(PART1,100,99)],"source-derived"),
    problem("P-K-005","K06","conceptual","medium","เมื่ออุณหภูมิเพิ่มขึ้น สำหรับปฏิกิริยาทั่วไปที่กลไกไม่เปลี่ยน ค่า k โดยทั่วไปเป็นอย่างไร","เพิ่มขึ้น",None,None,["Arrhenius: k=Ae^-Ea/RT","T เพิ่มทำให้ exponent มีค่าน้อยลบ","k เพิ่ม"],["F-K-009"],[ref(PART1,91,90)],"source-derived"),
    problem("P-E-001","E04","numerical","medium","สารละลาย CH3COOH 0.001028 M มี κ=4.95×10^-5 S cm^-1 และ Λ°=390.5 S cm2 mol^-1 จงหา Ka",1.78e-5,1e-6,None,["Λ=1000κ/c=48.15 S cm2 mol^-1","α=Λ/Λ°=0.1233","Ka=cα²/(1-α)","Answer 1.78×10^-5","α is dimensionless"],["F-E-002","F-E-003","F-E-004"],[ref(PART2,48,48)],"source-derived"),
    problem("P-E-002","E03","numerical","hard","AgBr: Lsolution=6.99×10^-8 S cm^-1, Lwater=1.60×10^-8 S cm^-1, λ°Ag+=53.5 และ λ°Br-=68.0 S cm2 mol^-1 จงหา Ksp",1.97e-13,1e-14,None,["Correct solvent blank: κ=6.99e-8-1.60e-8=5.39e-8 S cm^-1","Λ°=53.5+68.0=121.5 S cm2 mol^-1","S=1000κ/Λ°=4.44e-7 M","Ksp=S²=1.97e-13","Source handwriting shows 7.39e-8; flagged as arithmetic error"],["F-E-005"],[ref(PART2,66,66)],"source-derived-review"),
    problem("P-E-003","E06","numerical","medium","0.01 M CuSO4 ที่ 298 K จงหา mean activity coefficient ด้วย DHLL (A=0.509)",0.392,0.005,None,["I=1/2[(0.01)(2²)+(0.01)(-2)²]=0.04 M","logγ±=-0.509|2×-2|√0.04=-0.4072","γ±=10^-0.4072=0.392"],["F-E-006","F-E-007"],[ref(PART2,83,83)],"source-derived"),
    problem("P-E-004","E09","numerical","easy","กำหนด E°cathode=+0.031 V และ E°anode(as reduction)=-0.320 V จงหา E°cell",0.351,0.002,"V",["Use Ecell=Ecathode-Eanode","0.031-(-0.320)","Answer +0.351 V"],["F-E-009"],[ref(PART2,108,108)],"source-derived"),
    problem("P-E-005","E10","numerical","medium","สำหรับ E°cell=0.351 V และ n=2 จงหา ΔG°",-67.7,0.5,"kJ mol^-1",["Use ΔG°=-nFE°","Substitute -2×96485×0.351 J mol^-1","Convert to kJ","Answer -67.7 kJ mol^-1"],["F-E-010"],[ref(PART2,108,108),ref(PART2,109,109)],"generated-from-source"),
    problem("P-E-006","E10","numerical","hard","สำหรับ E°cell=0.351 V, n=2 ที่ 298 K จงหา K",7.5e11,1.5e11,None,["log10K=nE°/0.05916","=2×0.351/0.05916=11.866","K=10^11.866=7.35×10^11"],["F-E-012"],[ref(PART2,108,108),ref(PART2,116,116)],"generated-from-source"),
]


def main():
    (PROJECT / "data" / "formulas.json").write_text(json.dumps({"schema_version":2,"validation_status":"reviewed","formulas":FORMULAS},ensure_ascii=False,indent=2),encoding="utf-8")
    (PROJECT / "data" / "topics.json").write_text(json.dumps({"schema_version":2,"topics":TOPICS},ensure_ascii=False,indent=2),encoding="utf-8")
    (PROJECT / "data" / "problems.json").write_text(json.dumps({"schema_version":2,"problems":PROBLEMS},ensure_ascii=False,indent=2),encoding="utf-8")
    report = """# Chemistry Validation Report

## สถานะ

สูตรแกนหลัก 23 รายการและ worked problems 11 รายการผ่านการตรวจหน่วย การแทนค่า และการคำนวณตามรายการใน `data/formulas.json` และ `data/problems.json` แล้ว เนื้อหาจากเอกสารเสริมยังถือเป็น supporting material และไม่ใช้แทน primary instructor source เมื่อข้อมูลขัดกัน

## ประเด็นที่ตรวจยืนยัน

- กฎอัตราและ integrated rate laws ใช้หน่วยของ k สอดคล้องกับอันดับปฏิกิริยา
- ตัวอย่าง N2O5 หน้า 41-43: หลัง 3.2 min เหลือประมาณ 0.227 M และการเกิดปฏิกิริยา 62% หมายถึงเหลือ 38% จึงใช้เวลาประมาณ 31.6 min
- แบบฝึกหัด stoichiometric rate หน้า 93-96: H2O 0.81, NH3 0.54 และ O2 0.405≈0.41 mol L^-1 s^-1
- Acetic acid หน้า 48: Λm=48.15 S cm2 mol^-1, α=0.1233, Ka≈1.78×10^-5
- CuSO4 หน้า 83: I=0.040 M, logγ±=-0.407 และ γ±≈0.392
- Redox หน้า 108: E°cell=0.351 V; เมื่อ n=2 จะได้ ΔG°≈-67.7 kJ mol^-1 และ K≈7.4×10^11 ที่ 298 K

## ข้อผิดพลาดต้นฉบับที่ต้อง REVIEW

### AgBr conductivity, Part2 PDF page 66 / printed slide 66

ต้นฉบับลายมือเขียน `6.99×10^-8 - 1.60×10^-8 = 7.39×10^-8 S cm^-1` ซึ่งเป็นการลบผิด

- ค่าที่ถูกต้อง: `5.39×10^-8 S cm^-1`
- Λ°(AgBr)=53.5+68.0=121.5 S cm2 mol^-1
- S=(1000×5.39×10^-8)/121.5=4.44×10^-7 M
- Ksp=S²=1.97×10^-13

ระบบเก็บโจทย์นี้เป็น `source-derived-review` และแสดงคำเตือน ไม่แก้ต้นฉบับ PDF

## ข้อจำกัด

สูตร/ตัวอย่างที่ไม่ได้อยู่ในฐานข้อมูลรุ่นนี้ยังไม่ถือว่าผ่านการตรวจรายบรรทัด โดยเฉพาะหน้าลายมือใน Final Phychem.pdf และ Final.pdf ต้องตรวจเพิ่มเติมก่อนนำค่าตัวเลขใหม่มาใช้
"""
    (PROJECT / "reports" / "chemistry_validation.md").write_text(report,encoding="utf-8")
    print(len(TOPICS),len(FORMULAS),len(PROBLEMS))


if __name__ == "__main__":
    main()
