import { MagnifyingGlassCircleIcon } from '@heroicons/react/24/outline';
import Spinner from 'react-bootstrap/Spinner';

export default function SearchBox({
  value,
  onChange,
  loading,
}: {
  value: string;
  onChange: (value: string) => void;
  loading?: boolean;
}): JSX.Element {
  return (
    <div className="search-input-wrapper">
      <div className="search-icon">
        <MagnifyingGlassCircleIcon />
      </div>
      <input
        type="text"
        placeholder="Search patients and encounters..."
        className="search-input"
        value={value}
        onChange={e => onChange(e.target.value)}
      />
      {loading && <Spinner size="sm" />}
    </div>
  );
}
