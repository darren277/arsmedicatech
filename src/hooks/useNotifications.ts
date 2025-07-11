import { useCallback, useEffect, useState } from 'react';

export interface Notification {
  id: string;
  type: 'new_message' | 'appointment_reminder' | 'system_notification';
  title: string;
  message: string;
  timestamp: string;
  isRead: boolean;
  data?: any; // Additional data like conversation_id, appointmentId, etc.
}

const useNotifications = () => {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [unreadCount, setUnreadCount] = useState(0);

  // Calculate unread count whenever notifications change
  useEffect(() => {
    const unread = notifications.filter(n => !n.isRead).length;
    setUnreadCount(unread);
  }, [notifications]);

  // Add a new notification
  const addNotification = useCallback(
    (notification: Omit<Notification, 'id' | 'isRead'>) => {
      const newNotification: Notification = {
        ...notification,
        id: Date.now().toString(),
        isRead: false,
      };

      setNotifications(prev => [newNotification, ...prev]);
    },
    []
  );

  // Mark a notification as read
  const markAsRead = useCallback((notificationId: string) => {
    setNotifications(prev =>
      prev.map(n => (n.id === notificationId ? { ...n, isRead: true } : n))
    );
  }, []);

  // Mark all notifications as read
  const markAllAsRead = useCallback(() => {
    setNotifications(prev => prev.map(n => ({ ...n, isRead: true })));
  }, []);

  // Clear a notification
  const clearNotification = useCallback((notificationId: string) => {
    setNotifications(prev => prev.filter(n => n.id !== notificationId));
  }, []);

  // Clear all notifications
  const clearAllNotifications = useCallback(() => {
    setNotifications([]);
  }, []);

  // Get notifications by type
  const getNotificationsByType = useCallback(
    (type: Notification['type']) => {
      return notifications.filter(n => n.type === type);
    },
    [notifications]
  );

  // Get recent notifications (last 10)
  const getRecentNotifications = useCallback(
    (limit: number = 10) => {
      return notifications.slice(0, limit);
    },
    [notifications]
  );

  return {
    notifications,
    unreadCount,
    addNotification,
    markAsRead,
    markAllAsRead,
    clearNotification,
    clearAllNotifications,
    getNotificationsByType,
    getRecentNotifications,
  };
};

export default useNotifications;
