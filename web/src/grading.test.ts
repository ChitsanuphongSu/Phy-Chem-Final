import {describe,expect,it} from 'vitest';
import {gradeProblem,parseScientificAnswer,parseUnitAwareAnswer} from './grading';
import type{Problem}from'./types';

const numeric={id:'T-N',topic_id:'K01',type:'numerical',difficulty:'easy',prompt_th:'',source_classification:'',source_references:[],correct_answer:1e-3,tolerance:1e-6,unit:'M',hint_th:'',solution_steps:[],related_formula_ids:[],bookmarked_default:false,grading_policy:{mode:'numeric',absolute_tolerance:1e-6,relative_tolerance:0.001}} satisfies Problem;
const mcq={...numeric,id:'T-M',type:'multiple-choice',correct_answer:'B',correct_option_id:'B',grading_policy:{mode:'single-choice'}} satisfies Problem;
const conceptual={...numeric,id:'T-C',type:'conceptual',correct_answer:'anode',grading_policy:{mode:'accepted-text',accepted_answers:['anode','แอโนด'],case_sensitive:false}} satisfies Problem;

describe('deterministic grading',()=>{
  it('parses scientific notation variants',()=>{expect(parseScientificAnswer('1 × 10^-3')).toBe(1e-3);expect(parseScientificAnswer('1e-3')).toBe(1e-3)});
  it('accepts numerical answers inside tolerance only',()=>{expect(gradeProblem(numeric,'0.0010005')).toBe(true);expect(gradeProblem(numeric,'0.0011')).toBe(false)});
  it('grades MCQ by stable option ID',()=>{expect(gradeProblem(mcq,'B')).toBe(true);expect(gradeProblem(mcq,'A')).toBe(false)});
  it('accepts controlled conceptual synonyms',()=>{expect(gradeProblem(conceptual,' แอโนด ')).toBe(true);expect(gradeProblem(conceptual,'cathode')).toBe(false)});
});
describe('unit-aware safety fixtures',()=>{
  it.each([
    ['1e-3 M','M','VALID_NUMERIC_ANSWER',.001],['1 × 10^-3 M','M','VALID_NUMERIC_ANSWER',.001],
    ['1000 mV','V','VALID_NUMERIC_ANSWER',1],['1 V','mV','VALID_NUMERIC_ANSWER',1000],
    ['60 min','s','VALID_NUMERIC_ANSWER',3600],['1 h','min','VALID_NUMERIC_ANSWER',60],
    ['1 kJ mol^-1','J mol^-1','VALID_NUMERIC_ANSWER',1000],['1000 J mol^-1','kJ mol^-1','VALID_NUMERIC_ANSWER',1],
    ['1 S m^-1','S cm^-1','VALID_NUMERIC_ANSWER',.01],['1 S cm^-1','S m^-1','VALID_NUMERIC_ANSWER',100],
    ['1 S m2 mol^-1','S cm2 mol^-1','VALID_NUMERIC_ANSWER',10000],['10000 S cm2 mol^-1','S m2 mol^-1','VALID_NUMERIC_ANSWER',1],
    ['abc M','M','INVALID_NUMBER',null],['1 banana','M','UNKNOWN_UNIT',null],['1 V','M','INCOMPATIBLE_UNIT',null],
    ['1','M','VALID_NUMERIC_ANSWER',1],['-2.5e2 s','s','VALID_NUMERIC_ANSWER',-250],['0 mV','V','VALID_NUMERIC_ANSWER',0],
    ['2 M^-1 s^-1','M^-1 s^-1','VALID_NUMERIC_ANSWER',2],['2 s^-1','M^-1 s^-1','INCOMPATIBLE_UNIT',null],['','M','INVALID_NUMBER',null]
  ] as const)('parses %s for %s', (raw,unit,status,value)=>{const r=parseUnitAwareAnswer(raw,unit);expect(r.status).toBe(status);if(value!==null)expect(r.value).toBeCloseTo(value)});
});
