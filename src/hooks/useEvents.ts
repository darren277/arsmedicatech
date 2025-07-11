import { useCallback, useEffect, useRef } from 'react';
import API_URL from '../env_vars';

interface EventCallbacks {
  onNewMessage?: (data: any) => void;
  onAppointmentReminder?: (data: any) => void;
  onSystemNotification?: (data: any) => void;
}

const useEvents = (callbacks: EventCallbacks = {}) => {
  const eventSourceRef = useRef<EventSource | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const lastEventTimestampRef = useRef<string>('');

  const connect = useCallback(() => {
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
    }

    // Get user_id from localStorage or sessionStorage for testing
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    const user_id = user.id || 'test-user-id';

    const sseUrl = `${API_URL}/api/events/stream?since=${lastEventTimestampRef.current}&user_id=${user_id}`;
    console.log('Connecting to SSE URL:', sseUrl);
    console.log('API_URL:', API_URL);
    console.log('User ID for SSE:', user_id);

    // Create EventSource without credentials for SSE
    const eventSource = new EventSource(sseUrl);

    console.log('EventSource created:', eventSource);
    console.log('EventSource readyState:', eventSource.readyState);

    eventSource.onopen = () => {
      console.log('SSE connection opened successfully');
    };

    eventSource.onmessage = event => {
      console.log('SSE event received:', event);
      console.log('SSE event data:', event.data);

      try {
        const data = JSON.parse(event.data);
        console.log('Parsed SSE data:', data);
        lastEventTimestampRef.current = data.timestamp || '';

        switch (data.type) {
          case 'new_message':
            console.log('Processing new_message event:', data);
            if (callbacks.onNewMessage) {
              console.log('Calling onNewMessage callback');
              callbacks.onNewMessage(data);
            } else {
              console.log('No onNewMessage callback provided');
            }
            break;
          case 'appointment_reminder':
            console.log('Processing appointment_reminder event:', data);
            if (callbacks.onAppointmentReminder) {
              callbacks.onAppointmentReminder(data);
            }
            break;
          case 'system_notification':
            console.log('Processing system_notification event:', data);
            if (callbacks.onSystemNotification) {
              callbacks.onSystemNotification(data);
            }
            break;
          default:
            console.log('Unknown event type:', data.type, 'with data:', data);
        }
      } catch (error) {
        console.error('Error parsing SSE event:', error);
        console.error('Raw event data:', event.data);
      }
    };

    eventSource.onerror = err => {
      console.error('SSE connection error:', err);
      // Attempt to reconnect after 5 seconds
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }
      reconnectTimeoutRef.current = setTimeout(() => {
        console.log('Attempting to reconnect to SSE...');
        connect();
      }, 5000);
    };

    eventSourceRef.current = eventSource;
  }, [callbacks]);

  useEffect(() => {
    connect();

    return () => {
      if (eventSourceRef.current) {
        eventSourceRef.current.close();
      }
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }
    };
  }, [connect]);

  // Return a function to manually reconnect
  const reconnect = useCallback(() => {
    connect();
  }, [connect]);

  return { reconnect };
};

export default useEvents;
