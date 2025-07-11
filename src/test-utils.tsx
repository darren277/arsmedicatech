import { render, RenderOptions } from '@testing-library/react';
import React, { ReactElement } from 'react';
import { MemoryRouter } from 'react-router-dom';

// Mock the UserContext for tests
const MockUserProvider = ({ children }: { children: React.ReactNode }) => (
  <div data-testid="user-provider">{children}</div>
);

// Custom render function that includes common providers
const AllTheProviders = ({ children }: { children: React.ReactNode }) => {
  return (
    <MemoryRouter>
      <MockUserProvider>{children}</MockUserProvider>
    </MemoryRouter>
  );
};

const customRender = (
  ui: ReactElement,
  options?: Omit<RenderOptions, 'wrapper'>
) => render(ui, { wrapper: AllTheProviders, ...options });

// Re-export everything
export * from '@testing-library/react';

// Override render method
export { customRender as render };

// Test data factories
export const createMockPatient = (overrides = {}) => ({
  id: '1',
  name: 'John Doe',
  date_of_birth: '1990-01-01',
  email: 'john.doe@example.com',
  phone: '555-123-4567',
  address: '123 Main St, City, State 12345',
  created_at: '2024-01-01T00:00:00Z',
  updated_at: '2024-01-01T00:00:00Z',
  ...overrides,
});

export const createMockUser = (overrides = {}) => ({
  id: '1',
  username: 'testuser',
  email: 'test@example.com',
  role: 'provider',
  specialty: 'Cardiology',
  created_at: '2024-01-01T00:00:00Z',
  updated_at: '2024-01-01T00:00:00Z',
  ...overrides,
});

export const createMockAppointment = (overrides = {}) => ({
  id: '1',
  patient_id: '1',
  provider_id: '1',
  date: '2024-01-15',
  time: '10:00:00',
  type: 'consultation',
  status: 'scheduled',
  notes: 'Regular checkup',
  created_at: '2024-01-01T00:00:00Z',
  updated_at: '2024-01-01T00:00:00Z',
  ...overrides,
});

export const createMockMessage = (overrides = {}) => ({
  id: '1',
  conversation_id: '1',
  sender_id: '1',
  text: 'Hello, how are you?',
  created_at: '2024-01-01T00:00:00Z',
  ...overrides,
});

// Common test helpers
export const waitForLoadingToFinish = () =>
  new Promise(resolve => setTimeout(resolve, 0));

export const mockConsoleError = () => {
  const originalError = console.error;
  const mockError = jest.fn();
  console.error = mockError;
  return {
    mockError,
    restore: () => {
      console.error = originalError;
    },
  };
};

export const mockConsoleWarn = () => {
  const originalWarn = console.warn;
  const mockWarn = jest.fn();
  console.warn = mockWarn;
  return {
    mockWarn,
    restore: () => {
      console.warn = originalWarn;
    },
  };
};

// Mock fetch helper
export const mockFetch = (response: any, ok = true) => {
  const mockResponse = {
    ok,
    json: jest.fn().mockResolvedValue(response),
    status: ok ? 200 : 400,
    statusText: ok ? 'OK' : 'Bad Request',
  };

  global.fetch = jest.fn().mockResolvedValue(mockResponse);
  return global.fetch as jest.MockedFunction<typeof fetch>;
};

// Mock localStorage helper
export const mockLocalStorage = () => {
  const store: Record<string, string> = {};

  return {
    getItem: jest.fn((key: string) => store[key] || null),
    setItem: jest.fn((key: string, value: string) => {
      store[key] = value;
    }),
    removeItem: jest.fn((key: string) => {
      delete store[key];
    }),
    clear: jest.fn(() => {
      Object.keys(store).forEach(key => delete store[key]);
    }),
  };
};
