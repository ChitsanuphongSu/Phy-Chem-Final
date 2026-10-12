import type{Problem}from'../types';
import type{Attempt,MockExamSession}from'../storage';

export type MasteryState='NOT_STARTED'|'INSUFFICIENT_EVIDENCE'|'DEVELOPING'|'PROGRESSING'|'STRONG'|'MASTERED';
export type EvidenceConfidence='INSUFFICIENT'|'LOW'|'MODERATE'|'HIGH';
export type MasteryResult={id:string;score:number|null;state:MasteryState;confidence:EvidenceConfidence;attempts:number;uniqueAttempted:number;available:number;correct:number;recentPerformance:number|null;lastPractice:string|null;firstAttemptPerformance:number|null;latestAttemptPerformance:number|null};
export type Readiness={score:number|null;confidence:EvidenceConfidence;completeness:number;dimensions:{name:string;score:number;weight:number}[];explanation:string};
export type Recommendation={questionId:string;topicId:string;p1Ids:string[];category:'REVIEW_WEAK_TOPIC'|'PRACTICE_UNATTEMPTED_P1'|'RETRY_INCORRECT'|'INCREASE_DIFFICULTY'|'MAINTAIN_MASTERY';reason:string;priority:number;difficulty:Problem['difficulty'];learningObjective:string};
export type AnalyticsInput={problems:Problem[];attempts:Attempt[];topicIds:string[];traceItems:{p1_content_id:string;related_problem_ids:string[];source_evidence:{pdf_page:number}}[];mockSessions:MockExamSession[];now?:Date};
