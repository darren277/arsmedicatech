import { Notification } from '../hooks/useNotifications';
import { useSignupPopup } from '../hooks/useSignupPopup';
import authService from '../services/auth';
import NotificationIndicator from './NotificationIndicator';
import { ProfilePanel } from './ProfilePanel';
import SearchBox from './SearchBox';
import SignupPopup from './SignupPopup';
import { useUser } from './UserContext';

interface Props {
  query: string;
  onQueryChange(q: string): void;
  results: any[];
  loading: boolean;
  // Notification props
  unreadCount: number;
  recentNotifications: Notification[];
  onMarkAsRead: (id: string) => void;
  onMarkAllAsRead: () => void;
  onClearNotification: (id: string) => void;
  onClearAll: () => void;
}

export default function Topbar(props: Props) {
  const { user, isAuthenticated, setUser } = useUser();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

  const handleLogout = async () => {
    try {
      await authService.logout();
      setUser(null);
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <>
      <header className="topbar">
        <div className="search-container">
          <SearchBox
            value={props.query}
            onChange={props.onQueryChange}
            loading={props.loading}
          />
        </div>

        <div className="topbar-actions">
          {/* Notification Indicator */}
          {isAuthenticated && (
            <NotificationIndicator
              unreadCount={props.unreadCount}
              recentNotifications={props.recentNotifications}
              onMarkAsRead={props.onMarkAsRead}
              onMarkAllAsRead={props.onMarkAllAsRead}
              onClearNotification={props.onClearNotification}
              onClearAll={props.onClearAll}
            />
          )}

          <div className="auth-status">
            {isAuthenticated && user ? (
              <ProfilePanel
                user={{
                  name:
                    `${user.first_name || ''} ${user.last_name || ''}`.trim() ||
                    user.username,
                  role: user.role,
                }}
                onLogout={handleLogout}
              />
            ) : (
              <div className="guest-auth">
                <span className="guest-label">Guest User</span>
                <button onClick={showSignupPopup} className="auth-button">
                  Sign Up / Login
                </button>
              </div>
            )}
          </div>
        </div>
      </header>
      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />
    </>
  );
}
