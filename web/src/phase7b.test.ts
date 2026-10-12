import {describe,expect,it} from 'vitest';
import problemsData from './data/problems.json';
import traceData from './data/p1_traceability.json';
import {gradeProblem,isMockCompatible} from './grading';
import type{Problem}from'./types';

const problems=problemsData.problems as unknown as Problem[];
const legacyIds=['P-K-001','P-K-002','P-K-003','P-K-004','P-K-005','P-E-001','P-E-002','P-E-003','P-E-004','P-E-005','P-E-006'];
const added=problems.slice(legacyIds.length);

describe('Phase 7B question bank',()=>{
  it('preserves 11 legacy questions and adds 54 unique questions',()=>{
    expect(problems.slice(0,11).map(problem=>problem.id)).toEqual(legacyIds);
    expect(added).toHaveLength(54);
    expect(problems).toHaveLength(65);
    expect(new Set(problems.map(p=>p.id)).size).toBe(65);
  });
  it('matches the target difficulty distribution',()=>{
    expect(problems.filter(p=>p.difficulty==='easy')).toHaveLength(20);
    expect(problems.filter(p=>p.difficulty==='medium')).toHaveLength(29);
    expect(problems.filter(p=>p.difficulty==='hard')).toHaveLength(16);
  });
  it('gives every new question three progressive hints and a complete solution',()=>{
    added.forEach(problem=>{
      expect(problem.validation_status).toBe('VALIDATED');
      expect(problem.hints).toHaveLength(3);
      expect(problem.solution_steps.length).toBeGreaterThanOrEqual(problem.type==='numerical'?8:5);
    });
  });
  it('has valid single-answer MCQs with stable option IDs',()=>{
    added.filter(p=>p.type==='multiple-choice').forEach(problem=>{
      const ids=problem.answer_options?.map(option=>option.id)??[];
      expect(ids).toHaveLength(4);
      expect(new Set(ids).size).toBe(4);
      expect(ids).toContain(problem.correct_option_id);
      expect(gradeProblem(problem,problem.correct_option_id??'')).toBe(true);
      ids.filter(id=>id!==problem.correct_option_id).forEach(id=>expect(gradeProblem(problem,id)).toBe(false));
    });
  });
  it('makes all active questions mock-compatible',()=>{
    expect(problems.every(isMockCompatible)).toBe(true);
  });
  it('resolves all 20 P1 practice gaps with direct new questions',()=>{
    const newIds=new Set(added.map(p=>p.id));
    traceData.items.forEach(mapping=>{
      expect(mapping.coverage_status).toBe('COMPLETE');
      expect(mapping.gap_classification).toEqual([]);
      expect(mapping.related_problem_ids.some(id=>newIds.has(id))).toBe(true);
    });
  });
});
