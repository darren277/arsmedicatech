import { MagnifyingGlassCircleIcon } from '@heroicons/react/24/outline';
import Spinner from 'react-bootstrap/Spinner';

export default function SearchBox({ value, onChange, loading }) {
  return (
    <div className="search-input-wrapper">
      <div className="search-icon">
        <MagnifyingGlassCircleIcon />
      </div>
      <input
        type="text"
        placeholder="Search patient histories..."
        className="search-input"
        value={value}
        onChange={e => onChange(e.target.value)}
      />
      {loading && <Spinner size={16} />}
    </div>
  );
}
