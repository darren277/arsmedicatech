export default function SearchBox({
    value,
    onChange,
    loading
}) {
    return (
        <div className="search-input-wrapper">
            <div className="search-icon"><SearchIcon /></div>
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
