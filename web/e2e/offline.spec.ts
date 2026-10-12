import{test,expect}from'@playwright/test';
import{goto,seed}from'./helpers';

test('an already loaded study session keeps working offline',async({page,context})=>{
  await seed(page);
  await goto(page,'/practice');
  await goto(page,'/');
  await context.setOffline(true);
  await page.getByRole('link',{name:'แบบฝึกหัด'}).click();
  await expect(page).toHaveURL(/\/practice$/);
  await expect(page.locator('main')).toBeVisible();
  await expect(page.locator('h1').first()).toBeVisible();
});

test('first visit while offline is explicitly not supported',async({browser})=>{
  const context=await browser.newContext();
  await context.setOffline(true);
  const page=await context.newPage();
  const failed=await page.goto('http://127.0.0.1:5173/').then(()=>false,()=>true);
  expect(failed).toBe(true);
  await context.close();
});
