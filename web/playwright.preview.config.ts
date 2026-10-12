import{defineConfig}from'@playwright/test';import base from'./playwright.config';
export default defineConfig({...base,testMatch:'production-smoke.spec.ts',use:{...base.use,baseURL:'http://127.0.0.1:4173'},webServer:{command:'pnpm exec vite preview --host 127.0.0.1 --port 4173 --strictPort',url:'http://127.0.0.1:4173',reuseExistingServer:false,timeout:30_000}});
