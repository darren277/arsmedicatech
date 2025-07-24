import React, { useEffect, useState } from 'react';
import apiService from '../services/api';
import logger from '../services/logging';
import EditProfile from './EditProfile';
import Profile from './Profile';
import './Settings.css';
import { useUser } from './UserContext';

interface UserSettings {
  user_id: string;
  has_openai_api_key: boolean;
  has_optimal_api_key: boolean;
  created_at: string;
  updated_at: string;
}

interface UsageStats {
  requests_this_hour: number;
  max_requests_per_hour: number;
  window_start: number;
}

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

type TabType = 'settings' | 'profile' | 'edit-profile';

const Settings: React.FC = () => {
  const { user } = useUser();
  const [activeTab, setActiveTab] = useState<TabType>('settings');
  const [settings, setSettings] = useState<UserSettings | null>(null);
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [usageStats, setUsageStats] = useState<UsageStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [profileLoading, setProfileLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [openaiApiKey, setOpenaiApiKey] = useState('');
  const [showApiKey, setShowApiKey] = useState(false);
  const [optimalApiKey, setOptimalApiKey] = useState('');
  const [showOptimalApiKey, setShowOptimalApiKey] = useState(false);
  const [message, setMessage] = useState<{
    type: 'success' | 'error';
    text: string;
  } | null>(null);

  useEffect(() => {
    loadSettings();
    loadUsageStats();
    loadProfile();
  }, []);

  const loadSettings = async () => {
    try {
      setLoading(true);
      const response = await apiService.getAPI('/settings');
      if (response.success) {
        setSettings(response.settings);
      } else {
        setMessage({ type: 'error', text: 'Failed to load settings' });
      }
    } catch (error) {
      console.error('Error loading settings:', error);
      setMessage({ type: 'error', text: 'Failed to load settings' });
    } finally {
      setLoading(false);
    }
  };

  const loadProfile = async () => {
    try {
      logger.debug('loadProfile - Starting profile load');
      setProfileLoading(true);

      logger.debug('loadProfile - Making API request to /profile');
      const response = await apiService.getAPI('/profile');
      logger.debug('loadProfile - API response:', response);

      if (response.success) {
        console.log(
          '[DEBUG] loadProfile - Setting profile data:',
          response.profile
        );
        setProfile(response.profile);
      } else {
        console.error('Failed to load profile:', response.error);
        setMessage({ type: 'error', text: 'Failed to load profile' });
      }
    } catch (error) {
      console.error('Error loading profile:', error);
      setMessage({ type: 'error', text: 'Failed to load profile' });
    } finally {
      logger.debug('loadProfile - Setting profileLoading to false');
      setProfileLoading(false);
    }
  };

  const loadUsageStats = async () => {
    try {
      const response = await apiService.getAPI('/usage');
      if (response.success) {
        setUsageStats(response.usage);
      }
    } catch (error) {
      console.error('Error loading usage stats:', error);
      // Don't show error for usage stats as it's not critical
    }
  };

  const handleSaveApiKey = async () => {
    if (!openaiApiKey.trim()) {
      setMessage({ type: 'error', text: 'Please enter an API key' });
      return;
    }

    try {
      setSaving(true);
      const response = await apiService.postAPI('/settings', {
        openai_api_key: openaiApiKey.trim(),
      });

      if (response.success) {
        setMessage({ type: 'success', text: 'API key saved successfully' });
        setOpenaiApiKey('');
        setShowApiKey(false);
        // Reload settings to update the has_openai_api_key status
        await loadSettings();
      } else {
        setMessage({
          type: 'error',
          text: response.data.error || 'Failed to save API key',
        });
      }
    } catch (error: any) {
      console.error('Error saving API key:', error);
      const errorMessage =
        error.response?.data?.error || 'Failed to save API key';
      setMessage({ type: 'error', text: errorMessage });
    } finally {
      setSaving(false);
    }
  };

  const handleRemoveApiKey = async () => {
    if (
      !confirm(
        'Are you sure you want to remove your OpenAI API key? This action cannot be undone.'
      )
    ) {
      return;
    }

    try {
      setSaving(true);
      const response = await apiService.postAPI('/settings', {
        openai_api_key: '', // Empty string to remove the key
      });

      if (response.success) {
        setMessage({ type: 'success', text: 'API key removed successfully' });
        await loadSettings();
      } else {
        setMessage({
          type: 'error',
          text: response.data.error || 'Failed to remove API key',
        });
      }
    } catch (error: any) {
      console.error('Error removing API key:', error);
      const errorMessage =
        error.response?.data?.error || 'Failed to remove API key';
      setMessage({ type: 'error', text: errorMessage });
    } finally {
      setSaving(false);
    }
  };

  const handleSaveOptimalApiKey = async () => {
    if (!optimalApiKey.trim()) {
      setMessage({ type: 'error', text: 'Please enter an Optimal API key' });
      return;
    }

    try {
      setSaving(true);
      const response = await apiService.postAPI('/settings', {
        optimal_api_key: optimalApiKey.trim(),
      });

      if (response.success) {
        setMessage({
          type: 'success',
          text: 'Optimal API key saved successfully',
        });
        setOptimalApiKey('');
        setShowOptimalApiKey(false);
        // Reload settings to update the has_optimal_api_key status
        await loadSettings();
      } else {
        setMessage({
          type: 'error',
          text: response.data.error || 'Failed to save Optimal API key',
        });
      }
    } catch (error: any) {
      console.error('Error saving Optimal API key:', error);
      const errorMessage =
        error.response?.data?.error || 'Failed to save Optimal API key';
      setMessage({ type: 'error', text: errorMessage });
    } finally {
      setSaving(false);
    }
  };

  const handleRemoveOptimalApiKey = async () => {
    if (
      !confirm(
        'Are you sure you want to remove your Optimal API key? This action cannot be undone.'
      )
    ) {
      return;
    }

    try {
      setSaving(true);
      const response = await apiService.postAPI('/settings', {
        optimal_api_key: '', // Empty string to remove the key
      });

      if (response.success) {
        setMessage({
          type: 'success',
          text: 'Optimal API key removed successfully',
        });
        await loadSettings();
      } else {
        setMessage({
          type: 'error',
          text: response.data.error || 'Failed to remove Optimal API key',
        });
      }
    } catch (error: any) {
      console.error('Error removing Optimal API key:', error);
      const errorMessage =
        error.response?.data?.error || 'Failed to remove Optimal API key';
      setMessage({ type: 'error', text: errorMessage });
    } finally {
      setSaving(false);
    }
  };

  const handleSaveProfile = async (
    updates: Partial<UserProfile>
  ): Promise<boolean> => {
    try {
      setSaving(true);
      const response = await apiService.postAPI('/profile', updates);

      if (response.success) {
        setMessage({ type: 'success', text: 'Profile updated successfully' });
        await loadProfile(); // Reload profile data
        setActiveTab('profile'); // Switch back to profile view
        return true;
      } else {
        setMessage({
          type: 'error',
          text: response.error || 'Failed to update profile',
        });
        return false;
      }
    } catch (error: any) {
      console.error('Error updating profile:', error);
      const errorMessage =
        error.response?.data?.error || 'Failed to update profile';
      setMessage({ type: 'error', text: errorMessage });
      return false;
    } finally {
      setSaving(false);
    }
  };

  const clearMessage = () => {
    setMessage(null);
  };

  const renderTabContent = () => {
    switch (activeTab) {
      case 'profile':
        if (profileLoading) {
          return (
            <div className="settings-loading">
              <div className="loading-spinner"></div>
              <p>Loading profile...</p>
            </div>
          );
        }
        return profile ? (
          <Profile profile={profile} />
        ) : (
          <div className="settings-loading">
            <p>No profile data available</p>
          </div>
        );

      case 'edit-profile':
        if (profileLoading) {
          return (
            <div className="settings-loading">
              <div className="loading-spinner"></div>
              <p>Loading profile...</p>
            </div>
          );
        }
        return profile ? (
          <EditProfile
            profile={profile}
            onSave={handleSaveProfile}
            onCancel={() => setActiveTab('profile')}
          />
        ) : (
          <div className="settings-loading">
            <p>No profile data available</p>
          </div>
        );

      case 'settings':
      default:
        return renderSettingsContent();
    }
  };

  const renderSettingsContent = () => {
    if (loading) {
      return (
        <div className="settings-loading">
          <div className="loading-spinner"></div>
          <p>Loading settings...</p>
        </div>
      );
    }

    return (
      <>
        <div className="settings-header">
          <h1>Account Settings</h1>
          <p>Manage your account preferences and API keys</p>
        </div>

        {message && (
          <div className={`message ${message.type}`}>
            <span>{message.text}</span>
            <button onClick={clearMessage} className="message-close">
              ×
            </button>
          </div>
        )}

        <div className="settings-section">
          <h2>User Information</h2>
          <div className="user-info">
            <div className="info-row">
              <label>Username:</label>
              <span>{user?.username}</span>
            </div>
            <div className="info-row">
              <label>Email:</label>
              <span>{user?.email}</span>
            </div>
            <div className="info-row">
              <label>Role:</label>
              <span className="role-badge">{user?.role}</span>
            </div>
          </div>
        </div>

        {user?.role === 'admin' && (
          <button
            onClick={() => {
              throw new Error('Test error for Sentry logging'); // This will trigger an error to test Sentry logging
            }}
          >
            Test Sentry Error
          </button>
        )}

        <div className="settings-section">
          <h2>OpenAI API Key</h2>
          <p className="section-description">
            Your OpenAI API key is used to enable AI-powered features. It is
            encrypted and stored securely.
          </p>

          {settings?.has_openai_api_key ? (
            <div className="api-key-status">
              <div className="status-indicator success">
                <span className="status-dot"></span>
                API key is configured
              </div>
              <div className="api-key-actions">
                <button
                  onClick={() => setShowApiKey(!showApiKey)}
                  className="btn btn-secondary"
                >
                  {showApiKey ? 'Hide' : 'Show'} API Key
                </button>
                <button
                  onClick={handleRemoveApiKey}
                  className="btn btn-danger"
                  disabled={saving}
                >
                  {saving ? 'Removing...' : 'Remove API Key'}
                </button>
              </div>
            </div>
          ) : (
            <div className="api-key-form">
              <div className="form-group">
                <label htmlFor="openai-api-key">OpenAI API Key</label>
                <div className="input-group">
                  <input
                    type={showApiKey ? 'text' : 'password'}
                    id="openai-api-key"
                    value={openaiApiKey}
                    onChange={e => setOpenaiApiKey(e.target.value)}
                    placeholder="sk-..."
                    className="form-input"
                  />
                  <button
                    type="button"
                    onClick={() => setShowApiKey(!showApiKey)}
                    className="input-toggle"
                  >
                    {showApiKey ? '👁️' : '👁️‍🗨️'}
                  </button>
                </div>
                <small className="form-help">
                  Your API key should start with "sk-" and be 51 characters long
                </small>
              </div>
              <button
                onClick={handleSaveApiKey}
                disabled={saving || !openaiApiKey.trim()}
                className="btn btn-primary"
              >
                {saving ? 'Saving...' : 'Save API Key'}
              </button>
            </div>
          )}
        </div>

        <div className="settings-section">
          <h2>Optimal API Key</h2>
          <p className="section-description">
            Your Optimal API key is used to enable mathematical optimization
            features. It is encrypted and stored securely.
          </p>

          {settings?.has_optimal_api_key ? (
            <div className="api-key-status">
              <div className="status-indicator success">
                <span className="status-dot"></span>
                Optimal API key is configured
              </div>
              <div className="api-key-actions">
                <button
                  onClick={() => setShowOptimalApiKey(!showOptimalApiKey)}
                  className="btn btn-secondary"
                >
                  {showOptimalApiKey ? 'Hide' : 'Show'} API Key
                </button>
                <button
                  onClick={handleRemoveOptimalApiKey}
                  className="btn btn-danger"
                  disabled={saving}
                >
                  {saving ? 'Removing...' : 'Remove API Key'}
                </button>
              </div>
            </div>
          ) : (
            <div className="api-key-form">
              <div className="form-group">
                <label htmlFor="optimal-api-key">Optimal API Key</label>
                <div className="input-group">
                  <input
                    type={showOptimalApiKey ? 'text' : 'password'}
                    id="optimal-api-key"
                    value={optimalApiKey}
                    onChange={e => setOptimalApiKey(e.target.value)}
                    placeholder="Enter your Optimal API key..."
                    className="form-input"
                  />
                  <button
                    type="button"
                    onClick={() => setShowOptimalApiKey(!showOptimalApiKey)}
                    className="input-toggle"
                  >
                    {showOptimalApiKey ? '👁️' : '👁️‍🗨️'}
                  </button>
                </div>
                <small className="form-help">
                  Your Optimal API key for mathematical optimization services
                </small>
              </div>
              <button
                onClick={handleSaveOptimalApiKey}
                disabled={saving || !optimalApiKey.trim()}
                className="btn btn-primary"
              >
                {saving ? 'Saving...' : 'Save API Key'}
              </button>
            </div>
          )}
        </div>

        <div className="settings-section">
          <h2>API Usage</h2>
          <p className="section-description">
            Monitor your OpenAI API usage and rate limits.
          </p>
          {usageStats && (
            <div className="usage-info">
              <div className="info-row">
                <label>Requests This Hour:</label>
                <span className="usage-counter">
                  {usageStats.requests_this_hour} /{' '}
                  {usageStats.max_requests_per_hour}
                </span>
              </div>
              <div className="info-row">
                <label>Usage Progress:</label>
                <div className="usage-progress">
                  <div
                    className="usage-bar"
                    style={{
                      width: `${(usageStats.requests_this_hour / usageStats.max_requests_per_hour) * 100}%`,
                    }}
                  ></div>
                </div>
              </div>
              <div className="info-row">
                <label>Window Resets:</label>
                <span>
                  {new Date(
                    usageStats.window_start * 1000 + 3600000
                  ).toLocaleTimeString()}
                </span>
              </div>
            </div>
          )}
        </div>

        <div className="settings-section">
          <h2>Account Security</h2>
          <p className="section-description">
            Your account security information and settings.
          </p>
          <div className="security-info">
            <div className="info-row">
              <label>Account Created:</label>
              <span>
                {settings?.created_at
                  ? new Date(settings.created_at).toLocaleDateString()
                  : 'N/A'}
              </span>
            </div>
            <div className="info-row">
              <label>Last Updated:</label>
              <span>
                {settings?.updated_at
                  ? new Date(settings.updated_at).toLocaleDateString()
                  : 'N/A'}
              </span>
            </div>
          </div>
        </div>
      </>
    );
  };

  return (
    <div className="settings-container">
      <div className="settings-tabs">
        <button
          className={`tab-button ${activeTab === 'settings' ? 'active' : ''}`}
          onClick={() => setActiveTab('settings')}
        >
          Settings
        </button>
        <button
          className={`tab-button ${activeTab === 'profile' ? 'active' : ''}`}
          onClick={() => setActiveTab('profile')}
        >
          Profile
        </button>
        {activeTab === 'edit-profile' && (
          <button
            className={`tab-button ${activeTab === 'edit-profile' ? 'active' : ''}`}
            onClick={() => setActiveTab('edit-profile')}
          >
            Edit Profile
          </button>
        )}
      </div>

      <div className="settings-content">{renderTabContent()}</div>

      {/* Profile action buttons */}
      {activeTab === 'profile' && profile && (
        <div className="profile-actions">
          <button
            onClick={() => setActiveTab('edit-profile')}
            className="btn btn-primary"
          >
            Edit Profile
          </button>
        </div>
      )}
    </div>
  );
};

export default Settings;
