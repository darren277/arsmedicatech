# Redis/SSE Notifications System

This document explains how the Redis/SSE (Server-Sent Events) notifications system works in the ArsMedicaTech application.

## Overview

The notifications system provides real-time updates to users through:
- **Redis PubSub**: For immediate message delivery
- **Redis Lists**: For message buffering and replay
- **Server-Sent Events (SSE)**: For browser-based real-time updates

## Architecture

```
Frontend (React) ←→ SSE Stream ←→ Flask Backend ←→ Redis PubSub
                                    ↓
                              Redis Lists (Buffer)
```

## Components

### Backend Components

1. **`lib/services/redis_client.py`**: Redis connection management
2. **`lib/services/notifications.py`**: Event publishing functions
3. **`app.py`**: SSE endpoint and test endpoints
4. **`lib/routes/chat.py`**: Message sending with notification publishing

### Frontend Components

1. **`src/hooks/useEvents.ts`**: SSE connection and event handling
2. **`src/pages/Messages.tsx`**: Integration with real-time updates
3. **`src/components/NotificationTest.tsx`**: Testing interface

## Event Types

### 1. New Message (`new_message`)
```json
{
  "type": "new_message",
  "conversation_id": "123",
  "sender": "Dr. Smith",
  "text": "Hello, how are you feeling?",
  "timestamp": "2025-01-20T10:30:00Z"
}
```

### 2. Appointment Reminder (`appointment_reminder`)
```json
{
  "type": "appointment_reminder",
  "appointmentId": "456",
  "time": "2025-01-20T14:00:00Z",
  "content": "Annual checkup",
  "timestamp": "2025-01-20T10:30:00Z"
}
```

### 3. System Notification (`system_notification`)
```json
{
  "type": "system_notification",
  "content": "Your profile is incomplete",
  "timestamp": "2025-01-20T10:30:00Z"
}
```

## Setup Instructions

### 1. Redis Configuration

Add to your `.env` file:
```env
REDIS_HOST=localhost
REDIS_PORT=6379
```

### 2. Install Dependencies

Redis is already included in `requirements.txt`:
```
redis==6.2.0
```

### 3. Start Redis

Using Docker:
```bash
docker run -d -p 6379:6379 redis:alpine
```

Or install locally:
```bash
# Ubuntu/Debian
sudo apt-get install redis-server

# macOS
brew install redis
brew services start redis
```

## Testing

### 1. Test Redis Connection

Run the Redis test script:
```bash
python test/test_redis.py
```

### 2. Test SSE in Browser

1. Start the Flask backend:
```bash
python app.py
```

2. Start the React frontend:
```bash
npm start
```

3. Navigate to the Messages page
4. Use the "SSE Notification Test" component to send test events
5. Check the browser console for event logs

### 3. Test Endpoints

**Test SSE Message:**
```bash
curl -X GET http://localhost:5000/api/sse \
  -H "Cookie: session=your-session-cookie"
```

**Test Appointment Reminder:**
```bash
curl -X POST http://localhost:5000/api/test/appointment-reminder \
  -H "Content-Type: application/json" \
  -H "Cookie: session=your-session-cookie" \
  -d '{
    "appointmentId": "test-123",
    "time": "2025-01-20T14:00:00Z",
    "content": "Test appointment"
  }'
```

## How It Works

### 1. Event Publishing

When a message is sent:
1. Message is saved to the database
2. Event is published to Redis PubSub for immediate delivery
3. Event is stored in Redis List for replay (1-hour TTL)

### 2. Event Delivery

When a user connects via SSE:
1. Past events are replayed from Redis List
2. New events are delivered via Redis PubSub
3. Events are formatted as Server-Sent Events

### 3. Frontend Handling

The `useEvents` hook:
1. Establishes SSE connection
2. Handles reconnection on errors
3. Calls appropriate callbacks for each event type
4. Updates UI in real-time

## Integration Points

### Message Sending

In `lib/routes/chat.py`, after successfully saving a message:
```python
# Publish notification to all other participants
for participant_id in conversation.participants:
    if participant_id != current_user_id:
        event_data = {
            "type": "new_message",
            "conversation_id": conversation_id,
            "sender": sender_name,
            "text": message_text,
            "timestamp": str(msg_obj.created_at)
        }
        publish_event_with_buffer(participant_id, event_data)
```

### Frontend Integration

In `src/pages/Messages.tsx`:
```typescript
const handleNewMessage = useCallback((data: any) => {
  // Update conversation list
  setConversations(prevConversations => 
    prevConversations.map(conv => {
      if (conv.id.toString() === data.conversation_id) {
        return { ...conv, lastMessage: data.text };
      }
      return conv;
    })
  );
  
  // Refresh messages if conversation is selected
  if (selectedConversationId?.toString() === data.conversation_id) {
    // Fetch updated messages
  }
}, [selectedConversationId, setConversations]);

useEvents({
  onNewMessage: handleNewMessage,
  onAppointmentReminder: handleAppointmentReminder,
  onSystemNotification: handleSystemNotification,
});
```

## Troubleshooting

### Common Issues

1. **Redis Connection Failed**
   - Check if Redis is running: `redis-cli ping`
   - Verify host/port in settings
   - Check firewall settings

2. **SSE Connection Errors**
   - Ensure user is authenticated
   - Check browser console for CORS errors
   - Verify SSE endpoint is accessible

3. **Events Not Received**
   - Check Redis PubSub: `redis-cli monitor`
   - Verify user ID in event publishing
   - Check browser console for SSE errors

### Debug Commands

```bash
# Monitor Redis activity
redis-cli monitor

# Check Redis keys
redis-cli keys "user:*"

# Test Redis PubSub
redis-cli subscribe "user:test-user-123"

# Check SSE endpoint
curl -N http://localhost:5000/api/events/stream
```

## Future Enhancements

1. **WebSocket Support**: For bi-directional communication
2. **Message Encryption**: For sensitive medical data
3. **Delivery Acknowledgments**: For guaranteed message delivery
4. **Rate Limiting**: To prevent spam
5. **Message Persistence**: Longer-term message storage
6. **Push Notifications**: For mobile devices 