# Clinic-Organization Relationship

This document explains the relationship between clinics and organizations in the system, including the new features that allow organizations to manage multiple clinics.

## Overview

Organizations can now have multiple clinics associated with them, representing a chain of medical facilities under the same management. All clinics belonging to a particular organization share the same country.

## Data Model Changes

### Clinic Model Updates

The `Clinic` model now includes a `country` field:

```python
class Clinic:
    def __init__(
        self,
        name: str,
        street: str,
        city: str,
        state: str,
        zip_code: str,
        country: str,  # NEW: Country field
        longitude: float,
        latitude: float
    ):
        # ... existing fields ...
        self.country = country
```

### Organization Model Updates

The `Organization` model now includes:

```python
class Organization:
    def __init__(
        self,
        name: str,
        org_type: str,
        created_by: str,
        # ... existing fields ...
        country: Optional[str] = None,  # NEW: Country field
        clinic_ids: Optional[list[str]] = None,  # NEW: List of clinic IDs
    ):
        # ... existing fields ...
        self.country = country or ""
        self.clinic_ids = clinic_ids or []
```

## API Endpoints

### Organization Management

- `GET /api/organizations` - Get all organizations
- `GET /api/organizations/{org_id}` - Get specific organization
- `POST /api/organizations` - Create new organization
- `PUT /api/organizations/{org_id}` - Update organization

### Clinic Management within Organizations

- `GET /api/organizations/{org_id}/clinics` - Get all clinics for an organization
- `POST /api/organizations/{org_id}/clinics` - Add a clinic to an organization
- `DELETE /api/organizations/{org_id}/clinics` - Remove a clinic from an organization

## Frontend Components

### OrganizationForm

The organization creation/editing form now includes:
- Country field (optional)
- All existing fields (name, type, description)

### ClinicList

A new component for managing clinics within an organization:
- Display all clinics associated with the organization
- Add new clinics by entering clinic ID
- Remove clinics from the organization
- Show clinic details including address and location

## Usage Examples

### Creating an Organization with Country

```javascript
const orgData = {
  name: "Metropolitan Health Group",
  org_type: "provider",
  description: "Multi-location healthcare provider",
  country: "USA",
  created_by: "user123"
};

const response = await organizationAPI.create(orgData);
```

### Adding a Clinic to an Organization

```javascript
// Add clinic to organization
await organizationAPI.addClinic(organizationId, clinicId);

// Get all clinics for an organization
const clinics = await organizationAPI.getClinics(organizationId);

// Remove clinic from organization
await organizationAPI.removeClinic(organizationId, clinicId);
```

### Frontend Integration

The Organization page now includes:
1. Organization details with country information
2. Clinic management section
3. Ability to add/remove clinics
4. Real-time updates when clinics are modified

## Migration

To update existing data, run the migration script:

```bash
python lib/migrations/update_clinic_org_fields.py
```

This script will:
1. Add `country` field to existing clinics (defaults to "USA")
2. Add `country` and `clinic_ids` fields to existing organizations
3. Preserve existing data while adding new fields

## Business Rules

1. **Country Consistency**: All clinics in an organization must share the same country
2. **Clinic Ownership**: Clinics can belong to multiple organizations (many-to-many relationship)
3. **Organization Limits**: Users are still limited by the organization creation limit
4. **Data Integrity**: When adding a clinic to an organization, the system validates that the clinic exists

## Database Schema

### Clinic Table
```sql
DEFINE TABLE clinic SCHEMAFULL;
DEFINE FIELD name ON clinic TYPE string;
DEFINE FIELD address ON clinic TYPE object;
DEFINE FIELD address.street ON clinic TYPE string;
DEFINE FIELD address.city ON clinic TYPE string;
DEFINE FIELD address.state ON clinic TYPE string;
DEFINE FIELD address.zip ON clinic TYPE string;
DEFINE FIELD address.country ON clinic TYPE string;  -- NEW
DEFINE FIELD location ON clinic TYPE geometry (point);
```

### Organization Table
```sql
DEFINE TABLE organization SCHEMAFULL;
DEFINE FIELD name ON organization TYPE string;
DEFINE FIELD org_type ON organization TYPE string;
DEFINE FIELD created_by ON organization TYPE string;
DEFINE FIELD created_at ON organization TYPE string;
DEFINE FIELD description ON organization TYPE string;
DEFINE FIELD country ON organization TYPE string;  -- NEW
DEFINE FIELD clinic_ids ON organization TYPE array;  -- NEW
```

## Future Enhancements

Potential future improvements:
1. Clinic creation within organizations
2. Geographic clustering of clinics
3. Organization hierarchy (parent-child organizations)
4. Clinic-specific settings and configurations
5. Advanced search and filtering by location 