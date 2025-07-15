import { NavLink } from 'react-router-dom';
import { usePluginWidgets } from '../hooks/usePluginWidgets';
import logger from '../services/logging';
import { useUser } from './UserContext';
// It is recommended to use an icon library like react-icons
// import { FiGrid, FiUsers, FiMessageSquare, FiCalendar } from 'react-icons/fi';

const Sidebar = () => {
  const { user, isLoading } = useUser();
  const userType = user?.role || 'guest';
  const widgets = usePluginWidgets();

  logger.debug('Sidebar user:', user);

  if (isLoading) return null; // or a spinner

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
          {userType === 'admin' && (
            <li>
              <NavLink
                to="/organization"
                className={({ isActive }) => (isActive ? 'active' : '')}
              >
                Organization
              </NavLink>
            </li>
          )}
          {userType === 'patient' ? (
            <li>
              {user?.id && (
                <NavLink
                  to={`/intake/${user.id}`}
                  className={({ isActive }) => (isActive ? 'active' : '')}
                >
                  Intake Form
                </NavLink>
              )}
            </li>
          ) : (
            <>
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
                  to="/lab-results"
                  className={({ isActive }) => (isActive ? 'active' : '')}
                >
                  Lab Results
                </NavLink>
              </li>
            </>
          )}
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
          <li>
            <NavLink
              to="/settings"
              className={({ isActive }) => (isActive ? 'active' : '')}
            >
              Settings
            </NavLink>
          </li>
          {widgets.map((widget) => (
            <li key={widget.name}>
              <NavLink to={widget.path} className={({ isActive }) => (isActive ? 'active' : '')}>
                {widget.name}
              </NavLink>
            </li>
          ))}
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
