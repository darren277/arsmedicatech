import {
  BuildingOfficeIcon,
  EnvelopeIcon,
  MapPinIcon,
  PhoneIcon,
  UserIcon,
} from '@heroicons/react/24/outline';
import React from 'react';

interface UserProfile {
  id: string;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  role: string;
  specialty?: string;
  clinic_name?: string;
  clinic_address?: string;
  phone?: string;
  is_active: boolean;
  created_at: string;
}

interface ProfileProps {
  profile: UserProfile;
}

const Profile: React.FC<ProfileProps> = ({ profile }) => {
  const getRoleDisplayName = (role: string) => {
    switch (role) {
      case 'admin':
        return 'Administrator';
      case 'provider':
        return 'Healthcare Provider';
      case 'patient':
        return 'Patient';
      default:
        return role.charAt(0).toUpperCase() + role.slice(1);
    }
  };

  const getRoleBadgeColor = (role: string) => {
    switch (role) {
      case 'admin':
        return 'bg-red-100 text-red-800';
      case 'provider':
        return 'bg-blue-100 text-blue-800';
      case 'patient':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="profile-container">
      <div className="profile-header">
        <h1>Profile Information</h1>
        <p>Your account details and professional information</p>
      </div>

      <div className="profile-section">
        <h2>Personal Information</h2>
        <div className="profile-grid">
          <div className="profile-item">
            <div className="profile-label">
              <UserIcon className="w-4 h-4" />
              <span>Full Name</span>
            </div>
            <div className="profile-value">
              {profile.first_name && profile.last_name
                ? `${profile.first_name} ${profile.last_name}`
                : profile.first_name || profile.last_name || 'Not provided'}
            </div>
          </div>

          <div className="profile-item">
            <div className="profile-label">
              <span className="font-medium">Username</span>
            </div>
            <div className="profile-value">{profile.username}</div>
          </div>

          <div className="profile-item">
            <div className="profile-label">
              <EnvelopeIcon className="w-4 h-4" />
              <span>Email</span>
            </div>
            <div className="profile-value">{profile.email}</div>
          </div>

          <div className="profile-item">
            <div className="profile-label">
              <PhoneIcon className="w-4 h-4" />
              <span>Phone</span>
            </div>
            <div className="profile-value">
              {profile.phone || 'Not provided'}
            </div>
          </div>

          <div className="profile-item">
            <div className="profile-label">
              <span className="font-medium">Role</span>
            </div>
            <div className="profile-value">
              <span
                className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${getRoleBadgeColor(profile.role)}`}
              >
                {getRoleDisplayName(profile.role)}
              </span>
            </div>
          </div>

          <div className="profile-item">
            <div className="profile-label">
              <span className="font-medium">Account Status</span>
            </div>
            <div className="profile-value">
              <span
                className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                  profile.is_active
                    ? 'bg-green-100 text-green-800'
                    : 'bg-red-100 text-red-800'
                }`}
              >
                {profile.is_active ? 'Active' : 'Inactive'}
              </span>
            </div>
          </div>
        </div>
      </div>

      {(profile.role === 'provider' || profile.role === 'admin') && (
        <div className="profile-section">
          <h2>Professional Information</h2>
          <div className="profile-grid">
            {profile.specialty && (
              <div className="profile-item">
                <div className="profile-label">
                  <span className="font-medium">Specialty</span>
                </div>
                <div className="profile-value">{profile.specialty}</div>
              </div>
            )}

            {profile.clinic_name && (
              <div className="profile-item">
                <div className="profile-label">
                  <BuildingOfficeIcon className="w-4 h-4" />
                  <span>Clinic Name</span>
                </div>
                <div className="profile-value">{profile.clinic_name}</div>
              </div>
            )}

            {profile.clinic_address && (
              <div className="profile-item">
                <div className="profile-label">
                  <MapPinIcon className="w-4 h-4" />
                  <span>Clinic Address</span>
                </div>
                <div className="profile-value">{profile.clinic_address}</div>
              </div>
            )}
          </div>
        </div>
      )}

      <div className="profile-section">
        <h2>Account Information</h2>
        <div className="profile-grid">
          <div className="profile-item">
            <div className="profile-label">
              <span className="font-medium">Member Since</span>
            </div>
            <div className="profile-value">
              {new Date(profile.created_at).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}
            </div>
          </div>

          <div className="profile-item">
            <div className="profile-label">
              <span className="font-medium">User ID</span>
            </div>
            <div className="profile-value font-mono text-sm text-gray-600">
              {profile.id}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
