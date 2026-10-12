import{expect,type Page}from'@playwright/test';export const KEY='phychem-study-v1';
export const empty={schemaVersion:2,completed:[],bookmarkedFormulas:[],bookmarkedProblems:[],attempts:[],flashcards:{},mockSessions:[]};
export async function seed(page:Page,value:unknown=empty){await page.goto('/');await page.evaluate(([key,data])=>localStorage.setItem(key,JSON.stringify(data)),[KEY,value]as const)}
export async function store(page:Page){return page.evaluate(key=>JSON.parse(localStorage.getItem(key)||'{}'),KEY)}
export async function goto(page:Page,path='/'){await page.goto(path);await expect(page.locator('main')).toBeVisible()}
