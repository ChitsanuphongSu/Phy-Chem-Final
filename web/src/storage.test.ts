// @vitest-environment jsdom
import {describe,expect,it} from 'vitest';
import {createAttempt,loadStore,normalizeStore,saveStore,schedule,STORAGE_KEY} from './storage';
describe('spaced repetition schedule',()=>{
  it('resets interval after an unknown answer',()=>{expect(schedule({interval:4,due:'',reviews:2},false).interval).toBe(0)});
  it('starts and doubles known intervals',()=>{expect(schedule(undefined,true).interval).toBe(1);expect(schedule({interval:2,due:'',reviews:2},true).interval).toBe(4)});
});
describe('phase 7C storage safety',()=>{
  it('keeps the established storage key',()=>expect(STORAGE_KEY).toBe('phychem-study-v1'));
  it('recovers from corrupt JSON without throwing',()=>{localStorage.setItem(STORAGE_KEY,'{bad');expect(loadStore().completed).toEqual([])});
  it('adds mock session defaults without deleting legacy data',()=>{const s=normalizeStore({completed:['K01'],customFutureField:42});expect(s.completed).toEqual(['K01']);expect(s.mockSessions).toEqual([]);expect((s as unknown as Record<string,unknown>).customFutureField).toBe(42)});
  it('filters malformed attempts only',()=>{const s=normalizeStore({attempts:[null,{problemId:'P',correct:true,at:'x'}]});expect(s.attempts).toHaveLength(1)});
  it('creates traceable attempt metadata',()=>{const a=createAttempt('P',true,'1 M','smart-practice',2,500);expect(a.source).toBe('smart-practice');expect(a.submittedAnswer).toBe('1 M');expect(a.attemptId).toContain('P:')});
  it('supports the legacy three-argument source call',()=>{const a=createAttempt('P',true,'mock');expect(a.source).toBe('mock');expect(a.submittedAnswer).toBeUndefined()});
  it('round-trips mock sessions',()=>{const s=normalizeStore({mockSessions:[{sessionId:'s',seed:'x',blueprintVersion:'v',questionBankVersion:'q',questionIds:[],startedAt:'x',deadlineAt:'x',status:'ACTIVE',answers:{}}]});expect(saveStore(s)).toBe(true);expect(loadStore().mockSessions[0].sessionId).toBe('s')});
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
