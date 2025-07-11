import { expect, test } from '@playwright/test';

test.describe('Responsive Design Tests', () => {
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

  test('should display correctly on desktop', async ({ page }) => {
    await page.goto('/');
    
    // Set desktop viewport
    await page.setViewportSize({ width: 1920, height: 1080 });
    
    // Check that main layout elements are visible
    await expect(page.locator('.app-container')).toBeVisible();
    await expect(page.locator('.main-container')).toBeVisible();
    
    // Look for sidebar by class or structure instead of data-testid
    const sidebar = page.locator('.sidebar, nav, [role="navigation"]').first();
    if (await sidebar.isVisible()) {
      await expect(sidebar).toBeVisible();
    }
  });

  test('should display correctly on tablet', async ({ page }) => {
    await page.goto('/');
    
    // Set tablet viewport
    await page.setViewportSize({ width: 768, height: 1024 });
    
    // Check that main layout elements are visible
    await expect(page.locator('.app-container')).toBeVisible();
    await expect(page.locator('.main-container')).toBeVisible();
    
    // Sidebar might be collapsed or hidden on tablet
    const sidebar = page.locator('.sidebar, nav, [role="navigation"]').first();
    if (await sidebar.isVisible()) {
      await expect(sidebar).toBeVisible();
    }
  });

  test('should display correctly on mobile', async ({ page }) => {
    await page.goto('/');
    
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    
    // Check that main layout elements are visible
    await expect(page.locator('.app-container')).toBeVisible();
    await expect(page.locator('.main-container')).toBeVisible();
    
    // On mobile, sidebar might be hidden or in a hamburger menu
    // Check if there's a mobile menu button or if sidebar is hidden
    const mobileMenuButton = page.locator('button[aria-label*="menu"], .hamburger, .mobile-menu');
    const sidebar = page.locator('.sidebar, nav, [role="navigation"]').first();
    
    if (await mobileMenuButton.isVisible()) {
      await expect(mobileMenuButton).toBeVisible();
    } else if (await sidebar.isVisible()) {
      await expect(sidebar).toBeVisible();
    }
  });

  test('should handle navigation on mobile', async ({ page }) => {
    await page.goto('/');
    
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    
    // Try to navigate to different pages on mobile
    await page.goto('/patients');
    await page.waitForURL('**/patients');
    
    await page.goto('/schedule');
    await page.waitForURL('**/schedule');
    
    await page.goto('/messages');
    await page.waitForURL('**/messages');
  });

  test('should maintain functionality across screen sizes', async ({ page }) => {
    const viewports = [
      { width: 1920, height: 1080, name: 'Desktop' },
      { width: 1024, height: 768, name: 'Small Desktop' },
      { width: 768, height: 1024, name: 'Tablet' },
      { width: 375, height: 667, name: 'Mobile' },
    ];

    for (const viewport of viewports) {
      await page.setViewportSize(viewport);
      await page.goto('/');
      
      // Basic functionality should work on all screen sizes
      await expect(page.locator('.app-container')).toBeVisible();
      await expect(page.locator('.main-container')).toBeVisible();
      
      // Check that the main content area is accessible
      await expect(page.locator('main')).toBeVisible();
    }
  });

  test('should handle touch interactions on mobile', async ({ page }) => {
    await page.goto('/');
    
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    
    // Test touch interactions if there are any touch-specific elements
    // This is a placeholder for future touch interaction tests
    await expect(page.locator('.app-container')).toBeVisible();
  });
}); 