import {describe,expect,it} from 'vitest';
import {gradeProblem,parseScientificAnswer} from './grading';
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
