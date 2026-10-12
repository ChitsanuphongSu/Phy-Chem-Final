import{test,expect}from'@playwright/test';

test('GitHub Pages build renders every route and keeps source links under repository base',async({page})=>{
  const errors:string[]=[],badResponses:string[]=[];
  page.on('console',message=>{if(message.type()==='error')errors.push(message.text())});
  page.on('response',response=>{if(response.status()>=400)badResponses.push(`${response.status()} ${response.url()}`)});
  const deploymentRoot='http://127.0.0.1:4174/Phy-Chem-Final/';
  for(const route of['','#/notes','#/formulas','#/practice','#/mock','#/flashcards','#/exam-focus']){
    await page.goto(new URL(route,deploymentRoot).href);
    await expect(page.locator('main')).toBeVisible();
    await expect(page.locator('h1')).toBeVisible();
  }
  const sourceLink=page.getByRole('link',{name:'เปิดหน้าต้นฉบับ'}).first();
  await expect(sourceLink).toHaveAttribute('href',/^\/Phy-Chem-Final\/sources\//);
  expect({errors,badResponses}).toEqual({errors:[],badResponses:[]});
});
