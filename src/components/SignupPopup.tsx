import { useNavigate } from 'react-router-dom';
import { GOOGLE_LOGO } from '../env_vars';
import './SignupPopup.css';

const GOOGLE_AUTH_URL = '/auth/cognito'; // Adjust this to your backend's federated login endpoint

const SignupPopup = ({
  isOpen,
  onClose,
  onSwitchToLogin,
}: {
  isOpen: boolean;
  onClose: () => void;
  onSwitchToLogin?: () => void;
}): JSX.Element | null => {
  const navigate = useNavigate();

  if (!isOpen) return null;

  const handleSignupClick = () => {
    onClose();
    // Navigate to dashboard with register parameter to show the signup form
    navigate('/?auth=register');
  };

  const handleLoginClick = () => {
    onClose();
    // Navigate to dashboard with login parameter to show the login form
    navigate('/?auth=login');
  };

  return (
    <div className="signup-popup-overlay" onClick={onClose}>
      <div className="signup-popup" onClick={e => e.stopPropagation()}>
        <button className="popup-close-button" onClick={onClose}>
          ×
        </button>

        <div className="popup-content">
          <div className="popup-icon">🔒</div>

          <h2>Sign Up to Continue</h2>

          <p className="popup-description">
            You need to create an account to perform this action. Sign up now to
            unlock all features and start managing your patients.
          </p>

          <div className="popup-benefits">
            <div className="benefit-item">
              <span className="benefit-icon">✓</span>
              <span>Create and manage patient records</span>
            </div>
            <div className="benefit-item">
              <span className="benefit-icon">✓</span>
              <span>Send and receive messages</span>
            </div>
            <div className="benefit-item">
              <span className="benefit-icon">✓</span>
              <span>Schedule appointments</span>
            </div>
            <div className="benefit-item">
              <span className="benefit-icon">✓</span>
              <span>Access advanced features</span>
            </div>
          </div>

          <div className="popup-actions">
            <a
              href={GOOGLE_AUTH_URL}
              className="popup-google-button"
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                background: '#fff',
                border: '1px solid #ccc',
                borderRadius: 4,
                padding: '8px 16px',
                marginBottom: 12,
                textDecoration: 'none',
                color: '#444',
                fontWeight: 500,
                fontSize: 16,
                cursor: 'pointer',
                gap: 10,
              }}
            >
              <img
                src={GOOGLE_LOGO}
                alt="Google"
                style={{ width: 22, height: 22, marginRight: 8 }}
              />
              Sign up with Google
            </a>
            <button className="popup-signup-button" onClick={handleSignupClick}>
              Sign Up Now
            </button>

            <div className="popup-login-link">
              Already have an account?{' '}
              <button className="popup-login-button" onClick={handleLoginClick}>
                Sign In
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignupPopup;
