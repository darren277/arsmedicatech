"""
This module defines the Conversation and Message classes for managing conversations and messages
"""
from datetime import datetime
from typing import Dict, Any, List, Optional


class Conversation:
    """
    Represents a conversation between users or with an AI assistant.
    """
    def __init__(
            self,
            participants: List[str],
            conversation_type: str = "user_to_user",
            created_at: Optional[str] = None,
            id: Optional[str] = None,
            last_message_at: Optional[str] = None
    ) -> None:
        """
        Initialize a Conversation object
        
        :param participants: List of user IDs participating in the conversation
        :param conversation_type: Type of conversation ("user_to_user", "ai_assistant")
        :param created_at: Creation timestamp
        :param id: Database record ID
        :param last_message_at: Timestamp of last message
        """
        self.participants = participants
        self.conversation_type = conversation_type
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.last_message_at = last_message_at or self.created_at
        self.id = id
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert conversation to dictionary for database storage

        :return: Dictionary representation of the conversation
        """
        return {
            'participants': self.participants,
            'conversation_type': self.conversation_type,
            'created_at': self.created_at,
            'last_message_at': self.last_message_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Conversation':
        """
        Create conversation from dictionary

        :param data: Dictionary containing conversation data
        :return: Conversation object
        """
        # Convert RecordID to string if it exists
        conv_id = data.get('id')
        if hasattr(conv_id, '__str__'):
            conv_id = str(conv_id)
        
        return cls(
            participants=data.get('participants', []),
            conversation_type=data.get('conversation_type', 'user_to_user'),
            created_at=data.get('created_at'),
            id=conv_id,
            last_message_at=data.get('last_message_at')
        )
    
    def is_participant(self, user_id: str) -> bool:
        """
        Check if a user is a participant in this conversation

        :param user_id: ID of the user to check
        :return: True if the user is a participant, False otherwise
        """
        return user_id in self.participants
    
    def add_participant(self, user_id: str) -> bool:
        """
        Add a participant to the conversation

        :param user_id: ID of the user to add
        :return: True if the user was added, False if they were already a participant
        """
        if user_id not in self.participants:
            self.participants.append(user_id)
            return True
        return False
    
    def remove_participant(self, user_id: str) -> bool:
        """
        Remove a participant from the conversation

        :param user_id: ID of the user to remove
        :return: True if the user was removed, False if they were not a participant
        """
        if user_id in self.participants:
            self.participants.remove(user_id)
            return True
        return False


class Message:
    """
    Represents a message in a conversation.
    """
    def __init__(
            self,
            conversation_id: str,
            sender_id: str,
            text: str,
            created_at: Optional[str] = None,
            id: Optional[str] = None,
            is_read: bool = False
    ) -> None:
        """
        Initialize a Message object
        
        :param conversation_id: ID of the conversation this message belongs to
        :param sender_id: ID of the user who sent the message
        :param text: Message text content
        :param created_at: Creation timestamp
        :param id: Database record ID
        :param is_read: Whether the message has been read
        """
        self.conversation_id = conversation_id
        self.sender_id = sender_id
        self.text = text
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.is_read = is_read
        self.id = id
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert message to dictionary for database storage

        :return: Dictionary representation of the message
        """
        return {
            'conversation_id': self.conversation_id,
            'sender_id': self.sender_id,
            'text': self.text,
            'created_at': self.created_at,
            'is_read': self.is_read
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """
        Create message from dictionary

        :param data: Dictionary containing message data
        :return: Message object
        """
        # Convert RecordID to string if it exists
        msg_id = data.get('id')
        if hasattr(msg_id, '__str__'):
            msg_id = str(msg_id)
        
        return cls(
            conversation_id=data.get('conversation_id'),
            sender_id=data.get('sender_id'),
            text=data.get('text'),
            created_at=data.get('created_at'),
            id=msg_id,
            is_read=data.get('is_read', False)
        ) 