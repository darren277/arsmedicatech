import React, { useState, useEffect, useRef } from 'react';
import SearchBox      from "./SearchBox";
// import SearchDropdown from "./SearchDropdown";
import { ProfilePanel }   from "./ProfilePanel";
// import { FiSearch, FiChevronDown } from 'react-icons/fi';
// {/* Some placeholder icons */}
// <div className="icon">🔔</div>
// <div className="icon">⚙️</div>
// <div className="icon">👤</div>

import API_URL from '../env_vars'; // Adjust the import path as necessary

// Using inline SVGs for icons to avoid external dependencies
const SearchIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
    </svg>
);

const ChevronDownIcon = () => (
     <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <polyline points="6 9 12 15 18 9"></polyline>
    </svg>
);

const TopbarOld2 = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [results, setResults] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [isDropdownVisible, setDropdownVisible] = useState(false);
    const searchContainerRef = useRef(null);

    // Debounce effect to prevent API calls on every keystroke
    useEffect(() => {
        if (searchTerm.length < 2) {
            setResults([]);
            setDropdownVisible(false);
            return;
        }

        setIsLoading(true);
        const timerId = setTimeout(() => {
            fetch(`${API_URL}/api/patients/search?q=${searchTerm}`)
                .then(res => res.json())
                .then(data => {
                    setResults(data);
                    setIsLoading(false);
                    setDropdownVisible(true);

                    console.log("Search results:", data);
                })
                .catch(error => {
                    console.error("Search API failed:", error);
                    setIsLoading(false);
                });
        }, 500); // 500ms delay

        return () => {
            clearTimeout(timerId);
        };
    }, [searchTerm]);

    // Effect to handle clicks outside the search container to close dropdown
    useEffect(() => {
        function handleClickOutside(event) {
            if (searchContainerRef.current && !searchContainerRef.current.contains(event.target)) {
                setDropdownVisible(false);
            }
        }
        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, [searchContainerRef]);


    return (
        <>
            {/* Simple CSS for styling the component */}
            <header className="topbar">
                <div className="search-container" ref={searchContainerRef}>
                    <div className="search-input-wrapper">
                         <div className="search-icon"><SearchIcon /></div>
                        <input
                            type="text"
                            placeholder="Search patient histories..."
                            className="search-input"
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                            onFocus={() => setDropdownVisible(true)}
                        />
                    </div>
                    {isDropdownVisible && (searchTerm.length > 1) && (
                        <div className="search-results-dropdown">
                            {isLoading ? (
                                <div className="loading-message">Searching...</div>
                            ) : results.length > 0 ? (
                                results.map(result => (
                                    <div key={result.id} className="search-result-item">
                                        <div className="patient-name">{result.first_name} {result.last_name}</div>
                                        <div
                                            className="result-snippet"
                                            dangerouslySetInnerHTML={{ __html: result.highlighted_note }}
                                        />
                                    </div>
                                ))
                            ) : (
                                <div className="no-results-message">No results found for "{searchTerm}"</div>
                            )}
                        </div>
                    )}
                </div>
            </header>
        </>
    );
};

const TopbarOld = () => {
    return (
        <header className="topbar">
            <div className="search-container">
                {/* <FiSearch className="search-icon" /> */}
                <input type="text" placeholder="Search..." className="search-input" />
            </div>
            <div className="profile-section">
                <div className="customize-profile">
                    <span>Customize Profile</span>
                    {/* <FiChevronDown /> */}
                </div>
                <div className="user-profile">
                    <span>Hello<br/><b>Dr. Carvolth</b></span>
                    <div className="user-avatar"></div>
                </div>
            </div>
        </header>
    );
};

/*
interface Props {
    query: string;
    onQueryChange(q: string): void;
    results: any[];
    loading: boolean;
}
*/

//export default function Topbar(props: Props) {
export default function Topbar(props) {
    return (
        <header className="topbar">
            <div className="search-container">
                <SearchBox value={props.query} onChange={props.onQueryChange} loading={props.loading} />
            </div>

            <ProfilePanel />
        </header>
    );
}

//export default Topbar;
