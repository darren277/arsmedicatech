import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import React from 'react';
import LoginForm from '../LoginForm';

// Mock the auth service
jest.mock('../../services/auth', () => ({
  login: jest.fn(),
}));

describe('LoginForm', () => {
  const mockOnLogin = jest.fn();
  const mockOnSwitchToRegister = jest.fn();
  const mockOnClose = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('renders login form with all required fields', () => {
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    expect(screen.getByLabelText(/username/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /sign in/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /create account/i })).toBeInTheDocument();
  });

  it('shows validation errors for empty fields on submit', async () => {
    const user = userEvent.setup();
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/username is required/i)).toBeInTheDocument();
      expect(screen.getByText(/password is required/i)).toBeInTheDocument();
    });
  });

  it('validates username format', async () => {
    const user = userEvent.setup();
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    const usernameInput = screen.getByLabelText(/username/i);
    await user.type(usernameInput, 'invalid username!');

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/username can only contain letters, numbers, and underscores/i)).toBeInTheDocument();
    });
  });

  it('validates email format', async () => {
    const user = userEvent.setup();
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    const emailInput = screen.getByLabelText(/email/i);
    await user.type(emailInput, 'invalid-email');

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/please enter a valid email address/i)).toBeInTheDocument();
    });
  });

  it('validates password strength', async () => {
    const user = userEvent.setup();
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    const passwordInput = screen.getByLabelText(/password/i);
    await user.type(passwordInput, 'weak');

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/password must contain at least one uppercase letter/i)).toBeInTheDocument();
      expect(screen.getByText(/password must contain at least one lowercase letter/i)).toBeInTheDocument();
      expect(screen.getByText(/password must contain at least one number/i)).toBeInTheDocument();
    });
  });

  it('calls onLogin with valid form data', async () => {
    const user = userEvent.setup();
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    const usernameInput = screen.getByLabelText(/username/i);
    const passwordInput = screen.getByLabelText(/password/i);

    await user.type(usernameInput, 'testuser');
    await user.type(passwordInput, 'TestPass123');

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);

    await waitFor(() => {
      expect(mockOnLogin).toHaveBeenCalledWith({
        username: 'testuser',
        password: 'TestPass123',
      });
    });
  });

  it('calls onSwitchToRegister when create account button is clicked', async () => {
    const user = userEvent.setup();
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    const registerButton = screen.getByRole('button', { name: /create account/i });
    await user.click(registerButton);

    expect(mockOnSwitchToRegister).toHaveBeenCalled();
  });

  it('clears validation errors when user starts typing', async () => {
    const user = userEvent.setup();
    render(
      <LoginForm onLogin={mockOnLogin} onSwitchToRegister={mockOnSwitchToRegister} onClose={mockOnClose} />
    );

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/username is required/i)).toBeInTheDocument();
    });

    const usernameInput = screen.getByLabelText(/username/i);
    await user.type(usernameInput, 'test');

    await waitFor(() => {
      expect(screen.queryByText(/username is required/i)).not.toBeInTheDocument();
    });
  });

  it('shows loading state during form submission', async () => {
    const user = userEvent.setup();
    const mockLoginWithDelay = jest.fn().mockImplementation(() => 
      new Promise(resolve => setTimeout(resolve, 100))
    );
    
    render(
      <LoginForm 
        onLogin={mockLoginWithDelay} 
        onSwitchToRegister={mockOnSwitchToRegister} 
        onClose={mockOnClose}
      />
    );

    const usernameInput = screen.getByLabelText(/username/i);
    const passwordInput = screen.getByLabelText(/password/i);

    await user.type(usernameInput, 'testuser');
    await user.type(passwordInput, 'TestPass123');

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    await user.click(submitButton);

    expect(submitButton).toBeDisabled();
    expect(screen.getByText(/signing in/i)).toBeInTheDocument();
  });
}); 