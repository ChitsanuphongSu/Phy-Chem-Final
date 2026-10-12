import{describe,expect,it}from'vitest';import{createMockSession,DEFAULT_BLUEPRINT,generateSeededExam,remainingSeconds,submitSession,validateBlueprint}from'./mockEngine';import type{Problem}from'./types';
const make=(i:number):Problem=>({id:`P-${String(i).padStart(3,'0')}`,topic_id:i%2?'K01':'E01',type:'numerical',difficulty:i%3===0?'hard':i%3===1?'easy':'medium',prompt_th:'',source_classification:'generated',source_references:[],correct_answer:i,tolerance:.01,unit:'s',hint_th:'',solution_steps:[],related_formula_ids:[],related_p1_ids:i<21?[`X-${i}`]:[],bookmarked_default:false});const bank=Array.from({length:65},(_,i)=>make(i+1));
describe('seeded mock exam fixtures',()=>{
 it('same seed yields same order',()=>expect(generateSeededExam(bank,'a').questions.map(x=>x.id)).toEqual(generateSeededExam(bank,'a').questions.map(x=>x.id)));
 it('different seed changes order',()=>expect(generateSeededExam(bank,'a').questions.map(x=>x.id)).not.toEqual(generateSeededExam(bank,'b').questions.map(x=>x.id)));
 it.each([1,5,10,20,40,65])('returns requested count %i',(total)=>{const b={...DEFAULT_BLUEPRINT,total};expect(generateSeededExam(bank,'x',b).questions).toHaveLength(total)});
 it.each([0,66,-1,1.5])('rejects invalid count %s',(total)=>expect(validateBlueprint({...DEFAULT_BLUEPRINT,total})).not.toHaveLength(0));
 it('does not duplicate questions',()=>{const ids=generateSeededExam(bank,'x',{...DEFAULT_BLUEPRINT,total:65}).questions.map(x=>x.id);expect(new Set(ids).size).toBe(ids.length)});
 it('records stable metadata',()=>{const s=createMockSession('x',['P-001'],30,new Date('2026-01-01T00:00:00Z'));expect(s.questionBankVersion).toBe('65-v1');expect(s.blueprintVersion).toBe('practice-v1')});
 it('deduplicates session question IDs',()=>expect(createMockSession('x',['P-001','P-001'],1).questionIds).toEqual(['P-001']));
 it.each([[0,60],[30000,30],[60000,0],[90000,0]])('uses absolute deadline at +%i ms',(advance,expected)=>{const now=new Date('2026-01-01T00:00:00Z');const s=createMockSession('x',['P-001'],1,now);expect(remainingSeconds(s,new Date(now.getTime()+advance))).toBe(expected)});
 it('grades correct, wrong, unanswered centrally',()=>{const now=new Date('2026-01-01T00:00:00Z');const s=createMockSession('x',['P-001','P-002','P-003'],1,now);s.answers={'P-001':'1','P-002':'99'};expect(submitSession(s,new Map(bank.map(p=>[p.id,p])),now).gradingSummary).toEqual({total:3,correct:1,incorrect:1,unanswered:1})});
 it('submission is idempotent',()=>{const now=new Date('2026-01-01T00:00:00Z');const s=submitSession(createMockSession('x',['P-001'],1,now),new Map(bank.map(p=>[p.id,p])),now);expect(submitSession(s,new Map(),new Date('2027-01-01'))).toBe(s)});
 it('preserves answers on submit',()=>{const s=createMockSession('x',['P-001'],1);s.answers={'P-001':'1'};expect(submitSession(s,new Map(bank.map(p=>[p.id,p]))).answers['P-001']).toBe('1')});
});
