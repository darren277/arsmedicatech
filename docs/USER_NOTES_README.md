# User Notes Feature

This document describes the User Notes feature that allows any user role/type to take notes of various types (Private vs Shared).

## Overview

The User Notes feature provides a comprehensive note-taking system where users can:
- Create, read, update, and delete notes
- Organize notes with titles, tags, and content
- Choose between private and shared note types
- Use markdown formatting for rich content
- Search through their notes

## Features

### Note Types
- **Private**: Notes that are only visible to the user who created them
- **Shared**: Notes that are visible to all users in the system

### Note Fields
- `id`: Unique identifier for the note
- `title`: Note title (required, max 200 characters)
- `content`: Markdown content (required, max 10,000 characters)
- `note_type`: Either "private" or "shared"
- `tags`: Array of strings for categorization (max 50 characters per tag)
- `date_created`: ISO timestamp when the note was created
- `date_updated`: ISO timestamp when the note was last updated
- `user_id`: ID of the user who owns the note

## Backend Implementation

### Database Schema

The UserNote table is defined in SurrealDB with the following schema:

```sql
DEFINE TABLE UserNote SCHEMAFULL;

DEFINE FIELD user_id ON UserNote TYPE string;
DEFINE FIELD title ON UserNote TYPE string;
DEFINE FIELD content ON UserNote TYPE string;
DEFINE FIELD note_type ON UserNote TYPE string;
DEFINE FIELD tags ON UserNote TYPE array;
DEFINE FIELD date_created ON UserNote TYPE string;
DEFINE FIELD date_updated ON UserNote TYPE string;

DEFINE INDEX idx_user_id ON UserNote FIELDS user_id;
DEFINE INDEX idx_note_type ON UserNote FIELDS note_type;
DEFINE INDEX idx_date_updated ON UserNote FIELDS date_updated;

DEFINE TABLE UserNote PERMISSIONS 
    FOR select WHERE auth.id = user_id OR note_type = 'shared'
    FOR create WHERE auth.id = user_id
    FOR update WHERE auth.id = user_id
    FOR delete WHERE auth.id = user_id;
```

### API Endpoints

#### GET /api/user-notes
Get all notes for the current user (including shared notes from other users).

**Query Parameters:**
- `include_shared` (optional): Whether to include shared notes (default: true)
- `search` (optional): Search query to filter notes

**Response:**
```json
{
  "success": true,
  "notes": [
    {
      "id": "note_id",
      "title": "Note Title",
      "content": "Note content...",
      "note_type": "private",
      "tags": ["tag1", "tag2"],
      "date_created": "2023-01-01T00:00:00Z",
      "date_updated": "2023-01-02T00:00:00Z"
    }
  ]
}
```

#### GET /api/user-notes/{note_id}
Get a specific note by ID.

**Response:**
```json
{
  "success": true,
  "note": {
    "id": "note_id",
    "title": "Note Title",
    "content": "Note content...",
    "note_type": "private",
    "tags": ["tag1", "tag2"],
    "date_created": "2023-01-01T00:00:00Z",
    "date_updated": "2023-01-02T00:00:00Z"
  }
}
```

#### POST /api/user-notes
Create a new note.

**Request Body:**
```json
{
  "title": "Note Title",
  "content": "Note content in markdown...",
  "note_type": "private",
  "tags": ["tag1", "tag2"]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Note created successfully",
  "note": {
    "id": "note_id",
    "title": "Note Title",
    "content": "Note content...",
    "note_type": "private",
    "tags": ["tag1", "tag2"],
    "date_created": "2023-01-01T00:00:00Z",
    "date_updated": "2023-01-01T00:00:00Z"
  }
}
```

#### PUT /api/user-notes/{note_id}
Update an existing note.

**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content...",
  "note_type": "shared",
  "tags": ["updated", "tags"]
}
```

#### DELETE /api/user-notes/{note_id}
Delete a note.

**Response:**
```json
{
  "success": true,
  "message": "Note deleted successfully"
}
```

### Models and Services

#### UserNote Model (`lib/models/user/user_notes.py`)
- Handles validation for note fields
- Provides methods for updating individual fields
- Converts between dictionary and object representations

#### UserNotesService (`lib/services/user_notes_service.py`)
- Manages CRUD operations for notes
- Handles user permissions and access control
- Provides search functionality
- Manages database connections

## Frontend Implementation

### Components

#### UserNotesScreen (`src/components/UserNotes.tsx`)
Main component that provides:
- Split-pane interface with notes list and editor
- Search functionality
- Create, edit, and delete operations
- Markdown editor integration

#### UserNotesPage (`src/pages/UserNotesPage.tsx`)
Page wrapper for the user notes feature.

### Features
- **Notes List**: Shows all user notes with title, date, type, and tags
- **Search**: Real-time search through titles, content, and tags
- **Markdown Editor**: Rich text editing with MDXEditor
- **Note Types**: Visual indicators for private vs shared notes
- **Tags**: Color-coded tag display
- **Responsive Design**: Works on desktop and mobile devices

## Security and Permissions

### Access Control
- Users can only access their own notes or shared notes
- Users can only create, update, and delete their own notes
- Database-level permissions enforce these rules

### Validation
- Title validation (1-200 characters)
- Content validation (1-10,000 characters)
- Note type validation (private/shared only)
- Tag validation (max 50 characters per tag)

## Setup and Installation

### Database Migration
Run the migration script to set up the UserNote table:

```bash
python lib/migrations/setup_user_notes.py
```

### Testing
Run the integration test to verify functionality:

```bash
python test/integration/test_user_notes.py
```

## Usage Examples

### Creating a Note
1. Navigate to the User Notes page
2. Click "New Note"
3. Enter title and content
4. Select note type (private/shared)
5. Add tags (optional)
6. Click "Save"

### Editing a Note
1. Click on a note in the list
2. Click "Edit" button
3. Make changes in the markdown editor
4. Click "Save"

### Searching Notes
1. Use the search box in the notes list
2. Search by title, content, or tags
3. Results update in real-time

### Deleting a Note
1. Click the delete icon on a note
2. Confirm deletion in the dialog

## Future Enhancements

Potential improvements for the user notes feature:
- Note categories/folders
- Rich text formatting options
- Note sharing with specific users
- Note templates
- Export functionality (PDF, Word)
- Note versioning/history
- Collaborative editing
- Note attachments
- Advanced search filters
- Note analytics and insights 