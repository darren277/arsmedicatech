import { act, renderHook, waitFor } from '@testing-library/react';
import { usePatientSearch } from '../usePatientSearch';

// Mock the API service
const mockSearchPatients = jest.fn();

jest.mock('../../services/api', () => ({
  default: {
    searchPatients: mockSearchPatients,
  },
}));

describe('usePatientSearch', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should initialize with empty query and results', () => {
    const { result } = renderHook(() => usePatientSearch());

    expect(result.current.query).toBe('');
    expect(result.current.results).toEqual([]);
    expect(result.current.loading).toBe(false);
  });

  it('should update query when setQuery is called', () => {
    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('test query');
    });

    expect(result.current.query).toBe('test query');
  });

  it('should search patients when query changes', async () => {
    const mockResults = [
      { id: '1', name: 'John Doe', date_of_birth: '1990-01-01' },
      { id: '2', name: 'Jane Smith', date_of_birth: '1985-05-15' },
    ];

    mockSearchPatients.mockResolvedValue(mockResults);

    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('john');
    });

    await waitFor(() => {
      expect(mockSearchPatients).toHaveBeenCalledWith('john');
    });

    await waitFor(() => {
      expect(result.current.results).toEqual(mockResults);
      expect(result.current.loading).toBe(false);
    });
  });

  it('should show loading state during search', async () => {
    let resolveSearch: (value: any) => void;
    const searchPromise = new Promise(resolve => {
      resolveSearch = resolve;
    });

    mockSearchPatients.mockReturnValue(searchPromise);

    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('test');
    });

    expect(result.current.loading).toBe(true);

    act(() => {
      resolveSearch!([{ id: '1', name: 'Test Patient' }]);
    });

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });

  it('should handle search errors gracefully', async () => {
    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
    mockSearchPatients.mockRejectedValue(new Error('Search failed'));

    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('error test');
    });

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
      expect(result.current.results).toEqual([]);
    });

    expect(consoleErrorSpy).toHaveBeenCalledWith('Error searching patients:', expect.any(Error));

    consoleErrorSpy.mockRestore();
  });

  it('should debounce search requests', async () => {
    jest.useFakeTimers();
    
    mockSearchPatients.mockResolvedValue([]);

    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('a');
    });

    act(() => {
      result.current.setQuery('ab');
    });

    act(() => {
      result.current.setQuery('abc');
    });

    // Fast-forward time to trigger the debounced search
    act(() => {
      jest.runAllTimers();
    });

    await waitFor(() => {
      expect(mockSearchPatients).toHaveBeenCalledTimes(1);
      expect(mockSearchPatients).toHaveBeenCalledWith('abc');
    });

    jest.useRealTimers();
  });

  it('should not search with empty query', async () => {
    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('');
    });

    await waitFor(() => {
      expect(mockSearchPatients).not.toHaveBeenCalled();
    });
  });

  it('should handle rapid query changes', async () => {
    jest.useFakeTimers();
    
    mockSearchPatients.mockResolvedValue([]);

    const { result } = renderHook(() => usePatientSearch());

    // Rapidly change the query
    act(() => {
      result.current.setQuery('a');
    });

    act(() => {
      jest.advanceTimersByTime(100);
    });

    act(() => {
      result.current.setQuery('ab');
    });

    act(() => {
      jest.advanceTimersByTime(100);
    });

    act(() => {
      result.current.setQuery('abc');
    });

    act(() => {
      jest.runAllTimers();
    });

    await waitFor(() => {
      expect(mockSearchPatients).toHaveBeenCalledTimes(1);
      expect(mockSearchPatients).toHaveBeenCalledWith('abc');
    });

    jest.useRealTimers();
  });
}); 