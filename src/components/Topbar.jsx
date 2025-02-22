import React from 'react';

const Topbar = () => {
  return (
    <div className="topbar">
      <div className="logo">MedicCare</div>
      <input type="text" className="search-bar" placeholder="Search..." />

      <div className="topbar-right">
        <button className="customize-profile-btn">Customize Profile</button>

        {/* Some placeholder icons */}
        <div className="icon">🔔</div>
        <div className="icon">⚙️</div>
        <div className="icon">👤</div>
      </div>
    </div>
  );
};

export default Topbar;
