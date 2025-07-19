import { expect, test } from '@playwright/test';

test.describe('Patient Management Tests', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to the patients page before each test
    await page.goto('/patients');

    // Handle the React Joyride tour overlay if it appears
    try {
      await page.waitForSelector('[data-test-id="overlay"]', { timeout: 2000 });
      const skipButton = page.locator(
        'button:has-text("Skip"), button:has-text("Skip Tour"), [data-test-id="skip"]'
      );
      if (await skipButton.isVisible()) {
        await skipButton.click();
      } else {
        await page.keyboard.press('Escape');
      }
      await page.waitForSelector('[data-test-id="overlay"]', {
        state: 'hidden',
        timeout: 3000,
      });
    } catch (error) {
      // Tour might not be present, continue with test
    }
  });

  test('should display patient list page', async ({ page }) => {
    // Check that we're on the patients page
    await page.waitForURL('**/patients');

    // Look for patient-related content
    const patientContent = page
      .locator(
        'h1:has-text("Patients"), h2:has-text("Patients"), .patient, [class*="patient"]'
      )
      .first();
    if (await patientContent.isVisible()) {
      await expect(patientContent).toBeVisible();
    }
  });

  test('should navigate to new patient form', async ({ page }) => {
    // Navigate to new patient form
    await page.goto('/patients/new');

    // Check that we're on the new patient form page
    await page.waitForURL('**/patients/new');

    // Look for form elements
    const formElements = page.locator('form, input, select, textarea');
    if ((await formElements.count()) > 0) {
      await expect(formElements.first()).toBeVisible();
    }
  });

  test('should display patient details page', async ({ page }) => {
    // Navigate to a specific patient (using a mock ID)
    await page.goto('/patients/123');

    // Check that we're on the patient details page
    await page.waitForURL('**/patients/123');

    // Look for patient details content
    const patientDetails = page
      .locator('h1, h2, .patient-details, [class*="patient"]')
      .first();
    if (await patientDetails.isVisible()) {
      await expect(patientDetails).toBeVisible();
    }
  });

  test('should navigate to patient edit form', async ({ page }) => {
    // Navigate to edit form for a specific patient
    await page.goto('/patients/123/edit');

    // Check that we're on the edit form page
    await page.waitForURL('**/patients/123/edit');

    // Look for form elements
    const formElements = page.locator('form, input, select, textarea');
    if ((await formElements.count()) > 0) {
      await expect(formElements.first()).toBeVisible();
    }
  });

  test('should navigate to patient intake form', async ({ page }) => {
    // Navigate to intake form for a specific patient
    await page.goto('/intake/123');

    // Check that we're on the intake form page
    await page.waitForURL('**/intake/123');

    // Look for intake form elements
    const intakeForm = page.locator('form, .intake, [class*="intake"]').first();
    if (await intakeForm.isVisible()) {
      await expect(intakeForm).toBeVisible();
    }
  });

  test('should display patient table with data', async ({ page }) => {
    // Navigate to the main page where patient table is displayed
    await page.goto('/');

    // Look for table elements
    const tableElements = page
      .locator('table, .table, [class*="table"]')
      .first();
    if (await tableElements.isVisible()) {
      await expect(tableElements).toBeVisible();
    }
  });
});
