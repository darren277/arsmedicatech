"""
User Notes model.
"""
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class UserNote:
    """
    Model for user notes that can be private or shared
    """
    
    def __init__(
            self,
            user_id: str,
            title: str,
            content: str,
            note_type: str = "private",
            tags: Optional[List[str]] = None,
            date_created: Optional[str] = None,
            date_updated: Optional[str] = None,
            id: Optional[str] = None
    ) -> None:
        """
        Initialize a user note
        
        :param user_id: ID of the user who owns this note
        :param title: Title of the note
        :param content: Markdown content of the note
        :param note_type: Type of note ("private" or "shared")
        :param tags: List of tags for the note
        :param date_created: Creation timestamp
        :param date_updated: Last update timestamp
        :param id: Database record ID
        """
        self.user_id = user_id
        self.title = title
        self.content = content
        self.note_type = note_type
        self.tags = tags or []
        self.date_created = date_created or datetime.now(timezone.utc).isoformat()
        self.date_updated = date_updated or datetime.now(timezone.utc).isoformat()
        self.id = id
    
    @staticmethod
    def validate_note_type(note_type: str) -> tuple[bool, str]:
        """
        Validate note type

        :param note_type: Note type to validate
        :return: Tuple (is_valid: bool, error_message: str)
        """
        valid_types = ["private", "shared"]
        if note_type not in valid_types:
            return False, f"Note type must be one of: {', '.join(valid_types)}"
        return True, ""
    
    @staticmethod
    def validate_title(title: str) -> tuple[bool, str]:
        """
        Validate note title

        :param title: Title to validate
        :return: Tuple (is_valid: bool, error_message: str)
        """
        if not title:
            return False, "Title is required"
        if len(title) < 1:
            return False, "Title must be at least 1 character long"
        if len(title) > 200:
            return False, "Title must be less than 200 characters"
        return True, ""
    
    @staticmethod
    def validate_content(content: str) -> tuple[bool, str]:
        """
        Validate note content

        :param content: Content to validate
        :return: Tuple (is_valid: bool, error_message: str)
        """
        if not content:
            return False, "Content is required"
        if len(content) < 1:
            return False, "Content must be at least 1 character long"
        if len(content) > 10000:
            return False, "Content must be less than 10,000 characters"
        return True, ""
    
    @staticmethod
    def validate_tags(tags: List[str]) -> tuple[bool, str]:
        """
        Validate note tags

        :param tags: Tags to validate
        :return: Tuple (is_valid: bool, error_message: str)
        """
        for tag in tags:
            if len(tag) < 1:
                return False, "Tags cannot be empty"
            if len(tag) > 50:
                return False, "Tags must be less than 50 characters"
        
        return True, ""
    
    def update_content(self, content: str) -> None:
        """
        Update note content and set updated timestamp

        :param content: New content for the note
        :raises ValueError: If the content is invalid
        :return: None
        """
        valid, msg = self.validate_content(content)
        if not valid:
            raise ValueError(msg)
        
        self.content = content
        self.date_updated = datetime.now(timezone.utc).isoformat()
    
    def update_title(self, title: str) -> None:
        """
        Update note title and set updated timestamp

        :param title: New title for the note
        :raises ValueError: If the title is invalid
        :return: None
        """
        valid, msg = self.validate_title(title)
        if not valid:
            raise ValueError(msg)
        
        self.title = title
        self.date_updated = datetime.now(timezone.utc).isoformat()
    
    def update_note_type(self, note_type: str) -> None:
        """
        Update note type and set updated timestamp

        :param note_type: New note type
        :raises ValueError: If the note type is invalid
        :return: None
        """
        valid, msg = self.validate_note_type(note_type)
        if not valid:
            raise ValueError(msg)
        
        self.note_type = note_type
        self.date_updated = datetime.now(timezone.utc).isoformat()
    
    def update_tags(self, tags: List[str]) -> None:
        """
        Update note tags and set updated timestamp

        :param tags: New tags for the note
        :raises ValueError: If the tags are invalid
        :return: None
        """
        valid, msg = self.validate_tags(tags)
        if not valid:
            raise ValueError(msg)
        
        self.tags = tags
        self.date_updated = datetime.now(timezone.utc).isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert user note to dictionary for database storage

        :return: Dictionary representation of the user note
        """
        return {
            'user_id': self.user_id,
            'title': self.title,
            'content': self.content,
            'note_type': self.note_type,
            'tags': self.tags,
            'date_created': self.date_created,
            'date_updated': self.date_updated
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserNote':
        """
        Create user note from dictionary

        :param data: Dictionary containing user note data
        :return: UserNote object
        """
        # Convert RecordID to string if it exists
        note_id = data.get('id')
        if hasattr(note_id, '__str__'):
            note_id = str(note_id)
        
        return cls(
            user_id=str(data.get('user_id') or ""),
            title=str(data.get('title') or ""),
            content=str(data.get('content') or ""),
            note_type=data.get('note_type', 'private'),
            tags=data.get('tags', []),
            date_created=data.get('date_created'),
            date_updated=data.get('date_updated'),
            id=note_id
        )
