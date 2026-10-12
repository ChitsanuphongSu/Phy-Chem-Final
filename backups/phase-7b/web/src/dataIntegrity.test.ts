import {describe, expect, it} from 'vitest';
import topicsData from '../../data/topics.json';
import formulasData from '../../data/formulas.json';
import problemsData from '../../data/problems.json';
import examData from '../../data/exam_priority.json';
import traceData from '../../data/p1_traceability.json';

const topics = topicsData.topics;
const formulas = formulasData.formulas;
const problems = problemsData.problems;
const examItems = examData.items;
const mappings = traceData.items;

const ids = <T extends {id: string}>(records: T[]) => new Set(records.map((record) => record.id));

describe('Phase 7A data integrity', () => {
  it('preserves all registries and unique IDs', () => {
    expect(ids(topics).size).toBe(topics.length);
    expect(ids(formulas).size).toBe(formulas.length);
    expect(ids(problems).size).toBe(problems.length);
    expect(topics.length).toBeGreaterThanOrEqual(18);
    expect(formulas.length).toBeGreaterThanOrEqual(23);
    expect(problems.length).toBeGreaterThanOrEqual(11);
  });

  it('resolves topic and formula references', () => {
    const topicIds = ids(topics);
    const formulaIds = ids(formulas);
    formulas.forEach((formula) => expect(topicIds.has(formula.topic_id)).toBe(true));
    problems.forEach((problem) => {
      expect(topicIds.has(problem.topic_id)).toBe(true);
      problem.related_formula_ids.forEach((formulaId) => expect(formulaIds.has(formulaId)).toBe(true));
    });
    topics.forEach((topic) => topic.formula_ids.forEach((formulaId) => expect(formulaIds.has(formulaId)).toBe(true)));
  });

  it('uses the canonical electrochemistry topic mappings', () => {
    const topicByFormula = new Map(formulas.map((formula) => [formula.id, formula.topic_id]));
    expect(topicByFormula.get('F-E-006')).toBe('E06');
    expect(topicByFormula.get('F-E-007')).toBe('E06');
    expect(topicByFormula.get('F-E-008')).toBe('E06');
    expect(topicByFormula.get('F-E-009')).toBe('E09');
    expect(topicByFormula.get('F-E-013')).toBe('E11');
  });

  it('maps exactly the 20 confirmed P1 records', () => {
    const confirmed = examItems.filter((item) => item.priority === 'P1' && item.evidence_classification === 'CONFIRMED');
    expect(confirmed).toHaveLength(20);
    expect(confirmed.filter((item) => item.content_id.startsWith('K-'))).toHaveLength(12);
    expect(confirmed.filter((item) => item.content_id.startsWith('E-'))).toHaveLength(8);
    expect(new Set(mappings.map((item) => item.p1_content_id))).toEqual(new Set(confirmed.map((item) => item.content_id)));
  });

  it('has no dangling or duplicate traceability relationships', () => {
    const topicIds = ids(topics);
    const formulaIds = ids(formulas);
    const problemIds = ids(problems);
    mappings.forEach((mapping) => {
      expect(topicIds.has(mapping.canonical_topic_id)).toBe(true);
      expect(new Set(mapping.related_topic_ids).size).toBe(mapping.related_topic_ids.length);
      expect(new Set(mapping.related_formula_ids).size).toBe(mapping.related_formula_ids.length);
      expect(new Set(mapping.related_problem_ids).size).toBe(mapping.related_problem_ids.length);
      mapping.related_topic_ids.forEach((id) => expect(topicIds.has(id)).toBe(true));
      mapping.related_lesson_ids.forEach((id) => expect(topicIds.has(id)).toBe(true));
      mapping.related_formula_ids.forEach((id) => expect(formulaIds.has(id)).toBe(true));
      mapping.related_problem_ids.forEach((id) => expect(problemIds.has(id)).toBe(true));
    });
  });

  it('preserves the validated AgBr correction', () => {
    const agbr = problems.find((problem) => problem.id === 'P-E-002');
    expect(agbr?.source_classification).toBe('source-derived-review');
    expect(agbr?.correct_answer).toBe(1.97e-13);
    expect(agbr?.solution_steps.join(' ')).toContain('5.39e-8');
    expect(agbr?.solution_steps.join(' ')).toContain('7.39e-8');
  });
});
