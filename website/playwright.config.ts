import { defineConfig, devices } from '@playwright/test';
export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  use: { baseURL: 'http://127.0.0.1:4321', trace: 'retain-on-failure' },
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
  webServer: {
    command: 'npm run preview -- --host 127.0.0.1 --ignore-lock',
    url: 'http://127.0.0.1:4321',
    reuseExistingServer: !process.env.CI,
  },
});
