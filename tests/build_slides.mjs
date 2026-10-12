import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {Presentation, PresentationFile} from '@oai/artifact-tool';

const ROOT='D:/Luna/Phy-Chem/physical-chemistry-study-hub';
const OUT=path.join(ROOT,'outputs/slides');
const BUILD=path.join(ROOT,'tmp/slide-build');
const SKILL='C:/Users/ASUS/.codex/plugins/cache/openai-primary-runtime/presentations/26.1007.11041/skills/presentations';
const PY='C:/Users/ASUS/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe';
const {finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')).href);
await fs.mkdir(OUT,{recursive:true}); await fs.mkdir(BUILD,{recursive:true});

const C={bg:'#FFF9FC',pink:'#E88EAF',soft:'#F8C8DC',ink:'#34303A',accent:'#C66B95',white:'#FFFFFF',muted:'#716774',warn:'#F9E3AE'};
const FONT='Tahoma';
const W=1280,H=720;
function shape(slide,x,y,w,h,fill=C.white,r='roundRect',line=C.soft){return slide.shapes.add({geometry:r,position:{left:x,top:y,width:w,height:h},fill,line:{style:'solid',fill:line,width:1},borderRadius:'rounded-xl'});}
function text(slide,value,x,y,w,h,size=26,bold=false,color=C.ink,align='left'){const s=slide.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{style:'solid',fill:'none',width:0}});s.text=value;s.text.style={typeface:FONT,fontSize:size,bold,color,alignment:align,verticalAlignment:'middle',autoFit:'shrinkText'};return s;}
function title(slide,t,sub=''){text(slide,t,64,42,1152,58,34,true);if(sub)text(slide,sub,66,99,1148,34,16,false,C.muted);}
function footer(slide,source,n){text(slide,source,64,683,1030,22,12,false,C.muted);text(slide,String(n),1130,683,80,22,12,true,C.accent,'right');}
function addImage(slide,file,x,y,w,h){return fs.readFile(file).then(b=>slide.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:'image/jpeg',alt:'หลักฐานหน้าต้นฉบับที่มีดาวผู้สอน',fit:'contain',position:{left:x,top:y,width:w,height:h}}));}
function cover(deck,main,sub){const s=deck.slides.add();s.background.fill=C.bg;shape(s,68,64,1144,592,C.white);text(s,'✦  PHYSICAL CHEMISTRY',104,105,650,34,16,true,C.accent);text(s,main,104,190,760,150,52,true);text(s,sub,108,350,700,70,23,false,C.muted);text(s,'SC202301 · เรียบเรียงจากเอกสารผู้สอนและโน้ตเสริม',108,545,800,30,16,false,C.muted);text(s,'⚗',940,180,180,180,112,false,C.pink,'center');return s;}
function twoCols(slide,leftTitle,leftBody,rightTitle,rightBody){shape(slide,64,150,552,470,C.white);shape(slide,640,150,576,470,C.white);text(slide,leftTitle,92,175,500,44,26,true,C.accent);text(slide,leftBody,92,225,500,360,22,false);text(slide,rightTitle,670,175,510,44,26,true,C.accent);text(slide,rightBody,670,225,510,360,22,false);}
function equation(slide,eq,y,label=''){shape(slide,130,y,1020,100,'#FFF0F6');if(label)text(slide,label,160,y+15,250,25,15,true,C.accent);text(slide,eq,160,y+35,960,50,30,true,C.ink,'center');}

async function exportDeck(name,deck){const renderDir=path.join(BUILD,name);await fs.mkdir(renderDir,{recursive:true});for(const [i,s] of deck.slides.items.entries()){const png=await deck.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(renderDir,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));}const candidate=path.join(BUILD,`${name}-candidate.pptx`);await(await PresentationFile.exportPptx(deck)).save(candidate);const finalPath=path.join(OUT,`${name}.pptx`);const receipt=path.join(BUILD,`${name}.validation.json`);await finalizePresentation({workspaceDir:ROOT,candidatePath:candidate,finalPath,pythonExecutable:PY,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],requiredNativeTableOwnerSlides:[],fontPolicy:{basis:'design',families:[FONT]},verifyArtifactToolImport:true,receiptPath:receipt});return finalPath;}

