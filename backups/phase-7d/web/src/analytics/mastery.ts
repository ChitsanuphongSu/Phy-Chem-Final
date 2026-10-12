import type{Problem}from'../types';import type{Attempt}from'../storage';import type{EvidenceConfidence,MasteryResult,MasteryState}from'./types';
const weight={easy:1,medium:1.25,hard:1.5};
const validDate=(value?:string)=>{const time=Date.parse(value||'');return Number.isFinite(time)?time:null};
const clamp=(n:number)=>Math.max(0,Math.min(100,n));
function confidence(unique:number,available:number,difficulties:number,hasRecent:boolean):EvidenceConfidence{if(unique===0)return'INSUFFICIENT';const coverage=available?unique/available:0;if(unique>=8&&coverage>=.5&&difficulties>=2&&hasRecent)return'HIGH';if(unique>=4&&coverage>=.25&&difficulties>=2)return'MODERATE';return'LOW'}
function state(score:number|null,unique:number,difficulties:number):MasteryState{if(score===null)return'NOT_STARTED';if(unique<2)return'INSUFFICIENT_EVIDENCE';if(score<45)return'DEVELOPING';if(score<65)return'PROGRESSING';if(score<82)return'STRONG';return unique>=5&&difficulties>=2?'MASTERED':'STRONG'}
export function calculateMastery(id:string,availableProblems:Problem[],rawAttempts:Attempt[],now=new Date()):MasteryResult{
 const ids=new Set(availableProblems.map(p=>p.id));const attempts=rawAttempts.filter(a=>ids.has(a.problemId)&&typeof a.correct==='boolean');const byProblem=new Map<string,Attempt[]>();
 for(const a of attempts){const list=byProblem.get(a.problemId)||[];list.push(a);byProblem.set(a.problemId,list)}
 const unique=[...byProblem.keys()];if(!unique.length)return{id,score:null,state:'NOT_STARTED',confidence:'INSUFFICIENT',attempts:0,uniqueAttempted:0,available:availableProblems.length,correct:0,recentPerformance:null,lastPractice:null,firstAttemptPerformance:null,latestAttemptPerformance:null};
 const problemMap=new Map(availableProblems.map(p=>[p.id,p]));let first=0,latest=0,totalWeight=0;const allDates:number[]=[];const diffs=new Set<string>();
 for(const pid of unique){const list=byProblem.get(pid)!.slice().sort((a,b)=>(validDate(a.at)??0)-(validDate(b.at)??0));const w=weight[problemMap.get(pid)!.difficulty];totalWeight+=w;first+=(list[0].correct?1:0)*w;latest+=(list.at(-1)!.correct?1:0)*w;diffs.add(problemMap.get(pid)!.difficulty);list.forEach(a=>{const d=validDate(a.at);if(d!==null)allDates.push(d)})}
 const recent=attempts.filter(a=>{const d=validDate(a.at);return d!==null&&now.getTime()-d<=14*86400000});const recentScore=recent.length?recent.filter(a=>a.correct).length/recent.length:null;const coverage=availableProblems.length?unique.length/availableProblems.length:0;
 const firstScore=first/totalWeight,latestScore=latest/totalWeight;const score=clamp(100*(.15*firstScore+.60*latestScore+.10*Math.min(1,coverage)+(recentScore===null?.15*latestScore:.15*recentScore)));
 const last=allDates.length?new Date(Math.max(...allDates)).toISOString():null;const conf=confidence(unique.length,availableProblems.length,diffs.size,recent.length>0);
 return{id,score:Math.round(score),state:state(score,unique.length,diffs.size),confidence:conf,attempts:attempts.length,uniqueAttempted:unique.length,available:availableProblems.length,correct:attempts.filter(a=>a.correct).length,recentPerformance:recentScore===null?null:Math.round(recentScore*100),lastPractice:last,firstAttemptPerformance:Math.round(firstScore*100),latestAttemptPerformance:Math.round(latestScore*100)};
}
