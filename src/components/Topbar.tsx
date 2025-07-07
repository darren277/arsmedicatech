import { useSignupPopup } from '../hooks/useSignupPopup';
import authService from '../services/auth';
import { ProfilePanel } from './ProfilePanel';
import SearchBox from './SearchBox';
import SignupPopup from './SignupPopup';

interface Props {
  query: string;
  onQueryChange(q: string): void;
  results: any[];
  loading: boolean;
}

export default function Topbar(props: Props) {
  const isAuthenticated = authService.isAuthenticated();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

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

        <div className="auth-status">
          {isAuthenticated ? (
            <ProfilePanel
              user={{
                name: '',
                role: '',
              }}
              onLogout={function (): void {
                throw new Error('Function not implemented.');
              }}
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
      </header>
      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />
    </>
  );
}
