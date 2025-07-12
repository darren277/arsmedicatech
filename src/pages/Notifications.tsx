import React, { useMemo, useState } from 'react';
import { Notification } from '../hooks/useNotifications';
import './Notifications.css';

interface NotificationsPageProps {
  notifications: Notification[];
  onMarkAsRead: (id: string) => void;
  onMarkAllAsRead: () => void;
  onClearNotification: (id: string) => void;
  onClearAll: () => void;
}

const NotificationsPage: React.FC<NotificationsPageProps> = ({
  notifications,
  onMarkAsRead,
  onMarkAllAsRead,
  onClearNotification,
  onClearAll,
}) => {
  const [filter, setFilter] = useState<
    | 'all'
    | 'unread'
    | 'new_message'
    | 'appointment_reminder'
    | 'system_notification'
  >('all');

  const filteredNotifications = useMemo(() => {
    switch (filter) {
      case 'unread':
        return notifications.filter(n => !n.isRead);
      case 'new_message':
      case 'appointment_reminder':
      case 'system_notification':
        return notifications.filter(n => n.type === filter);
      default:
        return notifications;
    }
  }, [notifications, filter]);

  const unreadCount = notifications.filter(n => !n.isRead).length;

  const formatTime = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString();
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

  const getFilterCount = (filterType: typeof filter) => {
    switch (filterType) {
      case 'unread':
        return unreadCount;
      case 'new_message':
      case 'appointment_reminder':
      case 'system_notification':
        return notifications.filter(n => n.type === filterType).length;
      default:
        return notifications.length;
    }
  };

  return (
    <div className="notifications-page">
      <div className="notifications-header">
        <h1>Notifications</h1>
        <div className="notifications-actions">
          {unreadCount > 0 && (
            <button className="mark-all-read-btn" onClick={onMarkAllAsRead}>
              Mark all as read
            </button>
          )}
          {notifications.length > 0 && (
            <button className="clear-all-btn" onClick={onClearAll}>
              Clear all
            </button>
          )}
        </div>
      </div>

      <div className="notifications-filters">
        <button
          className={`filter-btn ${filter === 'all' ? 'active' : ''}`}
          onClick={() => setFilter('all')}
        >
          All ({getFilterCount('all')})
        </button>
        <button
          className={`filter-btn ${filter === 'unread' ? 'active' : ''}`}
          onClick={() => setFilter('unread')}
        >
          Unread ({getFilterCount('unread')})
        </button>
        <button
          className={`filter-btn ${filter === 'new_message' ? 'active' : ''}`}
          onClick={() => setFilter('new_message')}
        >
          Messages ({getFilterCount('new_message')})
        </button>
        <button
          className={`filter-btn ${filter === 'appointment_reminder' ? 'active' : ''}`}
          onClick={() => setFilter('appointment_reminder')}
        >
          Appointments ({getFilterCount('appointment_reminder')})
        </button>
        <button
          className={`filter-btn ${filter === 'system_notification' ? 'active' : ''}`}
          onClick={() => setFilter('system_notification')}
        >
          System ({getFilterCount('system_notification')})
        </button>
      </div>

      <div className="notifications-list">
        {filteredNotifications.length === 0 ? (
          <div className="no-notifications">
            <div className="no-notifications-icon">🔔</div>
            <h3>No notifications</h3>
            <p>
              {filter === 'all'
                ? "You're all caught up! No notifications to show."
                : `No ${filter} notifications to show.`}
            </p>
          </div>
        ) : (
          filteredNotifications.map(notification => (
            <div
              key={notification.id}
              className={`notification-card ${!notification.isRead ? 'unread' : ''}`}
            >
              <div className="notification-card-content">
                <div className="notification-icon-large">
                  {getNotificationIcon(notification.type)}
                </div>
                <div className="notification-details">
                  <div className="notification-header-row">
                    <h3 className="notification-title">
                      {getNotificationTitle(notification)}
                    </h3>
                    <div className="notification-actions">
                      {!notification.isRead && (
                        <button
                          className="mark-read-btn"
                          onClick={() => onMarkAsRead(notification.id)}
                          title="Mark as read"
                        >
                          ✓
                        </button>
                      )}
                      <button
                        className="clear-notification-btn"
                        onClick={() => onClearNotification(notification.id)}
                        title="Clear notification"
                      >
                        ×
                      </button>
                    </div>
                  </div>
                  <p className="notification-message">{notification.message}</p>
                  <div className="notification-meta">
                    <span className="notification-time">
                      {formatTime(notification.timestamp)}
                    </span>
                    <span className="notification-type">
                      {notification.type.replace('_', ' ')}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default NotificationsPage;
