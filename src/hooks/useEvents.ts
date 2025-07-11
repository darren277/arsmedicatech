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

    // Try using fetch with streaming instead of EventSource
    fetch(sseUrl, {
      method: 'GET',
      headers: {
        Accept: 'text/event-stream',
        'Cache-Control': 'no-cache',
      },
    })
      .then(response => {
        console.log('Fetch response status:', response.status);
        console.log('Fetch response headers:', response.headers);

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const reader = response.body?.getReader();
        if (!reader) {
          throw new Error('No response body reader available');
        }

        console.log('SSE connection opened successfully via fetch');

        const processStream = () => {
          reader
            .read()
            .then(({ done, value }) => {
              if (done) {
                console.log('SSE stream ended');
                return;
              }

              const chunk = new TextDecoder().decode(value);
              console.log('SSE chunk received:', chunk);

              // Process the chunk for SSE events
              const lines = chunk.split('\n');
              for (const line of lines) {
                if (line.startsWith('data: ')) {
                  const data = line.slice(6);
                  try {
                    const eventData = JSON.parse(data);
                    console.log('SSE event received:', eventData);

                    switch (eventData.type) {
                      case 'new_message':
                        console.log('Processing new_message event:', eventData);
                        if (callbacks.onNewMessage) {
                          console.log('Calling onNewMessage callback');
                          callbacks.onNewMessage(eventData);
                        } else {
                          console.log('No onNewMessage callback provided');
                        }
                        break;
                      case 'appointment_reminder':
                        console.log(
                          'Processing appointment_reminder event:',
                          eventData
                        );
                        if (callbacks.onAppointmentReminder) {
                          callbacks.onAppointmentReminder(eventData);
                        }
                        break;
                      case 'system_notification':
                        console.log(
                          'Processing system_notification event:',
                          eventData
                        );
                        if (callbacks.onSystemNotification) {
                          callbacks.onSystemNotification(eventData);
                        }
                        break;
                      default:
                        console.log(
                          'Unknown event type:',
                          eventData.type,
                          'with data:',
                          eventData
                        );
                    }
                  } catch (error) {
                    console.error('Error parsing SSE event:', error);
                    console.error('Raw event data:', data);
                  }
                }
              }

              // Continue reading
              processStream();
            })
            .catch(error => {
              console.error('Error reading SSE stream:', error);
              // Attempt to reconnect after 5 seconds
              if (reconnectTimeoutRef.current) {
                clearTimeout(reconnectTimeoutRef.current);
              }
              reconnectTimeoutRef.current = setTimeout(() => {
                console.log('Attempting to reconnect to SSE...');
                connect();
              }, 5000);
            });
        };

        processStream();
      })
      .catch(error => {
        console.error('SSE connection error:', error);
        // Attempt to reconnect after 5 seconds
        if (reconnectTimeoutRef.current) {
          clearTimeout(reconnectTimeoutRef.current);
        }
        reconnectTimeoutRef.current = setTimeout(() => {
          console.log('Attempting to reconnect to SSE...');
          connect();
        }, 5000);
      });
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