async function completeRevision(){const d=Presentation.create({slideSize:{width:W,height:H}});cover(d,'ทบทวน Physical Chemistry ฉบับครบ','Chemical Kinetics + Electrochemistry · เน้นความเข้าใจและการเลือกใช้สูตร');let s=d.slides.add();s.background.fill=C.bg;title(s,'ภาพรวมรายวิชา','สองแกนความคิดที่เชื่อมข้อมูล การเปลี่ยนแปลง และพลังงาน');twoCols(s,'Chemical Kinetics','อัตราการเกิดปฏิกิริยา\nกฎอัตราและ reaction order\nIntegrated rate laws\nHalf-life และ Arrhenius\nกลไกและตัวเร่ง','Electrochemistry','Electrolytes และ conductivity\nMolar conductivity และ dissociation\nActivity และ ionic strength\nElectrochemical cells\nNernst, ΔG และ K');footer(s,'Source: Part1 pp.3-166; Part2 pp.5-132',2);
const slides=[
['อัตราปฏิกิริยาและกฎอัตรา','ดุลสมการก่อน แล้วเชื่อมอัตราด้วยสัมประสิทธิ์','v = -(1/a)d[A]/dt = (1/p)d[P]/dt','rate = k[A]^m[B]^n','อันดับ m,n ต้องหาเชิงทดลอง ไม่อ่านตรงจากสมการรวม','Part1 pp.8-27'],
['Integrated rate laws','อันดับศูนย์: [A]t = [A]0 - k0t','อันดับหนึ่ง: ln([A]t/[A]0) = -k1t','อันดับสอง: 1/[A]t = 1/[A]0 + k2t','กราฟเส้นตรงช่วยตรวจอันดับและหน่วยของ k','Part1 pp.28-56'],
['Half-life','อันดับศูนย์: t1/2 = [A]0/(2k0)','อันดับหนึ่ง: t1/2 = ln2/k1','อันดับสอง: t1/2 = 1/(k2[A]0)','อันดับหนึ่งมี half-life คงที่เมื่ออุณหภูมิคงที่','Part1 pp.32-55'],
['Arrhenius และ activation energy','k = A exp(-Ea/RT)','ln(k2/k1) = -(Ea/R)(1/T2 - 1/T1)','T ต้องเป็น kelvin และ Ea ต้องสอดคล้องกับหน่วย R','ตัวเร่งลด Ea แต่ไม่เปลี่ยน ΔH','Part1 pp.57-70'],
['Conductivity และ dissociation','G = 1/R = κA/l','Λm = 1000κ/c','α = Λm/Λm°','Ka = cα²/(1-α)','Part2 pp.31-50'],
['Activity และ ionic strength','I = 1/2 Σ ci zi²','log γ± = -0.509|z+z-|√I ที่ 298 K','a± = γ±m±','DHLL ใช้กับสารละลายเจือจางมาก','Part2 pp.68-90'],
['Electrochemical cells','Oxidation ที่ anode · Reduction ที่ cathode','Ecell = Ecathode - Eanode','ΔG = -nFEcell','E = E° - (0.05916/n)log Q ที่ 298 K','Part2 pp.94-119'],
];let n=3;for(const a of slides){s=d.slides.add();s.background.fill=C.bg;title(s,a[0]);text(s,a[1],90,155,1100,55,27,true,C.accent);equation(s,a[2],235);equation(s,a[3],360);text(s,a[4],105,510,1070,70,22,false,C.ink,'center');footer(s,`Source: ${a[5]}`,n++);}s=d.slides.add();s.background.fill=C.bg;title(s,'สรุปก่อนทำโจทย์');twoCols(s,'ก่อนแทนค่า','1. เขียน Given และ Find\n2. เลือกสูตรตามชนิดข้อมูล\n3. แปลงหน่วยให้สอดคล้อง\n4. ดุลสมการและหา n ให้ถูก','หลังคำนวณ','1. ตรวจหน่วยของคำตอบ\n2. ตรวจเครื่องหมายและขนาด\n3. รายงาน significant figures\n4. ย้อนดู source เมื่อพบค่าขัดแย้ง');footer(s,'Validated formula set: data/formulas.json',n);return exportDeck('01_Complete_Revision',d);}

