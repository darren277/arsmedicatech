# OpenAI Security System

This document describes the comprehensive security system implemented for OpenAI API integration in ArsMedicaTech.

## 🔐 **Security Overview**

The system provides multiple layers of security for OpenAI API usage:

1. **User-Specific API Keys** - Each user has their own encrypted API key
2. **API Key Validation** - Real-time validation of API keys
3. **Rate Limiting** - Per-user rate limiting to prevent abuse
4. **Usage Monitoring** - Track and display API usage statistics
5. **Secure Storage** - AES-256 encryption for API keys

## 🏗️ **Architecture**

```
Frontend (Settings) → Backend (Security Service) → OpenAI API
       ↓                        ↓                      ↓
   User Input              Validation &              API Calls
   Usage Display           Rate Limiting             Response
```

## 🔧 **Components**

### 1. OpenAI Security Service (`lib/services/openai_security.py`)

**Features:**
- API key validation with OpenAI
- Rate limiting (100 requests/hour per user)
- Usage tracking and statistics
- Caching for performance

**Key Methods:**
```python
# Validate API key
is_valid, error = security_service.validate_api_key(api_key)

# Get user API key with validation
api_key, error = security_service.get_user_api_key_with_validation(user_id)

# Check rate limits
within_limit, error = security_service.check_rate_limit(user_id)

# Get usage statistics
stats = security_service.get_usage_stats(user_id)
```

### 2. Enhanced LLM Agent Route (`lib/routes/llm_agent.py`)

**Security Features:**
- Automatic API key validation
- Rate limit enforcement
- Usage logging
- Error handling

**Flow:**
1. Authenticate user
2. Validate API key
3. Check rate limits
4. Make API call
5. Log usage
6. Return response

### 3. Usage Monitoring (`/api/usage`)

**Endpoint:** `GET /api/usage`

**Response:**
```json
{
  "success": true,
  "usage": {
    "requests_this_hour": 5,
    "max_requests_per_hour": 100,
    "window_start": 1640995200
  }
}
```

### 4. Enhanced Settings UI

**Features:**
- API key management
- Usage statistics display
- Real-time progress bars
- Rate limit warnings

## 🛡️ **Security Features**

### **API Key Security**
- **Encryption**: AES-256 with PBKDF2 key derivation
- **Validation**: Real-time validation with OpenAI
- **Caching**: 1-hour validation cache
- **Format Check**: Ensures proper OpenAI key format

### **Rate Limiting**
- **Window**: 1-hour sliding window
- **Limit**: 100 requests per hour per user
- **Storage**: In-memory with automatic cleanup
- **Reset**: Automatic window reset

### **Usage Monitoring**
- **Tracking**: Per-user request counting
- **Statistics**: Real-time usage display
- **Logging**: API usage for audit trails
- **Alerts**: Rate limit warnings

## 📊 **Usage Statistics**

The system tracks:
- **Requests per hour**: Current usage vs limit
- **Window timing**: When limits reset
- **Model usage**: Which models are being used
- **Token usage**: Optional token counting

## 🔄 **API Flow**

### **1. User Makes Request**
```
User → Frontend → /api/llm_chat → Security Service
```

### **2. Security Validation**
```
Security Service → Rate Limit Check → API Key Validation → OpenAI API
```

### **3. Response Processing**
```
OpenAI API → Usage Logging → Response → User
```

## 🚀 **Configuration**

### **Environment Variables**
```bash
# Required for encryption
ENCRYPTION_KEY=your-secure-32-character-key

# Optional system fallback
MIGRATION_OPENAI_API_KEY=sk-system-key-for-migrations
```

### **Rate Limiting Configuration**
```python
# In OpenAISecurityService
self.rate_limit_window = 3600  # 1 hour
self.max_requests_per_hour = 100  # Adjust as needed
```

## 📈 **Monitoring & Analytics**

### **Usage Dashboard**
- Real-time usage statistics
- Rate limit progress bars
- Window reset timers
- Historical usage data

### **Admin Monitoring**
- System-wide usage statistics
- User-specific usage reports
- Rate limit violations
- API key validation failures

## 🔍 **Error Handling**

### **Common Errors**
1. **No API Key**: "Please configure your API key in Settings"
2. **Invalid Key**: "API key validation failed"
3. **Rate Limit**: "Rate limit exceeded. Please try again later"
4. **Network Error**: "API connection failed"

### **Error Recovery**
- Automatic retry for network issues
- Graceful degradation for validation failures
- User-friendly error messages
- Detailed logging for debugging

## 🧪 **Testing**

### **Security Tests**
```bash
# Test encryption
python test/test_encryption.py

# Test rate limiting
python test/test_rate_limiting.py

# Test API validation
python test/test_api_validation.py
```

### **Integration Tests**
- End-to-end API key flow
- Rate limiting enforcement
- Usage tracking accuracy
- Error handling scenarios

## 🔒 **Best Practices**

### **For Users**
1. **Secure Storage**: Never share API keys
2. **Regular Rotation**: Update keys periodically
3. **Monitor Usage**: Check usage statistics regularly
4. **Report Issues**: Contact support for problems

### **For Developers**
1. **Environment Variables**: Use secure key management
2. **Logging**: Implement comprehensive logging
3. **Monitoring**: Set up usage alerts
4. **Testing**: Regular security testing

## 🚨 **Security Considerations**

### **Data Protection**
- API keys encrypted at rest
- Secure transmission (HTTPS)
- No plain text storage
- Access control enforcement

### **Rate Limiting**
- Prevents API abuse
- Protects against DoS attacks
- Fair usage distribution
- Configurable limits

### **Monitoring**
- Real-time usage tracking
- Anomaly detection
- Audit trail maintenance
- Performance monitoring

## 🔮 **Future Enhancements**

### **Planned Features**
1. **Advanced Analytics**: Detailed usage reports
2. **Cost Tracking**: Dollar amount tracking
3. **Team Management**: Shared API keys
4. **Webhooks**: Usage notifications
5. **API Key Rotation**: Automatic key rotation

### **Security Improvements**
1. **Multi-factor Authentication**: Additional security
2. **IP Whitelisting**: Geographic restrictions
3. **Advanced Rate Limiting**: Adaptive limits
4. **Threat Detection**: Anomaly detection
5. **Compliance**: GDPR/HIPAA compliance

## 📞 **Support**

For security issues or questions:
1. Check the logs for detailed error information
2. Review usage statistics for anomalies
3. Contact the development team
4. Report security vulnerabilities immediately

---

**Note**: This security system is designed to protect both users and the platform while providing a seamless experience. Regular security audits and updates are performed to maintain the highest security standards. 