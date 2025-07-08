import {
  ArrowRightOnRectangleIcon,
  ChevronDownIcon,
} from '@heroicons/react/24/outline';
import { useState } from 'react';

export const ProfilePanel = ({
  user,
  onLogout,
}: {
  user: { name: string; role: string };
  onLogout: () => void;
}): JSX.Element => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  const handleLogout = () => {
    onLogout();
    setIsDropdownOpen(false);
  };

  return (
    <div className="profile-section relative">
      <div
        className="customize-profile cursor-pointer flex items-center gap-2"
        onClick={toggleDropdown}
      >
        <span>Customize Profile</span>
        <ChevronDownIcon
          className={`w-4 h-4 transition-transform ${isDropdownOpen ? 'rotate-180' : ''}`}
        />
      </div>

      <div className="user-profile">
        <span>
          Hello
          <br />
          <b>{user.name || 'User'}</b>
          <br />
          <small className="text-gray-600">{user.role}</small>
        </span>
        <div className="user-avatar"></div>
      </div>

      {/* Dropdown Menu */}
      {isDropdownOpen && (
        <div className="absolute right-0 top-full mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50 border border-gray-200">
          <button
            onClick={handleLogout}
            className="flex items-center gap-2 w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 transition-colors"
          >
            <ArrowRightOnRectangleIcon className="w-4 h-4" />
            Logout
          </button>
        </div>
      )}
    </div>
  );
};
