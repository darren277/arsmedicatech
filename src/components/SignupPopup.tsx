import { useNavigate } from 'react-router-dom';
import './SignupPopup.css';

const SignupPopup = ({ isOpen, onClose, onSwitchToLogin }) => {
  const navigate = useNavigate();

  if (!isOpen) return null;

  const handleSignupClick = () => {
    onClose();
    // Navigate to dashboard which will show the signup form
    navigate('/');
  };

  const handleLoginClick = () => {
    onClose();
    // Navigate to dashboard which will show the login form
    navigate('/');
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
