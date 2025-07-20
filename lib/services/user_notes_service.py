"""
User Notes Service for managing user notes.
"""
from typing import Any, Dict, List, Optional

from surrealdb import RecordID

from lib.db.surreal import DbController
from lib.models.user.user_notes import UserNote
from settings import logger


class UserNotesService:
    """
    Service for managing user notes.
    """
    def __init__(self, db_controller: Optional[DbController] = None) -> None:
        """
        Initialize UserNotesService with a database controller.
        :param db_controller: Optional DbController instance. If None, a default DbController will be used.
        :type db_controller: DbController
        :return: None
        """
        self.db = db_controller or DbController()
    
    def connect(self) -> None:
        """
        Connect to database
        This method attempts to connect to the database using the provided DbController.
        If the DbController does not have a connect method, it will log a message and continue in mock mode.
        :return: None
        """
        logger.debug("Connecting to database...")
        try:
            logger.debug(f"Database controller type: {type(self.db)}")
            logger.debug(f"Database controller has connect method: {hasattr(self.db, 'connect')}")
            
            if hasattr(self.db, 'connect'):
                self.db.connect()
                logger.debug("Database connection successful")
            else:
                logger.debug("Database controller does not have connect method - using mock mode")
        except Exception as e:
            logger.debug(f"Database connection error: {e}")
            logger.debug("Continuing with mock database mode")
            # Don't raise the exception, continue with mock mode
    
    def close(self) -> None:
        """
        Close database connection
        :return: None
        """
        try:
            if hasattr(self.db, 'close'):
                self.db.close()
                logger.debug("Database connection closed")
        except Exception as e:
            logger.debug(f"Error closing database connection: {e}")
    
    def create_note(
            self,
            user_id: str,
            title: str,
            content: str,
            note_type: str = "private",
            tags: Optional[List[str]] = None
    ) -> tuple[bool, str, Optional[UserNote]]:
        """
        Create a new user note
        
        :param user_id: ID of the user creating the note
        :param title: Title of the note
        :param content: Markdown content of the note
        :param note_type: Type of note ("private" or "shared")
        :param tags: List of tags for the note
        :return: Tuple (success: bool, message: str, note: Optional[UserNote])
        """
        try:
            # Validate input
            valid, msg = UserNote.validate_title(title)
            if not valid:
                return False, msg, None
            
            valid, msg = UserNote.validate_content(content)
            if not valid:
                return False, msg, None
            
            valid, msg = UserNote.validate_note_type(note_type)
            if not valid:
                return False, msg, None
            
            if tags:
                valid, msg = UserNote.validate_tags(tags)
                if not valid:
                    return False, msg, None
            
            # Create note
            note = UserNote(
                user_id=user_id,
                title=title,
                content=content,
                note_type=note_type,
                tags=tags or []
            )
            
            # Save to database
            logger.debug(f"Creating note with data: {note.to_dict()}")
            
            result = self.db.create('UserNote', note.to_dict())
            logger.debug(f"Database create result: {result}")
            
            if result:
                created_note_data = result # type: ignore
                created_note = UserNote.from_dict(created_note_data)
                logger.debug(f"Note created successfully: {created_note.id}")
                return True, "Note created successfully", created_note
            else:
                logger.error("Database create returned unexpected result")
                return False, "Failed to create note", None
                
        except Exception as e:
            logger.error(f"Error creating note: {e}")
            return False, f"Error creating note: {str(e)}", None
    
    def get_note_by_id(self, note_id: str, user_id: str) -> Optional[UserNote]:
        """
        Get a specific note by ID (only if user owns it or it's shared)
        
        :param note_id: ID of the note to retrieve
        :param user_id: ID of the user requesting the note
        :return: UserNote object if found and accessible, None otherwise
        """
        try:
            logger.debug(f"get_note_by_id - note_id: {note_id}, user_id: {user_id}")

            if note_id.startswith('UserNote:'):
                note_id = note_id.split(':')[1]
            
            result = self.db.query(
                "SELECT * FROM UserNote WHERE id = $note_id AND (user_id = $user_id OR note_type = 'shared')",
                {"note_id": RecordID('UserNote', note_id), "user_id": user_id}
            )
            
            if result and len(result) > 0:
                note_data = result[0]
                return UserNote.from_dict(note_data)
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting note by ID: {e}")
            return None
    
    def get_user_notes(self, user_id: str, include_shared: bool = True) -> List[UserNote]:
        """
        Get all notes for a user (including shared notes if requested)
        
        :param user_id: ID of the user
        :param include_shared: Whether to include shared notes from other users
        :return: List of UserNote objects
        """
        try:
            logger.debug(f"get_user_notes - user_id: {user_id}, include_shared: {include_shared}")
            
            if include_shared:
                result = self.db.query(
                    "SELECT * FROM UserNote WHERE user_id = $user_id OR note_type = 'shared' ORDER BY date_updated DESC",
                    {"user_id": user_id}
                )
            else:
                result = self.db.query(
                    "SELECT * FROM UserNote WHERE user_id = $user_id ORDER BY date_updated DESC",
                    {"user_id": user_id}
                )
            
            notes: List[UserNote] = []
            if result:
                for note_data in result:
                    notes.append(UserNote.from_dict(note_data))
            
            logger.debug(f"Found {len(notes)} notes for user {user_id}")
            return notes
            
        except Exception as e:
            logger.error(f"Error getting user notes: {e}")
            return []
    
    def update_note(
            self,
            note_id: str,
            user_id: str,
            title: Optional[str] = None,
            content: Optional[str] = None,
            note_type: Optional[str] = None,
            tags: Optional[List[str]] = None
    ) -> tuple[bool, str, Optional[UserNote]]:
        """
        Update a user note (only if user owns it)
        
        :param note_id: ID of the note to update
        :param user_id: ID of the user updating the note
        :param title: New title (optional)
        :param content: New content (optional)
        :param note_type: New note type (optional)
        :param tags: New tags (optional)
        :return: Tuple (success: bool, message: str, note: Optional[UserNote])
        """
        try:
            # Get existing note
            existing_note = self.get_note_by_id(note_id, user_id)
            if not existing_note:
                return False, "Note not found or access denied", None
            
            # Check if user owns the note
            if existing_note.user_id != user_id:
                return False, "You can only update your own notes", None
            
            # Update fields
            updates: Dict[str, Any] = {}
            
            if title is not None:
                valid, msg = UserNote.validate_title(title)
                if not valid:
                    return False, msg, None
                updates['title'] = title
            
            if content is not None:
                valid, msg = UserNote.validate_content(content)
                if not valid:
                    return False, msg, None
                updates['content'] = content
            
            if note_type is not None:
                valid, msg = UserNote.validate_note_type(note_type)
                if not valid:
                    return False, msg, None
                updates['note_type'] = note_type
            
            if tags is not None:
                valid, msg = UserNote.validate_tags(tags)
                if not valid:
                    return False, msg, None
                updates['tags'] = tags
            
            # Always update the date_updated field
            from datetime import datetime, timezone
            updates['date_updated'] = datetime.now(timezone.utc).isoformat()
            
            if not updates:
                return False, "No fields to update", None
            
            # Update in database
            logger.debug(f"Updating note {note_id} with data: {updates}")
            
            result = self.db.update(f'UserNote:{note_id}', updates)
            logger.debug(f"Database update result: {result}")
            
            if result:
                # Get updated note
                updated_note = self.get_note_by_id(note_id, user_id)
                if updated_note:
                    return True, "Note updated successfully", updated_note
                else:
                    return False, "Failed to retrieve updated note", None
            else:
                return False, "Failed to update note", None
                
        except Exception as e:
            logger.error(f"Error updating note: {e}")
            return False, f"Error updating note: {str(e)}", None
    
    def delete_note(self, note_id: str, user_id: str) -> tuple[bool, str]:
        """
        Delete a user note (only if user owns it)
        
        :param note_id: ID of the note to delete
        :param user_id: ID of the user deleting the note
        :return: Tuple (success: bool, message: str)
        """
        try:
            # Get existing note
            existing_note = self.get_note_by_id(note_id, user_id)
            if not existing_note:
                return False, "Note not found or access denied"
            
            # Check if user owns the note
            if existing_note.user_id != user_id:
                return False, "You can only delete your own notes"
            
            # Delete from database
            logger.debug(f"Deleting note {note_id}")
            
            result = self.db.delete(f'UserNote:{note_id}')
            logger.debug(f"Database delete result: {result}")
            
            if result:
                return True, "Note deleted successfully"
            else:
                return False, "Failed to delete note"
                
        except Exception as e:
            logger.error(f"Error deleting note: {e}")
            return False, f"Error deleting note: {str(e)}"
    
    def search_notes(self, user_id: str, query: str, include_shared: bool = True) -> List[UserNote]:
        """
        Search notes by title, content, or tags
        
        :param user_id: ID of the user
        :param query: Search query
        :param include_shared: Whether to include shared notes from other users
        :return: List of UserNote objects matching the search
        """
        try:
            logger.debug(f"search_notes - user_id: {user_id}, query: {query}, include_shared: {include_shared}")
            
            if include_shared:
                result = self.db.query(
                    """
                    SELECT * FROM UserNote 
                    WHERE (user_id = $user_id OR note_type = 'shared')
                    AND (title CONTAINS $query OR content CONTAINS $query OR array::any(tags) CONTAINS $query)
                    ORDER BY date_updated DESC
                    """,
                    {"user_id": user_id, "query": query}
                )
            else:
                result = self.db.query(
                    """
                    SELECT * FROM UserNote 
                    WHERE user_id = $user_id
                    AND (title CONTAINS $query OR content CONTAINS $query OR array::any(tags) CONTAINS $query)
                    ORDER BY date_updated DESC
                    """,
                    {"user_id": user_id, "query": query}
                )
            
            notes: List[UserNote] = []
            if result:
                for note_data in result:
                    notes.append(UserNote.from_dict(note_data))
            
            logger.debug(f"Found {len(notes)} notes matching query '{query}' for user {user_id}")
            return notes
            
        except Exception as e:
            logger.error(f"Error searching notes: {e}")
            return [] 