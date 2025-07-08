# Patient CRUD Operations

This document describes the full CRUD (Create, Read, Update, Delete) operations implemented for patients in the Flask/React application using SurrealDB.

## Backend API Endpoints

### 1. Get All Patients
- **GET** `/api/patients`
- Returns a list of all patients
- Response: Array of patient objects

### 2. Get Patient by ID
- **GET** `/api/patients/{patient_id}`
- Returns a specific patient by their demographic_no
- Response: Patient object or 404 if not found

### 3. Create New Patient
- **POST** `/api/patients`
- Creates a new patient record
- Required fields: `first_name`, `last_name`
- Optional fields: `date_of_birth`, `sex`, `phone`, `email`, `location`
- Response: Created patient object (201) or error (400/500)

### 4. Update Patient
- **PUT** `/api/patients/{patient_id}`
- Updates an existing patient record
- All fields are optional for updates
- Response: Updated patient object or 404 if not found

### 5. Delete Patient
- **DELETE** `/api/patients/{patient_id}`
- Deletes a patient record
- Response: Success message or 404 if not found

### 6. Search Patients
- **GET** `/api/patients/search?q={search_term}`
- Searches patient encounters using full-text search
- Requires at least 2 characters in search term

## Frontend Components

### 1. PatientList Component
- Displays all patients in a table format
- Includes actions for Edit and Delete
- "Add New Patient" button to create new patients
- Responsive design with loading states and error handling

### 2. Patient Component
- Displays detailed patient information
- Shows personal details and contact information
- Includes Edit and Delete buttons
- Handles loading states and error cases

### 3. PatientForm Component
- Used for both creating and editing patients
- Form validation for required fields
- Address fields for location information
- Responsive design with proper error handling

## API Service (src/services/api.js)

The `patientAPI` object provides methods for all CRUD operations:

```javascript
export const patientAPI = {
    getAll: () => api.get('/patients'),
    getById: (id) => api.get(`/patients/${id}`),
    create: (patientData) => api.post('/patients', patientData),
    update: (id, patientData) => api.put(`/patients/${id}`, patientData),
    delete: (id) => api.delete(`/patients/${id}`),
    search: (query) => api.get(`/patients/search?q=${encodeURIComponent(query)}`)
};
```

## Routes

The following routes are available in the React application:

- `/patients` - Patient list
- `/patients/new` - Create new patient form
- `/patients/{id}` - View patient details
- `/patients/{id}/edit` - Edit patient form

## Patient Data Structure

```javascript
{
    demographic_no: "string",      // Unique patient identifier
    first_name: "string",          // Required
    last_name: "string",           // Required
    date_of_birth: "string",       // ISO date format
    sex: "M|F|O",                  // Male, Female, Other
    phone: "string",               // Phone number
    email: "string",               // Email address
    location: ["city", "state", "country", "zipcode"]  // Address array
}
```

## Testing

A test endpoint is available at `/api/test_crud` that performs a complete CRUD cycle:
1. Creates a test patient
2. Reads the created patient
3. Updates the patient
4. Deletes the patient

This endpoint can be used to verify that all operations are working correctly.

## Error Handling

- All endpoints return appropriate HTTP status codes
- Frontend components display error messages to users
- Loading states are shown during API calls
- Form validation prevents invalid data submission

## Database Schema

The patient table in SurrealDB includes:
- Unique index on `demographic_no`
- All fields are properly typed
- Location stored as an array
- Full-text search capabilities for encounters

## Future Enhancements

- Medical history integration
- Encounter management
- File attachments
- Audit logging
- Advanced search and filtering
- Bulk operations 