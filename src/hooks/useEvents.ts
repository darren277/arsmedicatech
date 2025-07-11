import { useEffect } from 'react';

const useEvents = () => {
  useEffect(() => {
    let lastEventTimestamp = '';

    const eventSource = new EventSource(
      `/api/events/stream?since=${lastEventTimestamp}`
    );

    eventSource.onmessage = event => {
      const data = JSON.parse(event.data);

      lastEventTimestamp = data.timestamp;

      switch (data.type) {
        case 'new_message':
          // Show red dot on conversations
          // Optionally update message preview in sidebar
          break;
        case 'appointment_reminder':
          // Show toast or alert badge
          break;
        case 'system_notification':
          // Add to notifications panel or display inline
          break;
      }
    };

    eventSource.onerror = err => {
      console.error('SSE connection error:', err);
    };

    return () => eventSource.close();
  }, []);
};

export default useEvents;
