import { render, screen, waitFor } from '@testing-library/react';
import LabResults from '../pages/LabResults';
import apiService from '../services/api';

// Mock the API service
jest.mock('../services/api', () => ({
  getLabResults: jest.fn(),
}));

const mockApiService = apiService as jest.Mocked<typeof apiService>;

// Mock data that matches the structure from lab_results.py
const mockLabResults = {
  hematology: {
    WBC: {
      result: 8.9,
      reference_range: [4.0, 10.0],
      units: '10*9/L',
      description: 'White Blood Cell Count',
    },
    RBC: {
      result: 4.91,
      reference_range: [4.2, 5.4],
      units: '10*12/L',
      description: 'Red Blood Cell Count',
    },
  },
  differential_hematology: {
    Neutrophils: {
      result: 5.4,
      reference_range: [2.0, 7.5],
      units: '10*9/L',
      description: 'Neutrophils',
    },
  },
  general_chemistry: {
    Sodium: {
      result: 138,
      reference_range: [135, 145],
      units: 'mmol/L',
      description: 'Sodium',
    },
  },
  serum_proteins: {
    IgG: {
      result: 13.85,
      reference_range: [7.0, 16.0],
      units: 'g/L',
      description: 'IgG',
    },
  },
};

describe('LabResults Component', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('renders loading state initially', () => {
    mockApiService.getLabResults.mockImplementation(
      () => new Promise(() => {})
    );

    render(<LabResults />);

    expect(screen.getByText('Loading lab results...')).toBeInTheDocument();
  });

  it('renders lab results tables when data is loaded', async () => {
    mockApiService.getLabResults.mockResolvedValue(mockLabResults);

    render(<LabResults />);

    await waitFor(() => {
      expect(screen.getByText('Lab Results')).toBeInTheDocument();
      expect(screen.getByText('Hematology')).toBeInTheDocument();
      expect(screen.getByText('Differential Hematology')).toBeInTheDocument();
      expect(screen.getByText('General Chemistry')).toBeInTheDocument();
      expect(screen.getByText('Serum Proteins')).toBeInTheDocument();
    });
  });

  it('displays test names and results', async () => {
    mockApiService.getLabResults.mockResolvedValue(mockLabResults);

    render(<LabResults />);

    await waitFor(() => {
      expect(screen.getByText('WBC')).toBeInTheDocument();
      expect(screen.getByText('RBC')).toBeInTheDocument();
      expect(screen.getByText('Neutrophils')).toBeInTheDocument();
      expect(screen.getByText('Sodium')).toBeInTheDocument();
      expect(screen.getByText('IgG')).toBeInTheDocument();
    });
  });

  it('shows error message when API call fails', async () => {
    mockApiService.getLabResults.mockRejectedValue(new Error('API Error'));

    render(<LabResults />);

    await waitFor(() => {
      expect(
        screen.getByText('Failed to load lab results. Please try again later.')
      ).toBeInTheDocument();
      expect(screen.getByText('Retry')).toBeInTheDocument();
    });
  });

  it('displays legend with status indicators', async () => {
    mockApiService.getLabResults.mockResolvedValue(mockLabResults);

    render(<LabResults />);

    await waitFor(() => {
      expect(screen.getByText('Legend')).toBeInTheDocument();
      expect(screen.getByText('Within normal range')).toBeInTheDocument();
      expect(screen.getByText('Outside normal range')).toBeInTheDocument();
      expect(
        screen.getByText('Result indicator on range bar')
      ).toBeInTheDocument();
    });
  });

  it('shows click instructions', async () => {
    mockApiService.getLabResults.mockResolvedValue(mockLabResults);

    render(<LabResults />);

    await waitFor(() => {
      expect(
        screen.getByText(/Click on any test name to see detailed information/)
      ).toBeInTheDocument();
    });
  });
});
