import React, { useEffect, useState } from 'react';
import apiService from '../services/api';
import './Settings.css';
import { useUser } from './UserContext';

interface UserSettings {
  user_id: string;
  has_openai_api_key: boolean;
  created_at: string;
  updated_at: string;
}

interface UsageStats {
  requests_this_hour: number;
  max_requests_per_hour: number;
  window_start: number;
}

const Settings: React.FC = () => {
  const { user } = useUser();
  const [settings, setSettings] = useState<UserSettings | null>(null);
  const [usageStats, setUsageStats] = useState<UsageStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [openaiApiKey, setOpenaiApiKey] = useState('');
  const [showApiKey, setShowApiKey] = useState(false);
  const [message, setMessage] = useState<{
    type: 'success' | 'error';
    text: string;
  } | null>(null);

  useEffect(() => {
    loadSettings();
    loadUsageStats();
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

  const clearMessage = () => {
    setMessage(null);
  };

  if (loading) {
    return (
      <div className="settings-container">
        <div className="settings-loading">
          <div className="loading-spinner"></div>
          <p>Loading settings...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="settings-container">
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
    </div>
  );
};

export default Settings;
