import{describe,expect,it}from'vitest';
import{calculateMastery}from'./mastery';
import{buildAnalytics}from'.';
import type{Problem}from'../types';
import type{Attempt}from'../storage';

const problem=(id:string,difficulty:Problem['difficulty']='easy',topic_id='K01'):Problem=>({id,topic_id,type:'numerical',difficulty,prompt_th:'',source_classification:'generated',source_references:[],correct_answer:1,tolerance:.01,unit:'s',hint_th:'',solution_steps:[],related_formula_ids:[],bookmarked_default:false});
const ps=[problem('P1'),problem('P2','medium'),problem('P3','hard'),problem('P4'),problem('P5','medium'),problem('P6','hard')];
const attempt=(problemId:string,correct:boolean,days=0):Attempt=>({problemId,correct,at:new Date(Date.UTC(2026,9,12)-days*86400000).toISOString()});

describe('mastery deterministic fixtures',()=>{
  const cases:[string,Attempt[],string,number|null][]=[
    ['empty',[],'NOT_STARTED',null],['one correct',[attempt('P1',true)],'INSUFFICIENT_EVIDENCE',92],
    ['one wrong',[attempt('P1',false)],'INSUFFICIENT_EVIDENCE',2],['two wrong',[attempt('P1',false),attempt('P2',false)],'DEVELOPING',3],
    ['two mixed',[attempt('P1',true),attempt('P2',false)],'DEVELOPING',44],['two correct',[attempt('P1',true),attempt('P2',true)],'STRONG',93],
    ['latest recovery',[attempt('P1',false,1),attempt('P1',true)],'INSUFFICIENT_EVIDENCE',69],['latest decline',[attempt('P1',true,1),attempt('P1',false)],'INSUFFICIENT_EVIDENCE',24],
    ['old evidence',[attempt('P1',true,30),attempt('P2',true,30)],'STRONG',93],['recent wrong',[attempt('P1',true,30),attempt('P1',false)],'INSUFFICIENT_EVIDENCE',17],
    ['five mixed',[attempt('P1',true),attempt('P2',true),attempt('P3',false),attempt('P4',true),attempt('P5',false)],'PROGRESSING',58],
    ['five correct',[attempt('P1',true),attempt('P2',true),attempt('P3',true),attempt('P4',true),attempt('P5',true)],'MASTERED',98],
  ];
  it.each(cases)('%s',(_name,attempts,state,score)=>{const result=calculateMastery('K01',ps,attempts,new Date('2026-10-12T00:00:00Z'));expect(result.state).toBe(state);expect(result.score).toBe(score)});
  it('is deterministic',()=>expect(calculateMastery('K01',ps,[attempt('P1',true)] )).toEqual(calculateMastery('K01',ps,[attempt('P1',true)])));
  it('does not count unknown problem IDs',()=>expect(calculateMastery('K01',ps,[attempt('UNKNOWN',false)]).state).toBe('NOT_STARTED'));
  it('counts repeated attempts but unique coverage once',()=>{const r=calculateMastery('K01',ps,[attempt('P1',false),attempt('P1',true)]);expect(r.attempts).toBe(2);expect(r.uniqueAttempted).toBe(1)});
  it('requires two difficulty bands for mastered',()=>{const same=Array.from({length:5},(_,i)=>problem(`E${i}`));const r=calculateMastery('E01',same,same.map(p=>attempt(p.id,true)));expect(r.state).toBe('STRONG')});
});

describe('readiness and recommendation fixtures',()=>{
 const trace=[{p1_content_id:'K-P1-001',related_problem_ids:['P1'],source_evidence:{pdf_page:1}}];
 it('returns unavailable readiness for no evidence',()=>expect(buildAnalytics({problems:ps,attempts:[],topicIds:['K01'],traceItems:trace,mockSessions:[]}).readiness.score).toBeNull());
 it('does not label unattempted topics as weak failures',()=>expect(buildAnalytics({problems:ps,attempts:[],topicIds:['K01'],traceItems:trace,mockSessions:[]}).weak[0].classification).toBe('NOT_STUDIED'));
 it('recommends unattempted verified P1',()=>{const tagged=[{...ps[0],related_p1_ids:['K-P1-001']},...ps.slice(1)];expect(buildAnalytics({problems:tagged,attempts:[],topicIds:['K01'],traceItems:trace,mockSessions:[]}).recommendations[0].category).toBe('PRACTICE_UNATTEMPTED_P1')});
 it('recommends retry after incorrect response',()=>expect(buildAnalytics({problems:ps,attempts:[attempt('P1',false)],topicIds:['K01'],traceItems:trace,mockSessions:[]}).recommendations.some(r=>r.category==='RETRY_INCORRECT')).toBe(true));
 it('keeps confidence distinct from score',()=>{const r=buildAnalytics({problems:ps,attempts:[attempt('P1',true)],topicIds:['K01'],traceItems:trace,mockSessions:[]}).readiness;expect(r.score).not.toBeNull();expect(r.confidence).toBe('LOW')});
});
