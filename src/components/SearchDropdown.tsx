import { useEffect, useRef, useState } from 'react';

export default function SearchDropdown({
  show,
  loading,
  results,
}: {
  show: boolean;
  loading: boolean;
  results: Array<{
    id: number;
    first_name: string;
    last_name: string;
    highlighted_note: string;
  }>;
}): JSX.Element | null {
  const [open, setOpen] = useState(false);
  //const ref = useRef<HTMLDivElement | null>(null);
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => setOpen(show), [show]);

  useEffect(() => {
    // e: MouseEvent
    function handleOutside(e: MouseEvent): void {
      // e.target as Node
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener('mousedown', handleOutside);
    return () => document.removeEventListener('mousedown', handleOutside);
  }, []);

  if (!open) return null;

  return (
    <div ref={ref} className="search-results-dropdown">
      {loading ? (
        <div className="loading-message">Searching…</div>
      ) : results.length ? (
        results.map(r => (
          <div key={r.id} className="search-result-item">
            <div className="patient-name">
              {r.first_name} {r.last_name}
            </div>
            <div
              className="result-snippet"
              dangerouslySetInnerHTML={{ __html: r.highlighted_note }}
            />
          </div>
        ))
      ) : (
        <div className="no-results-message">No matches</div>
      )}
    </div>
  );
}