async function examFocus(){const d=Presentation.create({slideSize:{width:W,height:H}});cover(d,'Exam Focus','เฉพาะหัวข้อที่มีดาวผู้สอนยืนยันแล้ว พร้อมหลักฐานหน้า PDF');let s=d.slides.add();s.background.fill=C.bg;title(s,'ความหมายของ P1 และ P2');twoCols(s,'P1 · Confirmed Instructor Star','เห็นดาวสีชมพู/ม่วงแดงรูป asterisk ชัดเจนบนหน้าต้นฉบับ\nบันทึก PDF page และ printed slide\nใช้หลักฐานภาพตรวจย้อนกลับได้','P2 · Directly Related','แนวคิดที่จำเป็นต่อการทำโจทย์ P1\nเป็นการจัดลำดับเชิงวิชาการ\nไม่อ้างว่าอาจารย์ทำเครื่องหมาย');footer(s,'Source: reports/star_detection_report.md',2);
const focus=[
['Initial-rate method','Part1 PDF p.21 · slide 21','หา reaction order และ k จากคู่ทดลอง','page-021.jpg'],
['First-order rate law','Part1 PDF p.35 · slide 34','ln([A]t/[A]0)=-k1t และหน่วย k1=time^-1','page-035.jpg'],
['Half-life ของอันดับหนึ่ง','Part1 PDF p.40 · slide 39','ปริมาณลดครึ่งหนึ่งในช่วงเวลาเท่ากัน','page-040.jpg'],
['Reaction intermediate','Part1 PDF p.74 · slide 73','เกิดในกลไกแต่ไม่ปรากฏในสมการรวม','page-074.jpg'],
['Conductivity และ Ka','Part2 PDF p.48 · slide 48','κ → Λm → α → Ka','page-048.jpg'],
['Ionic strength และ γ±','Part2 PDF p.83 · slide 83','I=1/2Σcizi² และ Debye-Huckel limiting law','page-083.jpg'],
['Galvanic cell','Part2 PDF p.95 · slide 95','anode oxidation · cathode reduction · salt bridge','page-095.jpg'],
['Cell potential ต่อ ΔG และ K','Part2 PDF p.108 · slide 108','Ecell=Ec-Ea แล้วเชื่อม ΔG=-nFE และ K','page-108.jpg'],
];let n=3;for(const [head,src,desc,file] of focus){s=d.slides.add();s.background.fill=C.bg;title(s,head,src);const isP2=src.includes('Part2');const image=path.join(ROOT,'evidence/renders',isP2?'part2':'part1',file);await addImage(s,image,64,145,620,470);shape(s,720,170,495,360,C.white);text(s,'P1 · CONFIRMED',752,195,420,32,18,true,C.accent);text(s,desc,752,250,420,115,28,true);text(s,'ทบทวนสูตรที่เกี่ยวข้อง แล้วทำโจทย์โดยไม่เปิดเฉลยก่อน',752,395,410,80,20,false,C.muted);footer(s,`Evidence: ${src}`,n++);}s=d.slides.add();s.background.fill=C.bg;title(s,'Exam Cram Checklist');twoCols(s,'Chemical Kinetics','□ initial-rate method\n□ first-order integrated law\n□ half-life\n□ reaction mechanism\n□ stoichiometric rate','Electrochemistry','□ conductivity → dissociation\n□ ionic strength → activity\n□ anode/cathode sign\n□ Ecell → ΔG → K\n□ ตรวจ arithmetic ของ AgBr');footer(s,'No claim that any question is guaranteed to appear',n);return exportDeck('02_Exam_Focus',d);}

