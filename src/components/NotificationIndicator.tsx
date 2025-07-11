import React, { useEffect, useRef, useState } from 'react';
import { Notification } from '../hooks/useNotifications';
import './NotificationIndicator.css';

interface NotificationIndicatorProps {
  unreadCount: number;
  recentNotifications: Notification[];
  onMarkAsRead: (id: string) => void;
  onMarkAllAsRead: () => void;
  onClearNotification: (id: string) => void;
  onClearAll: () => void;
}

const NotificationIndicator: React.FC<NotificationIndicatorProps> = ({
  unreadCount,
  recentNotifications,
  onMarkAsRead,
  onMarkAllAsRead,
  onClearNotification,
  onClearAll,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const formatTime = (timestamp: string) => {
    const date = new Date(timestamp);
    const now = new Date();
    const diffInMinutes = Math.floor(
      (now.getTime() - date.getTime()) / (1000 * 60)
    );

    if (diffInMinutes < 1) return 'Just now';
    if (diffInMinutes < 60) return `${diffInMinutes}m ago`;
    if (diffInMinutes < 1440) return `${Math.floor(diffInMinutes / 60)}h ago`;
    return date.toLocaleDateString();
  };

  const getNotificationIcon = (type: Notification['type']) => {
    switch (type) {
      case 'new_message':
        return '💬';
      case 'appointment_reminder':
        return '📅';
      case 'system_notification':
        return '🔔';
      default:
        return '📢';
    }
  };

  const getNotificationTitle = (notification: Notification) => {
    switch (notification.type) {
      case 'new_message':
        return `New message from ${notification.data?.sender || 'Unknown'}`;
      case 'appointment_reminder':
        return 'Appointment Reminder';
      case 'system_notification':
        return 'System Notification';
      default:
        return notification.title;
    }
  };

  return (
    <div className="notification-indicator" ref={dropdownRef}>
      <button
        className="notification-button"
        onClick={() => setIsOpen(!isOpen)}
        title="Notifications"
      >
        <span className="notification-icon">🔔</span>
        {unreadCount > 0 && (
          <span className="notification-badge">
            {unreadCount > 99 ? '99+' : unreadCount}
          </span>
        )}
      </button>

      {isOpen && (
        <div className="notification-dropdown">
          <div className="notification-header">
            <h3>Notifications</h3>
            <div className="notification-actions">
              {unreadCount > 0 && (
                <button className="mark-all-read-btn" onClick={onMarkAllAsRead}>
                  Mark all read
                </button>
              )}
              {recentNotifications.length > 0 && (
                <button className="clear-all-btn" onClick={onClearAll}>
                  Clear all
                </button>
              )}
            </div>
          </div>

          <div className="notification-list">
            {recentNotifications.length === 0 ? (
              <div className="no-notifications">
                <p>No notifications</p>
              </div>
            ) : (
              recentNotifications.map(notification => (
                <div
                  key={notification.id}
                  className={`notification-item ${!notification.isRead ? 'unread' : ''}`}
                  onClick={() => onMarkAsRead(notification.id)}
                >
                  <div className="notification-content">
                    <div className="notification-icon-small">
                      {getNotificationIcon(notification.type)}
                    </div>
                    <div className="notification-text">
                      <div className="notification-title">
                        {getNotificationTitle(notification)}
                      </div>
                      <div className="notification-message">
                        {notification.message}
                      </div>
                      <div className="notification-time">
                        {formatTime(notification.timestamp)}
                      </div>
                    </div>
                  </div>
                  <button
                    className="clear-notification-btn"
                    onClick={e => {
                      e.stopPropagation();
                      onClearNotification(notification.id);
                    }}
                    title="Clear notification"
                  >
                    ×
                  </button>
                </div>
              ))
            )}
          </div>

          {recentNotifications.length > 0 && (
            <div className="notification-footer">
              <button
                className="view-all-btn"
                onClick={() => {
                  // TODO: Navigate to notifications page
                  setIsOpen(false);
                }}
              >
                View all notifications
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default NotificationIndicator;
