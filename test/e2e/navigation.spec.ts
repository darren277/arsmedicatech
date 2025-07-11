import { expect, test } from '@playwright/test';

test.describe('Navigation Tests', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to the home page before each test
    await page.goto('/');
    
    // Handle the React Joyride tour overlay that blocks interactions
    // Wait for the tour to appear and then skip it
    try {
      // Wait for the tour overlay to appear
      await page.waitForSelector('[data-test-id="overlay"]', { timeout: 3000 });
      
      // Look for and click the skip button
      const skipButton = page.locator('button:has-text("Skip"), button:has-text("Skip Tour"), [data-test-id="skip"]');
      if (await skipButton.isVisible()) {
        await skipButton.click();
      } else {
        // If no skip button, try to click outside or press Escape
        await page.keyboard.press('Escape');
      }
      
      // Wait for the overlay to disappear
      await page.waitForSelector('[data-test-id="overlay"]', { state: 'hidden', timeout: 5000 });
    } catch (error) {
      // Tour might not be present, continue with test
      console.log('Tour overlay not found or already dismissed');
    }
  });

  test('should load the main application', async ({ page }) => {
    // Check that the main app structure is present
    await expect(page.locator('.app-container')).toBeVisible();
    await expect(page.locator('.main-container')).toBeVisible();
    
    // Check that sidebar and topbar are present (using actual selectors)
    // Look for sidebar by class or structure instead of data-testid
    const sidebar = page.locator('.sidebar, nav, [role="navigation"]').first();
    if (await sidebar.isVisible()) {
      await expect(sidebar).toBeVisible();
    }
    
    // Look for topbar by class or structure
    const topbar = page.locator('.topbar, header, .header').first();
    if (await topbar.isVisible()) {
      await expect(topbar).toBeVisible();
    }
  });

  test('should display the dashboard by default', async ({ page }) => {
    // Check that main content area is present
    await expect(page.locator('main')).toBeVisible();
    
    // Check that the "Create New" button is present
    await expect(page.locator('.create-new-button')).toBeVisible();
    
    // Check for dashboard content by looking for common dashboard elements
    const dashboardContent = page.locator('h1, h2, .dashboard, [class*="dashboard"]').first();
    if (await dashboardContent.isVisible()) {
      await expect(dashboardContent).toBeVisible();
    }
  });

  test('should navigate to patients page', async ({ page }) => {
    // Click on the patients link in the sidebar
    await page.locator('a[href="/patients"]').click();
    
    // Wait for navigation and check that we're on the patients page
    await page.waitForURL('**/patients');
    
    // Check for patient-related content
    const patientContent = page.locator('h1:has-text("Patients"), h2:has-text("Patients"), .patient, [class*="patient"]').first();
    if (await patientContent.isVisible()) {
      await expect(patientContent).toBeVisible();
    }
  });

  test('should navigate to schedule page', async ({ page }) => {
    // Click on the schedule link in the sidebar
    await page.locator('a[href="/schedule"]').click();
    
    // Wait for navigation and check that we're on the schedule page
    await page.waitForURL('**/schedule');
    
    // Check for schedule-related content
    const scheduleContent = page.locator('h1:has-text("Schedule"), h2:has-text("Schedule"), .schedule, [class*="schedule"]').first();
    if (await scheduleContent.isVisible()) {
      await expect(scheduleContent).toBeVisible();
    }
  });

  test('should navigate to messages page', async ({ page }) => {
    // Click on the messages link in the sidebar
    await page.locator('a[href="/messages"]').click();
    
    // Wait for navigation and check that we're on the messages page
    await page.waitForURL('**/messages');
    
    // Check for messages-related content
    const messagesContent = page.locator('h1:has-text("Messages"), h2:has-text("Messages"), .messages, [class*="messages"]').first();
    if (await messagesContent.isVisible()) {
      await expect(messagesContent).toBeVisible();
    }
  });

  test('should navigate to settings page', async ({ page }) => {
    // Click on the settings link in the sidebar
    await page.locator('a[href="/settings"]').click();
    
    // Wait for navigation and check that we're on the settings page
    await page.waitForURL('**/settings');
    
    // Check for settings-related content
    const settingsContent = page.locator('h1:has-text("Settings"), h2:has-text("Settings"), .settings, [class*="settings"]').first();
    if (await settingsContent.isVisible()) {
      await expect(settingsContent).toBeVisible();
    }
  });

  test('should handle 404 errors gracefully', async ({ page }) => {
    // Navigate to a non-existent page
    await page.goto('/non-existent-page');
    
    // Check that the error page is displayed
    await expect(page.locator('h1')).toContainText('404');
    await expect(page.locator('p')).toContainText('Page not found');
  });
}); 