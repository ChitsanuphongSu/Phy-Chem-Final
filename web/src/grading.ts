import type {Problem} from './types';

export function parseScientificAnswer(raw:string):number{
  const normalized=raw.trim().replace(/,/g,'').replace(/−/g,'-').replace(/×\s*10\s*\^?\s*([+-]?\d+)/i,'e$1').replace(/\s+/g,'');
  return Number(normalized);
}

export type NumericParseStatus='INVALID_NUMBER'|'UNKNOWN_UNIT'|'INCOMPATIBLE_UNIT'|'VALID_NUMERIC_ANSWER';
export type NumericParseResult={status:NumericParseStatus;value?:number;normalizedUnit?:string;message:string};
const units:Record<string,{dimension:string;factor:number;canonical:string}>={
  's':{dimension:'time',factor:1,canonical:'s'},'min':{dimension:'time',factor:60,canonical:'s'},'h':{dimension:'time',factor:3600,canonical:'s'},
  'm':{dimension:'concentration',factor:1,canonical:'M'},'moll-1':{dimension:'concentration',factor:1,canonical:'M'},
  'j':{dimension:'energy',factor:1,canonical:'J'},'kj':{dimension:'energy',factor:1000,canonical:'J'},'jmol-1':{dimension:'molar-energy',factor:1,canonical:'J mol^-1'},'kjmol-1':{dimension:'molar-energy',factor:1000,canonical:'J mol^-1'},
  'v':{dimension:'potential',factor:1,canonical:'V'},'mv':{dimension:'potential',factor:.001,canonical:'V'},
  'scm-1':{dimension:'conductivity',factor:1,canonical:'S cm^-1'},'sm-1':{dimension:'conductivity',factor:.01,canonical:'S cm^-1'},
  'scm2mol-1':{dimension:'molar-conductivity',factor:1,canonical:'S cm2 mol^-1'},'sm2mol-1':{dimension:'molar-conductivity',factor:10000,canonical:'S cm2 mol^-1'},
  's-1':{dimension:'rate-constant-1',factor:1,canonical:'s^-1'},'m-1s-1':{dimension:'rate-constant-2',factor:1,canonical:'M^-1 s^-1'},'m-2s-1':{dimension:'rate-constant-3',factor:1,canonical:'M^-2 s^-1'},
  'ms-1':{dimension:'rate',factor:1,canonical:'M s^-1'}
};
function unitKey(raw:string){return raw.toLowerCase().replace(/mol\s*\/\s*l/g,'mol L^-1').replace(/[·⋅]/g,' ').replace(/²/g,'2').replace(/⁻¹/g,'-1').replace(/\^/g,'').replace(/\s+/g,'')}
function expectedUnitInfo(unit:string|null){if(!unit)return null;return units[unitKey(unit)]||null}
export function parseUnitAwareAnswer(raw:string,expectedUnit:string|null):NumericParseResult{
  const normalized=raw.trim().replace(/−/g,'-').replace(/×\s*10\s*\^?\s*([+-]?\d+)/i,'e$1').replace(/\s+(?=e[+-]?\d+)/i,'');
  const match=normalized.match(/^([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?)(.*)$/i);
  if(!match)return{status:'INVALID_NUMBER',message:'รูปแบบตัวเลขไม่ถูกต้อง'};const numeric=Number(match[1]);if(!Number.isFinite(numeric))return{status:'INVALID_NUMBER',message:'ค่าตัวเลขต้องเป็นจำนวนจำกัด'};
  const rawUnit=match[2].trim();const expected=expectedUnitInfo(expectedUnit);if(!rawUnit)return{status:'VALID_NUMERIC_ANSWER',value:numeric,normalizedUnit:expected?.canonical,message:'รับค่าตัวเลขตามหน่วยของโจทย์'};
  const provided=units[unitKey(rawUnit)];if(!provided)return{status:'UNKNOWN_UNIT',message:`ไม่รู้จักหน่วย ${rawUnit}`};if(!expected)return{status:'INCOMPATIBLE_UNIT',message:'โจทย์ต้องการคำตอบไร้หน่วย'};if(provided.dimension!==expected.dimension)return{status:'INCOMPATIBLE_UNIT',message:`หน่วย ${rawUnit} ไม่เข้ากับ ${expectedUnit}`};
  return{status:'VALID_NUMERIC_ANSWER',value:numeric*provided.factor/expected.factor,normalizedUnit:expected.canonical,message:'แปลงเป็นหน่วยของโจทย์แล้ว'};
}

export function normalizeText(raw:string):string{
  return raw.trim().toLocaleLowerCase('th-TH').replace(/\s+/g,' ');
}

export function gradeProblem(problem:Problem,raw:string):boolean{
  const policy=problem.grading_policy;
  if(problem.type==='multiple-choice'||policy?.mode==='single-choice') return raw===problem.correct_option_id;
  if(typeof problem.correct_answer==='number'||policy?.mode==='numeric'){
    const parsed=parseUnitAwareAnswer(raw,problem.unit);if(parsed.status!=='VALID_NUMERIC_ANSWER')return false;const value=parsed.value!;
    const expected=Number(problem.correct_answer);
    const absolute=policy?.absolute_tolerance??problem.tolerance??0;
    const relative=Math.abs(expected)*(policy?.relative_tolerance??0.001);
    return Math.abs(value-expected)<=Math.max(absolute,relative);
  }
  const accepted=policy?.accepted_answers?.length?policy.accepted_answers:[String(problem.correct_answer)];
  return accepted.map(normalizeText).includes(normalizeText(raw));
}

export function isMockCompatible(problem:Problem):boolean{
  return problem.validation_status!=='REJECTED'&&(
    problem.type==='numerical'||problem.type==='multiple-choice'||
    problem.grading_policy?.mode==='accepted-text'||typeof problem.correct_answer==='string'
  );
}
