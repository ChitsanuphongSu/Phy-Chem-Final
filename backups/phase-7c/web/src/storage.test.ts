// @vitest-environment jsdom
import {describe,expect,it} from 'vitest';
import {loadStore,schedule} from './storage';
describe('spaced repetition schedule',()=>{
  it('resets interval after an unknown answer',()=>{expect(schedule({interval:4,due:'',reviews:2},false).interval).toBe(0)});
  it('starts and doubles known intervals',()=>{expect(schedule(undefined,true).interval).toBe(1);expect(schedule({interval:2,due:'',reviews:2},true).interval).toBe(4)});
});
describe('backward-compatible progress storage',()=>{
  it('loads existing v1 progress without resetting any collection',()=>{
    localStorage.setItem('phychem-study-v1',JSON.stringify({
      theme:'dark',completed:['K01'],bookmarkedFormulas:['F-K-001'],bookmarkedProblems:['P-K-001'],
      attempts:[{problemId:'P-K-001',correct:true,at:'2026-01-01T00:00:00.000Z'}],
      flashcards:{'F-K-001':{interval:2,due:'2026-01-03T00:00:00.000Z',reviews:2}}
    }));
    const store=loadStore();
    expect(store.theme).toBe('dark');
    expect(store.completed).toEqual(['K01']);
    expect(store.bookmarkedFormulas).toEqual(['F-K-001']);
    expect(store.bookmarkedProblems).toEqual(['P-K-001']);
    expect(store.attempts).toHaveLength(1);
    expect(store.flashcards['F-K-001'].reviews).toBe(2);
  });
});
