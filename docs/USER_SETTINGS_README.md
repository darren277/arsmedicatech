# User Settings System

This document describes the secure user settings system implemented for ArsMedicaTech, focusing on OpenAI API key management.

## Overview

The user settings system provides a secure way for users to manage their account preferences, particularly their OpenAI API keys. All sensitive data is encrypted at rest and in transit.

## Security Features

### Encryption
- **AES-256 encryption** using Fernet (symmetric encryption)
- **PBKDF2 key derivation** with 100,000 iterations for key generation
- **Environment-based master key** for encryption/decryption
- **API key prefixing** for additional security identification

### Data Protection
- API keys are never stored in plain text
- Encryption happens before database storage
- Decryption only occurs when needed for API calls
- No API keys are returned in API responses

## Backend Components

### 1. Encryption Service (`lib/services/encryption.py`)
```python
from lib.services.encryption import get_encryption_service

# Encrypt API key
encryption_service = get_encryption_service()
encrypted_key = encryption_service.encrypt_api_key("sk-...")

# Decrypt API key
decrypted_key = encryption_service.decrypt_api_key(encrypted_key)
```

### 2. User Settings Model (`lib/models/user_settings.py`)
- Manages user settings data
- Handles API key validation
- Provides secure getter/setter methods

### 3. User Service Extensions (`lib/services/user_service.py`)
- `get_user_settings(user_id)` - Retrieve user settings
- `save_user_settings(user_id, settings)` - Save settings
- `update_openai_api_key(user_id, api_key)` - Update API key
- `get_openai_api_key(user_id)` - Get decrypted API key
- `has_openai_api_key(user_id)` - Check if API key exists

### 4. Settings Routes (`lib/routes/settings.py`)
- `GET /api/settings` - Get user settings (no API key returned)
- `POST /api/settings` - Update user settings

## Frontend Components

### Settings Component (`src/components/Settings.tsx`)
- Modern, responsive UI
- Secure API key input with show/hide toggle
- Real-time validation
- Success/error messaging
- Loading states

### Features
- **API Key Management**: Add, update, or remove OpenAI API keys
- **User Information Display**: Show user details and role
- **Security Information**: Display account creation and update dates
- **Responsive Design**: Works on desktop and mobile devices

## Environment Setup

### Required Environment Variables
```bash
# Master encryption key (32+ characters recommended)
ENCRYPTION_KEY=your-secure-encryption-key-here
```

### Database Schema
The system uses a `UserSettings` table with the following structure:
```sql
CREATE TABLE UserSettings (
    id STRING,
    user_id STRING,
    openai_api_key STRING,  -- Encrypted
    created_at STRING,
    updated_at STRING
);
```

## API Endpoints

### Get User Settings
```http
GET /api/settings
Authorization: Bearer <token>
```

Response:
```json
{
  "success": true,
  "settings": {
    "user_id": "user:123",
    "has_openai_api_key": true,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

### Update User Settings
```http
POST /api/settings
Authorization: Bearer <token>
Content-Type: application/json

{
  "openai_api_key": "sk-..."
}
```

Response:
```json
{
  "success": true,
  "message": "OpenAI API key updated successfully"
}
```

## Usage Examples

### Backend Usage
```python
from lib.services.user_service import UserService

user_service = UserService()
user_service.connect()

# Update API key
success, message = user_service.update_openai_api_key("user:123", "sk-...")

# Get API key for use
api_key = user_service.get_openai_api_key("user:123")

# Check if user has API key
has_key = user_service.has_openai_api_key("user:123")
```

### Frontend Usage
```typescript
import apiService from '../services/api';

// Load settings
const settings = await apiService.getAPI('/settings');

// Update API key
await apiService.postAPI('/settings', {
  openai_api_key: 'sk-...'
});
```

## Security Best Practices

1. **Environment Variables**: Always use environment variables for encryption keys
2. **Key Rotation**: Regularly rotate the master encryption key
3. **Access Control**: Ensure only authenticated users can access their settings
4. **Input Validation**: Validate API keys before encryption
5. **Error Handling**: Don't expose encryption errors to users
6. **Logging**: Log encryption/decryption operations for audit trails

## Testing

Run the encryption tests:
```bash
cd test
python test_encryption.py
```

## Troubleshooting

### Common Issues

1. **ENCRYPTION_KEY not set**
   - Error: "ENCRYPTION_KEY environment variable must be set"
   - Solution: Set the ENCRYPTION_KEY environment variable

2. **Invalid API key format**
   - Error: "OpenAI API key must start with 'sk-'"
   - Solution: Ensure API key follows OpenAI format (sk-...)

3. **Decryption failures**
   - Error: "Failed to decrypt data"
   - Solution: Check if encryption key has changed or data is corrupted

### Debug Mode
Enable debug logging by setting the log level to DEBUG in your application configuration.

## Future Enhancements

1. **Additional Settings**: Profile information, preferences, notifications
2. **Key Rotation**: Automatic encryption key rotation
3. **Audit Trail**: Track settings changes
4. **Backup/Restore**: Export/import settings
5. **Multi-factor Authentication**: Additional security for sensitive settings 