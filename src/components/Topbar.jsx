import React from 'react';
// import { FiSearch, FiChevronDown } from 'react-icons/fi';
// {/* Some placeholder icons */}
// <div className="icon">🔔</div>
// <div className="icon">⚙️</div>
// <div className="icon">👤</div>

const Topbar = () => {
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

export default Topbar;
