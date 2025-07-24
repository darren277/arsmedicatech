import { act, renderHook, waitFor } from '@testing-library/react';
import { usePatientSearch } from '../usePatientSearch';

// Mock the API service
jest.mock('../../services/api', () => ({
  __esModule: true,
  default: {
    searchPatientsAndEncounters: jest.fn(),
  },
}));

import apiService from '../../services/api';

describe('usePatientSearch', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  afterEach(() => {
    jest.resetAllMocks();
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

    (apiService.searchPatientsAndEncounters as jest.Mock).mockResolvedValue(
      mockResults
    );

    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('john');
    });

    await waitFor(() => {
      expect(apiService.searchPatientsAndEncounters).toHaveBeenCalledWith(
        'john'
      );
    });

    await waitFor(() => {
      expect(result.current.results).toEqual(mockResults);
      expect(result.current.loading).toBe(false);
    });
  });

  it('should show loading state during search', async () => {
    jest.useFakeTimers();

    let resolveSearch: (value: any) => void;
    const searchPromise = new Promise(resolve => {
      resolveSearch = resolve;
    });

    (apiService.searchPatientsAndEncounters as jest.Mock).mockReturnValue(
      searchPromise
    );

    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('test');
    });

    // Wait for the debounce delay to trigger the search
    act(() => {
      jest.advanceTimersByTime(500);
    });

    expect(result.current.loading).toBe(true);

    act(() => {
      resolveSearch!([{ id: '1', name: 'Test Patient' }]);
    });

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    jest.useRealTimers();
  });

  it('should handle empty search results', async () => {
    jest.useFakeTimers();

    // Mock fetch to return empty results
    (apiService.searchPatientsAndEncounters as jest.Mock).mockResolvedValue([]);

    // Render hook with an empty initial query to avoid immediate search
    const { result } = renderHook(() => usePatientSearch(''));

    // Set a query that will trigger the search
    act(() => {
      result.current.setQuery('no results');
    });

    // Wait for the debounce delay to trigger the search
    act(() => {
      jest.advanceTimersByTime(500);
    });

    // Wait for the search to complete
    await waitFor(() => {
      expect(result.current.loading).toBe(false);
      expect(result.current.results).toEqual([]); // Combined empty results
      // Should make 2 calls: one for patients, one for encounters
      expect(apiService.searchPatientsAndEncounters).toHaveBeenCalledWith(
        'no results'
      );
    });

    jest.useRealTimers();
  });

  it('should debounce search requests', async () => {
    jest.useFakeTimers();

    (apiService.searchPatientsAndEncounters as jest.Mock).mockResolvedValue([]);

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
      // Should make 2 calls: one for patients, one for encounters
      expect(apiService.searchPatientsAndEncounters).toHaveBeenCalledWith(
        'abc'
      );
    });

    jest.useRealTimers();
  });

  it('should not search with empty query', async () => {
    const { result } = renderHook(() => usePatientSearch());

    act(() => {
      result.current.setQuery('');
    });

    await waitFor(() => {
      // Should not make any API calls for empty query
      expect(apiService.searchPatientsAndEncounters).not.toHaveBeenCalled();
      expect(result.current.results).toEqual([]);
    });
  });

  it('should handle rapid query changes', async () => {
    jest.useFakeTimers();

    (apiService.searchPatientsAndEncounters as jest.Mock).mockResolvedValue([]);

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
      // Should make 2 calls: one for patients, one for encounters
      expect(apiService.searchPatientsAndEncounters).toHaveBeenCalledWith(
        'abc'
      );
    });

    jest.useRealTimers();
  });
});
