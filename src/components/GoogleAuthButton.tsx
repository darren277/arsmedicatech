import React from 'react';
import { GOOGLE_LOGO } from '../env_vars';

interface GoogleAuthButtonProps {
  onClick: () => void;
  children: React.ReactNode;
  style?: React.CSSProperties;
  className?: string;
}

const GoogleAuthButton: React.FC<GoogleAuthButtonProps> = ({
  onClick,
  children,
  style,
  className,
}) => (
  <button
    type="button"
    onClick={onClick}
    className={className || 'popup-google-button'}
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
      ...style,
    }}
  >
    <img
      src={GOOGLE_LOGO}
      alt="Google"
      style={{ width: 22, height: 22, marginRight: 8 }}
    />
    {children}
  </button>
);

export default GoogleAuthButton;
