import { ChevronDownIcon } from '@heroicons/react/24/outline';

export const ProfilePanel = ({ user, onLogout }) => {
  return (
    <div className="profile-section">
      <div className="customize-profile">
        <span>Customize Profile</span>
        <ChevronDownIcon />
      </div>
      <div className="user-profile">
        <span>
          Hello
          <br />
          <b>Dr. Carvolth</b>
        </span>
        <div className="user-avatar"></div>
      </div>
    </div>
  );
};
