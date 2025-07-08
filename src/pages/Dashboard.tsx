import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import BarChart from '../components/BarChart';
import LoginForm from '../components/LoginForm';
import RegisterForm from '../components/RegisterForm';
import SignupPopup from '../components/SignupPopup';
import API_URL from '../env_vars';
import { useSignupPopup } from '../hooks/useSignupPopup';
import apiService from '../services/api';
import authService from '../services/auth';

const Panel1 = () => {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch(`${API_URL}/time`, {
      headers: {
        'Access-Control-Allow-Origin': 'http://127.0.0.1:3010',
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
    })
      .then(res => res.json())
      .then(data => {
        setCurrentTime(data.time);
      });
  }, []);

  return (
    <header className="App-header">
      <p>The current time is {currentTime}.</p>
      <p>
        <Link to="patients">Patients</Link>
      </p>
      <p>
        <Link to="about">About</Link>
      </p>
      <p>
        <Link to="contact">Contact</Link>
      </p>
      <button className="sidebar-toggle-button">Toggle Sidebar</button>
      <button className="profile-button">Profile</button>
    </header>
  );
};

const DashboardOld = () => {
  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <div className="cards-grid">
        <div className="card">
          <Panel1 />
        </div>
        <div className="card">
          <BarChart />
        </div>
        <div className="card">Panel 3</div>
        <div className="card">Panel 4</div>
      </div>
    </div>
  );
};

const dashboardData = {
  totalPatients: '1,083',
  totalIncome: '723.43',
  appointments: '324',
  reports: '1,083',
};

const AuthenticatedDashboard = ({
  user,
  onLogout,
}: {
  user: any;
  onLogout: () => void;
}): JSX.Element => {
  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <div className="dashboard-title">
          <h1>Dashboard</h1>
          <p>Welcome back, {user.first_name || user.username}!</p>
        </div>
        <div className="user-info">
          <span className="user-role">{user.role}</span>
          <button onClick={onLogout} className="logout-button">
            Logout
          </button>
        </div>
      </div>
      <div className="dashboard-grid">
        <div className="card stats-card">
          <div className="card-title">Total Patients</div>
          <h2>{dashboardData.totalPatients}</h2>
          <p>+2.7%</p>
        </div>
        <div className="card stats-card">
          <div className="card-title">Total Income</div>
          <h2>${dashboardData.totalIncome}</h2>
          <p>+2.7%</p>
        </div>
        <div className="card stats-card">
          <div className="card-title">Appointments</div>
          <h2>{dashboardData.appointments}</h2>
          <p>+2.7%</p>
        </div>
        <div className="card stats-card">
          <div className="card-title">Reports</div>
          <h2>{dashboardData.reports}</h2>
          <p>+2.7%</p>
        </div>

        <div className="card appointments-card">
          <div className="card-title">Appointments</div>
          {/* This would be a list rendered from data */}
        </div>

        <div className="card activity-card">
          <div className="card-title">Recent Activity</div>
          {/* This would be a list rendered from data */}
        </div>
      </div>
    </div>
  );
};

const PublicDashboard = ({
  showSignupPopup,
}: {
  showSignupPopup: () => void;
}) => {
  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <div className="dashboard-title">
          <h1>Dashboard</h1>
          <p>Welcome to ArsMedicaTech - Your Healthcare Management Solution</p>
        </div>
        <div className="user-info">
          <span className="user-role">Guest</span>
          <button onClick={showSignupPopup} className="signup-button">
            Sign Up
          </button>
        </div>
      </div>
      <div className="dashboard-grid">
        <div className="card stats-card">
          <div className="card-title">Total Patients</div>
          <h2>{dashboardData.totalPatients}</h2>
          <p>+2.7%</p>
        </div>
        <div className="card stats-card">
          <div className="card-title">Total Income</div>
          <h2>${dashboardData.totalIncome}</h2>
          <p>+2.7%</p>
        </div>
        <div className="card stats-card">
          <div className="card-title">Appointments</div>
          <h2>{dashboardData.appointments}</h2>
          <p>+2.7%</p>
        </div>
        <div className="card stats-card">
          <div className="card-title">Reports</div>
          <h2>{dashboardData.reports}</h2>
          <p>+2.7%</p>
        </div>

        <div className="card appointments-card">
          <div className="card-title">Appointments</div>
          <div className="guest-notice">
            <p>Sign up to view and manage appointments</p>
            <button onClick={showSignupPopup} className="guest-action-button">
              Get Started
            </button>
          </div>
        </div>

        <div className="card activity-card">
          <div className="card-title">Recent Activity</div>
          <div className="guest-notice">
            <p>Sign up to view recent activity</p>
            <button onClick={showSignupPopup} className="guest-action-button">
              Get Started
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

interface UserData {
  id: number;
  username: string;
  first_name?: string;
  last_name?: string;
  email?: string;
  role: string;
}

const Dashboard = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState<UserData | null>(null);
  const [showLogin, setShowLogin] = useState(true);
  const [isLoading, setIsLoading] = useState(true);
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();
  const [usersExist, setUsersExist] = useState<boolean | null>(null);

  useEffect(() => {
    // Check if user is already authenticated
    const checkAuth = async () => {
      if (authService.isAuthenticated()) {
        const currentUser = await authService.getCurrentUser();
        if (currentUser) {
          setUser(currentUser);
          setIsAuthenticated(true);
        }
      }
      setIsLoading(false);
    };

    // Check if any users exist
    const checkUsersExist = async () => {
      try {
        const users = await apiService.getAllUsers();
        setUsersExist(Array.isArray(users.users) && users.users.length > 0);
      } catch (error) {
        // If error (e.g. 403), assume users exist to avoid exposing admin setup
        setUsersExist(true);
      }
    };

    checkAuth();
    checkUsersExist();
  }, []);

  const handleLogin = (userData: UserData): void => {
    setUser(userData);
    setIsAuthenticated(true);
  };

  const handleRegister = (userData: UserData): void => {
    setUser(userData);
    setIsAuthenticated(true);
  };

  const handleLogout = async () => {
    await authService.logout();
    setUser(null);
    setIsAuthenticated(false);
  };

  const handleSetupAdmin = async () => {
    const result = await authService.setupDefaultAdmin();
    if (result.success) {
      alert('Default admin user created! Username: admin, Password: Admin123!');
    } else {
      alert('Error creating admin user: ' + result.error);
    }
  };

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  if (isAuthenticated && user) {
    return (
      <>
        <AuthenticatedDashboard user={user} onLogout={handleLogout} />
        <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />
      </>
    );
  }

  return (
    <>
      <PublicDashboard showSignupPopup={showSignupPopup} />
      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />

      {/* Show auth forms when popup is triggered */}
      {isPopupOpen && (
        <div className="auth-overlay">
          <div className="auth-container">
            {showLogin ? (
              <LoginForm
                onLogin={handleLogin}
                onSwitchToRegister={() => setShowLogin(false)}
                onClose={hideSignupPopup}
              />
            ) : (
              <RegisterForm
                onRegister={handleRegister}
                onSwitchToLogin={() => setShowLogin(true)}
                onClose={hideSignupPopup}
              />
            )}

            {/* Admin setup button - only show if no users exist */}
            {usersExist === false && (
              <div className="admin-setup">
                <button
                  onClick={handleSetupAdmin}
                  className="setup-admin-button"
                >
                  Setup Default Admin
                </button>
                <p className="setup-note">
                  Use this to create the first admin user if no users exist in
                  the system.
                </p>
              </div>
            )}
          </div>
        </div>
      )}
    </>
  );
};

export default Dashboard;
