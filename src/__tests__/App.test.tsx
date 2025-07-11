import { render, screen } from '@testing-library/react';
import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import App from '../App';

// Mock the UserContext
jest.mock('../components/UserContext', () => ({
  UserProvider: ({ children }: { children: React.ReactNode }) => <div data-testid="user-provider">{children}</div>,
}));

// Mock components that might cause issues in tests
jest.mock('../components/Sidebar', () => {
  return function MockSidebar() {
    return <div data-testid="sidebar">Sidebar</div>;
  };
});

jest.mock('../components/Topbar', () => {
  return function MockTopbar() {
    return <div data-testid="topbar">Topbar</div>;
  };
});

jest.mock('../components/PatientTable', () => ({
  PatientTable: function MockPatientTable() {
    return <div data-testid="patient-table">Patient Table</div>;
  },
}));

jest.mock('../pages/Dashboard', () => {
  return function MockDashboard() {
    return <div data-testid="dashboard">Dashboard</div>;
  };
});

jest.mock('../pages/Messages', () => {
  return function MockMessages() {
    return <div data-testid="messages">Messages</div>;
  };
});

jest.mock('../pages/Schedule', () => {
  return function MockSchedule() {
    return <div data-testid="schedule">Schedule</div>;
  };
});

jest.mock('../components/PatientList', () => {
  return function MockPatientList() {
    return <div data-testid="patient-list">Patient List</div>;
  };
});

jest.mock('../components/PatientForm', () => {
  return function MockPatientForm() {
    return <div data-testid="patient-form">Patient Form</div>;
  };
});

jest.mock('../components/Patient', () => {
  return function MockPatient() {
    return <div data-testid="patient">Patient</div>;
  };
});

jest.mock('../components/PatientIntakeForm', () => {
  return function MockPatientIntakeForm() {
    return <div data-testid="patient-intake-form">Patient Intake Form</div>;
  };
});

jest.mock('../components/Settings', () => {
  return function MockSettings() {
    return <div data-testid="settings">Settings</div>;
  };
});

// Mock the usePatientSearch hook
jest.mock('../hooks/usePatientSearch', () => ({
  usePatientSearch: () => ({
    query: '',
    setQuery: jest.fn(),
    results: [],
    loading: false,
  }),
}));

describe('App Component', () => {
  it('renders the main app structure', () => {
    render(
      <MemoryRouter>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('user-provider')).toBeInTheDocument();
    expect(screen.getByTestId('sidebar')).toBeInTheDocument();
    expect(screen.getByTestId('topbar')).toBeInTheDocument();
    expect(screen.getByTestId('patient-table')).toBeInTheDocument();
  });

  it('renders dashboard on root path', () => {
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('dashboard')).toBeInTheDocument();
  });

  it('renders messages page on /messages path', () => {
    render(
      <MemoryRouter initialEntries={['/messages']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('messages')).toBeInTheDocument();
  });

  it('renders schedule page on /schedule path', () => {
    render(
      <MemoryRouter initialEntries={['/schedule']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('schedule')).toBeInTheDocument();
  });

  it('renders patient list on /patients path', () => {
    render(
      <MemoryRouter initialEntries={['/patients']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('patient-list')).toBeInTheDocument();
  });

  it('renders patient form on /patients/new path', () => {
    render(
      <MemoryRouter initialEntries={['/patients/new']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('patient-form')).toBeInTheDocument();
  });

  it('renders patient details on /patients/:id path', () => {
    render(
      <MemoryRouter initialEntries={['/patients/123']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('patient')).toBeInTheDocument();
  });

  it('renders patient edit form on /patients/:id/edit path', () => {
    render(
      <MemoryRouter initialEntries={['/patients/123/edit']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('patient-form')).toBeInTheDocument();
  });

  it('renders patient intake form on /intake/:patientId path', () => {
    render(
      <MemoryRouter initialEntries={['/intake/123']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('patient-intake-form')).toBeInTheDocument();
  });

  it('renders settings page on /settings path', () => {
    render(
      <MemoryRouter initialEntries={['/settings']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByTestId('settings')).toBeInTheDocument();
  });

  it('renders about page on /about path', () => {
    render(
      <MemoryRouter initialEntries={['/about']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByText('About')).toBeInTheDocument();
    expect(screen.getByText('This is the about page.')).toBeInTheDocument();
  });

  it('renders contact page on /contact path', () => {
    render(
      <MemoryRouter initialEntries={['/contact']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByText('Contact')).toBeInTheDocument();
    expect(screen.getByText('This is the contact page.')).toBeInTheDocument();
  });

  it('renders 404 page for unknown routes', () => {
    render(
      <MemoryRouter initialEntries={['/unknown-route']}>
        <App />
      </MemoryRouter>
    );

    expect(screen.getByText('404')).toBeInTheDocument();
    expect(screen.getByText('Page not found.')).toBeInTheDocument();
  });
}); 