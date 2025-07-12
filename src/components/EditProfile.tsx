import {
  BuildingOfficeIcon,
  EnvelopeIcon,
  MapPinIcon,
  PhoneIcon,
  UserIcon,
} from '@heroicons/react/24/outline';
import React, { useState } from 'react';

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

interface EditProfileProps {
  profile: UserProfile;
  onSave: (updates: Partial<UserProfile>) => Promise<boolean>;
  onCancel: () => void;
}

const EditProfile: React.FC<EditProfileProps> = ({
  profile,
  onSave,
  onCancel,
}) => {
  const [formData, setFormData] = useState({
    first_name: profile.first_name || '',
    last_name: profile.last_name || '',
    phone: profile.phone || '',
    specialty: profile.specialty || '',
    clinic_name: profile.clinic_name || '',
    clinic_address: profile.clinic_address || '',
  });

  const [errors, setErrors] = useState<Record<string, string>>({});
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<{
    type: 'success' | 'error';
    text: string;
  } | null>(null);

  const isProvider = profile.role === 'provider' || profile.role === 'admin';

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    // Basic validations
    if (formData.first_name.trim().length > 50) {
      newErrors.first_name = 'First name must be less than 50 characters';
    }

    if (formData.last_name.trim().length > 50) {
      newErrors.last_name = 'Last name must be less than 50 characters';
    }

    // Phone validation
    if (formData.phone && formData.phone.trim()) {
      const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
      const cleanPhone = formData.phone.replace(/[\s\-\(\)]/g, '');
      if (!phoneRegex.test(cleanPhone)) {
        newErrors.phone = 'Please enter a valid phone number';
      }
    }

    // Provider-specific validations
    if (isProvider) {
      if (formData.specialty.trim().length > 100) {
        newErrors.specialty = 'Specialty must be less than 100 characters';
      }

      if (formData.clinic_name.trim().length > 200) {
        newErrors.clinic_name = 'Clinic name must be less than 200 characters';
      }

      if (formData.clinic_address.trim().length > 500) {
        newErrors.clinic_address =
          'Clinic address must be less than 500 characters';
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleInputChange = (field: string, value: string) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    // Clear error when user starts typing
    if (errors[field]) {
      setErrors(prev => ({ ...prev, [field]: '' }));
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setSaving(true);
    setMessage(null);

    try {
      // Prepare updates (only include changed fields)
      const updates: Partial<UserProfile> = {};

      if (formData.first_name !== profile.first_name) {
        updates.first_name = formData.first_name.trim();
      }
      if (formData.last_name !== profile.last_name) {
        updates.last_name = formData.last_name.trim();
      }
      if (formData.phone !== profile.phone) {
        updates.phone = formData.phone.trim();
      }
      if (isProvider) {
        if (formData.specialty !== profile.specialty) {
          updates.specialty = formData.specialty.trim();
        }
        if (formData.clinic_name !== profile.clinic_name) {
          updates.clinic_name = formData.clinic_name.trim();
        }
        if (formData.clinic_address !== profile.clinic_address) {
          updates.clinic_address = formData.clinic_address.trim();
        }
      }

      if (Object.keys(updates).length === 0) {
        setMessage({ type: 'error', text: 'No changes to save' });
        setSaving(false);
        return;
      }

      const success = await onSave(updates);

      if (success) {
        setMessage({ type: 'success', text: 'Profile updated successfully' });
        // Auto-hide success message after 3 seconds
        setTimeout(() => {
          setMessage(null);
        }, 3000);
      } else {
        setMessage({ type: 'error', text: 'Failed to update profile' });
      }
    } catch (error) {
      console.error('Error updating profile:', error);
      setMessage({
        type: 'error',
        text: 'An error occurred while updating profile',
      });
    } finally {
      setSaving(false);
    }
  };

  const clearMessage = () => {
    setMessage(null);
  };

  return (
    <div className="edit-profile-container">
      <div className="edit-profile-header">
        <h1>Edit Profile</h1>
        <p>Update your personal and professional information</p>
      </div>

      {message && (
        <div className={`message ${message.type}`}>
          <span>{message.text}</span>
          <button onClick={clearMessage} className="message-close">
            ×
          </button>
        </div>
      )}

      <form onSubmit={handleSubmit} className="edit-profile-form">
        <div className="form-section">
          <h2>Personal Information</h2>

          <div className="form-grid">
            <div className="form-group">
              <label htmlFor="first_name">
                <UserIcon className="w-4 h-4" />
                First Name
              </label>
              <input
                type="text"
                id="first_name"
                value={formData.first_name}
                onChange={e => handleInputChange('first_name', e.target.value)}
                className={`form-input ${errors.first_name ? 'error' : ''}`}
                placeholder="Enter your first name"
              />
              {errors.first_name && (
                <span className="error-message">{errors.first_name}</span>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="last_name">
                <UserIcon className="w-4 h-4" />
                Last Name
              </label>
              <input
                type="text"
                id="last_name"
                value={formData.last_name}
                onChange={e => handleInputChange('last_name', e.target.value)}
                className={`form-input ${errors.last_name ? 'error' : ''}`}
                placeholder="Enter your last name"
              />
              {errors.last_name && (
                <span className="error-message">{errors.last_name}</span>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="phone">
                <PhoneIcon className="w-4 h-4" />
                Phone Number
              </label>
              <input
                type="tel"
                id="phone"
                value={formData.phone}
                onChange={e => handleInputChange('phone', e.target.value)}
                className={`form-input ${errors.phone ? 'error' : ''}`}
                placeholder="Enter your phone number"
              />
              {errors.phone && (
                <span className="error-message">{errors.phone}</span>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="email">
                <EnvelopeIcon className="w-4 h-4" />
                Email Address
              </label>
              <input
                type="email"
                id="email"
                value={profile.email}
                className="form-input disabled"
                disabled
                title="Email cannot be changed"
              />
              <small className="form-help">
                Email address cannot be changed
              </small>
            </div>
          </div>
        </div>

        {isProvider && (
          <div className="form-section">
            <h2>Professional Information</h2>

            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="specialty">
                  <span className="font-medium">Medical Specialty</span>
                </label>
                <input
                  type="text"
                  id="specialty"
                  value={formData.specialty}
                  onChange={e => handleInputChange('specialty', e.target.value)}
                  className={`form-input ${errors.specialty ? 'error' : ''}`}
                  placeholder="e.g., Cardiology, Pediatrics, etc."
                />
                {errors.specialty && (
                  <span className="error-message">{errors.specialty}</span>
                )}
              </div>

              <div className="form-group">
                <label htmlFor="clinic_name">
                  <BuildingOfficeIcon className="w-4 h-4" />
                  Clinic Name
                </label>
                <input
                  type="text"
                  id="clinic_name"
                  value={formData.clinic_name}
                  onChange={e =>
                    handleInputChange('clinic_name', e.target.value)
                  }
                  className={`form-input ${errors.clinic_name ? 'error' : ''}`}
                  placeholder="Enter clinic or practice name"
                />
                {errors.clinic_name && (
                  <span className="error-message">{errors.clinic_name}</span>
                )}
              </div>

              <div className="form-group full-width">
                <label htmlFor="clinic_address">
                  <MapPinIcon className="w-4 h-4" />
                  Clinic Address
                </label>
                <textarea
                  id="clinic_address"
                  value={formData.clinic_address}
                  onChange={e =>
                    handleInputChange('clinic_address', e.target.value)
                  }
                  className={`form-textarea ${errors.clinic_address ? 'error' : ''}`}
                  placeholder="Enter full clinic address"
                  rows={3}
                />
                {errors.clinic_address && (
                  <span className="error-message">{errors.clinic_address}</span>
                )}
              </div>
            </div>
          </div>
        )}

        <div className="form-actions">
          <button
            type="button"
            onClick={onCancel}
            className="btn btn-secondary"
            disabled={saving}
          >
            Cancel
          </button>
          <button type="submit" className="btn btn-primary" disabled={saving}>
            {saving ? 'Saving...' : 'Save Changes'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditProfile;
