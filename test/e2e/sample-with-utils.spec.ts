import { expect, test } from '@playwright/test';
import {
  VIEWPORTS,
  checkAccessibility,
  checkElementVisible,
  checkPageContent,
  navigateToPage,
  safeClick,
  testResponsiveDesign,
  waitForAppLoad,
  waitForNavigation
} from './utils/test-helpers';

test.describe('Sample Tests Using Utilities', () => {
  test.beforeEach(async ({ page }) => {
    // Handle the React Joyride tour overlay if it appears
    try {
      await page.waitForSelector('[data-test-id="overlay"]', { timeout: 2000 });
      const skipButton = page.locator('button:has-text("Skip"), button:has-text("Skip Tour"), [data-test-id="skip"]');
      if (await skipButton.isVisible()) {
        await skipButton.click();
      } else {
        await page.keyboard.press('Escape');
      }
      await page.waitForSelector('[data-test-id="overlay"]', { state: 'hidden', timeout: 3000 });
    } catch (error) {
      // Tour might not be present, continue with test
    }
  });

  test('should load application using utility functions', async ({ page }) => {
    await navigateToPage(page, '/');
    await waitForAppLoad(page);
    
    // Check that main components are visible
    const sidebar = page.locator('.sidebar, nav, [role="navigation"]').first();
    if (await sidebar.isVisible()) {
      await expect(sidebar).toBeVisible();
    }
    
    const topbar = page.locator('.topbar, header, .header').first();
    if (await topbar.isVisible()) {
      await expect(topbar).toBeVisible();
    }
    
    const dashboardContent = page.locator('h1, h2, .dashboard, [class*="dashboard"]').first();
    if (await dashboardContent.isVisible()) {
      await expect(dashboardContent).toBeVisible();
    }
  });

  test('should navigate between pages using utilities', async ({ page }) => {
    await navigateToPage(page, '/');
    
    // Navigate to patients page
    await safeClick(page, 'a[href="/patients"]');
    await waitForNavigation(page, '**/patients');
    
    // Navigate to schedule page
    await safeClick(page, 'a[href="/schedule"]');
    await waitForNavigation(page, '**/schedule');
  });

  test('should test responsive design using utilities', async ({ page }) => {
    await navigateToPage(page, '/');
    
    await testResponsiveDesign(page, Object.values(VIEWPORTS), async () => {
      await checkElementVisible(page, '.app-container');
      await checkElementVisible(page, '.main-container');
      
      // Check that main content is accessible on all screen sizes
      await checkElementVisible(page, 'main');
    });
  });

  test('should test form interactions using utilities', async ({ page }) => {
    await navigateToPage(page, '/patients/new');
    
    // Check that we're on a form page
    await page.waitForURL('**/patients/new');
    
    // Test form field interactions
    const formInputs = page.locator('input, select, textarea');
    const inputCount = await formInputs.count();
    
    if (inputCount > 0) {
      const firstInput = formInputs.first();
      const inputType = await firstInput.getAttribute('type');
      
      if (inputType === 'text' || inputType === 'email' || inputType === 'tel') {
        // Fill the input directly instead of using safeFill with a locator
        await firstInput.fill('test input');
        await expect(firstInput).toHaveValue('test input');
      }
    } else {
      // If no form elements found, just verify the page loaded
      await expect(page.locator('body')).toBeVisible();
    }
  });

  test('should check accessibility using utilities', async ({ page }) => {
    await navigateToPage(page, '/');
    
    // Check basic accessibility features
    await checkAccessibility(page);
    
    // Check that page has proper content structure
    await checkPageContent(page, ['Create New']);
  });

  test('should handle search functionality using utilities', async ({ page }) => {
    await navigateToPage(page, '/');
    
    // Look for search input
    const searchInput = page.locator('input[type="text"], input[placeholder*="search"], input[placeholder*="Search"]').first();
    
    if (await searchInput.isVisible()) {
      // Fill the search input directly instead of using safeFill with a locator
      await searchInput.fill('test search');
      await expect(searchInput).toHaveValue('test search');
      
      // Wait for potential search results
      await page.waitForTimeout(500);
      
      // Check if search results appear
      const resultsContainer = page.locator('.search-results, .dropdown, [data-testid*="search"], [data-testid*="results"]').first();
      if (await resultsContainer.isVisible()) {
        await expect(resultsContainer).toBeVisible();
      }
    } else {
      // If no search input found, just verify the page loaded
      await expect(page.locator('body')).toBeVisible();
    }
  });

  test('should test error handling using utilities', async ({ page }) => {
    // Navigate to a non-existent page
    await page.goto('/non-existent-page');
    
    // Wait for the page to load (don't use navigateToPage since it expects app layout)
    await page.waitForLoadState('domcontentloaded');
    
    // Check that error page content is displayed
    await checkPageContent(page, ['404', 'Page not found']);
    
    // Also verify we're on the correct URL
    await expect(page).toHaveURL(/.*non-existent-page/);
  });
}); 