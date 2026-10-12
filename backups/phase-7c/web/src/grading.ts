import type {Problem} from './types';

export function parseScientificAnswer(raw:string):number{
  const normalized=raw.trim().replace(/,/g,'').replace(/−/g,'-').replace(/×\s*10\s*\^?\s*([+-]?\d+)/i,'e$1').replace(/\s+/g,'');
  return Number(normalized);
}

export function normalizeText(raw:string):string{
  return raw.trim().toLocaleLowerCase('th-TH').replace(/\s+/g,' ');
}

export function gradeProblem(problem:Problem,raw:string):boolean{
  const policy=problem.grading_policy;
  if(problem.type==='multiple-choice'||policy?.mode==='single-choice') return raw===problem.correct_option_id;
  if(typeof problem.correct_answer==='number'||policy?.mode==='numeric'){
    const value=parseScientificAnswer(raw);
    if(!Number.isFinite(value))return false;
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
