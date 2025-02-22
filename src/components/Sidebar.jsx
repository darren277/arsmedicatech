import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidebar-top-section">
        {/* Silhouette or placeholder for the doctor icon */}
        <div className="doctor-icon"></div>

        <div className="sidebar-greeting">
          <p>Hello</p>
          <h3>Dr. Carvolth</h3>
          <p>You Have 4 Remaining<br/>Appointments Scheduled Today</p>
        </div>
      </div>

      {/* Nav links */}
      <nav>
        <ul>
          <li><Link to="/">Dashboard</Link></li>
          <li><Link to="/patients">Patients</Link></li>
          <li><Link to="/messages">Messages</Link></li>
          <li><Link to="/schedule">Schedule</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
