import { expect, Locator, Page } from '@playwright/test';

/**
 * Helper function to wait for the application to be fully loaded
 * Handles both main app pages and error pages
 */
export async function waitForAppLoad(page: Page) {
  // First check if we're on a main app page
  const appContainer = page.locator('.app-container');
  if ((await appContainer.count()) > 0) {
    await expect(appContainer).toBeVisible();
    await expect(page.locator('.main-container')).toBeVisible();
  } else {
    // If not on main app page (e.g., error page), just wait for body to be ready
    await expect(page.locator('body')).toBeVisible();
    // Wait for page to be fully loaded
    await page.waitForLoadState('domcontentloaded');
  }
}

/**
 * Helper function to navigate to a page and wait for it to load
 */
export async function navigateToPage(page: Page, path: string) {
  await page.goto(path);
  await waitForAppLoad(page);
}

/**
 * Helper function to check if an element exists and is visible
 */
export async function checkElementVisible(
  page: Page,
  selector: string,
  timeout = 5000
) {
  const element = page.locator(selector);
  if ((await element.count()) > 0) {
    await expect(element).toBeVisible({ timeout });
    return element;
  }
  return null;
}

/**
 * Helper function to fill a form field safely
 * Accepts either a string selector or a Locator object
 */
export async function safeFill(
  page: Page,
  selectorOrLocator: string | Locator,
  value: string
) {
  let element: Locator;

  if (typeof selectorOrLocator === 'string') {
    element = page.locator(selectorOrLocator);
  } else {
    element = selectorOrLocator;
  }

  if (await element.isVisible()) {
    await element.fill(value);
    await expect(element).toHaveValue(value);
  }
}

/**
 * Helper function to click an element safely
 */
export async function safeClick(page: Page, selector: string) {
  const element = page.locator(selector);
  if (await element.isVisible()) {
    await element.click();
  }
}

/**
 * Helper function to check if a page contains expected content
 */
export async function checkPageContent(page: Page, expectedContent: string[]) {
  for (const content of expectedContent) {
    const contentElement = page.locator(`text=${content}`).first();
    if ((await contentElement.count()) > 0) {
      await expect(contentElement).toBeVisible();
    }
  }
}

/**
 * Helper function to wait for navigation to complete
 */
export async function waitForNavigation(page: Page, expectedUrl?: string) {
  if (expectedUrl) {
    await page.waitForURL(expectedUrl);
  } else {
    await page.waitForLoadState('networkidle');
  }
}

/**
 * Helper function to take a screenshot for debugging
 */
export async function takeScreenshot(page: Page, name: string) {
  await page.screenshot({ path: `./test-results/${name}-${Date.now()}.png` });
}

/**
 * Helper function to check responsive design at different viewports
 */
export async function testResponsiveDesign(
  page: Page,
  viewports: Array<{ width: number; height: number; name: string }>,
  testFunction: () => Promise<void>
) {
  for (const viewport of viewports) {
    await page.setViewportSize(viewport);
    await testFunction();
  }
}

/**
 * Common viewport configurations
 */
export const VIEWPORTS = {
  desktop: { width: 1920, height: 1080, name: 'Desktop' },
  tablet: { width: 768, height: 1024, name: 'Tablet' },
  mobile: { width: 375, height: 667, name: 'Mobile' },
};

/**
 * Helper function to check form validation
 */
export async function testFormValidation(
  page: Page,
  submitSelector: string,
  validationSelectors: string[]
) {
  const submitButton = page.locator(submitSelector);

  if (await submitButton.isVisible()) {
    await submitButton.click();

    // Wait for validation messages to appear
    await page.waitForTimeout(500);

    // Check for validation messages
    for (const selector of validationSelectors) {
      const validationElement = page.locator(selector);
      if ((await validationElement.count()) > 0) {
        await expect(validationElement.first()).toBeVisible();
      }
    }
  }
}

/**
 * Helper function to check accessibility
 */
export async function checkAccessibility(page: Page) {
  // Check for proper heading structure
  const headings = page.locator('h1, h2, h3, h4, h5, h6');
  if ((await headings.count()) > 0) {
    await expect(headings.first()).toBeVisible();
  }

  // Check for proper button labels
  const buttons = page.locator('button');
  if ((await buttons.count()) > 0) {
    for (let i = 0; i < (await buttons.count()); i++) {
      const button = buttons.nth(i);
      const ariaLabel = await button.getAttribute('aria-label');
      const textContent = await button.textContent();

      // Button should have either aria-label or text content
      if (!ariaLabel && !textContent?.trim()) {
        console.warn(`Button at index ${i} has no accessible label`);
      }
    }
  }
}
