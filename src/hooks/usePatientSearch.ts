import { useEffect, useState } from 'react';

import apiService from '../services/api';

// generic debounce – re-usable everywhere
function useDebounce<T>(value: T, delay = 500) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);

  return debounced;
}

export function usePatientSearch(initialQuery = '') {
  const [query, setQuery] = useState(initialQuery);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const debouncedQuery = useDebounce(query, 500);

  useEffect(() => {
    if (debouncedQuery.trim().length < 2) {
      setResults([]);
      return;
    }

    let cancelled = false;
    (async () => {
      setLoading(true);
      try {
        const data = await apiService.searchPatients(debouncedQuery);
        if (!cancelled) setResults(data);
      } catch (error) {
        console.error('Search failed:', error);
        if (!cancelled) setResults([]);
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [debouncedQuery]);

  return { query, setQuery, results, loading };
}
