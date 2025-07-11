import { useCallback, useEffect, useRef } from 'react';

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

    const eventSource = new EventSource(
      `/api/events/stream?since=${lastEventTimestampRef.current}`
    );

    eventSource.onmessage = event => {
      try {
        const data = JSON.parse(event.data);
        lastEventTimestampRef.current = data.timestamp || '';

        switch (data.type) {
          case 'new_message':
            if (callbacks.onNewMessage) {
              callbacks.onNewMessage(data);
            }
            break;
          case 'appointment_reminder':
            if (callbacks.onAppointmentReminder) {
              callbacks.onAppointmentReminder(data);
            }
            break;
          case 'system_notification':
            if (callbacks.onSystemNotification) {
              callbacks.onSystemNotification(data);
            }
            break;
          default:
            console.log('Unknown event type:', data.type);
        }
      } catch (error) {
        console.error('Error parsing SSE event:', error);
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
