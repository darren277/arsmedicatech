import { NavLink } from 'react-router-dom';
import { useUser } from './UserContext';
// It is recommended to use an icon library like react-icons
// import { FiGrid, FiUsers, FiMessageSquare, FiCalendar } from 'react-icons/fi';

const Sidebar = () => {
  const { user } = useUser();
  const userType = user?.role || 'guest';

  return (
    <aside className="sidebar">
      <div className="logo-container">ArsMedicaTech</div>
      <nav>
        <ul>
          {/* Add the `active` class to the active route... */}
          <li>
            <NavLink
              to="/"
              className={({ isActive }) => (isActive ? 'active' : '')}
            >
              Dashboard
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/patients"
              className={({ isActive }) => (isActive ? 'active' : '')}
            >
              Patients
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/messages"
              className={({ isActive }) => (isActive ? 'active' : '')}
            >
              Messages
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/schedule"
              className={({ isActive }) => (isActive ? 'active' : '')}
            >
              Schedule
            </NavLink>
          </li>
        </ul>
      </nav>
      <div className="sidebar-footer">
        <div className="doctor-avatar"></div>
        <div className="doctor-info">
          <h4>Hello Dr. Carvolth</h4>
          <p>You have 4 remaining appointments scheduled today</p>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
