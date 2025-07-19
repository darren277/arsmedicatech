# Webhook System Documentation

This document describes the webhook system implementation for the ArsMedicaTech application, which allows external systems to receive real-time notifications about appointment events.

## Overview

The webhook system follows a clean, event-driven architecture that separates domain logic from webhook delivery concerns. It uses an in-process event bus to publish domain events, which are then handled by background tasks that deliver webhooks to subscribed endpoints.

## Architecture

### Components

1. **Domain Events** (`lib/events.py`)
   - `AppointmentCreated`
   - `AppointmentUpdated`
   - `AppointmentCancelled`
   - `AppointmentConfirmed`
   - `AppointmentCompleted`

2. **Event Bus** (`lib/infra/event_bus.py`)
   - Simple in-process event bus for publishing and subscribing to events

3. **Event Handlers** (`lib/event_handlers.py`)
   - Handlers that convert domain events to webhook payloads
   - Triggers background webhook delivery

4. **Webhook Delivery** (`lib/tasks.py`)
   - Background tasks for delivering webhooks with retry logic
   - HMAC signature generation for security

5. **Webhook Subscriptions** (`lib/models/webhook_subscription.py`)
   - Model for storing webhook subscription configurations

6. **Webhook Routes** (`lib/routes/webhooks.py`)
   - REST API endpoints for managing webhook subscriptions

## Setup

### 1. Run the Migration

```bash
python -m lib.migrations.setup_webhooks
```

This will create the `webhook_subscription` table and add some sample subscriptions.

### 2. Install Dependencies

The webhook system requires the `requests` library for HTTP delivery:

```bash
pip install requests
```

## API Endpoints

### Webhook Subscriptions

#### Create Webhook Subscription
```http
POST /api/webhooks
Content-Type: application/json

{
    "event_name": "appointment.created",
    "target_url": "https://your-endpoint.com/webhooks",
    "secret": "your-secret-key",
    "enabled": true
}
```

#### Get Webhook Subscriptions
```http
GET /api/webhooks
GET /api/webhooks?event_name=appointment.created
GET /api/webhooks?enabled=true
```

#### Get Specific Webhook Subscription
```http
GET /api/webhooks/{subscription_id}
```

#### Update Webhook Subscription
```http
PUT /api/webhooks/{subscription_id}
Content-Type: application/json

{
    "target_url": "https://new-endpoint.com/webhooks",
    "enabled": false
}
```

#### Delete Webhook Subscription
```http
DELETE /api/webhooks/{subscription_id}
```

#### Get Available Events
```http
GET /api/webhooks/events
```

## Webhook Payload Format

All webhooks are sent as JSON with the following structure:

```json
{
    "event": "appointment.created",
    "timestamp": "2023-09-01T12:00:00Z",
    "delivery_id": "uuid-v4",
    "data": {
        "appointment_id": "appointment:12345",
        "patient_id": "patient:67890",
        "provider_id": "provider:11111",
        "appointment_date": "2023-09-15",
        "start_time": "10:00",
        "end_time": "10:30",
        "appointment_type": "consultation"
    }
}
```

## Security

### HMAC Signatures

Each webhook includes an HMAC signature in the `X-Signature` header:

```http
X-Signature: sha256=abc123...
```

To verify the signature:

```python
import hmac
import hashlib

def verify_signature(payload: bytes, secret: str, signature: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```

### Headers

All webhooks include these headers:

- `Content-Type: application/json`
- `X-Event-Type: appointment.created`
- `X-Delivery-Id: uuid-v4`
- `X-Signature: sha256=...`
- `User-Agent: ArsMedicaTech-Webhooks/1.0`

## Available Events

| Event | Description | Triggered When |
|-------|-------------|----------------|
| `appointment.created` | New appointment created | Appointment is successfully saved to database |
| `appointment.updated` | Appointment updated | Any field of an appointment is modified |
| `appointment.cancelled` | Appointment cancelled | Appointment status changed to cancelled |
| `appointment.confirmed` | Appointment confirmed | Appointment status changed to confirmed |
| `appointment.completed` | Appointment completed | Appointment status changed to completed |

## Reliability Features

### Retry Logic

Webhook delivery includes exponential backoff retry logic:
- Maximum 5 retry attempts
- Exponential backoff: 1s, 2s, 4s, 8s, 16s
- 10-second timeout per attempt

### Idempotency

Each webhook includes a unique `delivery_id` to prevent duplicate processing.

### Error Handling

- Network timeouts and connection errors are handled gracefully
- Failed deliveries are logged but don't affect the main application
- Individual subscription failures don't prevent delivery to other subscriptions

## Testing

### Using webhook.site

1. Go to [webhook.site](https://webhook.site)
2. Copy your unique URL
3. Create a webhook subscription:

```bash
curl -X POST http://localhost:5000/api/webhooks \
  -H "Content-Type: application/json" \
  -H "Cookie: session=your-session-cookie" \
  -d '{
    "event_name": "appointment.created",
    "target_url": "https://webhook.site/your-unique-url",
    "secret": "test-secret"
  }'
```

4. Create an appointment through the API or UI
5. Check webhook.site to see the delivered webhook

### Local Testing

You can also test with a local HTTP server:

```bash
# Start a local server
python -m http.server 8000

# Create webhook subscription pointing to localhost
curl -X POST http://localhost:5000/api/webhooks \
  -H "Content-Type: application/json" \
  -H "Cookie: session=your-session-cookie" \
  -d '{
    "event_name": "appointment.created",
    "target_url": "http://localhost:8000/webhook",
    "secret": "test-secret"
  }'
```

## Monitoring

### Logs

The webhook system logs all activities:

- Event publishing: `DEBUG` level
- Webhook delivery attempts: `INFO` level
- Delivery failures: `WARNING` level
- System errors: `ERROR` level

### Metrics

Consider adding metrics for:
- Webhook delivery success/failure rates
- Delivery latency
- Retry counts
- Active subscriptions per event type

## Best Practices

### For Webhook Consumers

1. **Verify signatures** to ensure webhook authenticity
2. **Handle idempotency** using the `delivery_id`
3. **Respond quickly** (within 5 seconds) to avoid timeouts
4. **Return appropriate HTTP status codes**:
   - `200` for successful processing
   - `4xx` for client errors (will trigger retries)
   - `5xx` for server errors (will trigger retries)

### For Webhook Senders

1. **Use HTTPS** for all webhook URLs
2. **Keep secrets secure** and rotate them regularly
3. **Monitor delivery failures** and investigate issues
4. **Test webhook endpoints** before going live

## Troubleshooting

### Common Issues

1. **Webhooks not being delivered**
   - Check if the subscription is enabled
   - Verify the target URL is accessible
   - Check application logs for errors

2. **Signature verification failing**
   - Ensure the secret matches between sender and receiver
   - Verify the signature calculation method

3. **Duplicate webhooks**
   - Use the `delivery_id` to deduplicate
   - Check if multiple subscriptions exist for the same event

### Debug Mode

Enable debug logging to see detailed webhook activity:

```python
import logging
logging.getLogger('lib.tasks').setLevel(logging.DEBUG)
logging.getLogger('lib.event_handlers').setLevel(logging.DEBUG)
```

## Future Enhancements

1. **Dead Letter Queue** for permanently failed deliveries
2. **Webhook delivery metrics** and dashboards
3. **Rate limiting** per subscription
4. **Webhook payload versioning**
5. **Bulk webhook delivery** for high-volume scenarios
6. **Webhook delivery status tracking**
