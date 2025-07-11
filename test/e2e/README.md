# Playwright E2E Testing

This directory contains end-to-end tests for the ArsMedicaTech React application using Playwright.

**Location**: `test/e2e/` (integrated with existing test structure)

## Overview

Playwright is a powerful end-to-end testing framework that supports multiple browsers and provides excellent debugging capabilities. These tests verify that the application works correctly from a user's perspective.

## Test Structure

- `navigation.spec.ts` - Tests for application navigation and routing
- `patient-management.spec.ts` - Tests for patient-related functionality
- `search-functionality.spec.ts` - Tests for search features
- `responsive-design.spec.ts` - Tests for responsive design across different screen sizes
- `form-interactions.spec.ts` - Tests for form interactions and validation

## Running Tests

### Prerequisites

1. Make sure the development server is running:
   ```bash
   npm start
   ```

2. Install Playwright browsers (if not already installed):
   ```bash
   npm run test:e2e:install
   ```

### Basic Commands

```bash
# Run all e2e tests
npm run test:e2e

# Run tests with UI mode (interactive)
npm run test:e2e:ui

# Run tests in headed mode (see browser)
npm run test:e2e:headed

# Run tests in debug mode
npm run test:e2e:debug

# Show test report
npm run test:e2e:report
```

### Running Specific Tests

```bash
# Run a specific test file
npx playwright test navigation.spec.ts

# Run tests matching a pattern
npx playwright test --grep "navigation"

# Run tests in a specific browser
npx playwright test --project=chromium

# Run tests in mobile viewport
npx playwright test --project="Mobile Chrome"
```

## Configuration

The Playwright configuration is in `playwright.config.ts` at the project root. Key settings:

- **Base URL**: `http://localhost:3012` (matches your React dev server)
- **Test Directory**: `./test/e2e`
- **Browsers**: Chromium, Firefox, WebKit, Mobile Chrome, Mobile Safari
- **Web Server**: Automatically starts `npm start` before running tests
- **Screenshots**: Taken on test failures
- **Videos**: Recorded on test failures
- **Traces**: Collected on first retry

## Writing Tests

### Basic Test Structure

```typescript
import { test, expect } from '@playwright/test';

test.describe('Feature Name', () => {
  test.beforeEach(async ({ page }) => {
    // Setup code that runs before each test
    await page.goto('/');
  });

  test('should do something', async ({ page }) => {
    // Test implementation
    await expect(page.locator('.some-element')).toBeVisible();
  });
});
```

### Best Practices

1. **Use data-testid attributes**: Prefer `data-testid` over CSS classes for element selection
2. **Wait for elements**: Use `await expect().toBeVisible()` instead of `page.waitForSelector()`
3. **Test user workflows**: Focus on testing complete user journeys
4. **Keep tests independent**: Each test should be able to run in isolation
5. **Use descriptive test names**: Make test names clear about what they're testing

### Common Patterns

```typescript
// Navigate to a page
await page.goto('/patients');

// Click on an element
await page.locator('button').click();

// Fill a form field
await page.locator('input[name="email"]').fill('test@example.com');

// Check element visibility
await expect(page.locator('.some-element')).toBeVisible();

// Check element text
await expect(page.locator('h1')).toContainText('Expected Text');

// Wait for navigation
await page.waitForURL('/patients');

// Handle conditional elements
const element = page.locator('.optional-element');
if (await element.isVisible()) {
  await expect(element).toBeVisible();
}
```

## Debugging Tests

### UI Mode
```bash
npm run test:e2e:ui
```
Opens an interactive UI where you can:
- See test results in real-time
- Step through tests
- Inspect elements
- Modify selectors

### Debug Mode
```bash
npm run test:e2e:debug
```
Runs tests in debug mode with:
- Browser window visible
- Slower execution
- Ability to pause execution

### Trace Viewer
```bash
npm run test:e2e:report
```
Shows detailed traces of test execution including:
- Screenshots at each step
- Network requests
- Console logs
- Element interactions

## Continuous Integration

For CI environments, the configuration automatically:
- Runs tests in headless mode
- Retries failed tests twice
- Uses a single worker to avoid conflicts
- Fails the build if `test.only` is left in code

## Browser Support

Tests run against:
- **Desktop**: Chrome, Firefox, Safari
- **Mobile**: Chrome (Pixel 5), Safari (iPhone 12)

## Troubleshooting

### Common Issues

1. **Tests fail because server isn't running**
   - Make sure `npm start` is running on port 3012
   - Check that the webServer configuration in `playwright.config.ts` is correct

2. **Element not found**
   - Verify the element selector is correct
   - Check if the element is in a different viewport or hidden
   - Use `page.pause()` in debug mode to inspect the page

3. **Timing issues**
   - Use `await expect().toBeVisible()` instead of `page.waitForSelector()`
   - Add explicit waits for animations or loading states

4. **Mobile tests failing**
   - Check if the app has proper mobile responsive design
   - Verify touch interactions work correctly

### Getting Help

- [Playwright Documentation](https://playwright.dev/docs/intro)
- [Playwright API Reference](https://playwright.dev/docs/api/class-playwright)
- [Playwright Test API](https://playwright.dev/docs/test-api-testing)

## Adding New Tests

When adding new tests:

1. Create a new `.spec.ts` file in the `test/e2e` directory
2. Follow the existing naming convention
3. Add appropriate `data-testid` attributes to components being tested
4. Update this README if adding new test categories
5. Consider adding the new test file to CI if it's critical functionality 