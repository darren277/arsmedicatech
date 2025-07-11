# Testing Guide for ArsMedicaTech Frontend

This document provides a comprehensive guide to testing the React frontend application.

## Testing Setup

The project uses the following testing stack:

- **Jest** - Test runner and assertion library
- **React Testing Library** - Component testing utilities
- **@testing-library/user-event** - User interaction simulation
- **@testing-library/jest-dom** - Custom Jest matchers for DOM testing

## Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode (recommended for development)
npm run test:watch

# Run tests with coverage report
npm run test:coverage

# Run tests in CI mode (no watch, with coverage)
npm run test:ci
```

## Test File Structure

```
src/
├── __tests__/                    # Integration tests
│   ├── App.test.tsx             # Main app integration tests
│   └── test-utils.tsx           # Common test utilities
├── components/
│   └── __tests__/               # Component unit tests
│       └── LoginForm.test.tsx   # LoginForm component tests
├── hooks/
│   └── __tests__/               # Custom hook tests
│       └── usePatientSearch.test.ts
└── setupTests.ts                # Global test setup
```

## Writing Tests

### Component Tests

Component tests should focus on user behavior rather than implementation details. Use React Testing Library's queries in this order of preference:

1. `getByRole` - Most accessible and user-centric
2. `getByLabelText` - For form inputs
3. `getByText` - For visible text
4. `getByTestId` - Last resort for complex cases

Example component test:

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import LoginForm from '../LoginForm';

describe('LoginForm', () => {
  it('should validate required fields', async () => {
    const user = userEvent.setup();
    const mockOnLogin = jest.fn();
    
    render(<LoginForm onLogin={mockOnLogin} onSwitchToRegister={jest.fn()} onClose={jest.fn()} />);
    
    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);
    
    expect(screen.getByText(/username is required/i)).toBeInTheDocument();
    expect(screen.getByText(/password is required/i)).toBeInTheDocument();
  });
});
```

### Hook Tests

Use `renderHook` from React Testing Library to test custom hooks:

```tsx
import { renderHook, act } from '@testing-library/react';
import { usePatientSearch } from '../usePatientSearch';

describe('usePatientSearch', () => {
  it('should initialize with empty state', () => {
    const { result } = renderHook(() => usePatientSearch());
    
    expect(result.current.query).toBe('');
    expect(result.current.results).toEqual([]);
    expect(result.current.loading).toBe(false);
  });
});
```

### Integration Tests

Test how components work together and with routing:

```tsx
import { render, screen } from '../__tests__/test-utils';
import App from '../App';

describe('App Integration', () => {
  it('should render dashboard on root path', () => {
    render(<App />);
    
    expect(screen.getByTestId('dashboard')).toBeInTheDocument();
  });
});
```

## Testing Best Practices

### 1. Test User Behavior, Not Implementation

❌ Don't test implementation details:
```tsx
expect(component.state.isLoading).toBe(true);
```

✅ Do test user-visible behavior:
```tsx
expect(screen.getByText('Loading...')).toBeInTheDocument();
```

### 2. Use Semantic Queries

❌ Avoid test IDs when possible:
```tsx
screen.getByTestId('submit-button');
```

✅ Use semantic queries:
```tsx
screen.getByRole('button', { name: /submit/i });
```

### 3. Test Accessibility

Always test that your components are accessible:

```tsx
it('should have proper ARIA labels', () => {
  render(<SearchInput />);
  
  expect(screen.getByLabelText(/search patients/i)).toBeInTheDocument();
});
```

### 4. Mock External Dependencies

Mock API calls, external services, and browser APIs:

```tsx
// Mock API service
jest.mock('../services/api', () => ({
  default: {
    searchPatients: jest.fn(),
  },
}));

// Mock browser APIs
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: jest.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
  })),
});
```

### 5. Use Test Data Factories

Create reusable test data:

```tsx
import { createMockPatient } from '../__tests__/test-utils';

const mockPatient = createMockPatient({
  name: 'John Doe',
  email: 'john@example.com',
});
```

### 6. Test Error States

Always test error handling:

```tsx
it('should handle API errors gracefully', async () => {
  mockSearchPatients.mockRejectedValue(new Error('API Error'));
  
  const { result } = renderHook(() => usePatientSearch());
  
  act(() => {
    result.current.setQuery('test');
  });
  
  await waitFor(() => {
    expect(result.current.loading).toBe(false);
    expect(result.current.results).toEqual([]);
  });
});
```

## Common Testing Patterns

### Testing Forms

```tsx
it('should submit form with valid data', async () => {
  const user = userEvent.setup();
  const mockOnSubmit = jest.fn();
  
  render(<PatientForm onSubmit={mockOnSubmit} />);
  
  await user.type(screen.getByLabelText(/name/i), 'John Doe');
  await user.type(screen.getByLabelText(/email/i), 'john@example.com');
  await user.click(screen.getByRole('button', { name: /save/i }));
  
  expect(mockOnSubmit).toHaveBeenCalledWith({
    name: 'John Doe',
    email: 'john@example.com',
  });
});
```

### Testing Async Operations

```tsx
it('should show loading state during API call', async () => {
  let resolvePromise: (value: any) => void;
  const promise = new Promise(resolve => {
    resolvePromise = resolve;
  });
  
  mockApiCall.mockReturnValue(promise);
  
  render(<AsyncComponent />);
  
  await user.click(screen.getByRole('button', { name: /load/i }));
  
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
  
  resolvePromise!({ data: 'result' });
  
  await waitFor(() => {
    expect(screen.getByText('result')).toBeInTheDocument();
  });
});
```

### Testing Routing

```tsx
it('should navigate to patient details', async () => {
  const user = userEvent.setup();
  
  render(
    <MemoryRouter>
      <PatientList />
    </MemoryRouter>
  );
  
  await user.click(screen.getByText('John Doe'));
  
  expect(screen.getByText(/patient details/i)).toBeInTheDocument();
});
```

## Coverage Goals

Aim for the following coverage targets:

- **Statements**: 80%+
- **Branches**: 80%+
- **Functions**: 80%+
- **Lines**: 80%+

## Debugging Tests

### Common Issues

1. **Async operations not completing**: Use `waitFor` or `act`
2. **Mock not working**: Check import paths and mock setup
3. **Component not rendering**: Check for missing providers or context

### Debug Commands

```bash
# Run specific test file
npm test LoginForm.test.tsx

# Run tests with verbose output
npm test -- --verbose

# Run tests in debug mode
npm test -- --detectOpenHandles
```

## Continuous Integration

Tests are automatically run in CI with the following configuration:

- Runs on every pull request
- Requires all tests to pass
- Generates coverage reports
- Fails if coverage drops below thresholds

## Resources

- [React Testing Library Documentation](https://testing-library.com/docs/react-testing-library/intro/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [Testing Best Practices](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library) 