async function formulaProblems(){const d=Presentation.create({slideSize:{width:W,height:H}});cover(d,'Formula & Worked Problems','คู่มือเลือกสูตร พร้อมโจทย์และเฉลยเป็นขั้นตอน');let s=d.slides.add();s.background.fill=C.bg;title(s,'Formula Decision Guide');twoCols(s,'ข้อมูล Kinetics','concentration-time → integrated law\nhalf-life → สูตรตาม order\nk ที่ T1,T2 → Arrhenius\ninitial rates → rate ratios','ข้อมูล Electrochemistry','κ และ c → Λm\nΛm และ Λ° → α\nE° → ΔG° หรือ K\nnonstandard state → Nernst');footer(s,'Source: validated formula library',2);
const pairs=[
{q:'N2O5 เป็น first order\nk=5.1×10^-4 s^-1, [A]0=0.25 M\nหลัง 3.2 min เหลือเท่าใด?',sol:['Given: t=192 s','Formula: [A]=[A]0e^-kt','Substitute: 0.25e^(-5.1×10^-4×192)','Answer: 0.227 M','Unit check: kt ไม่มีหน่วย'],src:'Part1 PDF p.42 / slide 41'},
{q:'CH3COOH 0.001028 M\nκ=4.95×10^-5 S cm^-1, Λ°=390.5\nจงหา Ka',sol:['Λm=1000κ/c=48.15 S cm² mol^-1','α=Λm/Λ°=0.1233','Ka=cα²/(1-α)','Answer: 1.78×10^-5','Check: 0<α<1'],src:'Part2 PDF p.48 / slide 48'},
{q:'0.01 M CuSO4 ที่ 298 K\nจงหา γ± ด้วย DHLL (A=0.509)',sol:['I=1/2[(0.01)(2²)+(0.01)(-2)²]=0.04 M','logγ±=-0.509|2×-2|√0.04=-0.407','γ±=10^-0.407','Answer: 0.392','Condition: dilute solution'],src:'Part2 PDF p.83 / slide 83'},
{q:'E°cathode=+0.031 V\nE°anode(as reduction)=-0.320 V\nจงหา E°cell, ΔG° และ K เมื่อ n=2',sol:['E°cell=0.031-(-0.320)=0.351 V','ΔG°=-2(96485)(0.351)=-67.7 kJ mol^-1','logK=2(0.351)/0.05916=11.87','K≈7.4×10^11','Spontaneous forward under standard state'],src:'Part2 PDF p.108 / slide 108'},
];let n=3;for(const p of pairs){s=d.slides.add();s.background.fill=C.bg;title(s,'โจทย์',p.src);shape(s,100,165,1080,390,C.white);text(s,p.q,145,205,990,290,30,true,C.ink,'center');text(s,'ลองทำก่อนเปิดสไลด์ถัดไป',420,585,440,34,18,false,C.accent,'center');footer(s,`Source-derived problem: ${p.src}`,n++);s=d.slides.add();s.background.fill=C.bg;title(s,'เฉลยแบบเป็นขั้นตอน',p.src);shape(s,100,145,1080,455,C.white);text(s,p.sol.map((x,i)=>`STEP ${i+1}: ${x}`).join('\n'),145,180,990,360,24,false);footer(s,`Validated calculation: ${p.src}`,n++);}s=d.slides.add();s.background.fill=C.bg;title(s,'กรณี AgBr ที่ต้องระวัง','เก็บต้นฉบับและคำแก้ไขแยกกัน');twoCols(s,'ค่าที่ต้นฉบับเขียน','6.99×10^-8 - 1.60×10^-8\n= 7.39×10^-8 S cm^-1\n\nสถานะ: REVIEW','ค่าที่ตรวจคำนวณ','ผลต่างที่ถูกต้อง = 5.39×10^-8\nS=4.44×10^-7 M\nKsp=1.97×10^-13');footer(s,'Part2 PDF p.66 / slide 66 · arithmetic discrepancy preserved',n);return exportDeck('03_Formula_and_Problems',d);}

const outputs=[];outputs.push(await completeRevision());outputs.push(await examFocus());outputs.push(await formulaProblems());console.log(outputs.join('\n'));
