# Organization Limits

This document explains the organization limit system that prevents users from creating unlimited organizations.

## How It Works

### User Model Fields

Each user has two organization-related fields:

- `max_organizations`: Maximum number of organizations the user can create (default: 1)
- `user_organizations`: Current number of organizations the user has created (default: 0)

### Limit Enforcement

1. **Before Creation**: When a user tries to create an organization, the system checks if `user_organizations < max_organizations`
2. **After Creation**: If successful, the system increments `user_organizations` by 1
3. **Error Handling**: If the limit is reached, the API returns a 403 error with details

### Frontend Display

The organization creation page shows:
- Current organization count
- Maximum allowed organizations
- Remaining slots available

## Updating Organization Limits

### Method 1: Direct Database Update

You can directly update the `max_organizations` field in the database:

```sql
-- Update a specific user to allow 5 organizations
UPDATE user:user_id SET max_organizations = 5;

-- Update all admin users to allow 10 organizations
UPDATE user SET max_organizations = 10 WHERE role = 'admin';

-- Update all users to allow 3 organizations
UPDATE user SET max_organizations = 3;
```

### Method 2: Using the Migration Script

Use the provided migration utilities:

```python
from lib.migrations.update_org_limits import update_user_org_limit, bulk_update_org_limits

# Update a specific user
update_user_org_limit("User:abc123", 5)

# Update all admin users
bulk_update_org_limits(10, "admin")

# Update all users
bulk_update_org_limits(3)
```

### Method 3: Running the Migration Script

```bash
# Navigate to the project directory
cd /path/to/arsmedicatech

# Run the migration script
python -c "
from lib.migrations.update_org_limits import bulk_update_org_limits
result = bulk_update_org_limits(5, 'admin')
print(f'Updated {result[\"success\"]} admin users')
"
```

## Configuration Examples

### Free Tier (Default)
- `max_organizations = 1`
- Users can create one organization

### Premium Tier
- `max_organizations = 5`
- Users can create up to 5 organizations

### Enterprise Tier
- `max_organizations = 50`
- Users can create up to 50 organizations

### Unlimited
- `max_organizations = 999999`
- Users can create unlimited organizations

## Monitoring

Check current organization usage:

```python
from lib.migrations.update_org_limits import get_user_org_info

# Get info for all users
info = get_user_org_info()
for user in info['users']:
    print(f"{user['username']}: {user['user_organizations']}/{user['max_organizations']} orgs")
```

## API Response Examples

### Success Response
```json
{
  "organization": {
    "id": "organization:abc123",
    "name": "My Organization",
    "org_type": "admin",
    "created_by": "User:def456",
    "description": "My organization description"
  },
  "id": "organization:abc123"
}
```

### Limit Reached Error
```json
{
  "error": "Organization limit reached. You can create 1 organization(s) and have already created 1. Remaining slots: 0"
}
```

## Best Practices

1. **Set Reasonable Defaults**: Start with `max_organizations = 1` for new users
2. **Monitor Usage**: Regularly check organization creation patterns
3. **Gradual Increases**: Increase limits based on user needs and subscription tiers
4. **Clear Communication**: Make limits visible in the UI
5. **Easy Updates**: Use the migration script for bulk updates

## Troubleshooting

### User Can't Create Organization
1. Check if `user_organizations >= max_organizations`
2. Verify the user record exists in the database
3. Check for any database connection issues

### Migration Script Errors
1. Ensure database connection is working
2. Check user IDs are in correct format (e.g., "User:abc123")
3. Verify user records exist before updating

### Frontend Not Showing Limits
1. Check if user object includes `max_organizations` and `user_organizations` fields
2. Verify the User interface in TypeScript includes these fields
3. Ensure the API is returning the correct user data 