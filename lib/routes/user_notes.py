"""
User Notes routes for the application.
"""
from typing import Tuple

from flask import Response, jsonify, request

from lib.services.auth_decorators import get_current_user_id
from lib.services.user_notes_service import UserNotesService
from settings import logger


def get_user_notes_route() -> Tuple[Response, int]:
    """
    Get all notes for the current user

    This endpoint retrieves all notes for the currently authenticated user.
    It supports optional query parameters for filtering and searching.
    Returns a JSON response with a list of notes.

    Example request:
    GET /api/user-notes?include_shared=true&search=query
    Query parameters:
    - include_shared: Whether to include shared notes from other users (default: true)
    - search: Search query to filter notes by title, content, or tags

    Example response:
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

    :return: Response object containing a JSON list of notes.
    """
    try:
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401

        # Get query parameters
        include_shared = request.args.get('include_shared', 'true').lower() == 'true'
        search_query = request.args.get('search', '').strip()

        user_notes_service = UserNotesService()
        user_notes_service.connect()
        
        try:
            if search_query:
                notes = user_notes_service.search_notes(user_id, search_query, include_shared)
            else:
                notes = user_notes_service.get_user_notes(user_id, include_shared)

            return jsonify({
                "success": True,
                "notes": [
                    {
                        "id": note.id,
                        "title": note.title,
                        "content": note.content,
                        "note_type": note.note_type,
                        "tags": note.tags,
                        "date_created": note.date_created,
                        "date_updated": note.date_updated
                    }
                    for note in notes
                ]
            }), 200
        finally:
            user_notes_service.close()

    except Exception as e:
        logger.error(f"Error getting user notes: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_note_by_id_route(note_id: str) -> Tuple[Response, int]:
    """
    Get a specific note by ID

    This endpoint retrieves a specific note by its ID.
    Users can only access their own notes or shared notes.

    Example request:
    GET /api/user-notes/{note_id}

    Example response:
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

    :param note_id: ID of the note to retrieve
    :return: Response object containing the note data or an error message.
    """
    try:
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401

        user_notes_service = UserNotesService()
        user_notes_service.connect()
        
        try:
            note = user_notes_service.get_note_by_id(note_id, user_id)
            
            if not note:
                return jsonify({"error": "Note not found or access denied"}), 404

            return jsonify({
                "success": True,
                "note": {
                    "id": note.id,
                    "title": note.title,
                    "content": note.content,
                    "note_type": note.note_type,
                    "tags": note.tags,
                    "date_created": note.date_created,
                    "date_updated": note.date_updated
                }
            }), 200
        finally:
            user_notes_service.close()

    except Exception as e:
        logger.error(f"Error getting note by ID: {e}")
        return jsonify({"error": "Internal server error"}), 500


def create_note_route() -> Tuple[Response, int]:
    """
    Create a new note

    This endpoint allows authenticated users to create a new note.
    It expects a JSON payload with the note details.

    Example request:
    POST /api/user-notes
    Body:
    {
        "title": "Note Title",
        "content": "Note content in markdown...",
        "note_type": "private",
        "tags": ["tag1", "tag2"]
    }

    Example response:
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

    :return: Response object containing the created note or an error message.
    """
    try:
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401

        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        title = data.get('title')
        content = data.get('content')
        note_type = data.get('note_type', 'private')
        tags = data.get('tags', [])

        if not title or not content:
            return jsonify({"error": "Title and content are required"}), 400

        user_notes_service = UserNotesService()
        user_notes_service.connect()
        
        try:
            success, message, note = user_notes_service.create_note(
                user_id=user_id,
                title=title,
                content=content,
                note_type=note_type,
                tags=tags
            )

            if success and note:
                return jsonify({
                    "success": True,
                    "message": message,
                    "note": {
                        "id": note.id,
                        "title": note.title,
                        "content": note.content,
                        "note_type": note.note_type,
                        "tags": note.tags,
                        "date_created": note.date_created,
                        "date_updated": note.date_updated
                    }
                }), 201
            else:
                return jsonify({"error": message}), 400
        finally:
            user_notes_service.close()

    except Exception as e:
        logger.error(f"Error creating note: {e}")
        return jsonify({"error": "Internal server error"}), 500


def update_note_route(note_id: str) -> Tuple[Response, int]:
    """
    Update an existing note

    This endpoint allows users to update their own notes.
    It expects a JSON payload with the fields to update.

    Example request:
    PUT /api/user-notes/{note_id}
    Body:
    {
        "title": "Updated Title",
        "content": "Updated content...",
        "note_type": "shared",
        "tags": ["updated", "tags"]
    }

    Example response:
    {
        "success": true,
        "message": "Note updated successfully",
        "note": {
            "id": "note_id",
            "title": "Updated Title",
            "content": "Updated content...",
            "note_type": "shared",
            "tags": ["updated", "tags"],
            "date_created": "2023-01-01T00:00:00Z",
            "date_updated": "2023-01-02T00:00:00Z"
        }
    }

    :param note_id: ID of the note to update
    :return: Response object containing the updated note or an error message.
    """
    try:
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401

        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        user_notes_service = UserNotesService()
        user_notes_service.connect()
        
        try:
            success, message, note = user_notes_service.update_note(
                note_id=note_id,
                user_id=user_id,
                title=data.get('title'),
                content=data.get('content'),
                note_type=data.get('note_type'),
                tags=data.get('tags')
            )

            if success and note:
                return jsonify({
                    "success": True,
                    "message": message,
                    "note": {
                        "id": note.id,
                        "title": note.title,
                        "content": note.content,
                        "note_type": note.note_type,
                        "tags": note.tags,
                        "date_created": note.date_created,
                        "date_updated": note.date_updated
                    }
                }), 200
            else:
                return jsonify({"error": message}), 400
        finally:
            user_notes_service.close()

    except Exception as e:
        logger.error(f"Error updating note: {e}")
        return jsonify({"error": "Internal server error"}), 500


def delete_note_route(note_id: str) -> Tuple[Response, int]:
    """
    Delete a note

    This endpoint allows users to delete their own notes.

    Example request:
    DELETE /api/user-notes/{note_id}

    Example response:
    {
        "success": true,
        "message": "Note deleted successfully"
    }

    :param note_id: ID of the note to delete
    :return: Response object containing success message or an error.
    """
    try:
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401

        user_notes_service = UserNotesService()
        user_notes_service.connect()
        
        try:
            success, message = user_notes_service.delete_note(note_id, user_id)

            if success:
                return jsonify({
                    "success": True,
                    "message": message
                }), 200
            else:
                return jsonify({"error": message}), 400
        finally:
            user_notes_service.close()

    except Exception as e:
        logger.error(f"Error deleting note: {e}")
        return jsonify({"error": "Internal server error"}), 500 